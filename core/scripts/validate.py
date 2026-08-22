#!/usr/bin/env python3
"""
Sanketana course repo validator — convention 1.

Usage (from a course repo root):
    python3 scripts/validate.py            errors fail, warnings reported
    python3 scripts/validate.py --strict   warnings also fail

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
SKILLS = {
    "mental-modeling",
    "intentional-direction",
    "critical-evaluation",
    "selective-judgment",
    "ethical-reasoning",
}
ROOT_ALLOWED = {
    "course.yaml", "curriculum.md", "overview.md", "CONVENTION.md", "TRACK.md",
    "pedagogy.md", "CLAUDE.md", "README.md", "LICENSE",
    "_template", "scripts", "shared", "_drafts",
}
LESSON_DIR_RE = re.compile(r"^lesson-(\d{2})-([a-z0-9]+(?:-[a-z0-9]+)*)$")
LESSON_ID_RE = re.compile(r"^l\d{2}$")
LESSON_FILES_REQUIRED = {"lesson.yaml", "classwork.md", "homework.md"}
LESSON_FILES_OPTIONAL = {"solutions.md", "teacher-notes.md", "practice.md", "quiz.yaml"}
LESSON_DIRS_OPTIONAL = {"code", "assets"}
QUIZ_TYPES = {"single", "multi", "predict", "short"}

CORE_H2 = {
    "classwork.md": {
        "Lesson Theme", "What You'll Build", "Tools Used", "What You'll Learn",
        "Starter Materials", "Predict the Output", "In Class", "Reflection", "Key Takeaways",
    },
    "homework.md": {"Homework"},
    "solutions.md": set(),
    "practice.md": {"Practice Projects"},
    "teacher-notes.md": {"Prep", "Timing", "Common Pitfalls", "Differentiation", "What to Watch For"},
}
NUMBERED_OK = {"homework.md", "solutions.md", "practice.md"}

TRACK_H2 = {
    "text-code": {
        "classwork.md": {"Bug Hunt"},
    },
    "block-code": {
        "classwork.md": {"Build Steps", "Remix Challenge"},
    },
    "ai-fluency": {
        "classwork.md": {"Prompt Lab", "Ethics Check", "Tool Judgment"},
    },
}

FRONTMATTER_RE = re.compile(r"^---\s*\n")
H2_RE = re.compile(r"^## +(.+?)\s*$", re.MULTILINE)
H3_RE = re.compile(r"^### +(.+?)\s*$", re.MULTILINE)
NUMBERED_RE = re.compile(r"^\d+\.\s+\S")
DURATION_RE = re.compile(r"\(\d+ min\)$")
ABS_GITHUB_RE = re.compile(r"\]\(https?://(?:www\.)?github\.com/")


# ---------------------------------------------------------------- helpers
def load_yaml(path: Path):
    try:
        with path.open(encoding="utf-8") as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        err(f"{path.relative_to(ROOT)}: invalid YAML — {e}")
        return None


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

for name in ("curriculum.md", "overview.md"):
    if not (ROOT / name).exists():
        err(f"{name}: missing at repo root")

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
if track in TRACK_H2:
    for f, hs in TRACK_H2[track].items():
        allowed_h2.setdefault(f, set()).update(hs)

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
        require(L, "duration_min", lw, int)
        if "tier" not in L:
            warn(f"{lw}: no `tier` set")
        elif course.get("tiers"):
            tier_ids = {t.get("id") for t in course["tiers"]}
            if L["tier"] not in tier_ids:
                err(f"{lw}: `tier` `{L['tier']}` is not a tier id in course.yaml ({sorted(tier_ids)})")
        skills = L.get("thinking_skills") or []
        if not skills:
            warn(f"{lw}: no `thinking_skills` listed")
        for s in skills:
            if s not in SKILLS:
                err(f"{lw}: `thinking_skills` contains `{s}`; allowed: {sorted(SKILLS)}")
        if len(skills) > 2:
            warn(f"{lw}: {len(skills)} thinking skills — pedagogy says emphasise one or two")
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
        ok = allowed_h2.get(f, set())
        for h in H2_RE.findall(text):
            if h in ok:
                continue
            if f in NUMBERED_OK and NUMBERED_RE.match(h):
                continue
            err(f"{fw}: H2 `{h}` is not in the allowlist for {f}. "
                f"Allowed: {sorted(ok)}{' or numbered tasks' if f in NUMBERED_OK else ''}. "
                f"Use an allowed H2, or demote to H3.")
        if f == "classwork.md" and "## In Class" in text:
            block = text.split("## In Class", 1)[1]
            block = re.split(r"^## ", block, maxsplit=1, flags=re.MULTILINE)[0]
            for h3 in H3_RE.findall(block):
                if not DURATION_RE.search(h3):
                    warn(f"{fw}: In Class activity `{h3}` should end with a duration like `(8 min)`")
        if f == "classwork.md":
            low = text.lower()
            if "solutions.md" in low or "teacher-notes.md" in low:
                err(f"{fw}: student-facing file refers to a teacher-only file")
            for bad in ("fun", "exciting", "future-ready", "21st-century", "ai-powered", "unlock", "empower"):
                if re.search(rf"\b{re.escape(bad)}\b", low):
                    warn(f"{fw}: uses banned word `{bad}` (see pedagogy.md voice rules)")

    # quiz.yaml
    qz = d / "quiz.yaml"
    if qz.exists():
        Q = load_yaml(qz) or {}
        qw = f"{where}/quiz.yaml"
        if require(Q, "id", qw, str) and lesson_id and Q["id"] != f"{lesson_id}-quiz":
            err(f"{qw}: `id` must be `{lesson_id}-quiz`, got `{Q['id']}`")
        if require(Q, "questions", qw, list):
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
                    if require(q, "code_ref", qq, str) and not (d / q["code_ref"]).exists():
                        err(f"{qq}: `code_ref` `{q['code_ref']}` does not exist in {where}/")
                if "explanation" not in q:
                    warn(f"{qq}: no `explanation` — the reveal is where the learning happens")

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
