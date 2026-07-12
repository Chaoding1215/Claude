# Finance-0007: Factor Investing

**Date**: 2026-07-12
**Lesson**: `finance-0007-factor-investing.html`
**Track**: 财富管理（个人/家庭）

## What Was Covered

Four requirements for a valid factor (Fama-French criteria):
- **Persistent**: survives across time periods (multiple decades)
- **Pervasive**: holds across geographies, not just US market
- **Robust**: survives across specifications (different metrics for same factor)
- **Investable**: premium net of transaction costs and capacity constraints

Five core factors with empirical evidence:
1. **Market Beta** (CAPM 1964): 6.0% premium, t-stat 3.2 — baseline, everyone holds
2. **Size / SMB** (Fama-French 1993): 2.5% premium small vs large, t-stat 2.1 — weakened since publication; earnings-risk explanation
3. **Value / HML** (Fama-French 1993): 4.8% premium cheap vs expensive, t-stat 3.1 — most debated; disappeared 2007-2020, recovered 2021+; distress risk vs mispricing debate
4. **Momentum** (Jegadeesh & Titman 1993; Carhart 1997): 7.3% premium past 12-month winners, t-stat 4.5 — highest premium but behaviorally driven; susceptible to crashes (2009: momentum factor -83%)
5. **Profitability / RMW** (Fama-French 2015): 3.6% premium profitable vs unprofitable, t-stat 3.8 — most theoretically robust; quality flavor

Decade × Factor heatmap (1970s-2020s):
- Value strong in 1970s/1980s, weak in 2010s, recovered 2020s
- Momentum consistent except severe crash in 2009
- Profitability consistently positive across all decades
- Size was strongest in 1970s-1980s, mixed since

Factor correlation matrix (key insight):
- Value vs Momentum: **−0.51** — natural hedge pair; worst value decade tends to be best momentum decade
- This negative correlation is a core portfolio construction tool

Interactive tilt builder: four sliders (value/size/momentum/quality, each 0-100%) outputting:
- Expected annual alpha over market
- Tracking error (active risk)
- Maximum expected relative drawdown years

Factor risks (the "dark side"):
- **Timing risk**: Value factor had 13-year underperformance streak (2007-2020); requires conviction to hold
- **Crowding**: factor ETF assets grew 50x in 2010s; institutional crowding compresses premiums
- **Replication crisis**: Harvey, Liu & Zhu (2016) found 250+ factors — most are data-mined noise; adjusted t-stat threshold should be 3.0 not 2.0
- **Transaction costs**: momentum's high turnover (100-300%/yr) erodes net premium substantially
- **Theoretical debate**: risk-based explanations (Fama) vs behavioral explanations (Thaler) have different implications for persistence

ETF implementation table:
- US small-cap value: AVUV (Avantis, 0.25%) — AQR-methodology, tilts on value+profitability jointly
- US value (passive): VBR (Vanguard, 0.07%) — cheap but weaker factor loading
- US momentum: MTUM (iShares, 0.15%) — 12-month price momentum
- US quality: QUAL (iShares, 0.15%) — profitability + earnings quality screens
- International small-cap value: AVDV (Avantis, 0.36%) — best international factor fund
- A-share value tilt: 512890 (华宝中证价值ETF, 0.50%) — domestic option

## Non-Obvious Insights to Preserve

- The value/momentum −0.51 correlation means holding both simultaneously reduces factor-specific risk more than adding a third uncorrelated asset — they're a natural hedge that many retail factor investors miss
- The replication crisis (Harvey 2016) means most published factors are false positives: stick to the original five with 30+ years of data, not the 250+ in recent literature
- Factor premiums are partly compensation for bearing genuine pain: value investors sat through 13 years of underperformance vs growth; momentum investors lost 83% in 2009. The premium is the price of that psychological cost — it can't be arbitraged away easily
- Publication effect is real: the size premium has weakened materially since Fama-French 1993 published it, because capital flowed in. Newer, less published factors likely face the same fate.

## Series Progress

01 → Why allocation matters (Brinson 90%)
02 → MPT / efficient frontier (Markowitz)
03 → Classic models (60/40, All Weather, Permanent)
04 → Rebalancing mechanics
05 → Behavioral traps (DALBAR, loss aversion, disposition, recency)
06 → Chinese investor implementation
07 → Factor investing (Fama-French, momentum, profitability)

## Next Steps

Lesson #08 previewed at end of lesson 07: **退休提款与序列回报风险**
- 4% rule (Bengen 1994; Trinity Study 1998)
- Sequence-of-returns risk: same average return, different order → dramatically different outcomes
- Monte Carlo simulation: 10,000 scenarios replacing a single deterministic projection
- Dynamic withdrawal strategies (Guyton-Klinger, floor-and-upside)
- Application to Chinese investors (no Social Security analog; RMB inflation baseline)
