# Solar Battery System
## Installation, Maintenance & Upgrade Guide

**Chi River House — Satuek, Buriram Province, Thailand**

*Two independent 5kW+ solar systems — one per floor — fully off-grid*

---

## 1. System Overview

The house runs on two completely independent solar systems, one powering the upstairs circuit and one powering the downstairs circuit. A fault or battery issue on one system does not affect the other.

All panels, inverters, and batteries are **PSI Energy** brand throughout — a matched, integrated installation.

| | **Upstairs System** | **Downstairs System** |
|---|---|---|
| Panels | 10 × PSI Energy 550W | 10 × PSI Energy 500W |
| Generation | 5.5kW | 5.0kW |
| Inverter | PSI Energy Hybrid Pro 6 (Sep 2023) | PSI Energy Hybrid Pro 6 (Apr 2023) |
| Batteries | 3 × PSI Energy LiFePO4 48V 100Ah | 2 × PSI Energy LiFePO4 48V 100Ah |
| Battery capacity | 14.4kWh total / 7.2kWh usable (50% DoD) | 9.6kWh total / 4.8kWh usable (50% DoD) |
| Status | ✅ Fully operational | ⚠️ Battery replacement required |

---

## 2. What Each System Powers

### 2.1 Upstairs System

- Master bedroom air conditioner
- South-facing bedroom air conditioner
- West-facing bedroom air conditioner
- Washing machine (upstairs shared bathroom)

> **💡 NOTE:** Guests should run the washing machine during daylight hours when solar panels are actively generating. Running it at night draws from battery storage and can significantly impact overnight reserves.

### 2.2 Downstairs System

- 4th bedroom (downstairs) air conditioner
- Great room — 2 × air conditioner units
- Refrigerator
- Booster pump (house water pressure)
- Fence lighting — 20 × 8W bulbs (auto dusk-to-dawn, ~160W continuous)

> **💡 NOTE:** Great room AC units work well for daytime cooling. To preserve overnight battery reserves, avoid running great room AC all night. All bedroom AC units can run overnight without issue.

---

## 3. Battery Technology — LiFePO4

Both systems use **Lithium Iron Phosphate (LiFePO4)** batteries — the premium chemistry for off-grid solar installations.

**Advantages over lead-acid:**
- Much longer cycle life — 2,000–4,000+ cycles vs 300–500 for lead-acid
- Safer chemistry — no risk of thermal runaway
- More efficient charge/discharge — less energy wasted as heat
- Better performance in high temperatures — important for Thailand's climate
- Flatter discharge curve — more usable capacity per charge

**Expected lifespan:**
- Rated cycle life: 2,000–4,000 cycles at 80% depth of discharge
- At approximately 1 cycle per day: **5–11 years** under normal conditions
- Calendar life: approximately **10–15 years**

**Key factor — heat:** Sustained high temperatures accelerate battery degradation. The battery room has no air conditioning. Monitor battery temperatures periodically and ensure adequate ventilation.

---

## 4. The Downstairs Battery Problem

### 4.1 Symptoms

- One battery consistently holds higher charge than the other (observed: 93% vs 74%)
- Batteries no longer reliably power the downstairs circuit overnight
- Premature failure — batteries are approximately 2 years old

### 4.2 Root Cause: Cell Imbalance

The two downstairs batteries are not properly balanced with each other. The inverter sees the combined bank voltage only — it has no visibility into individual battery state of charge. As a result:

- The higher battery reaches full voltage first → inverter stops charging → lower battery is chronically undercharged
- The lower battery hits low voltage first → inverter cuts off → usable capacity in the higher battery is stranded
- Over time, the lower battery never completes a full charge/discharge cycle → accelerated degradation

**Contributing factors likely include:**
- Unequal cable lengths between batteries causing resistance imbalance
- No battery balancer installed to equalize charge between individual batteries

---

## 5. The Fix — Both Systems

### 5.1 Equal Length Interconnect Cables

All cables connecting batteries within a bank must be **identical length and identical gauge (AWG)**. Unequal cable lengths create unequal resistance, which causes uneven current distribution and imbalance between batteries.

This applies to both the downstairs replacement bank and should be verified on the upstairs existing bank.

### 5.2 Inverter Cable Connection Point

The cable from the inverter to the battery bank should connect to the **middle battery** in a 3-battery bank — not to the first or last battery. This promotes more even current distribution across all three batteries naturally.

### 5.3 Active Battery Balancer

Install an **active battery balancer** on each battery bank. This device:

- Connects across each individual battery's terminals
- Continuously monitors voltage of each battery independently
- Transfers small amounts of current from higher-charged batteries to lower-charged ones
- Keeps all batteries in the bank at equal state of charge at all times
- Works automatically and continuously — no configuration required

**Why not passive?**
- Passive balancers dump excess energy as heat — wasteful
- Active balancers transfer energy between batteries — much more efficient

**Recommended brands:** Heltec, Daly
**Specification needed:** 48V LiFePO4 active balancer
**Approximate cost:** 700–1,500 THB per unit (~$20–$43)
**Units required:** 2 (one per system)

