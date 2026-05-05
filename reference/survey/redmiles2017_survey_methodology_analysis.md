# Redmiles et al. (2017) 调查方法学最佳实践分析

> **论文信息**
> - **标题**: A Summary of Survey Methodology Best Practices for Security and Privacy Researchers
> - **作者**: Elissa M. Redmiles, Yasemin Acar, Sascha Fahl, Michelle L. Mazurek
> - **机构**: University of Maryland
> - **类型**: Technical Report (CS-TR-5055)
> - **年份**: 2017
> - **被引情况**: 安全与隐私研究领域广泛引用，是 HCI + Security 社区调查方法学的标准参考

---

## 一、论文核心框架

这篇技术报告从 **问卷设计 (Questionnaire Writing)**、**抽样方法 (Sampling)**、**预测试 (Pre-testing)** 三个维度，系统总结了来自调查方法学、心理学、社会学等 100+ 篇文献的最佳实践。

核心观点：**自我报告数据的质量完全取决于研究者在实验设计阶段所做的选择。**

---

## 二、关键最佳实践与我们的对照

### 2.1 措辞选择 (Word Choice)

**论文观点：**
- 即使是最常见的词汇，不同受访者也可能有完全不同的理解（例如 "usually" 一词在某研究中被参与者解读出 24 种不同含义）
- 安全与隐私领域充满技术术语，受访者往往不理解这些术语
- 更糟糕的是："受访者经常忽略问题旁提供的书面定义"
- 建议：使用受访者更熟悉的日常用语替代技术术语；必要时通过焦点小组识别受访者使用的语言

**我们问卷的问题：**
- Q14/Q17/Q19/Q22/Q26/Q31/Q39 等使用了 Likert 量表的同意/不同意格式，其中包含相对复杂的陈述句。例如：
  > *"AI tools have made it easier to generate 'Related Work' sections, but harder to ensure citation accuracy."*
  
  这类复合句包含两个子命题，受访者可能对前半句和后半句持不同态度，被迫选择一个总体回应。
- Q38/Q39 涉及 "copy-paste BibTeX" 和 "meticulously verify every single field"，虽然措辞通俗，但没有经过焦点小组验证这些术语在受访者群体中的理解一致性。

---

### 2.2 Likert 量表设计

**论文观点：**
- 点数太少或太多都会损害结果的有效性和可解释性
- **选项顺序效应**：在线调查中，第一个选项被选中的概率最高；电话/面访中最后一个选项更可能被选
- **量表方向效应**：如果最左侧是积极选项（如"强烈同意"），整体回应倾向于更高
- 建议：对随机一半受访者反转量表方向；或随机化选项顺序

**我们问卷的问题：**
- 我们的 Likert 量表（Q14, Q17, Q19, Q26, Q31, Q39 等）全部采用固定方向（左侧为"强烈同意"），**没有进行方向反转或随机化**
- 这意味着如果受访者有"首选项偏见"（倾向于选左侧），我们的数据会系统性地偏向积极回应
- 更重要的是：Reviewer A 指出的 "leading questions"（引导性问题）——我们的量表陈述本身可能隐含了期望方向

---

### 2.3 敏感问题与社会期望偏差 (Social Desirability Bias)

**论文观点（这是 Reviewer A 引用该论文的核心原因）：**

> "受访者倾向于**低报**社会不期望的行为（如药物使用、破产、犯罪行为），同时**高报**社会期望的行为（如去教堂、环保、锻炼、系安全带）。"

对于安全与隐私研究：
- 受访者可能感到压力而**高报**安全知识或"良好"行为（如及时打补丁）
- 即使只是轻微的社交压力（如知道面试官关心安全），也可能导致过度报告
- 建议措施：
  - **认知访谈 (Cognitive Interviewing)**：让受访者边回答边出声思考
  - **随机化回答技术 (Randomized Response Technique)**
  - ** bogus pipeline**：假装能检测谎言，促使诚实回答
  - 在问卷开头就明确告知数据匿名化，减少受访者对社会评判的担忧

**我们问卷的问题（这是核心问题）：**

我们的问卷中存在大量"社会期望敏感"问题：

| 问题 | 社会期望方向 | 潜在偏差 |
|------|-------------|---------|
| Q12: "If an AI tool provides a perfect-looking reference... do you still verify it externally?" | 高报验证行为 | 受访者可能声称会验证，实际上不会 |
| Q15: "Verify AI-given reference externally?" | 高报 diligence | 41.5% 承认不检查 vs 77.3% 声称"总是验证" |
| Q17: "How often do you verify that a cited paper actually contains the claim?" | 高报 carefulness | "Every single time" (57.1%) 可能夸大 |
| Q39: "I meticulously verify every single field... ensuring 100% accuracy" | 极端高报 diligence | 27.7% "Strongly agree" 与 Q38 的 13.8% "often copy-paste" 形成矛盾 |

**验证差距的本质就是社会期望偏差的证据：**
- 87.2% 使用 AI 工具，86.7% 声称"总是验证"
- 但实际行为：41.5% 直接复制粘贴不检查，44.4% 遇到可疑引用时不采取行动

这种" stated vs. actual "的巨大落差，**强烈暗示社会期望偏差在我们的数据中扮演了重要角色**。受访者在自我报告中倾向于呈现"理想化的研究者形象"。

---

### 2.4 问题顺序效应 (Question Order / Priming)

**论文观点：**
- 问题顺序会显著影响回答（启动效应）
- 人口统计问题放在开头会"框定"整个调查的语境，影响后续敏感问题的回答
- 建议：**将人口统计问题放在调查末尾**

