# Defence Spending Research: Strategic Posture Shifts & The 2026 U.S. National Defense Strategy

**Research Project Framework**  
*A Quantitative Investigation into Alliance Burden-Shifting, Capability Gaps, and Strategic Sentiment*

---

## 1. Executive Summary

Our world is changing rapidly. We are currently witnessing a shift in global power that will be reflected upon as a stark inflection point in geopolitical history. Through investigating the disruption depicted on the news, experienced on the high street, and felt at the fuel pump, this research aims to find order in the chaos.

State-level changes in both existing and increasingly dominant world powers have knock-on effects across the global economy — effects that are not always inherently obvious but can have extensive consequences for different economic players.

This study explores the political, economic, and military landscape to identify trends that illuminate the influence of the U.S. sentiment shift — as depicted in the **2026 National Defense Strategy (NDS)** — on the European region in particular. The central inquiry asks: *What is required to replace the defensive vacuum being created as these chess pieces move, and what are both the opportunities and risks arising from these factors?*

> *"The USA has long continued to be a hegemonic power across economic, political, military, and cultural domains. However... what do you do when your ally isn't your friend?"*

This research is designed to be useful for:
- **Investment opportunity discovery** — identifying structural demand shifts, sectoral rotations, and arbitrage gaps in defense-industrial and macro markets.
- **Academic knowledge development** — contributing novel empirical tests to defense economics, strategic studies, and computational social science.
- **Strategic understanding advancement** — providing data-grounded assessments of alliance credibility, deterrence viability, and force-structure adequacy.

---

## 2. Context: The 2026 National Defense Strategy & The Inflection Point

### 2.1 What is the 2026 NDS?

The 2026 U.S. National Defense Strategy represents a radical reorientation of American military posture. Key shifts include:

- **Hemispheric Primacy:** Elevating homeland and Western Hemisphere security above traditional great-power deterrence in Europe and Asia.
- **Theater Burden-Shifting:** Explicitly designating allies — particularly European NATO members — as the primary backfill for a potential "second conflict" scenario, while the U.S. focuses on a single major war.
- **The "Trump Corollary to the Monroe Doctrine":** A declaratory emphasis on U.S. dominance in the Americas, with reduced forward presence in other theaters.
- **Industrial Base Prioritization:** Continuity with the 2022 NDS emphasis on strengthening the defense industrial base, but with a geographic pivot.
- **Absence of Force Structure Specificity:** Noted by CSIS — the strategy declares hemispheric dominance as the "foremost priority" yet lacks discussion of force size, structure, or posture specifics required to achieve it.

### 2.2 Why Does This Matter?

Regardless of the stakeholder, this research is relevant because the outcomes of these strategic shifts have direct impacts on the production and transit of key resources in our globalised world.

It appears that Europe has grown too passive in its assumptions that allied dominant powers would remain part of the regional security infrastructure in perpetuity — an assumption curated in the years after WWII, when the Western world was assisted and protected by the U.S., which solidified its dominance through the Cold War period.

This post-war rebuilding era steamrolled our current world order of a U.S.-led Western alliance. These recent shifts have led to this alliance's priorities and future being shaped differently from the intentions of its creators.

The research does not aim to answer the normative question of whether the U.S. shift is justified. Instead, it looks at the pieces of the political, economic, and military chess board to ascertain — through thorough exploration — where these pieces will be moving, what is required to fill the defensive vacuum, and what opportunities and risks emerge.

---

## 3. Research Anchors & Literature Foundation

This project is grounded in recent peer-reviewed and policy literature:

| Author(s) / Source | Year | Contribution | Relevance to This Study |
|---|---|---|---|
| **George & Sandler** | 2024 | Spatial burden-sharing analysis in NATO; equipment spending shows greatest free-riding sensitivity. | Validates that threat proximity, not alliance rhetoric, drives capital investment. Provides the methodological anchor for RQ-A1. |
| **Benmelech & Monteiro** | 2025 (IMF WEO) | Defense spending increases lead to small, persistent long-term conflict decline, with **no short-term deterrent effect**. | Critical null result — spending is a slow-acting variable; posture and signals matter more for immediate stability. Anchors RQ-A3. |
| **IMF World Economic Outlook** | 2026 | Models defense-spending booms as macroeconomic shocks with modest deterrence effects but significant fiscal trade-offs. | Provides the macroeconomic framework for understanding how defense buildups crowd out social investment and alter debt trajectories. |
| **DGAP (German Council on Foreign Relations)** | 2025 | Europe would need €650–800 billion in additional investment by 2028 to close capability gaps, not just spending ratios. | Provides the empirical benchmark for RQ-C2 and the "One War Plus" assessment. |
| **RAND Corporation** | 2024–2025 | Comparative U.S.-China-Russia strategic competition framework; technological interoperability as the primary barrier to integrated deterrence. | Provides the schema for comparative whitepaper analysis (RQ-B2) and the interoperability lens for capability assessment. |
| **CSIS (Center for Strategic & International Studies)** | 2025 | Critique of the 2026 NDS for lacking force-size and posture specifics despite declaratory ambition. | Validates the "sentiment-action gap" concept central to RQ-B3. |
| **NATO STO (Science & Technology Organization)** | 2025 | Proceedings on LLM applications in military contexts, including sentiment analysis for information operations. | Validates the NLP methodology for RQ-B1. |
| **Gartzke** | 2007 | Deterrence emerges from credible power projection rather than pacifist preferences. | Theoretical anchor for RQ-C1 — combat history as a credibility signal. |
| **Dolan** | 2025 | Identifies technological incompatibility as the primary barrier to integrated deterrence, more important than spending levels. | Redirects analysis from pure spending to capability composition and interoperability. |
| **SIPRI / IISS Military Balance** | 2025 | Annual benchmarks for military expenditure and capability inventories. | External validation sources for dataset triangulation. |