### 5.4 Summary of Required Work

| Task | Upstairs | Downstairs |
|---|---|---|
| Replace batteries | Not required | Replace 2 batteries with 3 × PSI Energy LiFePO4 48V 100Ah |
| Equal length cables | Verify and correct if needed | Install correctly with new battery bank |
| Inverter connects to middle battery | Verify | Install correctly |
| Active battery balancer | Install (preventive) | Install with new battery bank |

---

## 6. Overnight Load Analysis

### 6.1 Downstairs System — Estimated Nightly Consumption

| Load | Draw | Duration | Consumption |
|---|---|---|---|
| Fence lighting (20 × 8W) | 160W | 11 hrs (dusk to dawn) | 1.76kWh |
| Bedroom mini-split (maintaining temp) | ~80W | 8 hrs | 0.64kWh |
| Refrigerator (cycling) | ~65W average | All night | 0.52kWh |
| Misc standby | ~20W | All night | 0.18kWh |
| **Total overnight** | | | **~3.1kWh** |

### 6.2 Downstairs Battery Capacity (after upgrade to 3 batteries)

| Metric | Value |
|---|---|
| Total capacity | 3 × 48V 100Ah = 14.4kWh |
| Usable at 50% DoD (recommended) | 7.2kWh |
| Estimated overnight draw | ~3.1kWh |
| Remaining at dawn (before charging) | ~4.1kWh |
| Headroom | ✅ Comfortable margin |

> **50% Depth of Discharge (DoD):** LiFePO4 batteries can technically discharge to 80–90%, but staying above 50% significantly extends battery lifespan. The system should be configured to cut off at 50% DoD for longevity.

### 6.3 Upstairs System — Key Load Note

The washing machine draws 400–1,000W during operation. This is a significant but short-duration load. Always run during daylight hours to draw from panel generation rather than battery storage.

---

## 7. AC Units — Power Consumption Notes

All AC units are inverter-driven mini-split type. Power consumption varies significantly:

- **Cooling down (startup):** 400–600W per unit — high draw while reaching target temperature
- **Maintaining temperature (overnight):** 80–100W per unit — very low once stable
- **Great room units:** Recommended for daytime use only to preserve downstairs overnight battery reserves
- **Bedroom units:** Can run all night without issue on their respective systems

---

## 8. Solar Generation vs. Load

### 8.1 Daily Generation Estimate (Thailand)

Thailand receives approximately 4–5 peak sun hours per day on average.

| System | Panel Output | Peak Sun Hours | Daily Generation |
|---|---|---|---|
| Upstairs | 5.5kW | 4.5 hrs | ~24.75kWh |
| Downstairs | 5.0kW | 4.5 hrs | ~22.5kWh |
| **Combined** | **10.5kW** | | **~47kWh/day** |

On a normal sunny Thai day, both systems generate far more than the house consumes, with plenty of surplus to fully charge all batteries.

### 8.2 Cloudy Days

During extended cloudy periods (common during rainy season June–September):
- Generation can drop to 20–30% of rated output
- Battery reserves become important
- Prioritize bedroom AC over great room AC
- Run washing machine only when sun is visible

---

## 9. Battery Lifespan & Replacement Planning

| Factor | Detail |
|---|---|
| Expected cycle life | 2,000–4,000 cycles |
| At 1 cycle/day | 5–11 years |
| Early failure warning signs | Capacity drop, imbalance between batteries, longer charge times |
| Downstairs current issue | Premature failure at ~2 years due to imbalance — preventable with balancer |
| Replacement cost estimate | ~8,000–12,000 THB per battery (~$230–$345) |
| 3-battery bank replacement cost | ~24,000–36,000 THB (~$685–$1,030) |

---

## 10. Recommended Maintenance Schedule

| Task | Frequency | Notes |
|---|---|---|
| Check battery display readings | Monthly | All batteries in a bank should show similar voltage and charge % |
| Check battery terminal connections | Every 6 months | Tighten if loose, check for corrosion |
| Check inverter display for warnings | Monthly | Note any error codes |
| Inspect panel surfaces for dust/debris | Every 3 months | Clean with soft cloth and water if dusty |
| Check battery room ventilation | Every 6 months | Ensure airflow is not blocked |
| Full system performance check | Annually | Have installer verify all settings and connections |

---

## 11. Where to Purchase Replacement Parts in Thailand

- **PSI Energy batteries and panels:** Contact PSI Corporation Co., Ltd. — www.psi.co.th
- **Active battery balancers (Heltec, Daly):** Lazada Thailand, Shopee Thailand
- **General solar components:** Global House (บุรีรัมย์/สุรินทร์), HomePro, or solar specialist shops in Buriram city

---

> **✅ SUMMARY:** Install active battery balancers on both systems (700–1,500 THB each). Replace downstairs bank with 3 × PSI Energy LiFePO4 48V 100Ah batteries using equal length cables with inverter connected to middle battery. Upstairs system is fully operational — add balancer preventively. Run washing machine and great room AC during daylight hours only. Expected battery lifespan 5–11 years with proper balancing and 50% DoD discipline.
