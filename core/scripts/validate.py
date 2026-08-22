#!/usr/bin/env python3
"""
Sanketana course repo validator — convention 1.

Usage (from a course repo root):
    python3 .kit/scripts/validate.py            errors fail, warnings reported
    python3 .kit/scripts/validate.py --strict   warnings also fail

Error messages are written so that Claude Code can fix them without asking.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(2)

ROOT = Path.cwd()
STRICT = "--strict" in sys.argv
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


# ---------------------------------------------------------------- constants
CONVENTION = 1
TRACKS = {"text-code", "block-code", "ai-fluency"}
SKILLS = {                       # ai-fluency track only
    "mental-modeling",
    "intentional-direction",
    "critical-evaluation",
    "selective-judgment",
    "ethical-reasoning",
}
# Kit files live in `.kit/`, and everything starting with a dot is skipped before this
# set is consulted — so the course root is only what a teacher or author authored.
ROOT_ALLOWED = {
    "course.yaml", "curriculum.md", "CLAUDE.md", "README.md", "LICENSE",
    "shared", "_drafts", "assessments",
}
# A course has exactly three assessments, at the repo root in `assessments/`.
#   stem -> (kind, questions, minutes)
ASSESSMENTS = {
    "formative-1": ("formative", 10, 15),
    "formative-2": ("formative", 10, 15),
    "summative": ("summative", 20, 45),
}
LESSON_DIR_RE = re.compile(r"^lesson-(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
LESSON_ID_RE = re.compile(r"^l\d{2}$")
LESSON_DIRS_OPTIONAL = {"code", "assets"}
QUIZ_TYPES = {"single", "multi", "predict", "short"}

CONCEPT_H2 = {
    "The Idea", "How It Works", "Worked Example", "Vocabulary",
    "Common Mistakes", "Where This Shows Up", "Key Takeaways",
}

# The six phases every §5 Class Activities table runs, in order. SHOULD, not MUST.
PHASES = [
    ("Recap", ("recap",)),
    ("New concept", ("new concept", "new idea", "concept")),
    ("Predict → Observe → Explain", ("predict", "poe")),
    ("Build", ("build",)),
    ("Reflection", ("reflect",)),
    ("Homework brief", ("homework",)),
]
PLAN_TABLE_HEAD = "| Phase | Min | What happens | Purpose |"

# `lesson-plan.md` is a fixed spine: these eight H2s, numbered, in this order.
PLAN_SECTIONS = [
    "Lesson Theme",
    "Key Activity",
    "Tools & Materials",
    "Learning Outcomes",
    "Class Activities",
    "Differentiation Notes",
    "Student Templates / Starter Materials",
    "Teacher Prep Notes",
]

LESSON_FILES_REQUIRED = {"lesson.yaml", "lesson-plan.md", "concepts.md", "homework.md", "practice.md"}
LESSON_FILES_OPTIONAL = {"solutions.md"}
STUDENT_FILE = "concepts.md"
TEACHER_ONLY = {"lesson-plan.md", "solutions.md"}
CORE_H2 = {
    "concepts.md": CONCEPT_H2,
    "homework.md": {"Homework"},
    "solutions.md": set(),
    "practice.md": {"Practice Projects"},
    "lesson-plan.md": set(),     # checked against PLAN_SECTIONS instead
}
NUMBERED_OK = {"homework.md", "solutions.md", "practice.md"}

FRONTMATTER_RE = re.compile(r"^---\s*\n")
H2_RE = re.compile(r"^## +(.+?)\s*$", re.MULTILINE)
H3_RE = re.compile(r"^### +(.+?)\s*$", re.MULTILINE)
NUMBERED_RE = re.compile(r"^\d+\.\s+\S")
ABS_GITHUB_RE = re.compile(r"\]\(https?://(?:www\.)?github\.com/")


# ---------------------------------------------------------------- helpers
def load_yaml(path: Path):
    try:
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        err(f"{path.relative_to(ROOT)}: invalid YAML — {e}")
        return None


def check_questions(Q: dict, qw: str, base: Path, covers) -> None:
    """Validate an assessment's `questions:` list."""
    if not isinstance(Q.get("questions"), list):
        return
    qids = set()
    for i, q in enumerate(Q["questions"], 1):
        qq = f"{qw} question {i}"
        if not isinstance(q, dict):
            err(f"{qq}: must be a mapping")
            continue
        if require(q, "id", qq, str):
            if q["id"] in qids:
                err(f"{qq}: duplicate question id `{q['id']}`")
            qids.add(q["id"])
        require(q, "prompt", qq, str)
        require(q, "answer", qq)
        if require(q, "type", qq, str) and q["type"] not in QUIZ_TYPES:
            err(f"{qq}: `type` must be one of {sorted(QUIZ_TYPES)}")
        if require(q, "lesson", qq, str) and q["lesson"] not in covers:
            err(f"{qq}: `lesson` `{q['lesson']}` is not in this assessment's `covers`")
        t = q.get("type")
        if t in ("single", "multi"):
            if require(q, "options", qq, list):
                oids = {o.get("id") for o in q["options"] if isinstance(o, dict)}
                ans = q.get("answer")
                ans_list = ans if isinstance(ans, list) else [ans]
                for a in ans_list:
                    if a not in oids:
                        err(f"{qq}: `answer` `{a}` is not an option id ({sorted(oids)})")
                if t == "single" and isinstance(ans, list):
                    err(f"{qq}: `single` question must have one answer, not a list")
        if t == "predict":
            if require(q, "code_ref", qq, str) and not (base / q["code_ref"]).exists():
                err(f"{qq}: `code_ref` `{q['code_ref']}` does not exist")
        if "explanation" not in q:
            warn(f"{qq}: no `explanation` — the reveal is where the learning happens")