---

## 4. Datasets: Assessment & Integration

### 4.1 Global Military Arsenal Dataset — Weapons Systems
**Source:** Kaggle (maulikgajera) | **Scale:** 10,000+ systems across 128 countries | **Files:** 2 (CSV + supplementary) | **Size:** ~959 KB

**Dimensions:**
- **Weapon Identity:** System name, variant/model, category (air, land, sea, missile, space), generation/era.
- **Specifications:** Technical parameters (weight, range, speed, caliber, crew size, payload).
- **Financial:** Unit cost, program cost, or export price.
- **Operational:** Current and historical operators by country, quantity in service, year introduced/retired.
- **Combat History:** Conflicts where the system was deployed, outcomes, operational notes.

**Strengths:** Granular system-level detail; cross-country operator mappings; combat deployment records. Exceptionally suited for capability-density calculations and interoperability analysis.

**Caveats:** Compiled/aggregated sourcing; cost figures should be treated as indicative (flyaway vs. lifecycle costs may be mixed); combat history is subjective and requires triangulation with UCDP/ACLED.

### 4.2 NATO Alliance Dataset
**Source:** Kaggle (maulikgajera) | **Scale:** 32 countries | **Files:** 3 | **Rows:** 10,700+

**File Structure:**
1. **NATO_1_Country_Stats.csv** (1,444 rows, 27 columns): Yearly economic & military statistics per NATO member, **1949–2024**.
2. **Equipment Inventory:** Individual equipment holdings per country.
3. **NATO Operations:** Mission records, outcomes, operational history.

**Likely Columns (Country Stats):**
- Economic: GDP, GDP growth, defense budget, defense spending as % of GDP.
- Military: Active personnel, reserve personnel, total force size.
- Temporal: Year, country membership status (founding vs. accession).
- Ratios: Personnel per capita, spending per soldier, equipment density metrics.

**Strengths:** 75-year time series — exceptional for longitudinal analysis. Tracks NATO burden-sharing, spending commitments, and force structures across the Cold War, post-Cold War drawdown, and the 2014/2022 inflection points.

**Caveats:** NATO-only scope; requires external data (SIPRI, Global Arsenal) for non-NATO benchmarking.

### 4.3 Tandem Integration Architecture

```
┌─────────────────────────────────────────────┐
│  NATO Alliance Dataset (Country Stats)        │
│  Macro: Budgets, personnel, GDP, time       │
│  1949–2024, 32 countries                      │
├─────────────────────────────────────────────┤
│  Global Military Arsenal Dataset              │
│  Micro: Individual weapon systems             │
│  Specs, costs, operators, combat              │
│  128 countries, 10,000+ systems               │
├─────────────────────────────────────────────┤
│  Strategic Document Corpus (NLP Layer)        │
│  U.S. NSS/NDS/QDR, Chinese Defense White      │
│  Papers, Russian Military Doctrines, etc.    │
│  1993–2026                                    │
└─────────────────────────────────────────────┘
```

**Natural Join Points:**
- **Country Name:** 32 NATO members (NATO) ↔ 128 global operators (Arsenal).
- **Year:** Annual time series (NATO) ↔ likely snapshot/current (Arsenal) — requires cross-sectional overlay.
- **Equipment Category:** Aggregated counts (NATO Equipment Inventory) ↔ individual system records (Arsenal).

---

## 5. Research Questions: Comprehensive Framework

### A. Macro-Strategic & Expenditure Dynamics

---

#### **RQ-A1: The "Offensive Posture Premium"**

*Does a measurable "offensive posture premium" exist in defense spending — i.e., do states shifting from deterrence-by-denial to power-projection exhibit discontinuous jumps in equipment vs. personnel spending ratios?*

**Methodology:**
- Code posture shifts from strategic documents (see Section B).
- Apply structural break tests (Chow, Bai-Perron) to NATO Country Stats (1949–2024).
- Test for discontinuities in:
  - Equipment spending / total defense spending
  - O&M spending / personnel spending
  - Force density per dollar (active personnel per $1B)
- Control for GDP, threat proximity, and alliance membership status.

**Expected Outputs:**
- Quantified "posture premium" coefficient.
- Timeline of structural breaks aligned with major strategy releases (1993 BUR, 2001 QDR, 2018 NDS, 2022 NDS, 2026 NDS).

