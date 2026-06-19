# Codex Thesis Review Skills

Two Codex skills for reviewing master's and doctoral theses before submission, defense, or blind review. The current workflows are primarily designed around doctoral dissertations, and can be adapted to master's thesis review by applying a lower threshold for research depth and contribution scale. The skills are written primarily for Chinese academic writing scenarios, with an emphasis on dissertation integrity, blind-review readiness, evidence-based critique, and structured revision guidance.

## Included Skills

### `review-thesis-integrity`

`review-thesis-integrity` is a layered integrity-review skill for doctoral dissertations. It is intended for pre-blind-review checks where the main concern is whether the thesis reads as one coherent dissertation rather than a collection of loosely connected papers.

It supports single-layer or explicitly requested multi-layer reviews, including:

- dissertation-level coherence and book-like completeness;
- main research thread and chapter-to-chapter progression;
- abstract, introduction, literature review, chapter positioning, innovation claims, and conclusion;
- contribution-evidence closure;
- terminology, concept, figure/table, and expression consistency;
- cross-chapter metric consistency.

Typical prompts:

```text
Use $review-thesis-integrity to review the introduction and check whether it can support the whole dissertation.
```

```text
Use $review-thesis-integrity to run a multi-layer pre-blind-review check on my thesis outline and chapter summaries.
```

### `review-phd-thesis-blind`

`review-phd-thesis-blind` simulates a formal doctoral dissertation blind-review process. It is designed for more judgment-heavy review tasks where Codex should behave like an external reviewer and produce a structured evaluation with scores, academic-level judgment, defense recommendation, and objection determination.

It includes:

- a five-item review rubric for topic selection, literature review, research outcomes, research capability, and thesis standards;
- hard rules for objection determination;
- a formal report template;
- a consistency-check script for review reports saved as Markdown;
- an additional review lens for computer architecture, chip architecture, digital IC design, integrated circuit/system design, RISC-V, hardware accelerators, processors, and EDA-adjacent hardware research.

Typical prompts:

```text
Use $review-phd-thesis-blind to produce a simulated blind-review report for this doctoral dissertation.
```

```text
Use $review-phd-thesis-blind to judge whether this dissertation can enter defense after minor revision.
```

## Anonymized Example Outputs

The following summaries are based on anonymized real-use outputs. Thesis title, institution, author identity, chapter-specific technical content, algorithm names, project names, and detailed metrics have been removed or generalized.

### Example 1: Full-Layer Integrity Review

Input: a near-final doctoral dissertation draft and a request for a full pre-blind-review integrity check.

Skill used: `review-thesis-integrity`

Output shape:

- a whole-thesis conclusion before the detailed review;
- a risk matrix covering L0-L11 review layers;
- separate diagnosis for book-like completeness, main research thread, abstract, introduction, literature review, chapter positioning, chapter progression, innovation claims, evidence closure, conclusion, expression consistency, and cross-chapter metric consistency;
- a prioritized revision list for blind-review readiness;
- suggested tables for mapping foundational content to chapters, mapping literature gaps to thesis contributions, linking contributions to evidence, and tracking metric sources.

An anonymized result summary:

```text
Overall judgment: basically passes the pre-blind-review integrity check, but should be revised according to the priority list before submission.

Main risks found:
- Some achievement descriptions should be checked against blind-review anonymity requirements.
- Some foundational material is broad and should be explicitly mapped to later chapters.
- The literature review is problem-oriented, but some parts can better show what prior work solved, what it did not solve, and how the thesis responds.
- Contribution-evidence closure is mostly sufficient, but a global contribution-to-evidence index would reduce reviewer search cost.
- A small number of cross-chapter metrics need clearer derivation, baseline, or wording.
- Terminology, spacing, abbreviations, and formal-version wording need one final consistency pass.

Final delivery judgment: structurally ready for blind review after targeted revisions.
```

This example shows how the integrity-review skill is used before final polishing. It does not primarily score the thesis; it identifies structural risks that may affect how reviewers perceive coherence, contribution closure, and readiness.

### Example 2: Simulated Blind-Review Report

Input: a doctoral dissertation draft and a request to simulate an external blind-review report from an engineering faculty perspective.

Skill used: `review-phd-thesis-blind`

Output shape:

- thesis basic information and review scope;
- overall review conclusion;
- thesis overview;
- five independent sub-scores: topic selection, literature review, research outcomes, research capability, and thesis standards;
- academic-level judgment;
- defense recommendation;
- objection determination using hard rules;
- major deficiencies and revision suggestions;
- final formal review opinion.

An anonymized result summary:

```text
Academic level: B. Good
Defense recommendation: B. Basically agree; allow defense after minor revision
Objection: No
Re-review required: No
Defense eligibility: Eligible after minor revision

Sub-score pattern:
- Topic selection: high 80s
- Literature review: low 80s
- Research outcomes: mid 80s
- Research capability: high 80s
- Thesis standards: high 70s

Main revision type:
The thesis meets doctoral dissertation requirements overall. Remaining issues are mainly minor revisions, such as tightening concept boundaries, strengthening selected parts of the literature review, making conclusion boundaries more cautious, unifying terminology, and fixing reference or formatting warnings.
```

This example shows how the simulated blind-review skill converts textual evidence into a formal review decision. It is stricter than a polishing checklist because it must keep scores, academic level, defense recommendation, and objection judgment mutually consistent.

## Repository Layout

```text
.
├── LICENSE
├── README.md
└── skills
    ├── review-phd-thesis-blind
    │   ├── SKILL.md
    │   ├── agents/openai.yaml
    │   ├── references/
    │   └── scripts/
    └── review-thesis-integrity
        ├── SKILL.md
        └── agents/openai.yaml
```

## Installation

Clone this repository and copy the skill folders into your Codex skills directory:

```bash
git clone https://github.com/YeyeQian/codex-thesis-review-skills.git
mkdir -p ~/.codex/skills
cp -R codex-thesis-review-skills/skills/review-thesis-integrity ~/.codex/skills/
cp -R codex-thesis-review-skills/skills/review-phd-thesis-blind ~/.codex/skills/
```

Restart Codex if the skills are not discovered immediately.

## Notes

- These skills provide structured review workflows and checklists. They do not replace a formal university review process or human expert judgment.
- The blind-review skill is intentionally strict about evidence, scoring consistency, and objection rules.
- The integrity-review skill is intended to find structural and argumentative risks before polishing the text.

## License

MIT License.
