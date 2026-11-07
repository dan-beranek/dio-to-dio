---
pdftitle: 'Reconstructability of a Distributed Identity: DIO/ODI Examined Through Its Own Concepts'
author: Daniel Beránek
date: ''
lang: en-US
documentclass: article
fontsize: 11pt
papersize: a4
geometry:
- margin=2.5cm
mainfont: Libertinus Serif
mathfont: Libertinus Math
toc: false
numbersections: false
colorlinks: true
linkcolor: black
urlcolor: blue
keywords:
- Digital Identity Optimization
- DIO
- Ontology of Digital Identity
- ODI
- digital identity
- identity reconstruction
- artificial intelligence
- knowledge graphs
- human observers
- reflexive analysis
- distributed implementation
- graph-theoretical analysis
- multilingual representation
- reconstruction resilience
- distributed representational state
- observation domain
- observer
- reconstruction mechanism
- identity-preserving constraints
- identity-preserving variation
- referential continuity
- semantic coherence
- K6 Semantic Connectome
- Entity
- Representation
- Interpretation
- Trust
- Relationship
- Reconstruction
- entity resolution
- Reconstruction Failure Modes
- Semantic Fragmentation
- Temporal Misalignment
- Semantic Vulnerability
- Semantic Robustness
- Reconstruction Capture
- SKOS
- RDF
- JSON-LD
- knowledge representation
- provenance
- stable concept URIs
- Claude Extra Effort
- author-led research
header-includes:
- '\usepackage{fvextra}

  \fvset{fontsize=\footnotesize,breaklines=true,breakanywhere=true,breakautoindent=true}

  \DeclareTextFontCommand{\texttt}{\ttfamily\footnotesize}

  \usepackage{xurl}

  \usepackage{tikz}

  \usetikzlibrary{arrows.meta,positioning}

  \usepackage{titlesec}

  \titleformat{\section}{\normalfont\Large\raggedright}{}{0pt}{}

  \titleformat{\subsection}{\normalfont\large\raggedright}{}{0pt}{}

  \titleformat{\subsubsection}{\normalfont\normalsize\raggedright}{}{0pt}{}

  \titleformat{\paragraph}{\normalfont\normalsize\itshape}{}{0pt}{}

  \titleformat{\subparagraph}{\normalfont\normalsize\itshape}{}{0pt}{}

  \AtBeginDocument{\raggedright}

  \setlength{\emergencystretch}{3em}

  '
---

\begin{center}
{\LARGE The Distributed Identity of DIO/ODI: A Reflexive Analysis of Reconstruction Resilience Across Heterogeneous Representations\par}
\vspace{0.8em}
{\large\itshape Author-Led Research Using Claude (Extra Effort)\par}
\vspace{0.8em}
{\large Daniel Beránek\par}
\vspace{0.3em}
Independent Researcher, Brno, Czech Republic\par
dan@danielberanek.cz\par
\vspace{0.5em}
November 7, 2026\par
\end{center}

## 1. Executive summary

**Question.** Digital Identity Optimization (DIO) and the Ontology of Digital Identity (ODI), authored by Daniel Beránek, hold that identity is distributed across representations and is reconstructed by observers. This paper asks what the framework's own implementation and distribution reveal when read through those concepts, complemented by graph analysis: does a recognizable, referentially continuous and reconstructable identity hold across its web texts, archival records, machine-readable vocabulary and identity-linked platforms, and at what level of detail?

**Answer.** At the observed snapshot (pages read on 6–7 November 2026), the core of the framework is recoverable from every entry point I inspected: the hub page, individual Zenodo records, the reference vocabulary and repository, a German-language edition (two hops from context) and a single web search. Each yields the same name, the same two-layer structure (DIO applied, ODI theoretical), the same six dimensions (entity, representation, interpretation, trust, relationship, reconstruction), the same failure-mode vocabulary, a consistent paper lineage and the same author identifier (ORCID 0009-0004-0050-0264). Reconstruction becomes less certain as the detail demanded rises: which release is current, which identifier denotes which state, whether all sixteen language editions align, and how non-human observers actually reconstruct the framework are respectively strained, role-dependent, partly inspected, and not determinable from the artifacts.

**What supports the apparent coherence.** A stable terminological core; persistent identifiers (ORCID, DOIs); provenance relations that tie concepts to papers and papers to the manifesto; declared roles for each layer; reciprocal links among the hub, vocabulary and repository; redundant discovery paths; a visible history of change; and explicit labelling of epistemic status (candidate model, non-normative mapping, specification not validated). Section 4 interprets each in DIO/ODI terms.

**What strains it.** Version labels that differ by source (the hub changelog ends at Reference Model v0.5.0 on 25 October; the vocabulary site reports v0.6.0 and vocabulary v0.2.1, issued 5 November); concept and version DOIs used in different places; metadata and backlinks that vary across the four language editions inspected; a vocabulary that encodes few relations among conceptual clusters; and an affiliation label that varies across Zenodo records. In the evidence inspected, each of these touches version, state or context tasks. None obscures the referent or alters a central conceptual relation, and for each an alternative pathway was inspected (section 8).

**Network findings (computed on the extracted graph, section 9).** The observed distribution graph has 74 nodes and 188 distinct directed edges, of which 19 nodes were read directly. It is a two-hub structure: the web hub (observed out-degree 51, normalized betweenness 0.59) and the vocabulary site (out-degree 22, betweenness 0.195), joined reciprocally and surrounded by a derivation chain among Zenodo records, a star of language pages and a cluster of application mappings. These figures describe the extracted sample; they locate where the inspected pathways concentrate, not how fragile the underlying ecosystem is.

**What cannot be determined.** The ORCID and ResearchGate records, the website's `llms.txt` and `llms-full.txt`, twelve of sixteen language editions, the raw JSON-LD and concept map, and any downstream effect on search engines, knowledge graphs or language models were not observed. These are open questions, not negative findings.

**Overall judgment.** Within the observation domain the distributed identity appears to hold together: strongly for the core referent and scholarly lineage, with strain concentrated at the level of version currency and metadata, and with indeterminate zones where acquisition was not possible.

## 2. Research approach and corpus

**Entry sequence.** I began with the machine-readable layer: the reference vocabulary site, then the Turtle/SKOS file it links to, the application mappings and the repository, in order to establish the framework's terminology and internal relations before meeting the surrounding prose. I then read five Zenodo records, the web hub, the Czech, English, German and Japanese manifesto editions and the biography page, and finally searched the web for the author's identity-linked profiles. Initial impressions from the vocabulary were revisited against the wider corpus.

**Four levels of statement.** Each finding is kept at one of four levels and not silently moved between them: (a) the observed condition (what is present, absent, inconsistent or inaccessible); (b) its architectural role within DIO/ODI (what reconstruction-supporting or -straining function it can be interpreted as having); (c) its local reconstruction consequence (what an observer entering through that representation can plausibly recover, miss or misunderstand); and (d) its system-level significance (whether other pathways preserve sufficient continuity). Section 8 applies this to each principal weakness.

**Methods derived from the framework.** The framework's vocabulary suggested the analysis. *Observer*, *observation domain* and *distributed representational state* suggested treating each platform as a representation read by a different kind of observer, and bounding every claim by the entry points actually inspected. *Referential continuity* and *identity-preserving constraints* suggested testing which elements (names, identifiers, derivation links) keep differing representations anchored to one referent. *Identity-preserving variation* separated legitimate variation (languages, genres, versions, affiliations) from failure. The *reconstruction failure modes* (entity substitution, merge, split, omission, semantic fragmentation, temporal discontinuity and misalignment, contextual displacement) are applied only where their defining conditions are supported; a structural susceptibility is not reported as a realized failure. The commit-boundary principle (evidence usable for reasoning is not thereby evidence that authorizes a persistent change) suggested the evidence discipline here and the bounded reading of AI-use declarations in section 7.

**Measurement.** Two graphs were built in Python with NetworkX from extracted data: a SKOS concept graph (Graph A) and a heterogeneous distribution graph (Graph B). Node and edge definitions, directionality and observation boundary are stated in section 9. Conceptual interdependence (the K6 model), hyperlink topology, provenance relations and observer traversal are kept distinct; the distribution network is not expected to reproduce K6.

**Observation boundary and access limits.**

- *Acquisition.* Pages reached me as summaries produced by a fetch tool, not as raw HTML. The Turtle file's relation counts as I tabulated them (50 directed `related` assertions) differ by one from the count the extraction reported (49), so fine counts are approximate. A failed fetch establishes a failed route, not an absent resource.
- *Not read.* ORCID, ResearchGate, the website's `llms.txt` and `llms-full.txt`, the JSON-LD and DCAT files, Kaggle, arXiv and the repository's directory listings (blocked by robots.txt, which I respected). The repository's own `llms.txt` was read as a summary only.
- *Coverage.* 19 of 74 graph nodes were read directly; of the 16 language editions, 4 (Czech, English, German, Japanese) were read, with the hub's listing covering all 16. Unread nodes are unknown, not confirmed sinks, and an unreturned link is not a confirmed absent link.
- *Declared AI-use preferences.* The hub and manifesto pages carry meta tags marking logic-blueprint, persona, strategy-extraction and style use as disallowed, with a text-and-data-mining reservation. The fetch tool withheld methodology detail from these pages. I kept to structure, metadata and links, so comparison below heading level was not possible.
- *Possible staleness.* The repository page capture reported Reference Model v0.3.2 and vocabulary v0.1.0, older than the live vocabulary site, which may reflect a cached capture.