**Relevance — Investment:**
An offensive posture shift is a **capital-structure signal** with direct sectoral implications. The marginal defense dollar flows toward platforms and precision munitions rather than personnel. This creates identifiable alpha in prime defense contractors (Lockheed Martin, RTX, Northrop Grumman, Rheinmetall, BAE Systems), precision-guided munition suppliers, and sovereign debt markets (long-dated capital commitments alter debt maturity profiles).

**Relevance — Academia:**
Tests whether Allison's organizational process models hold at the macro-alliance level: do air forces and navies capture budget share when strategic language shifts to "project" and "dominate"? Contributes to the literature on military innovation by quantifying the resource reallocation cost of posture change — a gap identified by George & Sandler (2024).

**Relevance — Strategic Understanding:**
Reveals whether offensive postures are actually affordable for mid-tier allies. If the premium requires 2–3× equipment spending ratios, the 2026 U.S. NDS shift to hemispheric dominance may be fiscally incompatible with simultaneous European burden-shifting — a critical insight for force designers.

---

#### **RQ-A2: Burden-Shifting as a Natural Experiment**

*When the U.S. explicitly shifts a theater responsibility to allies (e.g., Europe 2026), how quickly do regional partners backfill with spending and capability, and what determines the speed of adjustment?*

**Methodology:**
- Difference-in-differences design using the NATO dataset's 75-year panel.
- Treat the 2026 NDS announcement (or the 2022 Russo-Ukrainian war) as an exogenous shock.
- Compare European NATO members' spending trajectories against non-NATO European states (from SIPRI or Global Arsenal).
- **Key variable:** Capability composition — does the backfill match the U.S. capability being withdrawn? (e.g., if U.S. reduces ground forces in Europe, do allies increase MBT holdings or just personnel?)
- Spatial regression: threat proximity (distance to Russia) × alliance commitment → capability accumulation.

**Expected Outputs:**
- Speed-of-adjustment coefficients by country.
- Identification of "fast adjusters" (e.g., Poland, Baltics) vs. "laggards" (e.g., early-2010s Germany, pre-2022 Italy).
- Capability-mismatch index: gap between U.S. withdrawn capability and allied backfill.

**Relevance — Investment:**
A regime change with asymmetric equity implications. European defense industrials (Rheinmetall, Thales, Saab, Leonardo) have already surged ~40–60% since 2022, but the market may underprice which *specific* countries will backfill fastest. Infrastructure and logistics plays (basing, ammunition storage, railheads) spill into construction, energy, and materials equities. The IMF WEO (2026) models defense booms as macroeconomic shocks that crowd out social investment and raise deficits — identifying which states will deficit-finance the backfill creates sovereign debt positioning opportunities.

**Relevance — Academia:**
A rare natural experiment in collective action within an alliance. Olson's "free-rider" problem has been tested theoretically for decades but rarely with a clean exogenous shock and a 75-year panel. Applies difference-in-differences, synthetic control methods, or staggered treatment designs. Also speaks to hegemonic transition theory: does the withdrawal of a security guarantor trigger rapid balancing behavior, or does it create a power vacuum and buck-passing?

**Relevance — Strategic Understanding:**
Existential for NATO. If European allies cannot backfill U.S. capabilities at the speed the NDS assumes, the alliance faces a **deterrence gap** — a window of vulnerability measured in years, not decades. The DGAP analysis suggests Europe needs €650–800 billion in *additional* investment by 2028 to close capability gaps, not just spending ratios. This analysis quantifies whether the backfill is happening in **capabilities** (systems that matter) or just **spending** (accounting exercises).

---

#### **RQ-A3: Deterrence vs. Offense — The Conflict-Risk Paradox**

*Do defense spending buildups reduce short-term conflict risk (deterrence) or increase it (security dilemma / preemptive aggression)?*

**Methodology:**
- Use the Global Arsenal dataset's combat history field to test whether states with rapid capability accumulation (steep system-count growth) experience higher dispute initiation rates in the subsequent 5-year window.
- Control for spending levels, regime type, and geographic position.
- Cross-check against UCDP/ACLED conflict data.
- Test Benmelech & Monteiro (2025) finding: spending reduces long-term conflict risk but has no short-term effect.

**Expected Outputs:**
- Conflict-risk elasticity with respect to capability accumulation.
- Lag-structure analysis: at what time horizon does spending become deterrent vs. provocative?
- Identification of "tipping point" thresholds where accumulation shifts from deterrent to threatening.

**Relevance — Investment:**
A **geopolitical risk pricing** question with portfolio-level implications. If buildups increase short-term conflict risk (security dilemma), commodity markets (oil, LNG, wheat, rare earths) should price in higher tail-risk. Insurance and reinsurance sectors face mispriced conflict-exposure portfolios. Defense stocks may exhibit a "war scare" volatility premium — rallying on spending news but selling off on actual conflict initiation, creating a tradable cyclicality.