def check_class_activities(plan: str, fw: str, duration) -> None:
    """§5 is the whole class flow: it must be a table, and it should run the standard phases."""
    m = re.search(r"^## 5\. Class Activities\s*$", plan, re.MULTILINE)
    if not m:
        return                                   # the spine check already reported it
    rest = plan[m.end():]
    nxt = re.search(r"^## ", rest, re.MULTILINE)
    block = rest[: nxt.start()] if nxt else rest

    rows = [l.strip() for l in block.splitlines() if l.strip().startswith("|")]
    if not rows:
        err(f"{fw}: §5 Class Activities must be a table — `{PLAN_TABLE_HEAD}`")
        return
    if rows[0].replace("  ", " ") != PLAN_TABLE_HEAD:
        err(f"{fw}: §5 table header must be exactly `{PLAN_TABLE_HEAD}`, got `{rows[0]}`")
    body = [r for r in rows[2:] if r.count("|") >= 5]

    before = block[: block.index(rows[0])] if rows[0] in block else ""
    if "**" not in before:
        warn(f"{fw}: §5 should open with a bolded line naming what to protect if the hour runs short")

    names = [r.split("|")[1].strip().lower() for r in body]
    hit = sum(any(any(k in n for k in keys) for n in names) for _label, keys in PHASES)
    if body and hit < 4:
        warn(f"{fw}: §5 runs {len(body)} phases but matches only {hit} of the six standard ones "
             f"({[p[0] for p in PHASES]}) — see CONVENTION.md §5")

    mins = []
    for r in body:
        cell = r.split("|")[2].strip()
        if cell.isdigit():
            mins.append(int(cell))
    if duration and mins and abs(sum(mins) - duration) > max(5, duration * 0.15):
        warn(f"{fw}: §5 `Min` column sums to {sum(mins)} but `duration_min` is {duration}")


def require(d: dict, key: str, where: str, typ=None) -> bool:
    if key not in d or d[key] in (None, ""):
        err(f"{where}: missing required field `{key}`")
        return False
    if typ and not isinstance(d[key], typ):
        err(f"{where}: `{key}` must be {typ.__name__}, got {type(d[key]).__name__}")
        return False
    return True


# ---------------------------------------------------------------- course.yaml
course_path = ROOT / "course.yaml"
if not course_path.exists():
    err("course.yaml: missing at repo root")
    course = {}
else:
    course = load_yaml(course_path) or {}

W = "course.yaml"
track = None
if course:
    if require(course, "convention", W, int) and course["convention"] != CONVENTION:
        err(f"{W}: `convention` is {course['convention']}; this validator enforces {CONVENTION}")
    if require(course, "track", W, str):
        track = course["track"]
        if track not in TRACKS:
            err(f"{W}: `track` must be one of {sorted(TRACKS)}, got `{track}`")
    if require(course, "id", W, str):
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", course["id"]):
            err(f"{W}: `id` must be lowercase-hyphen slug, got `{course['id']}`")
        if course["id"] != ROOT.name:
            warn(f"{W}: `id` `{course['id']}` does not match folder name `{ROOT.name}`")
    require(course, "title", W, str)
    require(course, "lessons", W, list)
    if "kit_version" not in course:
        warn(f"{W}: add `kit_version` for traceability")

if not (ROOT / "curriculum.md").exists():
    err("curriculum.md: missing at repo root")

# ---------------------------------------------------------------- root layout
lesson_dirs: dict[str, Path] = {}
for p in sorted(ROOT.iterdir()):
    if p.name.startswith("."):
        continue
    if p.name in ROOT_ALLOWED:
        continue
    m = LESSON_DIR_RE.match(p.name)
    if m and p.is_dir():
        lesson_dirs[p.name] = p
    else:
        err(f"{p.name}: not allowed at repo root. Lesson folders are `lesson-NN-slug/`; scratch goes in `_drafts/`")