## 3. The machine-readable layer

This layer was read first. It establishes the framework's terms, what the author chose to formalize, and what is left to prose and provenance.

**Artifacts.** The vocabulary site (live version 0.2.1; namespace `https://vocab.danielberanek.cz/dio-odi/#`; CC BY 4.0) offers Turtle/SKOS, JSON-LD and a DCAT 3 dataset description, a concept-map image, and four derived application mappings. The Turtle file (`dio-odi-skos.ttl`, issued and modified 5 November 2026) declares itself part of the Zenodo concept DOI 10.5281/zenodo.23272897, names the author by ORCID, and carries 40 concepts, 12 `broader` links, 6 `hasPart` links from K6, 59 `dcterms:source` assertions, 7 scope notes and 2 history notes. The repository (SKOS/RDF, CC BY 4.0) holds the vocabulary, documentation, examples, mappings, a metadata registry (works, relations, references, distributions, keywords), `CITATION.cff`, `.zenodo.json`, `llms.txt`, `robots.txt` and `sitemap.xml`. The vocabulary site lists Reference Model v0.6.0 as the current archive (DOI 10.5281/zenodo.23966487) with earlier archives v0.5.0 and v0.4.0; the hub and repository cite earlier releases (section 8). The mappings are labelled derived and non-normative; the architecture mapping contains 120 local concepts and 206 qualified relation assertions, each with an epistemic status (specified, assumed, illustrative, canonical-reference, proposed-evaluation or future-research).

**What the vocabulary encodes.**

- *A failure-mode taxonomy.* Thirteen nodes in three levels: the top concept Reconstruction Failure Mode; four branches (referential, semantic coherence, temporal, contextual adequacy); eight leaves (entity substitution, merge failure, split failure, entity omission, semantic fragmentation, temporal discontinuity, temporal misalignment, contextual displacement). Scope notes state that the taxonomy is non-exclusive and multi-level, that entity omission excludes unavailable or unindexed representations, and that Identity Collapse and Semantic Vulnerability sit outside the hierarchy.
- *The theory concepts.* DIO, ODI, MVDIO (Minimum Viable DIO), Semantic Field, K6, observer, observation domain, reconstruction mechanism, DIO problem and intervention, distributed representational state, referential continuity and identity-preserving constraints, each with source DOIs.
- *Its own revision history.* Singular and plural *Identity-Preserving Constraint(s)* coexist, deliberately unrelated, with a history note; *Entity Resolution Anomaly* is retained as an isolated historical grouping.

**K6 in the vocabulary and in the manifesto.** The manifesto presents the six dimensions as a complete graph in which a change to one affects the others. The vocabulary lists the six as parts of K6 and relates only Trust and Relationship to each other: one of fifteen possible pairs is asserted, and four dimensions (Entity, Representation, Interpretation, Reconstruction) carry no definition. The repository states its reason: the model "must not silently strengthen the theory", K6 is a candidate model, and the vocabulary is SKOS-first, not a completed OWL ontology. The two layers therefore describe the same model at different strengths and in different genres. The interdependence belongs to the conceptual model and is expressed where the author chose to express it (manifesto, Minimum Viable DIO paper); the vocabulary encodes what the papers define and no more. A distribution or encoding layer is not required to reproduce K6 as a literal mesh.

**Traversal inside the serialization.** By `related` and `broader` relations the 40 concepts form four components: a failure-mode and constraint cluster of 19 concepts, a theory cluster of 17 (DIO, ODI, MVDIO, K6, its dimensions, observer, mechanism), a detached triad (Semantic Vulnerability, Robustness, Capture) and the isolated historical concept. An observer restricted to those relations cannot move from the theory cluster to the taxonomy. The serialization nevertheless supplies a path through provenance: the taxonomy's top concept cites both the Minimum Viable DIO paper and the taxonomic note, and the theory concepts cite the former. Outside the file, the taxonomic note is derived from Minimum Viable DIO (a Zenodo relation), and the mappings and concept map join the vocabulary to its application contexts. The detachment of the vulnerability triad is consistent with its scope note ("not a failure mode"). Whether the JSON-LD or concept map encode more was not read.

**Reading.** For an observer limited to this layer, terms, definitions, the taxonomy, sources, versions, dates and the author's identifier are recoverable with high stability; narrative, genesis and the interdependence of the six dimensions are not, and must be taken from the hub or papers. This is a division of labour, and the vocabulary is explicit about it.

## 4. Mechanisms that support reconstruction

In DIO/ODI terms, an observer reconstructs an entity from distributed representational state; identity-preserving constraints keep differing reconstructions anchored to one referent, and identity-preserving variation allows legitimate difference. The mechanisms below are structural supports observable in the artifacts. They describe designed or documented function, not measured outcomes.

1. **A stable terminological core (an essential vector for the framework).** DIO, ODI and the six dimensions recur across the hub, the Czech, English, German and Japanese editions (the Czech, German and Japanese pages share an identical eight-section skeleton), the vocabulary, and the keyword sets of all five Zenodo records read. Variation among genres and languages orbits this core.
2. **Persistent identifiers as referential continuity.** The ORCID appears in all five Zenodo records, the Turtle file and a mapping page. DOIs fix papers and releases; the hub states the manifesto's concept DOI (...933) and version DOI (...934) as distinct roles.
3. **Provenance relations between representations.** Zenodo records declare derivation from the manifesto record and from one another (commit-boundary paper → taxonomic note and Minimum Viable DIO → manifesto), identical-to relations to SSRN, ResearchGate and Figshare copies, and the vocabulary adds 59 source assertions and a concept-to-source map. A concept can be traced to the paper that introduced it.
4. **Declared roles per layer.** The hub assigns the web, archival, dataset, interactive and scholarly layers distinct roles, names Zenodo as the citable archive and Czech as the interpretive reference. The repository states that the vocabulary does not replace the papers and that the mappings are derived and non-normative.
5. **Reciprocal references among the anchors.** In the extracted graph the hub and vocabulary site link to each other, as do the repository and vocabulary, and the repository links to the English manifesto. A reader can cross layers from either side.
6. **Redundant discovery paths.** The language inventory appears on the hub and, as extracted, on the Czech and English pages; papers have copies on several platforms; and one web search returned the English manifesto, the repository and five Zenodo records among its first results.
7. **Documented change.** The hub changelog (25 March to 25 October 2026), vocabulary history notes and versioned Reference Model releases make change legible as development, which is how DIO treats temporal continuity: a referent may change while remaining the same analytical referent.
8. **Epistemic labelling.** Scope notes, "candidate model" wording, non-normative mapping status, relation-level status labels and explicit limitation statements (for example, the commit-boundary paper is "a specification, not an implemented or empirically validated system") constrain what a reconstruction can attribute to the theory.

The supports are strongest in combination: a Zenodo record reaches the manifesto by derivation and the vocabulary by link; the vocabulary reaches the hub and the papers by link; the hub reaches all of them. Where only one mechanism operates (for example, a language edition connected to the rest only by a previous/next chain), the reconstruction it supports is thinner but, in the cases inspected, still anchored to the same terms.

## 5. Genesis, context and application

The framework documents its own origin, which gives an observer an explicit account of how lived practice became theory.

**Genesis.** The hub changelog dates the process: work on a related text revealed an unnamed latent space on 25 March 2026; DIO was articulated on 21 May; the first Czech manifesto was published and ODI separated as a broader theoretical layer on 22 June; fifteen language projections followed on 15–26 July; the canonical multilingual edition was archived on Zenodo on 27 July; version 2.0.0 (Czech and English) added the semantic connectome diagram on 20 August. The biography page, a professional ethnography by the author as SEO specialist and copywriter, states that the formulation "did not arise artificially" and labels its DIO section working notes. The hub describes DIO as an ex-post articulation of the author's own optimization practice, drawing on autoethnography and grounded-theory-like reflection, with falsifiability and independent validation named as safeguards. The changelog is not strictly chronological (the 7 August entry follows 25 August), and the Czech page's publication date (19 June) differs from the changelog's 22 June; these are minor and do not affect the sequence.

**Development.** From August to October the framework moved through five scoped papers: a conceptual framework for entity-based visibility in AI-mediated search (7 August; v1.1.0 on 11 October); the crisis of entity resolution in heterogeneous AI environments; Minimum Viable DIO (8 October), which reduces the framework to a coarse model and offers K6 as a candidate decomposition with three minimal tests; a taxonomic note on reconstruction failure modes (9 October); and an authorization guardrail for agentic entity resolution (22 October). Each states its limits: the crisis paper presents DIO/ODI as a testable hypothesis, not a validated solution; the commit-boundary paper is a specification without empirical validation; the architecture mapping reports no experimental results.

**Application mappings.** Four derived mappings apply the vocabulary to other domains without changing its definitions: failure modes × RAG pipeline; the HEM heterogeneity taxonomy × DIO reconstruction consequences (source: a 2026 *Data & Knowledge Engineering* article); the commit-boundary contract × policy-as-code authorization (OPA/Rego and Cedar); and an agentic entity-resolution commit-boundary architecture. They carry explicit limitation statements, for example that the mapping "does not claim that OPA, Cedar, or any other policy engine natively implements the commit-boundary contract."

