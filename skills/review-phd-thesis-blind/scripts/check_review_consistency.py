#!/usr/bin/env python3
"""检查博士论文评审报告中的硬规则一致性。

用法：
  python check_review_consistency.py report.md
  cat report.md | python check_review_consistency.py -
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


SCORE_PATTERNS = [
    re.compile(r"建议分数[：:]\s*(\d{1,3})\s*/\s*100"),
    re.compile(r"\|\s*(?:论文选题|文献综述|研究成果|科研水平|论文规范)\s*\|\s*(\d{1,3})\s*/\s*100\s*\|"),
]


def read_text(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    return Path(path).read_text(encoding="utf-8")


def collect_scores(text: str) -> list[int]:
    scores: list[int] = []
    seen: set[tuple[int, int]] = set()
    for pattern in SCORE_PATTERNS:
        for match in pattern.finditer(text):
            key = (match.start(), match.end())
            if key in seen:
                continue
            seen.add(key)
            value = int(match.group(1))
            if 0 <= value <= 100:
                scores.append(value)
    return scores


def contains_academic_level_d(text: str) -> bool:
    patterns = [
        r"建议等级[：:]\s*D\s*[.．、]?\s*差",
        r"学术水平评价\s*\|\s*D\s*[.．、]?\s*差",
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def contains_defense_c_or_d(text: str) -> bool:
    patterns = [
        r"建议意见[：:]\s*C\s*[.．、]?\s*须作重大修改",
        r"建议意见[：:]\s*D\s*[.．、]?\s*不同意",
        r"答辩建议\s*\|\s*C\s*[.．、]?\s*须作重大修改",
        r"答辩建议\s*\|\s*D\s*[.．、]?\s*不同意",
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def reported_objection(text: str) -> str | None:
    matches = re.findall(r"是否存在异议[：:]\s*(是|否)", text)
    if matches:
        return matches[-1]
    table_matches = re.findall(r"\|\s*是否存在异议\s*\|\s*(是|否)\s*\|", text)
    if table_matches:
        return table_matches[-1]
    return None


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("用法：python check_review_consistency.py <report.md|->", file=sys.stderr)
        return 2

    text = read_text(argv[1])
    scores = collect_scores(text)
    any_score_below_60 = any(score < 60 for score in scores)
    level_d = contains_academic_level_d(text)
    defense_c_or_d = contains_defense_c_or_d(text)
    expected_objection = any_score_below_60 or level_d or defense_c_or_d
    reported = reported_objection(text)

    issues: list[str] = []
    if len(scores) < 5:
        issues.append(f"仅找到 {len(scores)} 个分数条目；预期至少 5 个。")
    if reported is None:
        issues.append("未找到最终的“是否存在异议：是/否”。")
    else:
        reported_bool = reported == "是"
        if reported_bool != expected_objection:
            issues.append(
                "异议判定不一致：硬规则预期为"
                f"{'是' if expected_objection else '否'}，报告写为{reported}。"
            )

    print("找到的分数：", ", ".join(map(str, scores)) if scores else "无")
    print("学术水平是否为 D：", "是" if level_d else "否")
    print("答辩建议是否为 C/D：", "是" if defense_c_or_d else "否")
    print("硬规则预期异议：", "是" if expected_objection else "否")
    print("报告中的异议：", reported or "未找到")

    if issues:
        print("\n发现的问题：")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("\n一致性检查通过。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