**我们问卷的问题：**
- 我们的调查将人口统计问题（Q1-Q4：职位、领域、发表论文数、审稿经历）放在了**开头**
- 这可能产生两种效应：
  1. **刻板印象威胁**：如果受访者先确认自己是"教授"或"资深审稿人"，后续关于"是否仔细检查引用"的问题可能触发更高的社会期望回应
  2. **启动效应**：先问"你是否是顶级会议审稿人"，可能让受访者在后续问题中更倾向于呈现"专业、严谨"的形象

---

### 2.5 调查长度

**论文观点：**
- 调查过长会导致完成率下降
- 提供进度条可以提高完成率
- 虚报调查长度（如 advertised 5 分钟实际 10 分钟）会显著降低完成率

**我们的情况：**
- 59 个问题（含反向措辞重复），预计 10-15 分钟
- 97 份回应 out of 300 封邮件 = 32.3% 回应率，94 份有效 = 31.3% 有效回应率
- 回应率不算高，可能与长度有关，但我们已经在 Limitations 中提及

---

### 2.6 预测试 (Pre-testing)

**论文观点（强烈推荐）：**
- **试点测试 (Piloting)**：在小样本上运行，检查技术问题和整体流程
- **认知访谈 (Cognitive Interviewing)**：让受访者出声思考；仅 10 名参与者就能发现 50%+ 的潜在问题；被证明能显著减少测量误差
- **专家评审 (Expert Review)**：请调查方法学或 HCI 专家审查
- 建议：**报告预测试结果**，这有助于未来研究者

**我们问卷的问题：**
- 我们的论文中**没有提及任何预测试过程**
- 我们不知道是否进行了：
  - 认知访谈来验证受访者如何理解"hallucination"、"ghost citation"、"verify"等关键术语
  - 试点测试来检查问题顺序是否产生启动效应
  - 专家评审来识别引导性问题和敏感问题

这是 Reviewer A 和 B 批评"methodology insufficiently described"的重要组成部分。

---

### 2.7 抽样方法

**论文观点：**
- 便利抽样 (Convenience Sampling) 和滚雪球抽样 (Snowball Sampling) 成本低但"可能导致低质量数据且缺乏学术可信度"
- 关键是要**明确描述抽样方法及其局限性**
- 特别注意：隐私担忧极高的个体可能更不愿意参与研究，导致这类人群被系统性低估

**我们的情况：**
- 我们通过社交媒体 + 向 300 名随机抽样的作者/PC 成员发送邮件招募
- 这属于**便利抽样 + 冷邮件招募**的混合
- 回应率 32.3% 意味着 2/3 的目标人群没有参与
- 未回应偏差 (Non-response Bias) 是一个重要局限：对引用完整性特别不关心的人可能根本不会填写调查

---

## 三、综合问题诊断

### 核心问题 1：社会期望偏差未充分讨论

我们的问卷设计中，大量问题涉及"好研究者应该做什么"（验证引用、仔细阅读、仔细检查 BibTeX）。Redmiles 等明确指出，安全与隐私研究中这种偏差尤其严重。我们观察到的"验证差距"（ stated 86.7% always verify vs. actual 41.5% copy-paste）本身就是社会期望偏差的强烈信号。

**当前论文的不足**：
- 没有在 Methodology 或 Limitations 中承认社会期望偏差的可能性
- 没有讨论这种偏差如何影响我们对"研究者实际行为"的结论

### 核心问题 2：缺乏预测试证据

Redmiles 等将认知访谈和专家评审列为"必要且高度重要的"预测试措施。我们的论文完全没有提及是否进行了这些步骤。

### 核心问题 3：问题顺序未优化

人口统计问题放在开头，可能通过刻板印象威胁和启动效应抬高了后续问题的社会期望回应。

### 核心问题 4：Likert 量表方向固定

没有反转量表方向或随机化选项顺序，可能导致系统性偏见。

---

## 四、改进建议（用于论文修改）

### 立即可做的修改（不需要重新跑实验）

1. **在 Limitations 中新增 "Survey Response Biases" 段落**：
   - 承认社会期望偏差可能导致受访者高报验证行为和 diligence
   - 指出"验证差距"（ stated vs. actual ）可能是这种偏差的体现
   - 引用 Redmiles et al. (2017) 说明安全研究中这种偏差的普遍性

2. **在 Experiment III 的方法论描述中补充**：
   - 说明我们使用了反向措辞问题（Q38/Q39）作为一致性检查，但承认这只能捕获极端不一致，无法消除系统性的社会期望偏差
   - 说明由于资源限制，我们没有进行认知访谈或专家问卷评审预测试

3. **在讨论"验证差距"发现时加一层解释**：
   - 即使考虑到社会期望偏差，stated 和 actual 行为之间的巨大差距仍然具有意义——它表明即使在"理想化自我报告"的情况下，研究者仍然承认大量不规范行为

### 未来工作建议（可用于 Future Work / Response Letter）

- 未来研究可以采用认知访谈预测试问卷措辞
- 可以采用随机化回答技术或 bogus pipeline 来减少敏感问题的社会期望偏差
- 可以考虑使用行为数据（如浏览器历史、引用管理软件日志）替代或补充自我报告数据

---

## 五、引用格式

如果要在论文中引用这篇技术报告：

```bibtex
@techreport{redmiles2017survey,
  title={A Summary of Survey Methodology Best Practices for Security and Privacy Researchers},
  author={Redmiles, Elissa M. and Acar, Yasemin and Fahl, Sascha and Mazurek, Michelle L.},
  institution={University of Maryland},
  number={CS-TR-5055},
  year={2017},
  url={https://drum.lib.umd.edu/items/683d78b0-a0e3-4fae-9c93-b75aae4ad11b}
}
```

---

*分析完成于 2026-05-05*