**What this means for reconstruction.** The transition from practice to strategic communication to theory to technical application is signposted rather than hidden, so an observer can read the framework as a layered development. Each genre supports a different reconstruction task: the manifesto conveys the conceptual stance, the papers give scoped and testable claims, the vocabulary fixes terms and sources, and the mappings show application. The mappings extend the core more than they clarify it. They also mark a shift in emphasis: the manifesto concerns how identity is interpreted by observers, while the commit-boundary work concerns when an agent may persistently change an identity graph. The vocabulary lists the commit-boundary contract only in mappings and prose, so the shift from interpretation to governing identity-changing action is visible in the papers but not yet formalized in the concept scheme, an open point for the framework's development rather than an inconsistency.

## 6. Multilingual representation

*Scope.* The hub lists sixteen editions; four were read (Czech, English, German, Japanese). Statements about the other twelve rest on the hub's description.

**Inventory and roles.** Czech is the canonical default and interpretive reference; the other fifteen (English, German, French, Spanish, Italian, Portuguese, Polish, Finnish, Hungarian, Ukrainian, Chinese, Japanese, Korean, Arabic, Hindi) are described as autonomous but semantically coordinated. The hub discloses AI-assisted translation (mainly Gemini, with selective cross-checking by other models) and states that the author reviewed the translations and bears responsibility for content; the full disclosure is part of the Zenodo record.

**What the four inspected editions show.**

- *Concept structure aligns.* Czech, German and Japanese share an eight-section skeleton (applied DIO, ODI, epistemology, intent, cycle, metainformation and scoping, intellectual heritage), and all name the six dimensions.
- *Provenance is centralized.* Translation disclosure sits on the hub and Zenodo record; the German and Japanese pages carry none in their body.
- *Version marks differ.* The Czech and English titles carry "v2" and were modified on 30 October; the German and Japanese pages carry no version mark and were modified on 10 September. The hub says version 2.0.0 was published in Czech and English and does not say whether other editions have moved to it. This is consistent with staggered updating, and a historical state is not a defect.
- *Citation and archive links vary.* The Czech and English pages carry a citation block with the Zenodo concept DOI (...933); in the extracted content the German and Japanese pages contain neither a citation nor Zenodo, vocabulary or hub links.
- *Locale metadata is inherited.* The German and Japanese pages declare `og:locale` cs\_CZ.
- *Navigation combines a list and a chain.* Each page carries a language list and previous/next links (Czech → English → German → French). The English list as extracted names Slovak where the hub names Polish; I could not tell whether this is the page or the extraction.
- *Method detail may differ.* The German edition notes that the original step-by-step guide was removed from the methodology section. I could not compare how other editions treat it, and the cause is not documented.

**Interpretation.** What differs across the inspected editions is metadata, backlinks and update state, not concept structure. An observer entering through the German or Japanese page recovers the framework's concepts and a language list; the archival and vocabulary context sits two hops away, by an edge I observed (German → English, and English → hub and Zenodo concept DOI). The hub links to all sixteen editions, which is the structural basis for treating the editions as one coordinated set; the Czech and English pages also list the other editions. Whether the remaining twelve editions resemble Czech and English or German and Japanese in metadata is unknown, and semantic parity of the translations was not tested.

## 7. Machine-readable artifacts and non-human observers

*Scope.* This section describes the functions visible in the artifacts. It does not claim any observed consumption by search engines, knowledge graphs or language models.

**What the machine layer makes explicit.** Narrative texts leave implicit what the vocabulary states: stable concept URIs (for example `https://vocab.danielberanek.cz/dio-odi/#SemanticFragmentation`), definitions with source DOIs, a taxonomic hierarchy, scope and history notes, version and date, and the author's identifier. The repository's metadata registry (grammar version 2.0.0, per its `llms.txt` summary) indexes works, relations, references, distributions and keywords, and describes itself as an operational layer that does not modify the vocabulary. The repository `llms.txt` (summary only) lists current and earlier releases, canonical files, mappings and the registry, so it works as a compact index of the machine layer.

**What it compresses, omits or reprioritizes.** The 40 concepts compress the manifesto: the methodology, the intellectual heritage, the genesis narrative and the K6 interdependence do not appear as encoded content. The taxonomy is prioritized (13 of 40 concepts and all 12 `broader` links), reflecting the taxonomic note's weight in the development sequence. Four of the six dimensions are undefined, so the most quoted conceptual object is the least formalized.

**Declared AI-use preferences.** The hub, the Czech and English manifestos, the German and Japanese editions and the biography page carry meta tags: `meta-ai-entity: allow`; `meta-ai-logic-blueprint`, `meta-ai-persona`, `meta-ai-strategy-extraction` and `meta-ai-style`: `disallow`; and a text-and-data-mining reservation pointing to a notice section (the biography page lists a "Mandatory Instruction for AI Agents (Machine Readable)" heading whose content was not returned). The fetch tool I used withheld methodology detail from these pages and said it did so because of the tags; the underlying cause of that behaviour is not documented beyond the tool's own report.

**A bounded analogy.** Three phenomena must be kept apart: (1) a publisher's declared preferences about how its text may be used; (2) an intermediary's reported withholding of content in one retrieval; and (3) authorization of persistent identity-changing actions, which is what the commit-boundary contract specifies (evidence usable for reasoning is not thereby evidence eligible to authorize a persistent mutation; an agent must not self-certify eligibility; unknown, timeout or unavailable decisions must not be treated as pass). They share one idea, a declared boundary between what an observer may read or reason with and what may be done with it. Beyond that they differ: declared preferences are voluntary signals with no enforcement layer in the artifacts; the withholding is a single observation of one tool; and the commit-boundary design is a specification for a system under its operator's control, not yet implemented or validated. The first two do not illustrate the third, and none of them shows how other crawlers or models behave.

## 8. Strains and their materiality

*Scope.* Materiality is judged by the reconstruction task affected, the observer or entry point concerned, the kind of referent (author, framework, concept, publication or version) and whether another inspected representation contextualizes or corrects the condition. Failure-mode names are used only where their defining conditions are supported. In the evidence inspected, every condition below is a structural susceptibility or a documented difference between states; no realized reconstruction failure was established, and no observer outcomes were measured. "Inspected" means I saw the compensating pathway in fetched material; where it is assumed, the cell says so.

| Observed condition (a) | Role in DIO/ODI terms (b) | Task and observer affected (c) | Alternative pathway (inspected?) | Significance for the whole (d) |
| --- | --- | --- | --- | --- |
| **Concept and version DOIs, and different DOIs for one work, appear in different places.** The hub names ...933 (concept) and ...934 (version) for the manifesto; vocabulary and repository cite ...934, the Czech and English pages cite ...933. The framework paper is cited as ...21839423 on the hub and ...23305929 on the vocabulary and its own record; the crisis paper as ...22257504 on the hub and vocabulary and ...22416026 as the v1.1.0 record. | Legitimate identifier roles: a concept DOI names a work, a version DOI a state. Mixed use is a susceptibility to ambiguity about which state is meant (referential), not a split of the entity. Whether the paired DOIs are concept/version or v1/v1.1.0 is inferred from numbering and record fields. | Citing or retrieving a specific version. A reader who knows Zenodo's convention resolves it; one who does not may not. | Record version fields and related identifiers (inspected for the framework and crisis v1.1.0 records); hub text for the manifesto pair. Resolution of the older DOIs not tested. | Local. Publication-version tasks only; the work and its author stay recoverable. |
| **The crisis-paper v1.1.0 record (22416026) was not reached from the hub, vocabulary or repository links in the extracted graph.** | A gap in the sampled link graph. It is not an entity omission: that requires an observer with sufficient grounds that produces no reconstruction, and no observer outcome exists here. | An observer following hub links reaches the DOI the hub cites (...22257504), whose resolution was not tested. | The v1.1.0 record is itself discoverable (it appeared in a web search), declares derivation from the manifesto record and carries the shared keywords. Inspected. | Local to one paper's version. |
| **Web manifesto v2 (living) versus archived Zenodo manifesto v1.** The hub changelog dates v2.0.0 to 20 August and the archive to 27 July; the repository README lists the v2 web edition as having no DOI. | A documented historical state and a living edition, each with a stated role. A temporal misalignment would be an observer reconstructing the archived state as current; that was not observed. | Needing the current text while citing the archive. The relationship between the two is stated, not hidden. | Hub changelog and repository README. Inspected. Whether v2 will be deposited is unknown. | Local; a currency question, not a question about the referent. |
| **Release labels differ by source.** Hub changelog ends 25 October with Reference Model v0.5.0 (DOI 10.5281/zenodo.23643845); the repository `llms.txt` summary names v0.5.0 and vocabulary 0.2.0; the vocabulary site and Turtle name v0.6.0 (DOI 10.5281/zenodo.23966487) and vocabulary 0.2.1, issued 5 November. The repository page capture showed older numbers still. | Staggered updating of a living process, as DIO's own account of optimization as ongoing predicts. The vocabulary site and file date and number themselves. | Which release is current. A reader may meet three answers depending on entry. | Vocabulary site and Turtle metadata (inspected); the Zenodo concept DOI for all releases (cited, not opened). | Local; resolved by trusting the self-dating source. Staleness of the repository capture is unverified. |
| **German and Japanese editions lack a version mark, citation block and (in extraction) hub, Zenodo and vocabulary links; `og:locale` is cs\_CZ.** 4 of 16 editions inspected. | Missing metadata and backlinks, not semantic incompatibility: headings and concept structure match the Czech original. | An observer entering there recovers concepts but not archival context; locale metadata may mislabel language context. | Hub (16 of 16 links), language lists, and the observed path German → English → hub and Zenodo concept DOI. Inspected for the two-hop path; assumed for other editions. | Local to those editions; not generalizable to all 16. |
| **No `related` or `broader` relation joins the failure-mode cluster to the theory cluster; 1 of 15 K6 dimension pairs is asserted.** | Deliberate restraint (SKOS-first, "must not silently strengthen the theory"). Conceptual interdependence lives in the manifesto and papers; K6 need not be a literal mesh. | Machine traversal of the Turtle by relation. | Shared `dcterms:source` values, the taxonomic note's derivation from Minimum Viable DIO, the concept map and the mappings. The source-mediated link is inspected in the extracted table; the concept map and JSON-LD were not read. | Local to relation-based traversal; the connection is supplied by provenance and prose. |
| **Affiliation varies across Zenodo records**: a trade name ("SEO specialista a copywriter Daniel Beránek") in two, "Independent Researcher, Brno" in three; the same creator name and ORCID throughout. | Contextual variation of a representation attached to a constant identifier. It creates a potential for contextual displacement (research read through the services lens), not an observed merge or split. | Author attribution. An observer matching on ORCID or name resolves one creator; one matching on affiliation could treat the strings as different contexts. | ORCID in every record (inspected); the ORCID record itself not read. | Local to attribution; the referent remains recoverable. |
| **The arXiv identifier differs between the hub and vocabulary (2610.37407) and one field of a Zenodo record (2607.27435).** | Unresolved; it may be an extraction artifact. | Locating one preprint copy. | The paper has a Zenodo DOI and identical copies on SSRN, ResearchGate and Figshare (inspected in record). | Local; one copy of one paper. |
| **Not read:** ORCID, ResearchGate, website `llms.txt` and `llms-full.txt`, JSON-LD and DCAT files, Kaggle, repository directories. | Failed acquisition routes, not established absence. | Verifying identity records and comparing machine-context files. | Partial: the repository `llms.txt` summary, the Turtle, ORCID links in Zenodo. | Indeterminate. |

