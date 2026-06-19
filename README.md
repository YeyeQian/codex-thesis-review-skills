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
