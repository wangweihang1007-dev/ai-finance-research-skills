---
name: finance-literature-review
description: Model-agnostic finance literature review skill for any AI assistant or coding agent, including ChatGPT, Claude, Gemini, Codex, and other LLMs. Use when organizing Chinese or English finance literature, classifying papers by research theme, extracting theoretical mechanisms, comparing findings, building literature matrices, identifying research gaps, writing thesis literature reviews, and generating thesis-ready research commentary and marginal contribution sections.
---

# Finance Literature Review

## Core Rule

This is a model-agnostic working standard for ChatGPT, Claude, Gemini, Codex, and other AI assistants. Turn scattered Chinese and English finance literature into a structured, thesis-ready review.

Always organize literature by argument and research stream, not by simply listing papers one by one.

```text
topic -> search scope -> paper matrix -> theme clusters -> mechanisms -> findings comparison -> gap -> marginal contribution -> thesis text
```

## Universal Agent Rules

Apply these rules regardless of the AI model, interface, database, or writing tool:

1. Separate domestic Chinese literature and international English literature when useful, but synthesize them in the final review.
2. Group papers by themes, mechanisms, data/methods, or conclusions instead of chronological summaries alone.
3. Extract each paper's research question, sample, method, key variables, conclusion, and limitation when information is available.
4. Compare agreements, disagreements, and boundary conditions across papers.
5. Identify what the user's thesis can add: new topic, new sample, new variable, new method, new mechanism, new heterogeneity, or updated period.
6. Do not invent citations, authors, journals, years, samples, or conclusions. Mark uncertain bibliographic details as needing verification.
7. When writing thesis prose, avoid annotated-bibliography style. Use paragraphs that synthesize multiple studies around one claim.
8. Keep the final contribution realistic for a master's thesis; do not overclaim originality.

## First Questions To Resolve

If the user has not provided them, infer cautiously and state assumptions:

- Thesis topic and core relationship, such as `X affects Y`.
- Research field: corporate finance, asset pricing, banking, fintech, ESG, green finance, risk management, behavioral finance, or macro-finance.
- Literature language scope: Chinese, English, or both.
- Target output: paper matrix, literature outline, written review, research gap, marginal contribution, or citation-ready paragraph.
- Citation style: Chinese thesis style, APA, MLA, Chicago, GB/T 7714, or school template.

Ask a direct question only when the missing information materially changes the review structure.

## Output Shape

For literature review tasks, return:

1. Search keywords in Chinese and English.
2. Literature classification framework.
3. Literature matrix fields to extract.
4. Theme-by-theme synthesis.
5. Theory and mechanism summary.
6. Comparison of empirical findings.
7. Limitations of existing research.
8. Research gap suitable for the user's thesis.
9. Marginal contribution written conservatively.
10. Suggested thesis section outline or thesis-ready prose.

For reviewing existing literature text, lead with problems and fixes: paper-by-paper listing, weak synthesis, missing foreign literature, unclear mechanism, unsupported contribution, outdated sources, citation inconsistency, or overclaiming.

## Literature Classification Patterns

Choose categories that match the topic:

- By research object: firms, banks, funds, investors, cities, industries, markets, policies.
- By explanatory variable: policy shock, digital finance, ESG, green finance, governance, analyst coverage, financial constraints, institutional ownership.
- By outcome variable: firm value, innovation, risk-taking, financing cost, investment efficiency, liquidity, crash risk, stock returns, performance.
- By mechanism: financing constraints, information asymmetry, governance, innovation, risk, resource allocation, market attention, environmental responsibility.
- By method: OLS, panel FE, DID, event study, IV, PSM, factor model, portfolio sort, text analysis.
- By conclusion: positive effect, negative effect, nonlinear effect, insignificant effect, mixed evidence.

## Thesis Writing Standards

When generating literature review prose:

- Start each paragraph with a theme claim, not an author name.
- Use multiple papers to support or contrast the claim.
- Explain why findings differ when possible: sample, period, country, variable proxy, identification method, or institutional context.
- End major sections with a short evaluation of what remains unresolved.
- Connect the research gap directly to the user's thesis design.

## Reference Use

When the task needs deeper structure, load `references/literature_review_framework.md` for:

- Literature matrix templates.
- Theme classification menus.
- Mechanism extraction prompts.
- Research gap and marginal contribution templates.
- Common problems in finance thesis literature reviews.
- Chinese and English paragraph templates.

## Quality Checks

Before finalizing a literature review:

- Check that each cited paper supports the claim made about it.
- Check that the review synthesizes themes instead of listing summaries.
- Check that Chinese and English literature are not isolated without comparison.
- Check that mechanisms connect to the later empirical design.
- Check that the research gap follows from the reviewed literature.
- Check that marginal contribution is specific and not exaggerated.
- Flag any citation details that require database verification.
