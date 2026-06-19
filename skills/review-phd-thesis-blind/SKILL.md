---
name: review-phd-thesis-blind
description: Use when Codex needs to simulate doctoral dissertation blind review, pre-review, internal quality review, defense qualification judgment, 分项评分, 学术水平评价, 答辩建议, or 存在异议判定 for PhD theses in computer architecture, chip architecture, digital IC design, integrated circuit/system design, hardware accelerators, processors, RISC-V, EDA-adjacent hardware research, or related engineering fields.
---

# 博士论文模拟盲审评审

## Core Principle

以模拟外审专家身份判断论文是否达到博士学位论文要求。先基于证据完成五项分项评价，再给出学术水平、答辩建议和异议判定；不要只润色文字或只给总体印象。

## Required References

每次正式评审前必须读取：

- `references/review-rubric.md`：五项评分标准、学术等级、答辩建议和异议硬规则。
- `references/report-template.md`：统一报告结构和写作格式。

若只做局部预检或用户明确要求短评，可只读取 `references/review-rubric.md`，但仍要说明输入范围有限。

## Review Workflow

1. 确认评审材料：论文题目、学科专业、研究方向、评审对象、版本日期、论文全文或章节文件、参考文献/编译日志/成果清单等可用证据。
2. 建立论文地图：概括总问题、分问题、技术路线、各章贡献、实验/实现证据和结论边界。
3. 按五项独立评分：论文选题、文献综述、研究成果、科研水平、论文规范。每项都写评价、优点、不足、分数、是否低于 60 分和达标判断。
4. 应用硬规则：任一分项低于 60 分、学术水平为 D. 差、答辩建议为 C 或 D，均必须判定“存在异议”。
5. 生成报告：遵循 `references/report-template.md`。用中文学术表达，语气接近计算机体系结构、芯片架构、数字芯片设计领域博士生导师的盲审意见。
6. 自检一致性：若报告保存为 Markdown 文件，运行 `scripts/check_review_consistency.py <report.md>` 检查分数、等级、答辩建议和异议判定是否一致。

## Domain Lens

面向计算机体系结构、芯片架构和数字芯片设计方向时，重点检查：

- 选题是否不止是工程实现，而是抽象出体系结构、微架构、数据通路、指令集、存储层次、互连、EDA/实现流程或系统协同中的博士层次问题。
- 创新是否落在可辨识机制上，如 ISA/接口抽象、负载建模、数据流组织、并行化/流水化/调度策略、存储访问优化、PPA 折中、安全/可靠性机制、软硬件协同或端到端系统路径。
- 实验是否覆盖合理基线、SOTA 对比、消融分析、面积/功耗/性能/能效/频率/资源利用率、FPGA/ASIC/流片或后端实现证据，以及结论适用边界。
- 是否明确作者本人贡献，避免把平台、工具链、标准 IP 或合作团队成果笼统写成论文贡献。
- 是否谨慎处理“领先”“安全”“通用”“全标准”“低功耗”等强结论，要求有数据、威胁模型、工艺条件、工作负载和对比口径支撑。

## Evidence Discipline

- 对每项判断尽量指向章节、图表、公式、算法、日志、实验表或论文文本位置。
- 资料不足时写明“无法充分判断”的范围，不要臆测。
- 已发表论文、录用论文或流片成果可作为质量证据，但不能自动替代博士论文的成书性、综述性、统一主线和规范性评价。
- 盲审匿名备注：论文中允许陈述博士在读期间论文发表成果、专利、流片或竞赛奖励等学术成果；只要不暴露作者姓名和具体论文名称等可直接识别身份的信息，不应将这类成果陈述本身判定为破坏盲审匿名要求。
- 不能用平均分抵消硬伤。只要触发异议条件，最终结论必须体现重新送审或不能直接答辩的处理规则。

## Output Expectations

报告应包含：基本信息、总体结论、论文概述、五项分项评价、评分汇总、学术水平评价、答辩资格建议、异议判定、主要不足与修改建议、最终评审意见。若用户要求“详细评审结果”，采用完整模板；若要求“快速预评审”，保留五项评分和硬规则结论。

## Common Mistakes

- 只写“论文质量较好，可以答辩”，没有分项证据。
- 分项低于 60 分却仍判定“不存在异议”。
- 答辩建议写“须重大修改并重新送审”，但最终又写“可进入答辩”。
- 把所有问题都写成语言润色问题，忽略创新性、实验支撑和博士层次科研能力。
- 盲审报告中泄露不必要的作者身份、导师信息或非评审必需的个人信息。