**Relevance — Academia:**
A **causal inference** contribution to the central debate in security studies: does capability accumulation stabilize or destabilize? Tests the classic deterrence model (more capability = less war) against the security dilemma spiral (more capability = more fear = more war). Using combat history as an outcome variable moves beyond theoretical modeling to large-n empirical testing — a methodological advance in a field historically reliant on case studies.

**Relevance — Strategic Understanding:**
The most consequential question for policymakers. If spending buildups have **no short-term deterrent effect**, then the current U.S. and European surge may not prevent a 2027–2028 Taiwan Strait or Baltic contingency. It implies that **posture, signaling, and diplomacy** matter more than budget size for immediate stability — a finding that would fundamentally reshape how the 2026 NDS is evaluated.

---

### B. Natural Language Processing (NLP) & Text-Based Strategic Sentiment

---

#### **RQ-B1: Whitepaper Sentiment as a Leading Indicator**

*Can the sentiment trajectory of U.S. National Security Strategy / NDS documents predict the direction of force posture changes 3–5 years ahead?*

**Methodology:**
- Build a corpus of U.S. strategy documents (NSS, NDS, QDR, BUR) from 1993–2026.
- Apply NLP sentiment analysis and topic modeling using transformer-based models (FinBERT derivatives, RoBERTa) fine-tuned on policy text.
- **Specific variables to extract:**
  - **Offensive vs. defensive lexical ratio:** Stems like "project," "dominate," "strike," "preempt" vs. "defend," "deter," "shield," "resilience."
  - **Threat inflation index:** Frequency of existential threat language normalized by document length.
  - **Burden-shifting sentiment:** Tone when describing allies (collaborative vs. transactional vs. dismissive).
  - **Geographic priority entropy:** Shannon entropy of region mentions — low entropy = concentrated focus (e.g., 2026 NDS is heavily Western Hemisphere-skewed).
- Validate against human coding of a random sample.
- Correlate sentiment shifts with subsequent budget allocations from the NATO dataset.

**Expected Outputs:**
- Time-series sentiment scores (1993–2026).
- Granger causality tests: does sentiment lead spending, or vice versa?
- Predictive model: sentiment trajectory → equipment spending composition (3–5 year lag).

**Relevance — Investment:**
Creates a **systematic, tradable signal** from unstructured text. If sentiment predicts equipment spending composition, this is an **event-driven hedge fund strategy**:
- **Sector rotation:** When "offensive" lexical density rises, overweight naval/aerospace; when "defensive" density rises, overweight missile defense and ground forces.
- **M&A prediction:** Strategic posture shifts drive defense industry consolidation around priority capabilities. Identifying target capabilities before they appear in budget documents creates private equity and venture capital entry points.
- **Defense tech VC:** The 2026 NDS emphasizes AI, autonomous systems, and space. Sentiment analysis identifies when these themes move from peripheral to central in strategy discourse — an early signal for startup investment timing.

