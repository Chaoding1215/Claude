# Finance-0008: Retirement Withdrawal & Sequence-of-Returns Risk

**Date**: 2026-07-12
**Lesson**: `finance-0008-retirement-withdrawal.html`
**Track**: 财富管理（个人/家庭）

## What Was Covered

### 4% Rule Origins
- Bengen (1994): tested every historical retirement cohort 1926-1992, found 4% survives worst-case 30-year period with 50-75% stock allocation
- Trinity Study (1998) expanded to full success-rate matrix: stock%, withdrawal rate × historical 30-yr windows
- Key Trinity finding: 75% stock + 4% withdrawal = 98% historical success rate; 0% stock + 4% = only 25% success → bonds alone are not safe in retirement

### Sequence of Returns Risk
- Same arithmetic average return, different order → radically different 30-year terminal values (2-4x difference)
- **Accumulation phase**: sequence is irrelevant; only geometric mean matters; early bear markets are a gift (DCA buys more shares cheap)
- **Withdrawal phase**: sequence is critical; fixed withdrawals force selling at market lows → permanently shrinks base → later bull market cannot recover the loss
- The tragedy of bad luck: 1999 retirees vs 2009 retirees — same savings, same plan, dramatically different outcomes

### Monte Carlo vs Historical Backtesting
- Historical backtesting: ~70 non-overlapping 30-year windows since 1926; real paths but limited sample
- Monte Carlo: generates 10,000 random paths from statistical parameters (μ, σ, correlation); can produce tail scenarios never seen historically
- Best practice: run both, use the more conservative result as planning baseline

### Dynamic Withdrawal Strategies
1. **Fixed Amount (Bengen)**: year-1 take 4% of initial, inflate by CPI each year; predictable but market-agnostic
2. **Guyton-Klinger Guardrails**: set a 4-6% "safe zone"; if withdrawal rate drifts above 6% (bad market) → cut 10%; if below 4% (bull market) → increase 10%. Monte Carlo success rate rises to ~97%.
3. **CAPE-based (Pfau 2012)**: withdrawal rate ≈ 1/CAPE × 0.5; market-valuation-responsive; higher CAPE → lower withdrawals

### Chinese Investor Specifics
- No Social Security analog as income floor; basic pension replacement rate ~40-45% (lower for high earners)
- 个人养老金 (IRA-equivalent) cap: 12,000 RMB/year — far below US 401k limits
- A-share volatility σ≈30% vs US σ≈15%; 13-year 2007-2020 period of near-zero A-share returns
- Recommended adjustment: use 3-3.5% safe withdrawal rate for pure A-share portfolio; global diversification allows 4%
- Medical cost inflation in China historically ~10%/year — budget separately

## Non-Obvious Insights to Preserve

- **The accumulation/decumulation asymmetry** is underappreciated: the same investor who should ignore market crashes during accumulation must respond to them during withdrawal. The shift from "stay the course" to "reduce spending in downturns" is a fundamental behavioral gear-shift, not a minor adjustment.
- **4% is not a law**: it's based on one country's historical data with a known anomaly (US outperformed every other developed market for 100 years). Pfau estimates that for today's low-yield environment, 3% is more appropriate. Citing 4% as a universal truth is a common advice industry error.
- **Guardrails beat fixed**: Guyton-Klinger allows more lifetime spending AND higher success rates than fixed 4%, because it actually responds to market reality instead of ignoring it. The income variability cost is worthwhile.
- **Ruin is asymmetric**: running out of money at 85 is catastrophic; dying with money left is only "sub-optimal." This asymmetry justifies taking the conservative route and accepting a 10-20% expected surplus portfolio at death in exchange for near-zero ruin probability.
- **A-share retirement risk is severely underestimated in Chinese personal finance media**: the popular "3.5%被动收入" advice assumes China equity performance similar to US history, which is not supported by data.

## Series Progress

01 → Why allocation matters (Brinson 90%)
02 → MPT / efficient frontier (Markowitz)
03 → Classic models (60/40, All Weather, Permanent)
04 → Rebalancing mechanics
05 → Behavioral traps (DALBAR, loss aversion, disposition, recency)
06 → Chinese investor implementation
07 → Factor investing (Fama-French, momentum, profitability)
08 → Retirement withdrawal & sequence risk (4% rule, Trinity Study, Monte Carlo, Guyton-Klinger)

## Next Steps

Lesson #09 previewed: **税务优化与税损收割**
- Tax-loss harvesting: mechanics, wash-sale rules, when it adds value
- Asset location strategy: which assets belong in tax-advantaged vs taxable accounts
- China-specific: 个税 rules for fund redemption gains, individual pension account tax benefits
- Tax-efficient rebalancing order: donate appreciated shares, harvest losses before year-end
