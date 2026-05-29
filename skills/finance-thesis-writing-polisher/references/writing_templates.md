# Finance Thesis Writing Templates

## Claim Strength Ladder

Use wording that matches evidence:

- Weak association: "is associated with", "shows a correlation with".
- Baseline support: "supports the hypothesis that", "is consistent with".
- Robust support: "the conclusion remains robust after".
- Causal design support: "suggests a causal effect" only when identification is credible.
- Avoid unless proven: "proves", "fully confirms", "eliminates endogeneity", "fills the blank".

Chinese equivalents:

- Association: "与...显著相关", "二者之间存在相关关系".
- Support: "支持了本文假设", "与理论预期一致".
- Robust: "说明基准结论具有一定稳健性".
- Causal cautious: "在一定程度上支持...的因果解释".
- Avoid: "证明了", "完全验证", "彻底解决内生性".

## Baseline Result Template

```text
表X报告了基准回归结果。核心解释变量 ... 的系数为正/负，并在 ... 水平上显著，说明在控制 ... 以及 ... 固定效应后，... 与 ... 之间存在显著正/负相关关系。该结果与假设H1的理论预期一致，表明 ... 可能通过 ... 影响 ... 。需要说明的是，基准回归主要反映条件相关关系，后文将进一步通过稳健性和内生性检验考察结论的可靠性。
```

## Robustness Template

```text
为检验基准结论是否受到变量度量、样本选择或模型设定的影响，本文进一步开展稳健性检验。表X显示，在采用 ... 后，核心解释变量的系数方向仍与基准回归保持一致，并在统计上保持显著/基本显著。上述结果说明，本文的主要结论不依赖于单一模型设定或变量度量，具有一定稳健性。
```

## Endogeneity Template

```text
考虑到 ... 可能存在反向因果、遗漏变量或样本选择问题，本文采用 ... 方法进行进一步检验。结果显示，核心解释变量的估计系数仍然为正/负，且与基准结论一致。这表明在一定程度上缓解相关内生性担忧后，本文结论仍具有较好的稳定性。但由于 ... 方法仍依赖于 ... 假设，结果解释仍需保持谨慎。
```

## Heterogeneity Template

```text
为考察 ... 的影响是否在不同类型样本中存在差异，本文按照 ... 将样本划分为 ... 和 ...。结果显示，核心解释变量在 ... 组中更为显著/系数更大，而在 ... 组中影响较弱。该结果说明，... 的作用可能受到 ... 的调节，符合 ... 理论逻辑。
```

## Mechanism Template

```text
前文结果表明 ... 对 ... 具有显著影响。为进一步解释其作用路径，本文从 ... 机制出发进行检验。表X结果显示，... 显著影响机制变量 ...，且机制变量与被解释变量之间的关系方向符合理论预期。该结果说明，... 可能是 ... 影响 ... 的重要渠道之一。
```

## Literature Review Transition

```text
综上，现有文献已经从 ... 角度对 ... 进行了较为充分的讨论，但对于 ... 的研究仍存在进一步拓展空间。具体而言，已有研究更多关注 ...，而对 ... 的作用机制和异质性特征讨论相对不足。基于此，本文拟在现有研究基础上，进一步考察 ... 对 ... 的影响，并从 ... 角度展开机制检验。
```

## Marginal Contribution Template

```text
本文可能的边际贡献主要体现在以下三个方面：第一，从研究视角看，本文将 ... 纳入 ... 的分析框架，补充了现有文献对 ... 的讨论；第二，从作用机制看，本文进一步检验 ... 渠道，有助于解释 ... 的内在逻辑；第三，从经验证据看，本文基于 ... 数据，采用 ... 方法，为 ... 提供了来自中国资本市场的经验证据。
```

## Conclusion Template

```text
本文以 ... 为研究样本，考察了 ... 对 ... 的影响。研究发现，... 。进一步分析表明，... 。异质性检验显示，... 。上述结论表明，... 。基于研究结论，本文认为应当 ... 。同时，受限于数据可得性和研究设计，本文仍存在 ... 等不足，未来研究可进一步从 ... 方面拓展。
```

## Policy Implication Rules

Policy implications should map to findings:

- If the finding concerns financing constraints, recommend financing access, information disclosure, or credit support.
- If the finding concerns governance, recommend governance structure, internal control, or disclosure quality.
- If the finding concerns ESG/green finance, recommend green disclosure, incentive mechanisms, or regulatory coordination.
- If heterogeneity is important, recommend differentiated policies.
- Do not recommend broad macro policy if the thesis only studies firm-level association.

## Common Fixes

- Replace "证明" with "表明" or "支持".
- Replace "显著提升企业价值" with "与企业价值提高显著相关" when causal design is weak.
- Add "在控制其他因素后" when interpreting regression.
- Add "可能" when discussing mechanisms.
- Add "一定程度上" when discussing robustness or endogeneity relief.
- Remove repeated coefficient details if the table already reports them and focus on interpretation.
