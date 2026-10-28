# New articles. Edit freely; run `python3 tools/build.py` afterwards.
# Each: slug, cat, emoji, date (YYYY-MM), title, lead, sections[(h2, para, [bullets])], end=(heading, text)

NEW = [
dict(slug="stablecoins-banks-position", cat="Stablecoins", emoji="🪙", date="2026-10",
 title="Stablecoins Are Becoming Payment Infrastructure — Banks Need a Position",
 lead="Stablecoins have moved from a crypto-trading tool to a serious settlement option for cross-border payments, treasury and e-commerce. Banks do not have to issue one, but every bank needs a clear stance on how it will interact with them.",
 sections=[
 ("Why the Conversation Has Changed", "Regulation has given institutions something they lacked: a legal route to participate. Clear rules on reserves, redemption and licensing turn stablecoins from a risk topic into a product and infrastructure topic.", [
  "Faster, always-on settlement outside correspondent banking cut-off times",
  "Programmable money that can be embedded in treasury and supply-chain workflows",
  "Pressure on cross-border payment margins as corporates ask for alternatives"]),
 ("The Four Positions a Bank Can Take", "Most banks will land on one of four postures, and the choice should be deliberate rather than reactive.", [
  "<strong>Observe:</strong> monitor regulation and client demand, with no exposure",
  "<strong>Connect:</strong> on/off-ramp, custody and banking services for issuers and corporates",
  "<strong>Distribute:</strong> offer client access to regulated stablecoins within existing channels",
  "<strong>Issue:</strong> launch a bank-branded stablecoin or tokenized deposit"])],
 end=("The Bottom Line", "Doing nothing is also a position, and it is the one most likely to be decided by someone else. Start with a capability assessment: liquidity impact, compliance readiness, and which client segments will ask first.")),

dict(slug="stablecoin-regulation-compared", cat="Stablecoins", emoji="⚖️", date="2026-10",
 title="Stablecoin Regulation Compared: GENIUS Act, MiCA, Hong Kong and India's Cautious Path",
 lead="Stablecoin rules are arriving jurisdiction by jurisdiction, and they are not identical. For banks operating across borders, the differences in reserves, licensing and permitted issuers shape product design.",
 sections=[
 ("The Major Frameworks", "The headline regimes share a common philosophy — fully backed, redeemable, supervised — but diverge in the detail. Check each regulator's current text before acting, as implementation rules continue to evolve.", [
  "<strong>United States:</strong> the GENIUS Act, signed in 2025, creates a federal framework for payment stablecoins with reserve and disclosure requirements",
  "<strong>European Union:</strong> MiCA regulates e-money tokens and asset-referenced tokens, with authorisation and reserve rules",
  "<strong>Hong Kong:</strong> a licensing regime for fiat-referenced stablecoin issuers administered by the HKMA",
  "<strong>India:</strong> no dedicated stablecoin framework; the RBI has publicly voiced caution and favours its own CBDC"]),
 ("What This Means for Indian and APAC Banks", "Even where a home regulator is cautious, banks with global clients face foreign stablecoin rules indirectly through correspondent relationships, treasury clients and group entities.", [
  "Map which stablecoins your clients and counterparties already touch",
  "Build a jurisdiction matrix for permitted activities and reporting duties",
  "Align AML, sanctions and liquidity policies before demand arrives"])],
 end=("The Takeaway", "Regulatory divergence is a design constraint, not a blocker. Banks that document it now will move faster when their own regulator acts.")),

dict(slug="tokenized-deposits-vs-stablecoins", cat="Digital Assets", emoji="🏦", date="2026-09",
 title="Tokenized Deposits vs Stablecoins: Which Model Wins for Banks?",
 lead="Banks have two routes to on-chain money: tokenize their own deposits, or participate in stablecoin ecosystems. They are often presented as rivals; in practice they solve different problems.",
 sections=[
 ("How They Differ", "A tokenized deposit is a bank liability represented on a ledger, carrying deposit insurance treatment and the bank's credit risk. A stablecoin is issued by a separate entity against reserve assets.", [
  "Tokenized deposits stay on the balance sheet and keep the interest-bearing, regulated deposit relationship",
  "Stablecoins offer wider public-network reach but sit outside the banking perimeter",
  "Interoperability between the two is the unresolved design question"]),
 ("Where Each Fits", "Tokenized deposits suit closed-loop and interbank use: intraday liquidity, wholesale settlement and corporate treasury. Stablecoins suit open ecosystems, such as payments to non-bank counterparties and digital marketplaces.", [
  "Wholesale and treasury flows: tokenized deposits",
  "Open-network consumer and merchant payments: regulated stablecoins",
  "Cross-border corridors: likely both, linked through shared standards"])],
 end=("Our View", "The strategic question is not which wins, but how a bank keeps customers' money inside its balance sheet while still reaching the networks where they want to spend it.")),

dict(slug="servicenow-agentic-ai-enterprise", cat="ServiceNow", emoji="⚙️", date="2026-09",
 title="ServiceNow and Agentic AI: From Workflow Automation to Autonomous Operations",
 lead="ServiceNow built its franchise on workflows. Its agentic AI push extends that foundation: AI agents that reason, decide and act across IT, customer and risk processes, using the same platform data and controls.",
 sections=[
 ("What Changes with Agents", "Traditional workflow automation follows a predefined path. Agents work toward a goal, selecting tools and steps as they go, then escalating to humans when confidence or authority runs out.", [
  "Goal-driven resolution of incidents, requests and cases",
  "Orchestration across multiple agents and existing workflows",
  "Platform-native context: CMDB, case history and knowledge in one place"]),
 ("Why the Platform Matters", "An agent is only as safe as the system it acts inside. ServiceNow's advantage is that agents run on the same permissions, audit trail and process definitions that already govern enterprise work.", [
  "Role-based access and approvals apply to agent actions",
  "Every action is logged against a ticket or case",
  "Central visibility and governance of the AI estate is becoming a core capability"])],
 end=("Where to Start", "Pick a high-volume, well-documented process, measure baseline resolution time, and deploy an agent with human approval gates. Widen autonomy only as evidence accumulates.")),

dict(slug="servicenow-ai-agents-banking-use-cases", cat="ServiceNow", emoji="🤖", date="2026-08",
 title="Where ServiceNow AI Agents Fit in a Bank: Five High-Value Use Cases",
 lead="Banks already run large parts of operations, risk and service management on ServiceNow. That makes it a practical place to deploy AI agents where governed workflow and clean data already exist.",
 sections=[
 ("Five Use Cases Worth Piloting", "These are chosen for volume, clear process boundaries and measurable outcomes.", [
  "<strong>IT incident triage:</strong> classify, enrich and route incidents, proposing fixes from knowledge and past tickets",
  "<strong>Customer case resolution:</strong> summarise history and draft responses for service agents",
  "<strong>Onboarding and KYC case orchestration:</strong> coordinate document checks and escalations",
  "<strong>Third-party and operational risk:</strong> collect evidence, flag control gaps and prepare assessments",
  "<strong>Regulatory change tracking:</strong> map new obligations to policies, controls and owners"]),
 ("Guardrails Banks Must Add", "Banking adds obligations beyond a typical enterprise deployment.", [
  "Human-in-the-loop for decisions that affect customers or capital",
  "Model risk management applied to agent behaviour and prompts",
  "Data residency, privacy and explainability documented for auditors"])],
 end=("The Bottom Line", "Treat agents as digital staff with defined roles, limits and supervisors. That framing makes governance conversations with risk and audit far more productive.")),

dict(slug="dlt-capital-markets-production", cat="DLT", emoji="🔗", date="2026-08",
 title="DLT in Capital Markets: Moving from Proof of Concept to Production",
 lead="After years of pilots, distributed ledger technology is delivering in production in specific corners of capital markets, notably repo, collateral mobility and tokenized funds. The lesson is that it works best where multiple parties need a shared, synchronised record.",
 sections=[
 ("Where DLT Is Proving Its Value", "The strongest cases remove reconciliation and settlement friction between institutions rather than replacing internal systems.", [
  "Intraday and term repo with atomic delivery-versus-payment",
  "Collateral transfer and mobility across venues",
  "Issuance and servicing of digital bonds and fund units"]),
 ("What Still Holds Projects Back", "Technology is rarely the blocker. Adoption depends on network effects and integration with existing market infrastructure.", [
  "Legal certainty on finality and ownership of tokenized instruments",
  "A settlement asset — tokenized cash or central bank money — on the same ledger",
  "Integration with front-to-back systems, custody and reporting"])],
 end=("Our Advice", "Start with a multi-party problem you already pay to reconcile, secure a consortium of counterparties, and design the interface to legacy platforms first.")),

dict(slug="tokenized-real-world-assets", cat="Digital Assets", emoji="🏛️", date="2026-07",
 title="Tokenizing Real-World Assets: Funds, Bonds and Private Credit On-Chain",
 lead="Tokenization represents ownership of traditional assets as digital tokens on a ledger. The appeal is operational: faster settlement, fractional access, automated servicing and 24/7 transferability.",
 sections=[
 ("The Asset Classes Leading the Way", "Tokenized money market funds and government securities have attracted the most institutional interest, followed by private credit, real estate and commodities.", [
  "Money market funds used as on-chain collateral and cash management",
  "Bonds issued natively on distributed ledgers",
  "Private credit and fund interests with automated distributions"]),
 ("Design Questions to Settle Early", "A token is a wrapper; its value depends on the legal and operational structure behind it.", [
  "Is the token the legal record of ownership or a mirror of it?",
  "Who is the transfer agent, and how are corporate actions handled?",
  "What secondary liquidity exists, and under which transfer restrictions?"])],
 end=("The Bottom Line", "Tokenization pays off when it removes real cost or unlocks real distribution. Test each candidate asset against that standard before building.")),

dict(slug="cbdc-india-digital-rupee", cat="Digital Assets", emoji="🇮🇳", date="2026-06",
 title="CBDCs and India's e₹: Where Retail and Wholesale Digital Currency Stand",
 lead="Central bank digital currencies are central bank money in digital form. India's Reserve Bank launched pilots for wholesale and retail versions of the digital rupee (e₹) in late 2022, and the programme has continued to evolve.",
 sections=[
 ("Two Models, Two Purposes", "Wholesale CBDCs target interbank and institutional settlement. Retail CBDCs target the public as a digital form of cash.", [
  "Wholesale: settlement of government securities and interbank transactions",
  "Retail: person-to-person and merchant payments through bank-provided wallets",
  "Programmability and offline capability remain active areas of exploration"]),
 ("What Banks Should Be Doing", "Banks are the distribution layer for e₹, which makes readiness a practical matter.", [
  "Integrate wallets and ledgers with core and payments systems",
  "Plan liquidity and reconciliation between deposits and CBDC",
  "Decide where CBDC fits beside UPI and existing instant payment rails"])],
 end=("The Takeaway", "CBDC is less a competitor to existing rails than a new settlement asset. Banks that build the plumbing early will shape how it is used.")),

dict(slug="digital-asset-custody-institutions", cat="Digital Assets", emoji="🔐", date="2026-05",
 title="Digital Asset Custody: What Institutions Need Before They Hold Tokens",
 lead="Custody is the gate through which institutional capital enters digital assets. Holding a private key safely is a different problem from holding a security in a depository, and the controls need to reflect that.",
 sections=[
 ("Core Custody Capabilities", "An institutional-grade solution combines technology, operations and legal structure.", [
  "Key management using hardware security modules or multi-party computation",
  "Segregation of client assets and clear legal ownership",
  "Governance workflows: approvals, whitelisting, transaction limits",
  "Independent assurance, such as SOC reports and insurance arrangements"]),
 ("Build, Buy or Partner", "Few banks will build the full stack. Most will select a specialist provider or a hybrid model.", [
  "Assess provider resilience, jurisdiction and regulatory status",
  "Test disaster recovery and key-recovery procedures, not just policy documents",
  "Integrate positions into existing risk, accounting and reporting systems"])],
 end=("Our View", "Custody decisions are hard to reverse. Run due diligence the way you would for a new securities depository or core banking vendor.")),

dict(slug="aml-digital-assets-travel-rule", cat="Compliance", emoji="🕵️", date="2026-04",
 title="AML for Digital Assets: Travel Rule, On-Chain Analytics and the Bank's Role",
 lead="Digital assets create financial-crime risk, but also unusually transparent data. Banks that serve crypto businesses or hold tokens need controls designed for public ledgers rather than borrowed from card or wire monitoring.",
 sections=[
 ("The Regulatory Baseline", "Global standards from the FATF extend AML obligations to virtual asset service providers, including the Travel Rule for sharing originator and beneficiary information. In India, VASPs were brought under PMLA obligations in 2023.", [
  "Customer due diligence on VASPs and their ownership",
  "Travel Rule data exchange between institutions",
  "Suspicious transaction reporting on digital asset activity"]),
 ("Using On-Chain Analytics", "Blockchain analytics tools trace fund flows and score wallet risk. Combined with traditional transaction monitoring, they give a fuller picture.", [
  "Screen counterparties and wallet addresses against risk and sanctions exposure",
  "Trace source of funds beyond the first hop",
  "Document alert handling for regulators and audit"])],
 end=("The Bottom Line", "Treat digital asset AML as an extension of your KYC and monitoring architecture, with extra data sources, not a separate silo.")),
]
