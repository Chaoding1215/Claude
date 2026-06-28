# Finance-0006: Implementation for Chinese Investors

**Date**: 2026-06-28
**Lesson**: `finance-0006-implementation-china.html`
**Track**: 财富管理（个人/家庭）

## What Was Covered

Three market access channels:
1. Domestic brokerage (A-share ETFs, bond ETFs, gold ETFs) — easiest
2. QDII funds (US/global equity exposure via domestic platforms) — medium; subject to quota suspension
3. Overseas accounts (Futu, Tiger, IBKR) — lowest fees, widest choice; requires forex conversion

Instrument table by asset class:
- A-share: 510300 (CSI 300, 0.15%), 515210 (全A, 0.15%), 510500 (CSI 500, 0.20%)
- Global equities: 513100 (Nasdaq 100 QDII, 0.40%), 513500 (S&P 500 QDII, 0.40%), VTI (0.03% overseas)
- Domestic bonds: 511020 (7-10yr govt, 0.15%), 511010 (10yr govt, 0.15%), VGLT (overseas)
- Gold: 518880 (华安黄金ETF, 0.50%), 159937 (博时黄金ETF, 0.50%), IAU (0.25% overseas)
- Cash: 511990 (华宝添益E, 0.20%), 余额宝 (0.30%)

Portfolio builder: 3 models → specific ETF mapping + weighted fee calculation
- 60/40: ~0.26%/yr
- All Weather: ~0.24%/yr
- Permanent Portfolio: ~0.29%/yr

5-step construction guide: determine allocation → open accounts → initial lump-sum → monthly auto-invest → annual rebalancing reminder

Key facts:
- Fee compounding: 0.15% vs 1.5% fee over 30 years at 8% return → ~17万元 difference on 10万元 initial investment
- Lump-sum vs DCA: research favors lump-sum (opportunity cost of waiting), but DCA's behavioral benefit (removes monthly emotional decisions) is real and important

## Non-Obvious Insights to Preserve

- QDII funds periodically suspend new subscriptions due to SAFE forex quota limits — always check status before planning a purchase. This is a structural constraint unique to Chinese investors.
- Commodity exposure (大宗商品) is the hardest component to replicate domestically — the All Weather model's 7.5% commodities is often substituted with additional gold or omitted for domestic portfolios.
- 境外账户 annual forex quota is $50,000 USD (个人结汇额度) — sufficient for most personal investors but needs planning for larger portfolios.

## Series Completion

Six-lesson core series is now complete. User has covered:
01 → Why allocation matters (Brinson 90%)
02 → MPT / efficient frontier (Markowitz)
03 → Classic models (60/40, All Weather, Permanent)
04 → Rebalancing mechanics
05 → Behavioral traps (DALBAR, loss aversion, disposition, recency)
06 → Chinese investor implementation

## Next Steps (if user continues)

Possible future lessons:
- Factor investing: value, momentum, quality tilts on top of base models
- Monte Carlo retirement planning: withdrawal rates, sequence-of-returns risk
- Tax optimization: tax-loss harvesting, timing of rebalancing
- Chinese-specific: RMB currency risk, A-share characteristics vs global markets