# ---------------------------------------------------------------- lessons
seen_ids: dict[str, str] = {}
allowed_h2 = {k: set(v) for k, v in CORE_H2.items()}

for dname, d in lesson_dirs.items():
    where = dname
    present = {c.name for c in d.iterdir() if not c.name.startswith(".")}

    for f in LESSON_FILES_REQUIRED - present:
        err(f"{where}/: missing required file `{f}`")
    for f in present:
        fp = d / f
        if fp.is_dir():
            if f not in LESSON_DIRS_OPTIONAL:
                err(f"{where}/{f}/: folders allowed in a lesson are only {sorted(LESSON_DIRS_OPTIONAL)}")
        elif f not in LESSON_FILES_REQUIRED | LESSON_FILES_OPTIONAL:
            err(f"{where}/{f}: not an allowed lesson file. Allowed: "
                f"{sorted(LESSON_FILES_REQUIRED | LESSON_FILES_OPTIONAL)}. Audience is decided by filename.")

    # lesson.yaml
    ly = d / "lesson.yaml"
    lesson_id = None
    lesson_duration = None
    if ly.exists():
        L = load_yaml(ly) or {}
        lw = f"{where}/lesson.yaml"
        if require(L, "id", lw, str):
            lesson_id = L["id"]
            if not LESSON_ID_RE.match(lesson_id):
                err(f"{lw}: `id` must look like `l03`, got `{lesson_id}`")
            if lesson_id in seen_ids:
                err(f"{lw}: duplicate lesson id `{lesson_id}` (also in {seen_ids[lesson_id]})")
            seen_ids[lesson_id] = dname
        require(L, "title", lw, str)
        require(L, "summary", lw, str)
        if require(L, "duration_min", lw, int):
            lesson_duration = L["duration_min"]
        if "tier" not in L:
            warn(f"{lw}: no `tier` set")
        elif course.get("tiers"):
            tier_ids = {t.get("id") for t in course["tiers"]}
            if L["tier"] not in tier_ids:
                err(f"{lw}: `tier` `{L['tier']}` is not a tier id in course.yaml ({sorted(tier_ids)})")
        skills = L.get("thinking_skills") or []
        if track == "ai-fluency":
            if not skills:
                warn(f"{lw}: no `thinking_skills` listed")
            for s in skills:
                if s not in SKILLS:
                    err(f"{lw}: `thinking_skills` contains `{s}`; allowed: {sorted(SKILLS)}")
            if len(skills) > 2:
                warn(f"{lw}: {len(skills)} thinking skills — TRACK.md says emphasise one or two")
        elif skills:
            warn(f"{lw}: `thinking_skills` is an ai-fluency field; drop it on the {track} track")
        for v in L.get("video") or []:
            if not isinstance(v, dict) or "url" not in v:
                err(f"{lw}: each `video` entry needs `label` and `url`")
        for pre in L.get("prerequisites") or []:
            if not LESSON_ID_RE.match(str(pre)):
                err(f"{lw}: `prerequisites` entries must be lesson ids like `l02`, got `{pre}`")

    # markdown files
    for f in present:
        if not f.endswith(".md"):
            continue
        fp = d / f
        text = fp.read_text(encoding="utf-8")
        fw = f"{where}/{f}"
        if FRONTMATTER_RE.match(text):
            err(f"{fw}: starts with YAML frontmatter. Remove it; metadata belongs in lesson.yaml")
        if ABS_GITHUB_RE.search(text):
            err(f"{fw}: contains an absolute github.com link. Use relative links")
        if f == "lesson-plan.md":
            found = H2_RE.findall(text)
            expect = [f"{i}. {n}" for i, n in enumerate(PLAN_SECTIONS, 1)]
            if found != expect:
                extra = [h for h in found if h not in expect]
                missing = [h for h in expect if h not in found]
                detail = []
                if missing:
                    detail.append(f"missing {missing}")
                if extra:
                    detail.append(f"unexpected {extra}")
                if not detail:
                    detail.append("sections are out of order")
                err(f"{fw}: the plan spine is fixed — H2s must be exactly "
                    f"{expect}, numbered and in order ({'; '.join(detail)}). "
                    f"Demote anything else to H3.")
            check_class_activities(text, fw, lesson_duration)
        else:
            ok = allowed_h2.get(f, set())
            for h in H2_RE.findall(text):
                if h in ok:
                    continue
                if f in NUMBERED_OK and NUMBERED_RE.match(h):
                    continue
                err(f"{fw}: H2 `{h}` is not in the allowlist for {f}. "
                    f"Allowed: {sorted(ok)}{' or numbered tasks' if f in NUMBERED_OK else ''}. "
                    f"Use an allowed H2, or demote to H3.")
        if f not in TEACHER_ONLY:
            low = text.lower()
            for tf in sorted(TEACHER_ONLY):
                if tf in low:
                    err(f"{fw}: student-facing file refers to the teacher-only file `{tf}`")
        if f == "practice.md":
            projects = [h for h in H3_RE.findall(text)] or \
                       [l for l in text.splitlines() if NUMBERED_RE.match(l.strip())]
            if len(projects) < 2:
                warn(f"{fw}: {len(projects)} practice project(s) — a lesson should carry at least two, "
                     f"so a fast student has a choice")
        if f == STUDENT_FILE:
            low = text.lower()
            for bad in ("fun", "exciting", "future-ready", "21st-century", "ai-powered", "unlock", "empower"):
                if re.search(rf"\b{re.escape(bad)}\b", low):
                    warn(f"{fw}: uses banned word `{bad}` (see pedagogy.md voice rules)")