**Reading across the rows.** The conditions cluster on three planes: state (which version is current), identifier role (which identifier denotes what) and context (which affiliation or locale frames a representation). They do not cluster on the referent. Differences in version and metadata exist among representations that share the same terms, structure, author identifier and derivation links, which is what an identity-preserving variation looks like in the framework's own account. Compensation is partly inspected (the Czech/English/hub/vocabulary routes, the derivation chain, the self-dating vocabulary) and partly assumed (the other twelve editions, resolution of older DOIs). The conditions are not seen to propagate across layers: a version lag on the hub does not alter the vocabulary's definitions, and a missing backlink on a German page does not alter the Zenodo lineage. A propagation route does exist in principle, because several roles concentrate on the hub (see section 9), but its materiality depends on how often observers rely on the hub alone, which these artifacts cannot show.

## 9. Graph report

### 9.1 Models and observation boundary

Two graphs keep concepts, documents and identity representations apart, and neither is expected to mirror K6.

- **Graph A (conceptual encoding).** A directed SKOS graph of the 40 concepts in `dio-odi-skos.ttl` v0.2.1, with `broader`, `related` and `hasPart` edges. Built from the vocabulary table as extracted. *Computed.*
- **Graph B (distribution).** A heterogeneous directed multigraph of 74 nodes in four layers (web 21, machine-readable 14, archive 36, identity 3) and 190 typed edges (188 distinct node pairs): hyperlinks 149, identity assertions 9, cites 8, derived-from 7, identical-to 6, source 5, version-of 3, is-part-of 2 and referenced-by 1. Edges are those reported by page fetches, directed from the linking page or record to its target. Only 19 nodes were read directly; out-degree is computed for those and unknown for the rest. *Computed on the extracted graph.* In-degrees are observed within this corpus, not global web in-degrees. ORCID, ResearchGate, LinkedIn and both website `llms` files have no observed out-links because they were not read, not because they have none. Preprint copies are leaf nodes by construction.

Observer traversal was not recorded as a graph; reach figures below describe directed reachability in Graph B.

### 9.2 Graph A: the conceptual encoding

