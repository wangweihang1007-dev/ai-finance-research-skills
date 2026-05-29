---
name: finance-thesis-writing-polisher
description: Model-agnostic finance master's thesis writing and polishing skill for any AI assistant or coding agent, including ChatGPT, Claude, Gemini, Codex, and other LLMs. Use when converting empirical finance designs, regression outputs, literature reviews, variable definitions, robustness tests, heterogeneity tests, mechanism tests, conclusions, and policy implications into thesis-ready Chinese or English academic prose with cautious claims, coherent structure, and defensible interpretation.
---

# Finance Thesis Writing Polisher

## Core Rule

This is a model-agnostic working standard for ChatGPT, Claude, Gemini, Codex, and other AI assistants. Turn finance empirical content into clear, cautious, thesis-ready academic writing.

```text
evidence -> interpretation -> limitation -> thesis wording
```

Do not beautify weak logic. Fix structure, claims, and empirical interpretation before polishing language.

## Universal Agent Rules

Apply these rules regardless of model, software, or interface:

1. Preserve the user's substantive meaning unless correcting a clear logic or evidence problem.
2. Match claims to evidence: association, support, consistency, or causal effect.
3. Avoid overclaiming with words such as "prove", "fully confirms", "eliminates", or "first ever" unless justified.
4. Use thesis-style transitions and paragraph structure.
5. Translate regression output into economic interpretation, not just significance statements.
6. Keep variable names, table numbers, hypotheses, and model names consistent.
7. Make limitations explicit when identification or data are imperfect.
8. Write in Chinese academic style by default if the user writes Chinese; write in English if requested.
9. Keep the tone formal, concise, and defensible.
10. Flag missing table numbers, undefined variables, or unsupported claims.

## First Questions To Resolve

Infer cautiously if missing:

- Target section: introduction, literature review, hypotheses, methodology, empirical results, robustness, heterogeneity, mechanism, conclusion, policy implications, abstract.
- Language: Chinese or English.
- Evidence base: regression table, bullet notes, model design, variable definitions, or rough draft.
- Required style: school template, journal style, GB/T 7714 citation context, or general master's thesis style.

Ask only when the target section or language is unclear.

## Output Shape

For polishing tasks, return:

1. Revised thesis-ready text.
2. Brief notes on major logic changes.
3. Claims that need evidence or citation verification.
4. Optional stronger/weaker wording alternatives when useful.

For converting results into prose, include:

1. What the coefficient means.
2. Whether it supports the hypothesis.
3. Economic interpretation.
4. Robustness or limitation.
5. Transition to the next empirical section.

## Writing Standards

Use compact academic prose:

- Topic sentence first.
- Evidence from table/model second.
- Interpretation third.
- Limitation or transition last.

Avoid:

- Paper-by-paper listing in literature review.
- Mechanical "significant at 1%" sentences without economic meaning.
- Unsupported causal language.
- Repeating the same phrase across every table.
- Policy recommendations that do not follow from the empirical findings.

## Reference Use

Load `references/writing_templates.md` when deeper structure is needed for:

- Chinese thesis paragraph templates.
- Regression result interpretation.
- Robustness, heterogeneity, and mechanism writing.
- Abstract, conclusion, and policy implication templates.
- Claim-strength wording ladder.

## Quality Checks

Before finalizing:

- Check that every empirical claim points to a result, table, or hypothesis.
- Check coefficient signs and significance are described correctly.
- Check causal wording matches identification strength.
- Check section transitions are coherent.
- Check terminology is consistent across the thesis.
- Flag any missing citation, variable definition, or table reference.
