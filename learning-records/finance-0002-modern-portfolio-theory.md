# Finance-0002: Modern Portfolio Theory

**Date**: 2026-06-27
**Lesson**: `finance-0002-modern-portfolio-theory.html`
**Track**: 财富管理（个人/家庭）

## What Was Covered

- Harry Markowitz (1952) — Nobel Prize 1990, "Portfolio Selection"
- Correlation coefficient ρ: the key variable for diversification
  - ρ = 1: no diversification benefit (portfolio σ = weighted average)
  - ρ = 0: significant benefit
  - ρ = −1: maximum benefit (theoretical zero-risk possible)
- Portfolio variance formula (conceptually): reduces due to covariance term when ρ < 1
- Interactive slider: 50% stocks (σ=20%) + 50% bonds (σ=8%) — shows actual vs naive σ at any ρ
- Efficient frontier: set of portfolios with maximum return per unit of risk
  - Visualized as canvas chart with MVP, 100% stocks, 100% bonds labeled
  - Feasible region shaded below the frontier
  - Minimum variance portfolio identified
- Real-world correlation table: stocks/bonds (≈-0.2 to 0), stocks/gold (≈0.0-0.1), stocks/intl (≈0.7-0.85)

## Non-Obvious Insights to Preserve

- The efficient frontier shifts when ρ changes — lower ρ pushes the frontier further left (more risk reduction possible). The static chart uses ρ = 0.10.
- Correlations are NOT stable: during financial crises (2008, 2020 COVID crash), many assets that were previously uncorrelated became highly correlated simultaneously — this is called "correlation breakdown" and is a known limitation of MPT.
- The minimum variance portfolio is NOT the optimal portfolio for most investors — it has the lowest volatility but also lower return. The right point on the frontier depends on time horizon and risk capacity.

## Zone of Proximal Development — Next Steps

Ready for:
- Classic portfolio models: 60/40, All Weather (Dalio), Permanent Portfolio (Browne) — lesson 3
- How to choose where on the efficient frontier to sit (risk capacity, not just tolerance)

NOT yet ready for:
- Correlation breakdown / tail risk
- Monte Carlo simulation
- Factor models (Fama-French)
