# Finance Literature Review Framework

## Model-Agnostic Use

These instructions are for any AI model or assistant. The assistant should produce plain, reusable literature-review reasoning that can be used in Word, LaTeX, note-taking software, Excel, Zotero, EndNote, CNKI, Web of Science, Google Scholar, SSRN, or manual thesis writing.

Universal rule:

```text
do not list papers; synthesize arguments
```

## Literature Search Keywords

Build bilingual search terms from the thesis relationship:

- Core explanatory variable `X`: Chinese name, English name, synonyms, abbreviations.
- Dependent variable `Y`: Chinese name, English name, common proxies.
- Mechanism terms: financing constraints, information asymmetry, innovation, governance, risk-taking, resource allocation.
- Method terms: panel data, fixed effects, DID, event study, instrumental variable, PSM, text analysis.
- Context terms: China, A-share, listed firms, banks, capital market, green finance, digital finance, ESG.

Example format:

```text
Chinese: 数字金融, 企业创新, 融资约束, 信息不对称, A股上市公司
English: digital finance, corporate innovation, financing constraints, information asymmetry, Chinese listed firms
```

## Literature Matrix

Use this matrix when extracting papers:

| Field | What to record |
| --- | --- |
| Citation | Author, year, title, journal or source |
| Language | Chinese or English |
| Research question | What relationship or mechanism is studied |
| Theory | Main theoretical basis |
| Sample | Country, market, sample period, observation unit |
| Method | OLS, panel FE, DID, IV, PSM, event study, factor model, etc. |
| Dependent variable | Definition and proxy |
| Key independent variable | Definition and proxy |
| Mechanism variable | Channel tested, if any |
| Main finding | Direction, significance, and interpretation |
| Limitation | Data, method, external validity, omitted mechanism, sample period |
| Relevance | How it supports or contrasts with the user's thesis |

## Theme Classification Menu

Choose three to five themes. Do not use too many categories.

Common finance literature themes:

- Theoretical foundations.
- Economic consequences of the core explanatory variable.
- Determinants of the dependent variable.
- Mechanism and channel evidence.
- Identification strategies and empirical methods.
- Heterogeneity and boundary conditions.
- Chinese institutional context.
- International evidence and comparison.
- Measurement and variable construction.

For a master's thesis, a practical structure is:

1. Literature on the core explanatory variable.
2. Literature on the dependent variable.
3. Literature on the relationship between them.
4. Literature on mechanisms and heterogeneity.
5. Literature review and marginal contribution.

## Mechanism Extraction

For each mechanism, answer:

- What theory predicts this channel?
- Which papers support it?
- What variable proxies are used?
- Is the channel direct, mediating, moderating, or contextual?
- How can the user's thesis test it empirically?

Common finance mechanisms:

- Financing constraint: credit availability, external financing cost, debt maturity, SA/KZ/WW index.
- Information asymmetry: analyst coverage, forecast dispersion, disclosure quality, bid-ask spread.
- Governance: agency cost, board structure, ownership concentration, internal control, executive incentives.
- Innovation: R&D, patent applications, invention patents, green patents.
- Risk-taking: leverage, volatility, crash risk, earnings volatility.
- Resource allocation: investment efficiency, overinvestment, underinvestment, capital expenditure.
- Market attention: investor attention, media attention, turnover, institutional ownership.
- Environmental responsibility: environmental disclosure, green investment, ESG score, pollution control.

## Findings Comparison

When findings differ, compare:

- Country or institutional environment.
- Sample period and market cycle.
- Industry coverage.
- Variable proxy.
- Identification method.
- Fixed effects and controls.
- Whether the paper studies short-term or long-term effects.
- Whether nonlinear or threshold effects are considered.

Use cautious wording:

```text
Existing studies generally support ..., but the magnitude and significance vary across samples and measurement choices.
```

## Research Gap Templates

Use one or more of these gap types:

