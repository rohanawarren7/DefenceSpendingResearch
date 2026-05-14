# Defence Spending Research

## Intro
Our world is changing rapidly, we're currently witnessing a shift in global power that will be reflected on as a stark inflection point in geopolitcal history. 

Through the investigating the disruption that's depicted on the news, experienced on the high street and felt at the fuel pump, my aim is to see if we can see order in the chaos. 
These state level changes in both existing and growingly dominant world powers have knock on effects to other areas of the global economy which aren't always inherently obvious
but can have extensive effects on different economic players.

I want to explore the political, economic and militarial landscape to find trends that could be used to understand the influence of the US sentiment shift as depicted in the 2026 National Defense Strategy on the European region in particular. 

## What is the 2026 NDS?
...To Come

## Why Does This Matter?
Regardless of the stakeholder, this research study is relevant as the outcomes of what we're exploring have direct impacts on the production and transit of key resources in this globalised world.
It appears in Europe we have grown too passive in our assumptions that allied dominant powers would remain a part of the regional infrastructure in perpetuity, as was curated in the years after WWII ended when the Western World was assisted and protected by the US who solidified their dominance through the Cold War period. 

This post-war rebuilding era steam rolled our current world order of a US led Western alliance, these recent shifts have led to this alliance's priorities and future being shaped differently to the creators of these alliances.

*"The USA has long continued to be a hegemonic power across economic, political, militarial and cultural domains. However...what do you do when your ally is no longer your friend?"*

My aim isn't to answer this question but instead to look at the pieces of the political, economic and militarial chess board by ascertaining through thorough exploration where these chess pieces will be moving, what's required to replace the defensive vacuum that's being created as these pieces move and what are both the opportunites & risks due to these factors. This could be useful for deriving insights in areas such as finding investment opportunities, developing knowledge within academia or simply to further strategic understanding of world affairs.

## My Research Questions
### A - Macro-Strategic & Expenditure Dynamics
#### The "Offensive Posture Premium"
*Does a measurable "offensive posture premium" exist in defense spending — i.e, do states shifting from deterrence-by-denial to power-projection exhibit discontinuous jumps in equipment vs. personnel spending ratios?*

Why it matters: 
- The 2026 NDS shifts Europe to allies and pivots to hemispheric dominance. 
- Historically, offensive postures require higher capital-to-labor ratios (precision munitions, naval power projection, long-range strike). 
- Using the NATO Country Stats dataset (1949–2024), we can test whether posture shifts (coded from Strategic Sentiment - see B) precede structural breaks in:
-- Equipment spending / total defense spending
-- O&M spending / personnel spending
-- Force density per dollar (active personnel per $1B)

Recent research anchor: 
George & Sandler (2024) find equipment spending shows the greatest free-riding sensitivity, but post-2014 (Crimea), equipment free-riding declined — suggesting threat perception drives capital investment more than personnel.

#### Burden-Shifting as a Natural Experiment
*When the U.S. explicitly shifts a theater responsibility to allies (e.g., Europe 2026), how quickly do regional partners backfill with spending and capability, and what determines the speed of adjustment?*

The NATO dataset's 75-year panel allows a difference-in-differences design. Treat the 2026 NDS announcement (or the 2022 Russo-Ukrainian war) as a shock. Compare European NATO members' spending trajectories against non-NATO European states (from SIPRI or the Global Arsenal dataset).

Key variable: 
Not just spending % of GDP, but capability composition — does the backfill match the U.S. capability being withdrawn? (e.g., if U.S. reduces ground forces in Europe, do allies increase MBT holdings or just personnel?)

#### Deterrence vs. Offense: The Conflict-Risk Paradox
*Do defense spending buildups reduce short-term conflict risk (deterrence) or increase it (security dilemma / preemptive aggression)?*

Recent finding: 
Benmelech & Monteiro (2025), cited in the IMF WEO, show that increases in defense spending lead to a small and persistent decline in conflict over the long term, with no effect on short-term conflict risk. This is a critical null result for policy — it suggests spending itself is a slow-acting variable, and posture/signals matter more for immediate deterrence.

I could use the Global Arsenal dataset's combat history field to test whether states with rapid capability accumulation (steep system-count growth) experience higher dispute initiation rates in the subsequent 5-year window, controlling for spending levels.

### B - Natural Language Processing (NLP) & Text-Based Strategic Sentiment
*Can the sentiment trajectory of U.S. National Security Strategy/NDS documents predict the direction of force posture changes 3–5 years ahead?*

I will be applying NLP sentiment analysis and topic modeling. The literature confirms this methodolgy is viable: transformer-based models (FinBERT derivatives, RoBERTa) are already used for geopolitical media sentiment, and military applications of LLMs explicitly include sentiment analysis for information operations.

### C - System-Level & Operational Research Questions
*The "One War Plus" Force Sizing Model - Under the 2026 NDS "one war + ally burden" framework, does the aggregate NATO capability dataset support the assumption that allies can credibly handle a second theater?*

Aggregate the Global Arsenal dataset by NATO region. Compare European NATO total MBT, fighter, and naval tonnage counts against U.S. Pacific holdings. If the U.S. is shifting to a single-war assumption, is the European pillar actually capable of autonomous conventional defense? The DGAP analysis suggests Europe would need €650–800 billion in additional investment by 2028 to close capability gaps, not just spending ratios.



## Datasets