# ---------------------------------------------------------------- assessments
adir = ROOT / "assessments"
if not adir.is_dir():
    err("assessments/: missing at repo root. A course has three: "
        + ", ".join(f"{k}.yaml" for k in ASSESSMENTS))
else:
    expected = set()
    for stem in ASSESSMENTS:
        expected |= {f"{stem}.yaml", f"{stem}-solutions.md"}
    present = {c.name for c in adir.iterdir() if not c.name.startswith(".")}
    for missing in sorted(expected - present):
        err(f"assessments/{missing}: missing. A course has exactly three assessments, "
            f"each with a teacher-only marking file")
    for extra in sorted(present - expected):
        err(f"assessments/{extra}: not an allowed file. Allowed: {sorted(expected)}")

    for stem, (kind, want_q, want_min) in ASSESSMENTS.items():
        ap = adir / f"{stem}.yaml"
        if not ap.exists():
            continue
        A = load_yaml(ap) or {}
        aw = f"assessments/{stem}.yaml"
        if require(A, "id", aw, str) and A["id"] != stem:
            err(f"{aw}: `id` must be `{stem}`, got `{A['id']}`")
        covers = A.get("covers") or []
        if not covers and not A.get("questions"):
            # Assessments are written once the lessons they cover exist. A stub is not an error.
            warn(f"{aw}: not written yet — {want_q} questions over the lessons it covers "
                 f"(shape: assessment-template.yaml)")
            continue
        require(A, "title", aw, str)
        if require(A, "kind", aw, str) and A["kind"] != kind:
            err(f"{aw}: `kind` must be `{kind}`, got `{A['kind']}`")
        if require(A, "duration_min", aw, int) and A["duration_min"] != want_min:
            warn(f"{aw}: `duration_min` is {A['duration_min']}; the standard {kind} is {want_min}")
        if not covers:
            err(f"{aw}: missing required field `covers` (the lesson ids this assessment tests)")
        for lid in covers:
            if lid not in seen_ids:
                err(f"{aw}: `covers` lists `{lid}` but no lesson folder has that id")
        if require(A, "after", aw, str) and A["after"] not in seen_ids:
            err(f"{aw}: `after` `{A['after']}` is not a lesson id")
        qs = A.get("questions") or []
        if not qs:
            err(f"{aw}: missing required field `questions`")
        elif len(qs) != want_q:
            warn(f"{aw}: {len(qs)} questions; the standard {kind} is {want_q}")
        check_questions(A, aw, ROOT, set(covers))
        untested = [l for l in covers if l not in {q.get("lesson") for q in qs if isinstance(q, dict)}]
        if untested:
            warn(f"{aw}: no question tests {untested} — every lesson in `covers` should appear")

# ---------------------------------------------------------------- cross checks
if course.get("lessons"):
    listed = list(course["lessons"])
    if len(listed) != len(set(listed)):
        err("course.yaml: `lessons` contains duplicates")
    for lid in listed:
        if lid not in seen_ids:
            err(f"course.yaml: `lessons` lists `{lid}` but no lesson folder has that id")
    for lid, dname in seen_ids.items():
        if lid not in listed:
            err(f"{dname}/: id `{lid}` is not listed in course.yaml `lessons` — add it to set its order")
    for t in course.get("tiers") or []:
        for lid in t.get("lessons") or []:
            if lid not in listed:
                err(f"course.yaml: tier `{t.get('id')}` lists `{lid}` which is not in `lessons`")

# ---------------------------------------------------------------- report
for w in warnings:
    print(f"WARN  {w}")
for e in errors:
    print(f"ERROR {e}")
print(f"\n{len(lesson_dirs)} lesson folders · {len(errors)} errors · {len(warnings)} warnings")
if errors or (STRICT and warnings):
    sys.exit(1)
print("OK")