- Topic gap: existing studies rarely examine the direct relationship between `X` and `Y`.
- Mechanism gap: existing studies document the effect but do not fully explain the channel.
- Context gap: international evidence may not apply directly to China's institutional environment.
- Data gap: existing studies use earlier samples and do not cover recent policy or market changes.
- Measurement gap: existing studies rely on a single proxy; alternative measures can improve robustness.
- Method gap: existing studies mostly use correlation analysis and lack stronger identification.
- Heterogeneity gap: existing studies pay insufficient attention to ownership, region, industry, financing constraints, or governance differences.

Avoid claiming "no research exists" unless a careful search supports it. Prefer "relatively limited", "insufficiently explored", or "still lacks consensus".

## Marginal Contribution Templates

Conservative contribution structure:

```text
Compared with existing studies, this thesis may contribute in three ways.
First, it extends the research perspective by examining ...
Second, it enriches the mechanism analysis by testing ...
Third, it provides evidence from ... using ..., which helps supplement existing findings under ...
```

Chinese thesis-style version:

```text
本文可能的边际贡献主要体现在以下三个方面：第一，从研究视角看，本文将 ... 纳入 ... 的分析框架，补充了现有文献对 ... 的讨论；第二，从作用机制看，本文进一步考察 ... 渠道，有助于解释 ... 的内在逻辑；第三，从经验证据看，本文基于 ... 数据，采用 ... 方法，为 ... 提供了来自中国资本市场的经验证据。
```

Do not use absolute claims such as "首次", "填补空白", or "完全解决" unless the user has strong evidence.

## Thesis Paragraph Templates

Theme synthesis paragraph:

```text
围绕 ... 的经济后果，现有研究主要从 ... 和 ... 两个角度展开。一类研究认为，...；另一类研究则指出，在 ... 条件下，该影响可能减弱或呈现差异。造成结论差异的原因可能与样本区间、变量度量以及识别方法有关。总体来看，已有文献为理解 ... 提供了重要基础，但对于 ... 的作用机制仍有进一步讨论空间。
```

English synthesis paragraph:

```text
Existing studies examine the economic consequences of ... mainly from two perspectives. One stream suggests that ... through ..., whereas another stream emphasizes that the effect may depend on ... . The mixed findings can be attributed to differences in sample periods, variable measurement, and empirical identification. Overall, this literature provides a useful foundation, but the mechanism through which ... affects ... remains insufficiently explored.
```

Review and gap paragraph:

```text
综上，现有文献已经从 ... 方面对 ... 进行了较为充分的讨论，但仍存在以下不足：第一，...；第二，...；第三，...。基于此，本文拟从 ... 角度出发，考察 ... 对 ... 的影响，并进一步检验 ... 机制和 ... 异质性。
```

## Common Problems And Fixes

- Problem: The review lists one paper per sentence.
  Fix: reorganize by themes and use each paper as evidence for a claim.

- Problem: Chinese and English literature are separated mechanically.
  Fix: compare whether they study the same mechanism under different institutional contexts.

- Problem: The marginal contribution is too broad.
  Fix: narrow it to topic, mechanism, sample, method, variable, or heterogeneity.

- Problem: The review does not lead to hypotheses.
  Fix: end each theme with the theoretical implication for the user's `X -> Y` relationship.

- Problem: The literature gap is unsupported.
  Fix: tie the gap to concrete limitations in prior data, methods, mechanisms, or settings.

- Problem: Citation details are uncertain.
  Fix: mark them for verification instead of inventing journal, year, or conclusion details.

## Final Review Checklist

- At least three coherent research streams are identified.
- Each stream has a theme sentence and synthesis.
- Domestic and international literature are compared where relevant.
- Mechanisms are connected to empirical variables.
- Differences in findings are explained rather than ignored.
- The research gap is specific and defensible.
- The marginal contribution is conservative and thesis-appropriate.
- Any uncertain citation details are flagged for verification.