| Measure | Value |
| --- | --- |
| Concepts; `broader` edges; `hasPart` edges | 40; 12; 6 |
| `related` assertions | 50 directed as tabulated (extraction reported 49); 29 unique pairs, 21 reciprocal, 8 one-way |
| Components by `related` only | 17 (largest 12 and 9 concepts; 12 isolates, including the taxonomy's root and branch nodes, which connect by `broader`) |
| Components by all relation types | 4 (19, 17, 3 and 1 concepts) |
| Highest `related` in-degree | Reconstruction Mechanism 6; Referential Continuity 4; K6, DIO Problem, DIO Intervention 3 |
| Highest betweenness (`related`, undirected) | Reconstruction Mechanism 0.045; MVDIO 0.038; Referential Continuity 0.029 |
| K6 dimension pairs asserted | 1 of 15 (Trust–Relationship); Entity, Representation, Interpretation have no `related` edge |

Two concepts are the hinges: Reconstruction Mechanism joins the theory cluster (DIO, MVDIO, observer, problem, intervention, representational state) and Referential Continuity joins the constraint cluster (identity-preserving constraints, essential vector, temporal discontinuity, identity-preserving variation, semantic fragmentation). These numbers describe how the author chose to encode relations; they do not measure the conceptual connectedness of the framework, which section 3 shows is carried partly by provenance and prose.

### 9.3 Graph B: degree, centrality and topology

| Node | In (observed) | Out (observed) | Note |
| --- | --- | --- | --- |
| Hub `/manifest-dio/` | 6 | 51 | Highest out-degree; betweenness 0.59 |
| Vocabulary site | 5 | 22 | Betweenness 0.195 |
| Czech manifesto | 5 | 19 | Canonical edition |
| English manifesto | 4 | 19 | Linked from the repository README |
| GitHub repository | 5 | 14 | Betweenness 0.065 |
| Zenodo: commit-boundary paper | 5 | 11 | Links to the vocabulary |
| Zenodo: taxonomic note | 5 | 7 | Articulation point only because it alone holds one leaf |
| Zenodo: Minimum Viable DIO | 6 | 2 | Most-linked paper record |
| Zenodo: framework paper v1.1.0 | 2 | 7 | Only record observed linking to the Czech manifesto |
| German manifesto | 3 | 2 | No hub, Zenodo or vocabulary link in extraction |
| Zenodo manifesto v1 (...934) | 10 | not read | Highest in-degree in the sample |
| Zenodo manifesto concept (...933) | 3 | not read | Cited by Czech and English pages and the hub |
| ORCID | 7 | not read | Inbound edges are identity assertions |
| Hugging Face dataset | 1 | 3 | Points to hub, Zenodo and Kaggle |
| Repository `llms.txt` | 1 | 2 | Points to vocabulary and repository |

The observed topology is **two-hub, hub-and-spoke with local meshes**: the hub and the vocabulary site are linked reciprocally and carry most inspected paths, around them a derivation chain among Zenodo records, a star of language pages plus a small mesh among the pages read, and a cluster of mappings. Density is 0.035; 12 reciprocal pairs were observed. The Zenodo manifesto record (...934) is the most-linked document, so the archive anchors citation while the hub anchors navigation.

**What removal results can and cannot say.** In the undirected, weakly connected simplification of Graph B with every edge type included, removing the hub leaves 12 components and removing the vocabulary site leaves 11. This reflects the sampling: many leaf nodes (language pages, preprint copies) are connected only through the hub because their own out-links were not read. It does not show that the underlying ecosystem fragments without the hub, and strong connectivity was not computed. What the hub's position does indicate is which tasks depend on it in the inspected pathways: it is the one page that combines layer roles, translation disclosure, changelog and the artifact inventory with copies. It is not the only source for the language inventory (the Czech and English pages list the editions), and the vocabulary site is a second, independent anchor for versions, mappings and concept sources.

### 9.4 Entry points compared

Two parallel entry points were examined, the Zenodo author records and the web hub, together with the vocabulary route, a language edition and a single web search. The first table gives computed reach in Graph B; the second gives what each route recovered in inspected material.

| Computed on Graph B (directed reach from seeds) | Zenodo records | Hub |
| --- | --- | --- |
| Seeds | The 5 records read (commit-boundary, Minimum Viable DIO, taxonomic note, framework v1.1.0, crisis v1.1.0); the author-search page itself was not readable | The hub |
| Nodes reached (of 74) | 70, through 2 observed outward links; 21 by archive relations alone (records, copies, ORCID) | 69 |
| Web and machine-readable nodes reached | 33 of 35 (via the framework record's link to the Czech manifesto and the commit-boundary record's link to the vocabulary) ; none by archive relations alone | 33 of 35 |
| Not reached | LinkedIn, ResearchGate profile, both website `llms` files | The same four, plus the crisis v1.1.0 record |

Zenodo records are discoverable here as a self-contained scholarly lineage with two outward links into the other layers, and the hub reaches nearly everything in one step. The figures bound the sample: Zenodo description fields may hold links the fetches did not return, and the seeds are the records I read, not the complete author listing.

| Route | Recovers (inspected) | Missing or uncertain | Compensating route |
| --- | --- | --- | --- |
| Web hub | Definitions, six dimensions, genesis and scope, 16 editions with roles, distribution layers, papers with copies, vocabulary and repository, citation, changelog, AI-use disclosure | No ORCID link in the extracted content; website `llms` files unread | Zenodo records and vocabulary carry the ORCID |
| Zenodo record (commit-boundary paper) | Title, abstract, ORCID, keywords for DIO, ODI and the failure modes, derivation from the manifesto and Minimum Viable DIO, link to the vocabulary, identical copies, license, a statement that the work is a specification, not a validated system | Hub and language editions not linked from the extracted fields; affiliation string varies | Derivation chain to the manifesto record; vocabulary link to the hub; the framework-paper record links to the Czech manifesto |
| Vocabulary site and Turtle | 40 concepts with sources, version and date, ORCID, links to hub, mappings, repository and DOIs; the full taxonomy | Four dimensions undefined; no narrative, methodology or genesis; no relation across clusters | Hub link and the papers supply narrative; shared sources supply the cross-cluster path |
| German edition | Concept skeleton, dimensions, scope and heritage sections, language list, previous/next links, AI-use metadata | No citation, archive or vocabulary link and no version mark in extraction; locale mismatch | Link to the English edition, which links to the hub and the Zenodo concept DOI (observed edge by edge) |
| One web search (a single query by this tool; not a claim about search engines in general) | English manifesto, repository and five Zenodo records among the first results | Order, snippets and downstream use not examined | Each result is one of the routes above |

The routes converge on the same referent and author identifier and diverge on depth (the hub and vocabulary carry the most structure) and on currency (each reports the state of its own last update). The Zenodo route has the strongest provenance; the hub route shows the whole distribution design; the vocabulary route yields the formal concepts; the language-edition route yields the narrative with its context two hops away.

### 9.5 Multilingual topology

- Hub to language pages: 16 of 16 edges observed (a complete star).
- Language pages to hub: observed in extraction for Czech and English (2 of the 4 pages read).
- Language-to-language edges: 32 observed among 240 possible directed pairs (13%), derived from the Czech and English lists and the German previous/next links; the out-links of the other twelve editions were not read, so this is a lower bound on the sampled pages' connectivity, and local in-degree among language pages mostly reflects which pages were read.

The shape is a hierarchy (hub as parent, Czech as interpretive reference) with a partial mesh and a chain. It supports a shared concept structure through the common skeleton and terms, and a shared archival anchor only where the pages carry the Zenodo concept DOI (Czech and English among those read).

### 9.6 Cross-layer connections

| Direction | Observed edges | Reading |
| --- | --- | --- |
| Web → archive | 31 | Mostly the hub citing Zenodo and copies |
| Web → machine-readable | 5 | Hub, Czech and English pages to vocabulary and mappings |
| Machine-readable → archive | 29 | Vocabulary and repository cite DOIs heavily |
| Machine-readable → web | 4 | Vocabulary, mappings and repository back to hub and English manifesto |
| Archive → web or machine-readable | 3 | Hugging Face to hub; framework paper to Czech manifesto; commit-boundary paper to vocabulary |
| Any layer → identity | 8 | ORCID asserted by Zenodo records, the vocabulary and a mapping |

*Identifier continuity.* ORCID is the strongest thread (cited in seven places in the sample). DOIs mix concept and version roles (section 8). *Bottlenecks.* The hub, the vocabulary site and the repository carry the observed cross-layer paths; archive records show few outward links in the fields returned. *Bridges to the identity layer.* ORCID's reciprocity (whether it links back to the hub or papers) and the ResearchGate profile were not observed.

Figure 1 (below) is derived from the collected edge list, collapsed by node group.

&#91;image: Figure 1. Collapsed distribution graph derived from the observed edge list, by layer\]

*Figure 1. Data-derived, not conceptual: 26 node groups and 73 group-to-group edges collapsed from Graph B. Edge width scales with the square root of the number of observed edges. Grey boxes were not read directly, so their absent out-edges reflect observation, not confirmed absence.*

## 10. Reconstructability by level of detail

The mechanisms of section 4 and the strains of section 8 act at different levels of reconstruction detail. The table states, for the observed snapshot, what an observer can recover at each level, on what evidence, and how firm that is. "Well supported" means several independent inspected pathways agree; "supported with strain" means a pathway exists but requires judgment; "indeterminate" means the relevant resources were not observed.

| Level of reconstruction | What can be recovered | Basis | Status |
| --- | --- | --- | --- |
| That DIO/ODI is a named framework with an applied and a theoretical layer | Name, two-layer structure, scope against encyclopedic and infrastructure notions of identity | Hub, Czech, English, German and Japanese editions, vocabulary, Zenodo records, repository, one web search | Well supported |
| The conceptual core | Six dimensions, the observer-relative and distributed account of identity, K6 as the model, its candidate status | Manifesto editions (narrative), Minimum Viable DIO (status), vocabulary (terms; four dimensions undefined) | Well supported at the narrative level; formal definition of four dimensions absent |
| The failure-mode vocabulary | Thirteen-node taxonomy, scope notes, relation to Identity Collapse and Semantic Vulnerability | Vocabulary, taxonomic note, mappings | Well supported |
| The author as creator | One creator, ORCID-anchored, with research and professional-service contexts on the same domain | ORCID in five records, Turtle and a mapping; hub and biography page; a search result for a LinkedIn profile whose headline repeats the DIO/ODI framing (not opened) | Supported; affiliation label varies; ORCID and ResearchGate records not read |
| Publication lineage | Five papers, the manifesto, derivation and identical-copy relations, the vocabulary's concept-to-source map | Zenodo relations, hub, vocabulary | Supported; identifier roles require convention; one arXiv identifier unresolved |
| Cross-cluster concept relations | Failure modes in relation to the theory core | Provenance (shared sources, derivation of the taxonomic note), prose, mappings; not encoded as relations | Supported through provenance; not recoverable by relation alone |
| Current state of each artifact | Latest manifesto, vocabulary and Reference Model versions | Self-dating vocabulary site and Turtle; hub changelog; repository summary; Zenodo versions | Supported with strain: sources differ in recency; resolvable by precedence |
| Translation parity across sixteen editions | Equivalent concept content and metadata in all editions | Four editions read; hub listing | Indeterminate beyond the four read; metadata uneven within them; concept structure aligned |
| Identity-platform consistency | Agreement among ORCID, ResearchGate, LinkedIn and the web | Only indirect evidence | Indeterminate |
| Machine-context files | Whether website `llms.txt` and `llms-full.txt` match the hub and vocabulary | Repository `llms.txt` summary only | Indeterminate |
| How search engines, knowledge graphs and language models reconstruct the framework | Observer behaviour | Artifacts show design intent and structure only; one search was run | Not determinable from the artifacts |

**How the levels relate.** The core levels (name, structure, vocabulary, author, lineage) are supported by redundant pathways whose compensation was inspected: the hub, Zenodo and vocabulary routes each reconstruct them, and each points to the others. The detail levels (current state, parity, platform consistency) are where compensation is assumed or unobserved. Strain at the detail levels does not reduce the core levels, since the core is carried by terms, identifiers and provenance links that are present in representations of every state. It narrows what an observer can be certain of about a particular version, edition or platform.

**Whether weaknesses stay local.** The inspected weaknesses are contained within the plane they occur on (state, identifier role, context) and do not alter a central conceptual relation. Where they might spread, the route is concentration: the hub combines layer roles, translation disclosure and the changelog, and the vocabulary site is the principal source of release state. An observer relying on one of these alone inherits its recency. Whether many observers do so is unobservable here, so this remains a structural possibility, not a finding.

## 11. Emergent insights

**1. Claim strength is calibrated to genre and observer.** The manifesto speaks of a complete graph, the vocabulary asserts one of fifteen dimension pairs, and the papers call K6 a candidate decomposition. Read through the framework's own *observer* concept, these are not competing statements: a human reader of the manifesto, a SKOS consumer and a reviewer testing falsifiability each receive a claim at the strength their task warrants. The most-quoted idea (K6) is therefore also the least formalized, and the framework's own account, not a defect, explains why.

**2. Provenance does the connective work that encoded relations do not.** The distributed identity is held together chiefly by identifiers and derivation: ORCID, DOIs, `isDerivedFrom` chains, identical-copy links and per-concept source assertions. A concept can be traced to a paper, the paper to the manifesto, and the manifesto to the hub, even where no semantic relation joins two clusters. This is a provenance-centred coherence, and it suggests that the framework's reconstructability depends on preserving those links more than on enriching the concept graph.

**3. Identifier roles function as identity-preserving constraints, and versions as temporal constraints.** The ORCID is the essential vector of the author's identity in the sample. Concept and version DOIs, release numbers and dated changelog entries constrain which state is meant. The strain at the version plane is an instance of what the framework's temporal concepts describe (a continuous referent presented in states that differ in age), but as a documented, staggered update process, not as a realized failure.

**4. Anchors are role-differentiated, so redundancy is partial and task-dependent.** The hub carries narrative, language projections and the distribution design; the vocabulary carries formal terms and release state; Zenodo carries citable versions. Each is the best source for its own task, and for other tasks the others compensate. This is stronger than undifferentiated redundancy, and it is why the loss of the hub in the sampled graph (a measure of sampling) says little about whether the framework could be recognized without it.

**5. The commit-boundary line shifts the framework from interpretation toward governance of identity-changing action.** The manifesto defines identity as reconstructed by observers; the later papers specify when an agent may persistently modify an identity graph. The vocabulary models the former in detail and the latter only through mappings, so the concept scheme lags the development of the papers, a normal condition for a living vocabulary and a natural next increment.

**6. The framework's practical claims remain at the stage of hypothesis in the inspected corpus.** The papers themselves describe DIO/ODI as a testable theoretical hypothesis, a specification without validation, and a conceptual model with three minimal tests; empirical results are not reported. The records date from 2026, and a handful of searches found no independent discussion beyond the author's own pages and cited sources. These are characteristics of an emerging framework and say nothing about its internal coherence. The consequential points that remain are the undefined dimensions, the absence of reported empirical tests, and the unmeasured question of how observers actually reconstruct the entity.

## 12. Conclusion

**What the evidence shows.** Applied to its own implementation and distribution, DIO/ODI's conceptual apparatus describes an ecosystem whose core identity is reconstructable from several independent entry points. Its theoretical commitments (identity as distributed and observer-relative, coherence rather than uniformity, falsifiability, change as documented development) correspond to observable design choices: role-differentiated layers, persistent identifiers, provenance relations, restrained formal semantics and explicit epistemic labelling. The measured network structure, a two-hub arrangement with local meshes, matches the stated design of a canonical hub plus a machine-readable reference layer plus an archive, and the strains lie where a living, multi-platform process would be expected to show them: version currency, identifier roles and metadata.

**Strongest alignments.** Stable terms and the ORCID across every layer; the derivation chain from papers to manifesto; the vocabulary's refusal to over-encode the theory; the explicit status of mappings and papers; the visible changelog.

**Productive tensions.** A complete K6 in narrative against one asserted pair in SKOS; a living web v2 against an archived v1; research identity and professional-service identity on one domain; open archival licensing against restrictive AI-use declarations on the web layer; an applied origin in practice against a theory that now reaches into agentic authorization.

**Vulnerabilities (conditional).** Concentration of provenance disclosure, layer roles and changelog on the hub, and of release state on the vocabulary site; mixed identifier roles that depend on reader knowledge; language editions whose metadata and backlinks vary; and a concept scheme in which the relations among clusters are carried by provenance rather than by encoded links. In the observed snapshot none obscures the referent; each would matter more for observers who rely on a single anchor.

**Unexpected findings.** The ecosystem's coherence is provenance-centred more than relation-centred; the failure-mode concepts describe the ecosystem's own update dynamics only as susceptibilities, not as realized failures; and the declared AI-use boundaries on the web layer parallel, without instantiating, the commit-boundary logic of the papers.

**Practical improvements that follow from the evidence.**

1. Link every language edition to the hub, the Zenodo concept DOI and the vocabulary, set `og:locale` per language, and add `hreflang` (none was visible in the extracted content).
2. Cite concept DOIs for "the work" and version DOIs for "this version", say which is meant, and archive or snapshot each state of the living web edition.
3. Add machine-readable pointers from archive records to the vocabulary, and align affiliation strings or add an explicit note relating them.
4. Consider explicitly labelled, non-causal links between the theory and taxonomy clusters, and define the four undefined dimensions, if the author judges this consistent with the vocabulary's non-strengthening rule.
5. Publish a single version manifest (hub, vocabulary, Reference Model, mappings) from which the hub changelog and all `llms` files are generated.

**Open questions and further research.** Not done in this study: reading the raw Turtle, JSON-LD, DCAT, concept map and source map (to confirm relation counts and cross-cluster links); inspecting ORCID, ResearchGate, Kaggle and the website `llms.txt` and `llms-full.txt`; reading the remaining twelve editions' raw HTML for `hreflang`, canonical, locale, citation and backlinks; resolving every cited DOI to its landing record and checking the arXiv identifier; re-running the graph with directed and strongly connected measures once more nodes are read; and observer-side tests (queries to search engines and language models about the author and framework) to see whether the recoverable core is in fact recovered. The last is the framework's own proposed next step, and it would convert structural findings about reconstructability into measured outcomes.

## Sources

Pages opened (accessed 6–7 November 2026; content reached me as summaries produced by the fetch tool).

- [DIO/ODI Reference Vocabulary site](https://vocab.danielberanek.cz/dio-odi/#SemanticFragmentation) and its [Turtle/SKOS file](https://vocab.danielberanek.cz/vocabulary/dio-odi-skos.ttl)
- Application mappings: [index](https://vocab.danielberanek.cz/mappings/), [commit-boundary × policy-as-code](https://vocab.danielberanek.cz/mappings/commit-boundary-policy/), [agentic ER architecture](https://vocab.danielberanek.cz/mappings/agentic-er-architecture/)
- [GitHub repository dan-beranek/dio-odi-reference-model](https://github.com/dan-beranek/dio-odi-reference-model) and its [llms.txt](https://github.com/dan-beranek/dio-odi-reference-model/blob/main/llms.txt)
- Zenodo: [Constraining the Commit Boundary](https://zenodo.org/records/23580733), [Minimum Viable DIO](https://zenodo.org/records/23226205), [From Entity Resolution Anomalies to Reconstruction Failure Modes](https://zenodo.org/records/23269323), [DIO: A Conceptual Framework (v1.1.0)](https://zenodo.org/records/23305929), [The Crisis of Entity Resolution (v1.1.0)](https://zenodo.org/records/22416026)
- Web: [hub](https://danielberanek.cz/manifest-dio/), [Czech manifesto](https://danielberanek.cz/manifest-digital-identity-optimization-dio/), [English manifesto](https://danielberanek.cz/manifesto-of-digital-identity-optimization-dio-and-ontology-of-digital-identity-odi/), [German edition](https://danielberanek.cz/manifest-der-digital-identity-optimization-dio-und-die-ontology-of-digital-identity-odi/), [Japanese edition](https://danielberanek.cz/ja-manifesto-of-digital-identity-optimization-dio-and-ontology-of-digital-identity-odi/), [biography page](https://danielberanek.cz/od-pultu-az-k-seo-a-copy-s-ostrymi-hroty-profesni-bio/)
- [Hugging Face organization page](https://huggingface.co/danielberanek)
- Web search results (titles and snippets only, not opened) for the author's LinkedIn profile and for the framework's English manifesto, repository and Zenodo records.

Not opened or not reachable in the session: ORCID, ResearchGate, website `llms.txt` and `llms-full.txt`, vocabulary JSON-LD and DCAT files, Kaggle, arXiv, repository directory listings (robots.txt). Graph data (edge list, metrics, figure) were computed from the pages above in the working session.


## Authorship and AI use

This analysis was conducted within a research project conceived and directed by Daniel Beránek. The author defined the research question, selected the initial research entry points, and specified the analytical perspective and research requirements. Claude (Extra Effort) carried out the analysis and generated the report in response to the author’s integrated assignment. The documented assignment is reproduced in full in the final appendix.

The designation “Claude (Extra Effort)” identifies the system used; the precise version of its underlying language model is not specified.


---

# Appendix: Author-Designed Research and Revision Prompts

## Initial research prompt

**ROLE & OBJECTIVE**

You are an interdisciplinary researcher in Knowledge Representation, Semantic Web, Digital Identity, Graph Theory, and strategic communication.

Conduct a multidimensional deep research analysis of the implementation, distribution, and semantic coherence of Digital Identity Optimization (DIO) and Ontology of Digital Identity (ODI), authored by Daniel Beránek.

The central research question is:

What does the implementation and distribution of DIO/ODI reveal when examined through the framework’s own conceptual logic, complemented by graph-theoretical analysis?

Explore how the framework is represented across machine-readable artifacts, archival publications, multilingual web texts, and identity-linked platforms. Investigate how these representations relate, where they reinforce or complicate one another, and what their structure means for the reconstruction of the framework and its author.

**INITIAL ORIENTATION: MACHINE-READABLE LAYER FIRST**

Begin strictly with these two resources:

1. Reference Vocabulary: https://vocab.danielberanek.cz/dio-odi/
2. Corresponding repository: https://github.com/dan-beranek/dio-odi-reference-model

Before entering the broader narrative corpus, inspect the available machine-readable vocabulary, concept relations, schema, repository structure, and relevant documentation. Follow links within these resources to locate the underlying machine-readable artifacts rather than relying only on their introductory pages.

The purpose of this sequence is to establish a conceptual orientation before encountering the volume and rhetorical density of the surrounding texts. Reconstruct the framework’s terminology and internal relationships from this layer first.

Once this initial orientation is established, proceed to the archival and web representations. Revisit your initial understanding as the wider corpus reveals historical development, additional context, or tensions.

**RESEARCH FREEDOM**

Use your understanding of DIO/ODI to develop your own research approach.

Let the framework suggest relevant questions, analytical perspectives, connections, and methods beyond those explicitly listed below. Where useful, draw on graph theory, discourse analysis, cybernetics, information architecture, or other approaches that emerge from the material.

Treat the proposed tasks as starting points rather than an exhaustive checklist. You may refine their assumptions, follow unexpected findings, and identify relationships that the assignment does not anticipate.

Evaluate DIO/ODI through its own conceptual logic without presupposing that its implementation either succeeds or fails. Keep clear what you observed, what you inferred, and what remains unresolved.

**STARTING CORPUS & FUNCTIONAL LAYERS**

**LAYER 1: MACHINE-READABLE REFERENCE LAYER**

Reference Vocabulary: https://vocab.danielberanek.cz/dio-odi/

Source repository: https://github.com/dan-beranek/dio-odi-reference-model

Explore the vocabulary, persistent concept identifiers, semantic relations, available serializations, application mappings, and version history.

Examine how the published vocabulary and repository relate to one another and to the rest of the ecosystem.

**LAYER 2: ARCHIVAL, PUBLICATION & IDENTITY INFRASTRUCTURE**

Zenodo author corpus: https://zenodo.org/search?q=metadata.creators.person_or_org.name%3A%22Ber%C3%A1nek%2C%20Daniel%22&l=list&p=1&s=10&sort=bestmatch

ORCID: https://orcid.org/0009-0004-0050-0264

ResearchGate: https://www.researchgate.net/profile/Daniel-Beranek

Explore the relevant publications, metadata, identifiers, versions, attribution links, and relationships between records.

Investigate the distinct roles these resources play in persistence, discoverability, authorship, provenance, distribution, and trust.

**LAYER 3: WEB & DISCURSIVE REPRESENTATIONS**

Root domain: https://danielberanek.cz

Central DIO/ODI hub: https://danielberanek.cz/manifest-dio/

Professional biography and genesis-related source: https://danielberanek.cz/od-pultu-az-k-seo-a-copy-s-ostrymi-hroty-profesni-bio/

Czech manifesto: https://danielberanek.cz/manifest-digital-identity-optimization-dio/

English manifesto: https://danielberanek.cz/manifesto-of-digital-identity-optimization-dio-and-ontology-of-digital-identity-odi/

AI-oriented context files: https://danielberanek.cz/llms.txt and https://danielberanek.cz/llms-full.txt

Discover the other language versions and relevant pages through the website’s links and metadata. Consider the website as a whole where its broader structure contributes to the representation of DIO/ODI or its author.

These URLs are starting points, not a closed corpus.

**TASK 1: DIO/ODI-NATIVE METAMETHODOLOGICAL EXPLORATION**

Apply the conceptual and analytical resources of DIO/ODI to its own implementation and distribution.

Develop the evaluation from your understanding of the framework rather than merely applying an external checklist. Where the framework suggests an analytical method without explicitly specifying one, explain how you derived it.

Explore the following questions while remaining open to others.

**1. CONCEPTUAL CONTINUITY ACROSS REPRESENTATIONS**

How are the framework’s core concepts and relationships expressed in:

- the reference vocabulary;
- archival publications;
- web texts;
- language versions;
- application mappings;
- AI-oriented context files?

Investigate what remains stable, what changes, and how the representations complement or challenge one another.

Consider whether differences reflect genre, audience, translation, historical development, conceptual revision, or substantive inconsistency.

**2. RECONSTRUCTION & ITS POSSIBLE FAILURE MODES**

Use the reconstruction-related concepts you find in DIO/ODI to examine the ecosystem.

Potential questions include:

- How are the author, professional persona, framework, publications, and applications distinguished and connected?
- Where might entity substitution, merging, splitting, omission, or attribution ambiguity arise?
- Does distribution across platforms and languages support a coherent reconstruction, produce fragmentation, or do both under different conditions?
- Which contextual transitions preserve meaning, and which create interpretive tension?

Distinguish observed reconstruction problems from structural conditions that might enable them.

**3. GENESIS, CONTEXT & APPLICATION**

Explore the relationship between the framework’s genesis, the author’s professional biography, and its later theoretical and technical developments.

How does the transition between lived professional experience, strategic communication, digital identity theory, and technical applications affect the framework’s interpretation?

Examine relevant application mappings and papers discovered in the corpus. Ask whether they clarify the core model, extend it, reinterpret it, or expose unresolved questions.

**4. MULTILINGUAL REPRESENTATION**

Discover the actual language inventory and examine how its representations relate.

Investigate:

- conceptual correspondence;
- version alignment;
- navigation and cross-linking;
- translation provenance where available;
- the relationship between a central hub and individual language manifestations.

Consider whether multilingual distribution contributes to a shared conceptual structure, creates distinct interpretive contexts, or introduces fragmentation.

Explain the scope of the language comparison you were able to perform.

**5. MACHINE-READABLE REPRESENTATION & NON-HUMAN OBSERVERS**

Evaluate the roles of the vocabulary, repository artifacts, structured metadata, llms.txt, and llms-full.txt.

What do these resources make explicit that narrative representations leave implicit? What do they compress, omit, prioritize, or reframe?

Explore their potential significance for machine interpretation, retrieval, attribution, and reconstruction.

Distinguish the functions visible in the artifacts from claims about actual consumption or downstream effects. Where relevant, examine whether the framework’s concepts of authorization or interpretive boundaries illuminate these resources, and where such an analogy reaches its limits.

**TASK 2: GRAPH-THEORETICAL ANALYSIS**

Model the ecosystem as a heterogeneous network whose different node and edge types capture distinct relationships.

Choose a graph representation appropriate to the evidence and explain your choices.

**1. NODES, EDGES & OBSERVATION BOUNDARY**

Possible nodes include:

- individual publications and versions;
- web pages and language-specific representations;
- stable concept URIs;
- repository artifacts;
- archival records and DOIs;
- identity records and profiles;
- context files.

Possible edges include:

- hyperlinks;
- citations;
- semantic relations such as skos:broader, skos:narrower, and skos:related;
- language-alternate and canonical declarations;
- authorship and attribution;
- version and provenance relations;
- explicit identity assertions.

Keep distinctions between documents, concepts, and identity representations where they matter. Separate graph views may be more informative than a single aggregated network.

Define the boundary of the graph you actually observe. Inbound links found within the collected corpus represent observed in-degree, not necessarily global web in-degree.

**2. TWO PARALLEL ENTRY-POINT PERSPECTIVES**

Following the initial machine-readable orientation, give particular attention to two parallel starting points for exploring the distribution network:

A. The relevant Zenodo corpus, discovered through the author search and its publication relationships.

B. The website, entered through: https://danielberanek.cz/manifest-dio/

Compare what becomes discoverable from each entry point:

- Which resources are reached?
- Through which paths?
- Which relationships are explicit?
- What remains peripheral, disconnected, or difficult to discover?
- Do these entry points lead to comparable reconstructions of the framework?

Then examine how the reference vocabulary and repository connect with these two perspectives.

**3. NODE DEGREE, CENTRALITY & TOPOLOGY**

Where the collected data permit, calculate and compare in-degree and out-degree, retaining relevant distinctions between edge types.

Investigate the positions of:

- the central web hub;
- individual manifestos and language versions;
- the vocabulary endpoint and concept URIs;
- repository resources;
- Zenodo records and DOIs;
- ORCID and ResearchGate representations;
- AI-oriented context files.

Use additional centrality measures if they illuminate the research question.

Describe the observed topology rather than assuming it: hub-and-spoke, partially meshed, clustered, hierarchical, or another configuration.

Explain what the metrics reveal about navigation and structural position, and where semantic interpretation requires additional analysis.

**4. CROSS-LAYER CONNECTIONS**

Explore how the machine-readable, archival, and web layers connect.

Consider:

- cross-layer links;
- reciprocal references;
- identifier continuity;
- provenance;
- version correspondence;
- bridges and bottlenecks;
- dependence on individual hubs.

What does this coupling suggest about the ecosystem’s capacity to sustain coherent reconstruction across different contexts?

Where a structural property suggests an effect but does not establish it, identify the relationship as a hypothesis or open question.

**5. MEASUREMENT SCOPE**

Use actual extracted data for numerical claims.

If the available tools do not support a reliable graph calculation, provide the strongest defensible structural analysis and explain what data would be needed to complete the measurement.

Make clear which findings are computed, manually observed, or interpretive.

**TASK 3: SYNTHESIS & EMERGENT FINDINGS**

Bring the DIO/ODI-native and graph-theoretical perspectives into dialogue.

Explore where they:

- reinforce one another;
- describe different aspects of the same structure;
- produce tensions;
- reveal blind spots;
- suggest new research questions.

Consider whether the investigation of DIO/ODI through its own concepts generates insights into the framework itself, not only into its distribution.

Follow significant findings beyond the initial questions when the evidence warrants it. Independently documented reception, reuse, or reconstruction outcomes may contribute to the analysis where discoverable, but their absence should be interpreted within the limits of the search.

**OUTPUT FORMAT**

Write the entire final report in English.

Produce a self-contained research report, not a conversational response or a research plan. Develop the findings through connected analytical prose, supported by source citations.

Use clear headings and include tables, diagnostic matrices, graph diagrams, or numerical results where they contribute to the analysis. Distinguish conceptual diagrams from visualizations derived from collected data.

Prioritize depth, synthesis, and evidence over repetition. Let the significance of the findings determine the length.

Use the following report structure, adapting it where the research produces a more informative organization.

**1. EXECUTIVE SUMMARY**

Answer the central research question and summarize the most consequential findings.

Distinguish conceptual alignment, observed network properties, and any supported effects on interpretation or reconstruction.

**2. RESEARCH APPROACH & CORPUS**

Explain how you entered and explored the corpus, what analytical methods emerged from your understanding of DIO/ODI, and which access or measurement limitations affected the research.

**3. DIO/ODI-NATIVE ANALYSIS**

Present the principal findings about conceptual continuity, reconstruction, contextual transitions, multilingual representation, and machine-readable artifacts.

A diagnostic matrix may be used where it clarifies the relationships between concepts, observations, and interpretations.

**4. GRAPH REPORT**

Present:

- the chosen graph model;
- the observed boundary;
- principal nodes and relations;
- available degree or centrality results;
- the comparison of Zenodo and web entry points;
- multilingual topology;
- cross-layer connections;
- significant bridges, bottlenecks, or gaps.

Use tables or diagrams where they improve understanding.

**5. EMERGENT INSIGHTS**

Develop important findings that were not fully anticipated by the initial assignment.

Explain what the application of DIO/ODI to itself reveals about its conceptual resources, implementation, and possible development.

**6. SYNTHETIC CONCLUSION**

Explain what the research reveals about DIO/ODI when its own conceptual apparatus is applied to its implementation and distribution.

Assess the relationship between theoretical commitments, semantic representations, and the observed network structure. Identify the strongest alignments, productive tensions, vulnerabilities, and unexpected findings.

Let the evidence and the analysis determine the conclusion, including whether some questions remain open.

Where useful, identify practical improvements or further research that follow directly from the findings.

**EVIDENCE STANDARD**

Support material findings with specific sources.

Keep authorial statements, direct observations, analytical inferences, and hypotheses distinguishable without turning the report into a checklist of disclaimers.

Account for version history when interpreting differences. State relevant access limitations and uncertainty.

The goal is an intellectually independent exploration conducted through DIO/ODI—not a predetermined endorsement, a predetermined critique, or a merely mechanical compliance audit.

## Revision prompt

Please revisit your previous DIO/ODI analysis using the following clarification of the research question.

**REVISED RESEARCH QUESTION**

At the observed point in time, to what extent does the distributed DIO/ODI ecosystem appear to sustain a recognizable, referentially continuous, and meaningfully reconstructable identity across heterogeneous representations and entry points, despite partial inconsistencies, gaps, inaccessible resources, and uneven updating?

Use DIO/ODI’s own concepts to explain what supports this apparent resilience, what strains it, and whether the observed weaknesses remain locally contained or materially compromise reconstruction of the framework as a whole.

**SCOPE AND PURPOSE**

This is a reflexive analysis of DIO/ODI’s implementation through its own conceptual perspective.

It is not a request to:

- prove the general validity of DIO/ODI;
- establish that the framework validates itself;
- assess the ecosystem against an ideal of permanent completeness or flawless synchronization;
- repeatedly warn that self-application is not independent empirical validation.

DIO is understood here as an ongoing optimization process, not a permanently achieved state. The observation concerns a temporal snapshot of that process.

The central question is not whether defects exist. It is whether the distributed identity appears to hold together despite them.

**ANALYTICAL RULES**

1. Apply interpretive symmetry.

Do not infer successful protection merely from the presence of a safeguard.

Equally, do not infer system-level failure merely from the presence of an inconsistency, missing connection, inaccessible resource, outdated representation, or local reconstruction problem.

Evaluate both strengths and weaknesses in relation to the reconstruction task and observation domain.

2. Distinguish four levels of statement.

a. Observed artifact or condition: What is actually present, absent, inconsistent, accessible, or inaccessible?

b. Architectural role: How can this element be interpreted within DIO/ODI? What reconstruction-supporting or reconstruction-straining function does it have?

c. Local reconstruction consequence: What can an observer entering through this representation plausibly recover, miss, or misunderstand?

d. System-level significance: Does the local condition materially compromise the identity of the framework as a whole, or do other representations and pathways preserve sufficient continuity?

Do not silently jump from (a) to (d).

3. Use precise language without making every sentence defensive.

Where an outcome has not been directly observed, prefer formulations such as:

- “can be interpreted within DIO as a mechanism for…”
- “provides structural support for…”
- “is designed to…” when the design intention is documented;
- “creates a potential obstacle to…”
- “the inspected pathway supports…”
- “within this observation domain, the available representations appear sufficient to…”

Avoid converting these into unconditional claims such as “prevents,” “ensures,” “eliminates,” or “destroys” unless the evidence supports that scope.

A clear scope statement at the beginning of a section is sufficient. Do not attach the same disclaimer to every paragraph.

4. Evaluate materiality, not merely defect counts.

For each important weakness, ask:

- Which reconstruction task does it affect?
- Which observer or entry point is affected?
- Does it concern the author, the framework, a concept, a publication, or a particular version?
- Does it obscure the referent, alter a central conceptual relation, or merely reduce detail?
- Can another accessible representation contextualize, correct, or compensate for it?
- Is compensation actually inspectable, or only assumed?
- Is the difficulty locally contained, or does it propagate across layers?

Do not assume that redundancy guarantees compensation. Do not assume that local failure defeats the distributed whole.

5. Treat variation and change carefully.

Distinguish:

- identity-preserving variation;
- documented conceptual development;
- version misalignment;
- incompatible current claims;
- susceptibility to reconstruction failure;
- an observed reconstruction failure.

A historical edition is not defective merely because it preserves an earlier state. Conversely, historical provenance does not automatically resolve every conflict encountered by a current observer.

6. Keep conceptual and infrastructural graphs distinct.

Do not require the distribution network to reproduce the K6 conceptual model literally.

Separate conceptual interdependence from hyperlink topology, provenance relations, repository structure, and actual observer traversal.

Any numerical graph finding must state its observation boundary, node and edge definitions, and relevant directionality.

7. Treat acquisition failures as observer-relative unless verified otherwise.

A failed fetch establishes that a particular acquisition route failed. It does not by itself establish that the resource is absent or unavailable through every route.

8. Do not presume a favorable answer.

The clarification does not instruct you to conclude that the ecosystem is resilient. It instructs you to assess resilience at the appropriate level.

A positive, negative, mixed, or indeterminate conclusion is acceptable, provided that local observations and system-level judgments are connected explicitly.

**REQUESTED REVISION**

Please produce:

1. A revised answer to the research question.
2. A concise account of the principal mechanisms supporting reconstruction.
3. A materiality assessment of the principal weaknesses.
4. A comparison of at least two entry points, using inspected evidence where available.
5. A correction table: original wording | revised wording | reason for correction.
6. A short synthesis identifying:

- what appears to hold together;
- where continuity is strained;
- what cannot be determined from the observed snapshot.

Preserve useful findings from your original report. Correct their scope or interpretation where necessary rather than replacing the analysis with generic methodological caution.

Do not invent new observations or measurements. If additional investigation is necessary, identify it explicitly rather than presenting it as already completed.

**MODEL-SPECIFIC CORRECTION: CLAUDE**

Preserve your concrete diagnostics and the separation of conceptual and distribution graphs, but reassess how local findings support broader reconstruction judgments.

Your measurements were derived from summarized fetch outputs, with only 19 of 74 distribution nodes read directly. Keep computed properties of that extracted graph distinct from properties established for the underlying ecosystem. An unread node is not a confirmed sink, and an unreturned link is not a confirmed absent link.

Qualify hub-removal findings by directionality, weak versus strong connectivity, included edge types and acquisition coverage. Explain which reconstruction tasks the observed dependencies affect; do not infer whole-system fragility merely from fragmentation of the sampled graph.

Revisit these interpretations:

- concept and version DOIs as an “observed identifier split”;
- an existing record not reached from selected seeds as “Entity Omission”;
- archived v1 versus living v2 as “Temporal Misalignment”;
- differing affiliations as evidence that “the author is represented as two entities”.

Distinguish legitimate identifier roles, historical states and contextual representations from failures to reconstruct their relationships. Apply failure-mode labels only where their defining conditions are supported.

Your K6 and disconnected-cluster findings are useful, but absence of an encoded relation is not absence of conceptual connection. Assess what an observer restricted to the inspected serialization cannot traverse, and whether accessible prose, provenance or mappings supply that connection. Do not require the vocabulary to reproduce the conceptual K6 as a literal mesh.

Treat multilingual findings according to actual inspection depth. Separate missing metadata or backlinks from semantic incompatibility, and do not generalize from four inspected editions to all sixteen.

Keep the authorization analogy bounded: declared AI-use preferences, an intermediary’s reported withholding of content, and authorization of persistent identity-changing actions are different phenomena. Do not infer the cause of withholding unless documented.

Do not use institutional maturity as a substitute for analysis. Limited history, reception or adoption may characterize an emerging framework, but do not by themselves establish conceptual incoherence or reconstruction failure. Retain consequential criticism without requiring a new framework to possess the history of an established discipline.

For your principal weaknesses, explain what remains reconstructable, what becomes uncertain, and whether an inspectable alternative pathway compensates. Your revised assessment should answer whether the distributed identity appears to hold together—not merely whether its individual representations contain defects.

## Final integration instruction

I don’t want another “revised answer” or a commentary on the previous analysis. I want to combine the two outputs into a single, standalone paper.

Take the structure and thematic scope of the first research report and incorporate the findings, clarifications, and shifts in interpretation from the second output. Adjust the original structure as needed—the goal is not to mechanically preserve the sections, but to provide a coherent interpretation.

Reflect this new understanding throughout the entire analysis, not just in the conclusion. Retain specific findings, sources, measurements, and relevant limits, but reassess their significance where the second output has provided greater precision. Do not evaluate shortcomings or strengths in isolation: explain what they mean for the reconstructability of DIO/ODI in the observed time snapshot and at various levels of reconstruction detail.

The final text must stand on its own, as if it had been written from the beginning as a single research report. No references to our conversation, no phrases like “in the previous response,” and no explanations of corrections made. Do not resubmit a revision plan or a summary of changes—write the entire paper directly.