**Relevance — Academia:**
Sits on the frontier of **computational social science** and **international relations**. Tests whether **declaratory strategy** has predictive validity or is merely epiphenomenal. The NATO STO proceedings (2025) explicitly identify sentiment analysis as a validated application of LLMs in military contexts. Contributes a longitudinal, quantitative corpus study to a field that has relied on qualitative hermeneutics (e.g., Freedman's "Strategic Studies" tradition). Also bridges **policy implementation theory**: do words actually lead to resource flows?

**Relevance — Strategic Understanding:**
If sentiment is a leading indicator, it becomes an **early warning system** for allies and adversaries alike. A sudden shift in U.S. whitepaper sentiment toward "hemispheric dominance" without corresponding Pacific force reductions would signal a **capability-lag risk** — the strategy has shifted but the force hasn't. For adversaries, tracking sentiment trajectories provides a more granular threat assessment than waiting for budget releases.

---

#### **RQ-B2: Comparative Whitepaper Analysis — Is It Worthwhile?**

*How do U.S., Chinese, Russian, and European defense whitepapers differ in strategic culture, threat framing, and capability prioritization — and do these differences predict capability trajectories?*

**Methodology:**
- Scrape comparable strategy documents: Chinese Defense White Papers, Russian Military Doctrines, UK Strategic Defence Reviews, French National Strategic Reviews.
- Code each whitepaper using the RAND comparative framework for U.S.-China-Russia strategic competition:
  - Primary theater of concern
  - Preferred instrument of power (military vs. economic vs. information)
  - Alliance dependency framing (self-reliant vs. collective)
- Apply lexical convergence/divergence analysis: do adversaries mirror each other's threat language?
- **Temporal responsiveness:** How quickly does each state adjust its declaratory posture to the other's shifts? (lag analysis)
- Correlate with Global Arsenal dataset operator patterns.

**Expected Outputs:**
- Strategic culture quantification index by country.
- Lexical convergence/divergence heatmap over time.
- Lag-structure: days/months between a U.S. posture shift and responsive language in Chinese/Russian documents.

**Relevance — Investment:**
Reveals **technological convergence and divergence** — direct inputs for patent/IP strategy and cross-border defense M&A:
- If Chinese and U.S. whitepapers converge on "autonomous systems" and "space dominance," the **dual-use technology sector** faces synchronized demand from both superpowers, creating a global investment boom.
- If they diverge — U.S. emphasizes "allied interoperability" while China emphasizes "self-reliance" — then **supply chain bifurcation** is accelerating. This creates opportunities in reshoring/friend-shoring plays and risks in companies with China-dependent defense revenue.
- **Russian whitepaper sentiment** (constrained by sanctions) can signal where Moscow is ceding technological competition, creating secondhand market opportunities for ex-Russian equipment buyers.

**Relevance — Academia:**
Contributes to **comparative foreign policy analysis** and **strategic culture quantification**. The literature on strategic culture (Gray, Johnston, Katzenstein) has been criticized for being unfalsifiable. By coding whitepapers for lexical patterns and correlating them with capability trajectories from the Global Arsenal dataset, this creates a **testable operationalization** of strategic culture.

**Relevance — Strategic Understanding:**
Prevents **mirror-imaging** — the cognitive trap of assuming adversaries share your decision logic. If the U.S. whitepaper frames allies as "burden-sharers" while Chinese whitepapers frame partnerships as "strategic alignment against hegemony," then U.S. expectations of Chinese isolation may be misplaced. Also reveals **responsive strategy**: fast responsiveness suggests agile strategic planning; slow responsiveness suggests bureaucratic sclerosis or hidden intent.

---

#### **RQ-B3: The Sentiment-Action Gap**

*How large is the gap between declaratory sentiment (whitepaper rhetoric) and actual capability deployment (dataset operators + combat history)?*

**Methodology:**
- Quantify the gap: **Sentiment-Capability Delta** = (Offensive sentiment score × budget growth) / (Actual force structure change in dataset).
- High delta = "all talk, no walk"; low delta = "quiet buildup."
- Track the gap across administrations (Clinton, Bush, Obama, Trump I, Biden, Trump II).
- Cross-reference with IISS Military Balance assessments for external validation.

**Expected Outputs:**
- Sentiment-action gap index by administration and by country.
- Identification of "performative militarism" vs. "genuine military-industrial expansion."
- Predictive model: which gap patterns precede strategic surprises or credibility crises?

**Relevance — Investment:**
An **arbitrage opportunity** between rhetoric-driven market pricing and fundamentals:
- **Sovereign credit ratings:** Agencies often lag in adjusting ratings for defense-spending commitments. If a country's whitepaper is highly aggressive but its Global Arsenal dataset shows flat capability counts, the credit rating may overstate fiscal sustainability.
- **Defense contractor revenue predictability:** Contracts follow budgeted actions, not words. A wide sentiment-action gap means defense stocks may be overpriced on rhetoric-driven enthusiasm.
- **ESG and ethical investing:** As defense spending rises, ESG funds face pressure to divest. The sentiment-action gap helps distinguish between states with genuine military-industrial expansion (higher ESG controversy risk) and states with performative militarism (lower actual risk).

**Relevance — Academia:**
Speaks to a core tension in **organizational theory** and **public policy implementation**: the gap between discourse and practice. Tests whether **strategic documents are performative** (aimed at domestic audiences or adversary signaling) or **instrumental** (actual planning tools). The 2026 NDS has been criticized by CSIS for lacking force-size specifics — a clear sentiment-action gap. Quantifying this across multiple states and time periods creates a new dependent variable for implementation studies.

**Relevance — Strategic Understanding:**
The **most policy-relevant question** of the entire set. A wide sentiment-action gap creates **strategic miscalculation risk**: adversaries may believe declaratory posture and act preemptively, or allies may believe commitments and under-prepare. If the 2026 NDS declares hemispheric dominance as the "foremost priority" but the dataset shows no Pacific force reduction or Western Hemisphere force increase, then the strategy is **hollow** — and adversaries will eventually test it.

---

### C. System-Level & Operational Research Questions

---

#### **RQ-C1: Capability Churn vs. Strategic Persistence**

*Do states undergoing posture shifts exhibit higher "capability churn" (rapid retirement + acquisition of new systems) or do they persist with legacy platforms and re-role them?*

**Methodology:**
- Use Global Arsenal dataset year introduced/retired fields to calculate churn rates by country and by administration.
- Cross-reference with NATO Country Stats personnel trends.
- Test whether posture shifts (coded from RQ-B1) correlate with churn spikes.
- **Example:** The U.S. is reportedly shifting from ground forces in Korea to missile defense. Does the dataset show Patriot/THAAD acquisitions increasing while Army MBT counts in PACOM remain flat?

**Expected Outputs:**
- Capability churn index by country and time period.
- "Re-roling ratio" — legacy platforms assigned new missions vs. new platform acquisitions.
- Cost comparison: churn cost vs. persistence cost over a 10-year lifecycle.

**Relevance — Investment:**
A **platform lifecycle and aftermarket** investment question:
- **Legacy sustainment plays:** If states persist with legacy platforms, then **defense aftermarket and upgrade** companies (Elbit, L3Harris, Rafael) see sustained demand.
- **Obsolescence risk:** If states favor churn, then **new platform developers** capture share, but incumbents with legacy portfolios face revenue cliffs.
- **Secondary markets:** Rapid churn creates surplus equipment flows. The Global Arsenal dataset's operator history can identify which legacy platforms are being offloaded — creating opportunities in the **refurbished defense export market** (e.g., ex-European Leopard 2s to Southeast Asia).

**Relevance — Academia:**
Tests theories of **military innovation and organizational learning**. Does rapid capability churn indicate organizational adaptability (Posen's "military innovation") or strategic incoherence (constant reorganization without mastery)? Also speaks to **path dependency** in weapons acquisition: are states locked into platform families by sunk costs and industrial bases, or can they pivot cleanly? The literature on military transformation (e.g., Farrell & Terriff) lacks large-n empirical tests — these datasets provide one.

**Relevance — Strategic Understanding:**
Force structure stability is critical for **readiness and credibility**. Too much churn = training pipeline collapse, maintenance expertise loss, and alliance interoperability breakdown. Too much persistence = obsolescence against peer adversaries. For the 2026 NDS, if the U.S. is shifting from ground forces to missile defense but the dataset shows slow Patriot/THAAD acquisition relative to Abrams retirement, there is a **capability trough** — a window where the force is less capable than either the old or new posture intended.

---

#### **RQ-C2: Combat History as a Deterrence Signal**

*Does a weapon system's combat history predict its export success and alliance adoption?*

**Methodology:**
- Use Global Arsenal dataset to identify systems with documented combat use (e.g., F-16, HIMARS, Bayraktar TB2, Javelin).
- Model adoption curves among NATO members, controlling for unit cost, range, payload, and generation.
- Test whether combat-proven systems see faster adoption than systems without combat validation at the same price/performance tier.
- Cross-reference with NATO Operations data: were these systems deployed together in missions?

**Expected Outputs:**
- Combat-validation premium coefficient (adoption speed increase attributable to combat history).
- Price premium elasticity: how much more are allies willing to pay for combat-proven systems?
- Interoperability clustering: which combat-proven systems create "platform families" across the alliance?

**Relevance — Investment:**
Combat history is a **market validation signal** in defense procurement:
- **Export market sizing:** Systems with documented combat success see faster adoption curves. The Global Arsenal dataset can quantify this, creating predictive models for which platforms will generate follow-on orders.
- **Platform valuation premiums:** Combat-proven platforms command 20–40% price premiums in export markets. Identifying which systems are approaching "combat validation" status allows early positioning in supplier equities.
- **Insurance and risk:** Systems without combat history carry higher operational risk for buyer nations. This affects export credit agency pricing and sovereign buyer creditworthiness.

**Relevance — Academia:**
An empirical test of **signaling theory in international relations**. Gartzke (2007) argues that deterrence emerges from credible power projection rather than pacifist preferences; combat history is the ultimate credibility signal. Tests whether alliance adoption is driven by **material capability** (range, payload, cost) or **reputational signaling** (combat use). Also contributes to the literature on **weapons diffusion**: what determines which systems proliferate?

**Relevance — Strategic Understanding:**
Informs **procurement rationality**. Militaries face a constant tension between buying **combat-proven** systems (lower risk, higher interoperability) and **cutting-edge** systems (potential overmatch, higher obsolescence risk). If the data shows that combat history is the dominant predictor of alliance adoption, then the 2026 NDS emphasis on "new capabilities" (AI, autonomous systems) may face adoption resistance from allies who prefer proven platforms — undermining interoperability goals.

---

#### **RQ-C3: The "One War Plus" Force Sizing Model**

*Under the 2026 NDS "one war + ally burden" framework, does the aggregate NATO capability dataset support the assumption that allies can credibly handle a second theater?*

**Methodology:**
- Aggregate the Global Arsenal dataset by NATO region (European NATO vs. U.S. Pacific holdings).
- Compare European NATO total MBT, fighter, and naval tonnage counts against U.S. Indo-Pacific holdings.
- Calculate **capability density per dollar**: European NATO total systems / European NATO total defense spending vs. U.S. Pacific systems / U.S. Pacific spending.
- Cross-reference with DGAP's €650–800 billion gap estimate.
- Model scenarios: if the U.S. is committed to one war (e.g., Indo-Pacific), can European NATO autonomously defend against a second war (e.g., Baltic/Russian)?

**Expected Outputs:**
- European NATO autonomous defense capability index.
- Capability gap by domain (land, air, sea, space, cyber).
- Force-sizing model: what would European NATO need to acquire/retain to credibly handle a second theater?
- Fiscal feasibility assessment: can the gap be closed by 2028, 2030, or 2035 at current spending trajectories?

**Relevance — Investment:**
The **largest absolute capital implications** of any question:
- **European defense industrial base:** If the analysis shows Europe cannot credibly handle autonomous conventional defense, the DGAP investment gap becomes a **structural demand floor** for European defense contractors through 2035.
- **U.S. Pacific pivot plays:** If the "one war" assumption holds, U.S. force structure shifts to the Indo-Pacific are credible, and **Pacific logistics, basing, and naval/aerospace** equities see sustained demand. If the assumption fails, the U.S. must either reverse the pivot (bad for Pacific plays) or accept extreme risk (bad for global risk assets).
- **Infrastructure:** A credible European pillar requires new ammunition plants, rail logistics, and energy resilience. This is a **greenfield infrastructure** opportunity.

**Relevance — Academia:**
Tests **extended deterrence and alliance credibility theory** at the highest stakes. The literature on "cumulative deterrence" vs. "sequential deterrence" (can you deter one adversary while fighting another?) has been theoretical since the Cold War. This analysis allows a **quantitative capability audit** of the assumption. Also contributes to **force sizing models**: how much capability is "enough" for autonomous defense?

**Relevance — Strategic Understanding:**
**Existential for NATO and U.S. grand strategy.** If the 2026 NDS assumes allies can handle a second theater, but the Global Arsenal dataset shows European NATO lacks the MBT, fighter, and naval tonnage for autonomous high-intensity operations, then the entire strategic edifice is built on a false premise. The next administration — or the current one, if data is presented credibly — must either:
1. Reverse the burden-shift,
2. Accept catastrophic risk in a two-theater scenario, or
3. Fund a European capability surge that the U.S. currently shows no appetite for.

This analysis can provide the **empirical foundation** for this debate.

---

## 6. Cross-Cutting Variables: More Pressing Than Whitepapers Alone

While comparative whitepaper analysis is valuable, the recent literature suggests these variables are **more causally potent** and should be treated as primary controls:

| Variable | Why It Matters | Source Integration |
|---|---|---|
| **Spatial threat proximity** | George & Sandler (2024) show NATO allies nearest Russia increased operational spending post-2014; geography trumps alliance rhetoric. | Merge NATO dataset with distance-to-threat (Russia border, South China Sea). |
| **Fiscal space / debt capacity** | IMF WEO shows defense booms financed by deficit spending crowd out social investment and create medium-term instability. | NATO Country Stats GDP/debt + defense budget. |
| **Industrial base capacity** | The 2026 NDS emphasizes "strengthening the industrial base" as continuity; France's 2025 Strategic Review aims for an "economy prepared for war" by 2030. | Use Global Arsenal unit costs as a proxy for domestic production capacity (can they afford their own gear?). |
| **Allied interoperability** | Dolan (2025) identifies technological incompatibility as the primary barrier to integrated deterrence — more important than spending levels. | Global Arsenal dataset operator overlap (who shares platforms?). |
| **AI/ML integration** | The capability-vulnerability paradox: AI enhances decision speed but introduces bias and attack surfaces. | Not directly in datasets, but can be proxied by precision-guided munition % of arsenal. |

---

## 7. Methodological Framework

### 7.1 Phase 1 — Corpus Construction (Weeks 1–2)
- Scrape all U.S. NSS/NDS/QDR/BUR documents (1993–2026).
- Scrape comparable Chinese Defense White Papers, Russian Military Doctrines, UK Strategic Defence Reviews, French National Strategic Reviews.
- Build a domain-specific lexicon for military posture sentiment (offensive / defensive / deterrent / burden-shifting).

### 7.2 Phase 2 — NLP Pipeline (Weeks 3–4)
- Use transformer-based models (BERT/RoBERTa fine-tuned on policy text) for sentiment and topic extraction.
- Generate time-series sentiment scores and threat-priority indices.
- Validate against human coding of a random sample.

### 7.3 Phase 3 — Quantitative Merge (Weeks 5–6)
- Join sentiment time-series with NATO Country Stats (annual, 1949–2024).
- Join capability aggregates from Global Military Arsenal Dataset.
- Run structural break tests (Chow / Bai-Perron) around major strategy releases.

### 7.4 Phase 4 — Causal Inference (Weeks 7–8)
- Difference-in-differences: posture shifts vs. spending composition.
- Granger causality: does sentiment lead spending, or vice versa?
- Spatial regression: threat proximity × alliance commitment → capability accumulation.

### 7.5 Phase 5 — Validation (Week 9)
- Cross-check combat history claims against UCDP/ACLED conflict data.
- Cross-check spending against SIPRI Military Expenditure Database.
- Triangulate whitepaper claims with IISS Military Balance assessments.

---

## 8. Risk, Limitations & Mitigations

| Challenge | Severity | Mitigation |
|---|---|---|
| **Year alignment** | Medium | Country Stats is annual 1949–2024; Arsenal dataset is likely a current snapshot. Join on "most recent year" or treat Arsenal as cross-sectional overlay. |
| **Country name standardization** | Low-Medium | Both datasets share the same curator, so naming conventions should be consistent. Still verify (e.g., "Türkiye" vs. "Turkey"). |
| **Cost comparability** | High | Global Arsenal unit costs may mix flyaway, production, and export prices. Normalize by cost category before cross-country comparison. |
| **Double-counting equipment** | Medium | If NATO Equipment Inventory and Global Arsenal both list holdings, decide source of truth. The curator may have designed them as separate views. |
| **Whitepaper sourcing opacity** | Medium | Chinese figures are known to underreport; Russian documents may be aspirational. Treat as declaratory discourse, not audit-grade data. |
| **NATO Operations granularity** | Unknown | Combat history in Global Arsenal is system-level; NATO Operations is mission-level. Joining requires mapping missions → systems deployed. |
| **Temporal endogeneity** | Medium | Strategy documents may be written *after* budget decisions, not before. Use Granger causality and lead-lag structures to disentangle. |

---

## 9. Expected Outputs & Deliverables

### 9.1 Academic Outputs
- **Working paper:** "The Offensive Posture Premium: Strategy, Spending, and Structural Breaks in NATO, 1949–2024."
- **Conference submission:** International Studies Association (ISA) or European Consortium for Political Research (ECPR).
- **Dataset publication:** Cleaned and merged dataset with documentation for replication.

### 9.2 Investment Outputs
- **Sector rotation signal:** Quarterly "Posture Premium" index derived from whitepaper sentiment + budget composition.
- **Capability gap dashboard:** European NATO autonomous defense feasibility tracker.
- **Arbitrage monitor:** Sentiment-Action Gap index by country and administration.

### 9.3 Strategic Outputs
- **Policy brief:** "Can Europe Handle a Second Theater? A Capability Audit of the 2026 NDS Assumptions."
- **Alliance readiness tracker:** Force-structure adequacy scorecard by NATO region.
- **Early warning system:** Strategic sentiment trajectory monitor for major powers.

---

## 10. Synthesis: Prioritization by Objective

| Your Primary Goal | Top-Tier RQs | Rationale |
|---|---|---|
| **Investment** | RQ-A2, RQ-B1, RQ-B3, RQ-C3 | These identify regime changes, systematic signals, arbitrage gaps, and structural demand floors with the clearest capital-market pathways. |
| **Academia** | RQ-A3, RQ-B1, RQ-B2, RQ-C1 | These offer methodological innovation (causal inference, NLP, comparative text analysis), theoretical testing (deterrence, strategic culture, organizational learning), and interdisciplinary bridging. |
| **Strategic Understanding** | RQ-A1, RQ-A3, RQ-B3, RQ-C3 | These expose affordability limits, conflict-risk paradoxes, credibility gaps, and alliance viability — the raw material of statecraft. |

---

## 11. The Central Question

> **"Does the sentiment-action gap in the 2026 U.S. strategic pivot predict a credible capability reallocation, or does it signal a deterrence deficit that allies must backfill — and can they?"**

This ties all three tiers together: NLP sentiment (Tier B), macro spending/personnel (Tier A), and system-level capability verification (Tier C). It is directly answerable with the two datasets plus publicly available strategy documents. The recent research consensus is clear: spending alone is a slow-acting deterrent, posture and signals matter more for short-term stability, and Europe's capability gaps are structural — not just fiscal.

This analysis can quantify exactly how large that gap is.

---

## 12. References

1. George, J. & Sandler, T. (2024). *NATO Burden Sharing: A Spatial Analysis.* Defence and Peace Economics.
2. Benmelech, E. & Monteiro, N. (2025). *Defense Spending and Conflict Risk.* IMF World Economic Outlook, April 2026.
3. International Monetary Fund. (2026). *World Economic Outlook: Defense Spending Booms and Macroeconomic Stability.*
4. German Council on Foreign Relations (DGAP). (2025). *Europe's Capability Gap: The €650–800 Billion Challenge.*
5. RAND Corporation. (2024–2025). *U.S.-China-Russia Strategic Competition Framework.*
6. Center for Strategic & International Studies (CSIS). (2025). *The 2026 National Defense Strategy: Continuity and Ambition.*
7. NATO Science & Technology Organization (STO). (2025). *Proceedings on LLM Applications in Military Contexts.*
8. Gartzke, E. (2007). *The Capitalist Peace.* American Journal of Political Science.
9. Dolan, B. (2025). *Technological Incompatibility and Integrated Deterrence.*
10. Stockholm International Peace Research Institute (SIPRI). (2025). *Military Expenditure Database.*
11. International Institute for Strategic Studies (IISS). (2025). *The Military Balance.*
12. Freedman, L. (2013). *Strategy: A History.* Oxford University Press.
13. Allison, G. (1971). *Essence of Decision: Explaining the Cuban Missile Crisis.* Little, Brown.
14. Olson, M. (1965). *The Logic of Collective Action.* Harvard University Press.
15. Posen, B. (1984). *The Sources of Military Change.* Cornell University Press.
16. Gray, C. (1999). *Modern Strategy.* Oxford University Press.
17. Johnston, A.I. (1995). *Cultural Realism: Strategic Culture and Grand Strategy in Chinese History.* Princeton University Press.

---

*Document compiled: May 2026*  
*Research framework for quantitative analysis of strategic posture shifts, alliance burden-sharing, and capability adequacy in the context of the 2026 U.S. National Defense Strategy.*
