[Versione italiana](README.it.md) · [Web page with progress checkboxes](https://dilettafalcone.it/en/open-medical-informatics/)

# Open Medical Informatics

**A free medical informatics curriculum for physicians.**

Modelled on [OSSU Computer Science](https://github.com/ossu/computer-science), for those starting from zero in computing: a common core (levels 0–5), then a track of your choice, *Clinician-Bridge* (leads projects, writes little code) or *Clinician-Developer* (programs and analyses data).

Curator: [Diletta Falcone](https://dilettafalcone.it) · Revised: 22 Nov 2026

## Principles

- **Free:** free resources only ("audit" courses are flagged in the Notes).
- **Authoritative sources, always cited:** every entry points to the References; the rules for proposing an entry are in [CONTRIBUTING.md](CONTRIBUTING.md).
- **From zero in computing, not in medicine:** you program in **Python** and build something at every level, never with real patient data.
- **AI as a tutor:** always verify every fact against a primary source [1], never paste patient data [2], write the exercise code yourself.

## How to use this guide

Levels 0–5 are taken in order, then you choose a track (A or B). Numbers in square brackets point to the References.

---

## Level 0 · Introduction

**Goal:** understand what biomedical informatics is, which roles exist, and how the Italian digital health system is organised. **Total: ~15 hours.**

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Definition of biomedical informatics and competencies in medical informatics | AMIA (Kulikowski et al., 2012) [3] and IMIA (Mantas et al., 2010) [4]. [PubMed 22683918](https://pubmed.ncbi.nlm.nih.gov/22683918/), [PubMed 20054502](https://pubmed.ncbi.nlm.nih.gov/20054502/) | Scientific society, Peer-reviewed | EN | ~4 h (estimate) | None | Two reference articles on what the discipline is and which competencies are needed. |
| Introduction to Biomedical Informatics | CHOP OPEN, Children's Hospital of Philadelphia (Bonafide, 2022 seminar). [Link](https://open.chop.edu/?p=8933) | Institution (university hospital) | EN | ~1 h | None | Free with an account. A single lecture; the page warns that it may be dated. |
| Global strategy on digital health 2020–2025 | WHO, 2021. [Link](https://www.who.int/publications/i/item/9789240020924) [5] | Institution | EN | ~3 h (estimate) | None | Free PDF (CC BY-NC-SA 3.0 IGO). Summary and principles. |
| Digital health in Italy: FSE 2.0, Ecosistema Dati Sanitari, PNRR Missione 6 | Ministero della Salute: [FSE](https://www.salute.gov.it/new/it/tema/fascicolo-sanitario-elettronico/), [PNRR Missione Salute](https://www.salute.gov.it/new/it/tema/pnrr-missione-salute/); national portal [fascicolosanitario.gov.it](https://www.fascicolosanitario.gov.it/); decrees [6] [7] | Institution | IT | ~4 h (estimate) | None | Guided reading, not a course. The FSE 2.0 decree is dated 7 September 2023 [6]; the EDS was established by the decree of 31 December 2024 [7]. |
| Collaborative Data Science for Healthcare (HST.953, 2020), introductory lectures | MIT OpenCourseWare / MIT Critical Data. [Link](https://ocw.mit.edu/courses/hst-953-collaborative-data-science-for-healthcare-fall-2020) | University | EN | ~3 h (estimate) | None | Only the first lectures, for an overview; the rest returns in levels 3 and 5. |

---

## Level 1 · Computing basics

**Goal (bare minimum):** write small programs in Python, work from the command line with git, and query a database with SQL. **Total: ~65 hours.** The full CS50P course and algorithms are moved to Track B.

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Python for Everybody | C. R. Severance, [py4e.com](https://www.py4e.com/) [8] | Open materials | EN | ~35 h (estimate) | None | Free materials (book, videos, exercises); certificates are elsewhere. Chapters on variables, loops, functions, strings, files, lists, dictionaries: enough for the common core. |
| The Missing Semester of Your CS Education | MIT (CSAIL / MIT Open Learning). [Link](https://missing.csail.mit.edu/) | University | EN | ~10 h (estimate) | Basic Python | Notes under an open licence, CC BY-NC-SA. Only the lectures on the shell, editors and version control (git) are followed. |
| CS50's Introduction to Databases with SQL (first lectures) | Harvard University (CS50). [Link](https://cs50.harvard.edu/sql/) | University | EN | ~20 h (estimate) | None | Free via OpenCourseWare; here only the first lectures: SQLite, joins, normalisation. |

---

## Level 2 · Data and statistics (in Python)

**Goal (bare minimum):** read and write a correct statistical analysis of clinical data, clean data, make honest charts. **Total: ~60 hours.**

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Think Stats: Exploratory Data Analysis in Python (3rd ed.) | A. B. Downey [9]. [Link](https://allendowney.github.io/ThinkStats/) | Open materials | EN | ~30 h (estimate) | Level 1 | Free online (Creative Commons licence), with executable notebooks on Google Colab. Probability, distributions, estimation, hypothesis tests, regression, survival analysis. |
| Python Data Science Handbook (NumPy, pandas, Matplotlib) | J. VanderPlas [10]. [Link](https://jakevdp.github.io/PythonDataScienceHandbook/) | **Industry** (publisher O'Reilly; text free online, CC-BY-NC-ND licence) | EN | ~20 h (estimate) | Level 1 | Only chapters 2–4. |
| Guided analysis of real anonymised clinical data: MIMIC-IV demo | PhysioNet / MIT Laboratory for Computational Physiology. [Demo](https://physionet.org/content/mimic-iv-demo/); article [11] | Institution, Peer-reviewed | EN | ~10 h (estimate) | The two previous entries | The demo is openly accessible. Exercise: cohort, descriptive statistics, a regression model. |
| *(optional, for those doing clinical research)* Introduction to Statistics for the Life and Biomedical Sciences, with exercises in **R** | OpenIntro [12]. [Link](https://www.openintro.org/book/biostat/) | Open materials | EN | ~50 h (estimate) | Level 1 | Free PDF (the price can be set to $0). Linear and logistic regression, survival. It is the only R entry; excluded from the total. |

---

## Level 3 · Health informatics

**Goal (bare minimum):** understand how clinical data are represented and exchanged (standards and terminologies), use FHIR and OMOP at a basic level, and recognise how decision support and human factors determine the real-world use of a system. **Total: ~65 hours.** The materials are those published free of charge by the standards bodies.

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Terminologies: SNOMED CT, LOINC, ICD-11 (with an overview of standards) | **SNOMED International**: [education](https://www.snomed.org/education) (introductory tutorials accessible without an account); **Regenstrief**: [LOINC](https://www.regenstrief.org/real-world-solutions/loinc/) (LOINC is free); **WHO**: [ICD-11 Training Package](https://icdcdn.who.int/icd11training/index.html) [13]; **NLM**: [tutorial on standards and terminologies](https://www.nlm.nih.gov/oet/ed/healthdatastandards/index.html) [14] | Standards body (SNOMED, Regenstrief, WHO); Institution (NLM) | EN | ~19 h (estimate) | Level 0 | **Italy does not appear among the member countries of SNOMED International** (list of 54–55 members, consulted on 22 Nov 2026) [15]: the official courses are free for members and paid outside the members [16], so the introductory tutorials and the NLM tutorial are used here. |
| HL7 FHIR: concepts, resources, REST and search | HL7 International, FHIR specification [17]: [clinical overview](https://www.hl7.org/fhir/overview-clinical.html), [developer overview](https://www.hl7.org/fhir/overview-dev.html), [resource list](https://www.hl7.org/fhir/resourcelist.html), [search](https://www.hl7.org/fhir/search.html); NIH (NCPI), notebook [fhir-101](https://github.com/NIH-NCPI/fhir-101); HL7 Italia, [hl7.it](https://hl7.it/) | Standards body, Institution | EN (HL7 Italia: IT) | ~12 h (estimate) | Level 1 | The official HL7 courses are not free: the specification's teaching material is studied, with the exercises of the NIH notebook. |
| DICOM: data model and image flow | NEMA/MITA, DICOM Standard, Part PS3.1 [18]: [PS3.1](https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html), [presentation of the standard](https://www.dicomstandard.org/about) | Standards body | EN | ~4 h (estimate) | Level 1 | Only the introduction and overview, not the whole standard. |
| OMOP CDM and OHDSI | OHDSI, *The Book of OHDSI* [19] (CC0): [link](https://ohdsi.github.io/TheBookOfOhdsi/); EHDEN Academy (European consortium): [link](https://academy.ehden.eu/) | Standards body (OHDSI) | EN | ~12 h (estimate) | Levels 1–2 (SQL) | EHDEN Academy: free, with an account (confirmed by EHDEN sources). Chapters 4–6 of the book (CDM, vocabularies, ETL). Reference article: Hripcsak et al. [20]. |
| Electronic health records and secondary data analysis | MIT Critical Data, *Secondary Analysis of Electronic Health Records* (Springer, 2016, open access) [21]. [Link](https://www.ncbi.nlm.nih.gov/books/NBK543627/) | University (open-access book) | EN | ~10 h (estimate) | Level 2 | Choose the chapters on data cleaning, bias and study design. |
| Clinical decision support, human factors and workflows | Sutton et al. 2020 [22]; Zhang and Walji (TURF) 2011 [23]; NIST, NISTIR 7741 [24]: [link](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7741.pdf); HL7, [CDS Hooks](https://cds-hooks.org/) | Peer-reviewed, Institution | EN | ~8 h (estimate) | Level 0 | Two articles and a NIST guide on the usability of health records; CDS Hooks to integrate decision support into the clinical workflow. |

---

## Level 4 · Regulation, privacy and cybersecurity in healthcare

**Goal:** know what can be done with health data, when software is a medical device, and the fundamentals of cybersecurity in healthcare. **Total: ~35 hours.**

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| GDPR and health data (art. 9) | Regulation (EU) 2016/679 [2]: [text and page of the Garante](https://www.garanteprivacy.it/regolamentoue); Garante, [Sanità e ricerca scientifica](https://www.garanteprivacy.it/temi/sanita-e-ricerca-scientifica) | Institution | IT | ~6 h (estimate) | Level 0 | Reading of art. 9 (special categories of data, including data concerning health) and of the Garante's decisions on healthcare. |
| FSE 2.0 and Ecosistema Dati Sanitari: rules and privacy | Decreto 7 settembre 2023 (GU n. 249 del 24/10/2023) [6]: [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/gu/2023/10/24/249/sg/pdf); decreto 31 dicembre 2024 (GU n. 53 del 5/3/2025) [7]: [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/gu/2025/03/05/53/sg/pdf); Garante, [FAQ sul fascicolo sanitario](https://www.garanteprivacy.it/faq/fascicolo-sanitario) | Institution | IT | ~6 h (estimate) | Level 0 | The 2023 decree has been amended by later decrees: always read the most recent consolidated text. |
| European Health Data Space (EHDS) | Regulation (EU) 2025/327 [25]; European Commission, [EHDS page](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en) | Institution | EN/IT | ~4 h (estimate) | Level 0 | Published in the Official Journal of the EU on 5 March 2025. Application dates are staggered: check the Commission's page. |
| Software as a medical device (MDR) | Regulation (EU) 2017/745 [26]; European Commission, MDCG 2019-11 (qualification and classification of software) [27]: [MDCG page](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en); Ministero della Salute, [dispositivi medici](https://www.salute.gov.it/new/it/tema/dispositivi-medici/) | Institution | EN/IT | ~5 h (estimate) | Level 0 | When software is a medical device and how it is classified. |
| Cybersecurity: fundamentals and threats to healthcare | Harvard University (CS50), [CS50's Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/); ENISA, *Health Threat Landscape* (2023) [28]: [page](https://www.enisa.europa.eu/publications/health-threat-landscape) | University, Institution | EN | ~14 h (estimate) | None | Of the CS50 course the parts on accounts, data and privacy are followed. The ENISA report analyses cybersecurity incidents in the EU health sector from January 2021 to March 2023. |

---

## Level 5 · AI in medicine (core pillar)

**Goal:** understand how ML, deep learning and LLMs work, what their limits are (hallucinations included), be able to evaluate a model clinically (validation, calibration, bias, reporting guidelines) and know ethics and rules (AI Act, MDR, WHO). **Total: ~87 hours.** Where possible, in Italian.

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| AI fundamentals (in Italian) | University of Helsinki with MinnaLearn, *Elements of AI*, Italian version promoted by the Dipartimento per la trasformazione digitale: [link](https://www.elementsofai.it/). *(alternative)* Federica Web Learning, *Intelligenza artificiale e scienza dei dati - le basi*: [AI catalogue](https://www.federica.eu/intelligenza-artificiale/) | University | **IT** | ~20 h (estimate) | None | Both are free (Federica states that all its courses are "100% gratuiti"). Federica requires registration to open the courses; duration not stated. |
| Fundamentals of machine learning and deep learning | G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor, *An Introduction to Statistical Learning with Applications in Python* (Springer, 2023) [29]: [link](https://www.statlearning.com/). *(alternative in Italian)* Federica Web Learning, *Machine Learning* (F. Stella): [AI catalogue](https://www.federica.eu/intelligenza-artificiale/). *(optional)* Google, [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | University (book, free PDF); the optional entry is **Industry** | EN (alternative IT) | ~20 h (estimate) | Levels 1–2 | Choose the chapters on regression, classification, model evaluation, trees and an introduction to neural networks. |
| Machine learning for healthcare | MIT 6.S897 / HST.956, *Machine Learning for Healthcare* (Sontag, Szolovits, 2019). [Link](https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/) | University | EN | ~10 h (estimate) | Basic ML | Free notes and videos. Only a few lectures are followed (risk stratification, bias, interpretability); the full course assumes university-level ML. |
| Generative AI and LLMs: how they work, limits, hallucinations, prompting | Politecnico di Milano, POK, *Data, Algorithms, and Ethical Challenges: Exploring the AI Revolution in Medicine* (free, 12 hours): [link](https://www.pok.polimi.it/course/view.php?id=177) [30]. Articles: Thirunavukarasu et al. 2023 (LLMs in medicine) [31]; Meskó 2023 (prompting for healthcare professionals) [32]; Ji et al. 2023 (hallucinations) [1]. *(optional)* Stanford, CS324 *Large Language Models* (lecture notes): [link](https://stanford-cs324.github.io/winter2022/) [33] | University, Peer-reviewed | EN | ~19 h (12 h stated by the POK course + 7 h of articles, estimate) | Level 2 | The CS324 notes do not cite hallucinations: the articles cover them. |
| Clinical evaluation of models | TRIPOD+AI [34], CONSORT-AI [35], DECIDE-AI [36] (EQUATOR Network: [TRIPOD](https://www.equator-network.org/reporting-guidelines/tripod-statement/), [CONSORT-AI](https://www.equator-network.org/reporting-guidelines/consort-artificial-intelligence/), [DECIDE-AI](https://www.equator-network.org/reporting-guidelines/decide-ai/)); Van Calster et al. 2019, calibration [37] | Peer-reviewed, Scientific society (EQUATOR) | EN | ~8 h (estimate) | Level 2 | External validation, calibration, bias and checklists for reporting studies with AI. A checklist is applied to a real study. |
| Ethics and regulation of AI in healthcare | WHO, *Ethics and governance of AI for health* (2021) [38]: [link](https://www.who.int/publications/i/item/9789240029200); WHO, guidance on *large multi-modal models* (2025) [39]: [link](https://www.who.int/publications/i/item/9789240084759); Regulation (EU) 2024/1689 (AI Act) [40]: [Commission page](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Institution | EN/IT | ~10 h (estimate) | Level 4 | WHO documents as free PDFs (CC BY-NC-SA 3.0 IGO). For the AI Act and its relationship with the MDR use the official text in the EU Official Journal. |

---

## Track A · Clinician-Bridge

**For whom:** leads digital health projects, evaluates and buys technology, governs AI in the hospital; writes little code. **Hours: ~118.**

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Technology governance and assessment (HTA) | C. S. Goodman, *HTA 101* (NICHSR / National Library of Medicine, 2014) [41]: [archive](https://wayback.archive-it.org/org-350/https://www.nlm.nih.gov/nichsr/hta101/ta10101.html); O'Rourke et al. 2020, definition of HTA [42]; NICE, [Evidence standards framework](https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies) [43] | Institution, Peer-reviewed | EN | ~26 h (estimate) | Level 3 | The original NLM page is archived: the copy is used. Italian material (AGENAS) not found. |
| Designing decision support systems and usability | Sutton 2020 [22]; Bates 2003 [44]; Zhang and Walji 2011 [23]; NIST NISTIR 7741 [24]; HL7 [CDS Hooks](https://cds-hooks.org/) | Peer-reviewed, Institution | EN | ~20 h (estimate) | Level 3 | From reading to design: each student designs a decision flow using the criteria read. |
| Project and change management | WHO, *Digital Implementation Investment Guide* [45]: [link](https://www.who.int/publications/i/item/9789240010567); MIT OpenCourseWare, HST.921, *Information Technology in the Health Care System of the Future* (2009): [link](https://ocw.mit.edu/courses/hst-921-information-technology-in-the-health-care-system-of-the-future-spring-2009/) | Institution, University | EN | ~45 h (estimate) | Level 3 | The MIT material is from 2009: valid method, dated examples. |
| Buying and evaluating AI products | NHS AI Lab, *A buyer's guide to AI in health and care* [46]: [link](https://www.gov.uk/data-ethics-guidance/a-buyers-guide-to-ai-in-health-and-care); NICE, Evidence standards framework (link above); Regulations [26] and [40] | Institution | EN | ~12 h (estimate) | Levels 4–5 | Ten questions for AI buyers. A British document: adapt it to the Italian context with the MDR and the AI Act. |
| AI governance in the hospital | NIST, *AI Risk Management Framework 1.0* [47]: [link](https://www.nist.gov/itl/ai-risk-management-framework); WHO [38] [39] | Institution | EN | ~15 h (estimate) | Level 5 | AI risk management framework. Not specific to healthcare: complement it with the WHO documents. |

## Track B · Clinician-Developer

**For whom:** programs, analyses data, builds models and applications. **Hours: ~524.** The heaviest entries moved out of the common core are here.

| Course | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Complete Python | Harvard University, [CS50P](https://cs50.harvard.edu/python/) (here the completion beyond Python for Everybody) | University | EN | ~50 h (estimate: remaining hours) | Level 1 | Demanding university course. |
| Computer science and algorithms | Harvard University, [CS50x](https://cs50.harvard.edu/x/), CS50's Introduction to Computer Science; MIT OpenCourseWare, [6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (spring 2020) | University | EN | ~165 h (estimate: 11 weeks at 10–20 h per week, per the CS50x FAQ; 6.006 not counted) | Level 1 | All the weeks in C stay: demanding but formative (memory and data structures); then 6.006 as a rigorous in-depth follow-up, which requires discrete mathematics. |
| Web development and FHIR apps (SMART on FHIR) | University of Helsinki, [Full Stack Open](https://fullstackopen.com/en/) (parts 0–5); HL7, [SMART App Launch](https://www.hl7.org/fhir/smart-app-launch/); SMART Health IT (Boston Children's Hospital), [docs](https://docs.smarthealthit.org/); Mandel et al. 2016 [48] | University, Standards body, Peer-reviewed | EN | ~75 h (estimate) | Levels 1 and 3 | Full Stack Open is free (CC BY-NC-SA). The SMART App Launcher can be used without registration. |
| ML and deep learning in depth | Stanford University, [CS229 Machine Learning](https://cs229.stanford.edu/). *(optional)* fast.ai, [Practical Deep Learning](https://course.fast.ai/) | University; the optional entry is **Industry** | EN | ~65 h (estimate; fast.ai states 9 lessons, ~13.5 h) | Levels 2 and 5 | fast.ai requires about a year of Python. |
| Medical imaging | 3D Slicer (NIH-funded; Fedorov et al. 2012) [49]: [training](https://training.slicer.org/); Stanford, [CS231n](https://cs231n.stanford.edu/). *(optional)* MONAI, [tutorials](https://github.com/Project-MONAI/tutorials) | University, Peer-reviewed; MONAI is **Industry** | EN | ~35 h (estimate) | Level 3 (DICOM), 5 | MONAI is an open-source project with strong industry participation. |
| Clinical NLP and LLMs | Stanford University, [CS224N NLP with Deep Learning](https://web.stanford.edu/class/cs224n/). Hugging Face, [LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) (free). Systematic review of RAG (retrieval-augmented generation) in healthcare: Amugongo et al. 2025 [50], [PubMed 40498738](https://pubmed.ncbi.nlm.nih.gov/40498738/) | University, Peer-reviewed; the HF course is **Industry** | EN | ~83 h (estimate, review included, ~3 h) | Level 5; good Python | The HF course covers transformers, fine-tuning and LLMs, not RAG or local inference: for RAG in medicine the systematic review [50] is read. |
| Basic AI agents | Hugging Face, [AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) (free; frameworks smolagents, LlamaIndex, LangGraph) | **Industry** | EN | ~21 h (estimate) | NLP/LLM and ML | Free. |
| MLOps: from models to products | C. Kästner (Carnegie Mellon University), *Machine Learning in Production: From Models to Products* (MIT Press, 2025) [51]: [online book](https://mlip-cmu.github.io/book/) | University | EN | ~30 h (estimate) | Levels 1 and 5 | Text freely readable online (CC BY-NC-ND 4.0 licence). Choose the chapters on architecture and deployment, pipeline automation, quality assurance and responsible engineering. |

---

## Electives (about 25 hours each)

| Topic | Source | Source type | Language | Effort | Prerequisites | Notes |
|---|---|---|---|---|---|---|
| Genomics and bioinformatics | Galaxy Community [52]: [Galaxy Training Network](https://training.galaxyproject.org/) | Peer-reviewed | EN | ~25 h (estimate) | Level 1 | Galaxy Training Network learning paths on biological data analysis. |
| Digital public health and computational epidemiology | WHO, [OpenWHO](https://openwho.org/); ISS, [EpiCentro](https://www.epicentro.iss.it/) and [EDUISS](https://www.eduiss.it/) (free ISS distance learning, catalogues on public health and SABiC) | Institution | EN/IT | ~25 h (estimate) | Level 2 | Choose the OpenWHO courses on epidemiology and data; EDUISS and EpiCentro for the Italian context (registration required). |
| Advanced imaging | See Track B (3D Slicer, CS231n, MONAI) and [PS3.1 DICOM](https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html) [18]. | University, Standards body | EN | ~25 h (estimate) | Level 3 | For those who choose Track A: concepts only, without code. |
| Telemedicine | Conferenza Stato-Regioni, *Indicazioni nazionali per l'erogazione di prestazioni in telemedicina*, Accordo del 17 dicembre 2020, Rep. Atti n. 215/CSR [53]: [atto](https://www.statoregioni.it/it/conferenza-stato-regioni/sedute-2020/seduta-del-17122020/atti/repertorio-atto-n-215csr/), [PDF](https://www.statoregioni.it/media/3221/p-3-csr-rep-n-215-17dic2020.pdf) | Institution | IT | ~25 h (estimate) | Level 4 | The official text of the agreement was verified on the Conference's website (PDF reachable). |

---

## Contributing

Proposals and corrections by issue or pull request, following [CONTRIBUTING.md](CONTRIBUTING.md).

---

## References

(Vancouver style. Citations in the text point to the numbers below, in order of first appearance. Date of access to all links: 22 November 2026.)

1. Ji Z, Lee N, Frieske R, Yu T, Su D, Xu Y, et al. Survey of hallucination in natural language generation. ACM Comput Surv. 2023;55(12):Art. 248. doi:10.1145/3571730.
2. Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016, relativo alla protezione delle persone fisiche con riguardo al trattamento dei dati personali (GDPR). Gazzetta Ufficiale dell'Unione europea L 119, 4.5.2016, pp. 1-88. EUR-Lex: http://data.europa.eu/eli/reg/2016/679/oj. Italian text also at: https://www.garanteprivacy.it/regolamentoue
3. Kulikowski CA, Shortliffe EH, Currie LM, Elkin PL, Hunter LE, Johnson TR, et al. AMIA Board white paper: definition of biomedical informatics and specification of core competencies for graduate education in the discipline. J Am Med Inform Assoc. 2012;19(6):931-8. doi:10.1136/amiajnl-2012-001053. PMID: 22683918.
4. Mantas J, Ammenwerth E, Demiris G, Hasman A, Haux R, Hersh W, et al. Recommendations of the International Medical Informatics Association (IMIA) on education in biomedical and health informatics. Methods Inf Med. 2010;49(2):105-20. doi:10.3414/ME5119. PMID: 20054502.
5. World Health Organization. Global strategy on digital health 2020-2025. Geneva: WHO; 2021. Available from: https://www.who.int/publications/i/item/9789240020924
6. Italia. Ministero della Salute. Decreto 7 settembre 2023. Fascicolo sanitario elettronico 2.0. Gazzetta Ufficiale della Repubblica Italiana, Serie Generale n. 249, 24 ottobre 2023 (23A05829). Available from: https://www.gazzettaufficiale.it/eli/gu/2023/10/24/249/sg/pdf. Amended by later decrees (including the one of 11 November 2025, GU n. 286 of 10 December 2025).
7. Italia. Ministero della Salute. Decreto 31 dicembre 2024. Istituzione dell'Ecosistema dati sanitari (EDS). Gazzetta Ufficiale della Repubblica Italiana, Serie Generale n. 53, 5 marzo 2025 (25A01321). Available from: https://www.gazzettaufficiale.it/eli/gu/2025/03/05/53/sg/pdf
8. Severance CR. Python for Everybody (py4e). Available from: https://www.py4e.com/
9. Downey AB. Think Stats: exploratory data analysis in Python. 3rd ed. Green Tea Press. Available from: https://allendowney.github.io/ThinkStats/
10. VanderPlas J. Python data science handbook. Sebastopol (CA): O'Reilly Media; 2016. Available from: https://jakevdp.github.io/PythonDataScienceHandbook/
11. Johnson AEW, Bulgarelli L, Shen L, Gayles A, Shammout A, Horng S, et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci Data. 2023;10(1):1. doi:10.1038/s41597-022-01899-x. PMID: 36596836.
12. OpenIntro. Introduction to statistics for the life and biomedical sciences. 1st ed.. Available from: https://www.openintro.org/book/biostat/
13. World Health Organization. ICD-11 training package. Geneva: WHO. Available from: https://icdcdn.who.int/icd11training/index.html
14. National Library of Medicine. Health data standards and terminologies: a tutorial. Bethesda (MD): NLM. Available from: https://www.nlm.nih.gov/oet/ed/healthdatastandards/index.html
15. SNOMED International. Members [Internet]. Available from: https://www.snomed.org/members (cited 22 Nov 2026: list of 54-55 countries and territories; Italy does not appear).
16. National Library of Medicine. SNOMED CT overview [Internet]. Bethesda (MD): NLM. Available from: https://www.nlm.nih.gov/healthit/snomedct/snomed_overview.html (the NLM distributes SNOMED CT at no cost to its US users as a member; fees may apply outside member countries).
17. HL7 International. HL7 FHIR: Fast Healthcare Interoperability Resources (specification). Available from: https://www.hl7.org/fhir/
18. National Electrical Manufacturers Association (NEMA). DICOM PS3.1: Introduction and overview. In: Digital Imaging and Communications in Medicine (DICOM) Standard. Rosslyn (VA): NEMA. Available from: https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html
19. OHDSI Collaborative. The Book of OHDSI: Observational Health Data Sciences and Informatics. 2019 (continuously updated). Available from: https://ohdsi.github.io/TheBookOfOhdsi/
20. Hripcsak G, Duke JD, Shah NH, Reich CG, Huser V, Schuemie MJ, et al. Observational Health Data Sciences and Informatics (OHDSI): opportunities for observational researchers. Stud Health Technol Inform. 2015;216:574-8. PMID: 26262116.
21. MIT Critical Data. Secondary analysis of electronic health records. Cham: Springer; 2016. doi:10.1007/978-3-319-43742-2. Open access at: https://www.ncbi.nlm.nih.gov/books/NBK543627/
22. Sutton RT, Pincock D, Baumgart DC, Sadowski DC, Fedorak RN, Kroeker KI. An overview of clinical decision support systems: benefits, risks, and strategies for success. NPJ Digit Med. 2020;3:17. doi:10.1038/s41746-020-0221-y. PMID: 32047862.
23. Zhang J, Walji MF. TURF: toward a unified framework of EHR usability. J Biomed Inform. 2011;44(6):1056-67. doi:10.1016/j.jbi.2011.08.005. PMID: 21867774.
24. Schumacher RM, Lowry SZ. NIST guide to the processes approach for improving the usability of electronic health records. NISTIR 7741. Gaithersburg (MD): National Institute of Standards and Technology; 2010. Available from: https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7741.pdf
25. Regolamento (UE) 2025/327 del Parlamento europeo e del Consiglio, dell'11 febbraio 2025, sullo spazio europeo dei dati sanitari (EHDS). Gazzetta Ufficiale dell'Unione europea L, 2025/327, 5.3.2025. EUR-Lex: https://eur-lex.europa.eu/eli/reg/2025/327/oj. Commission page: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en
26. Regolamento (UE) 2017/745 del Parlamento europeo e del Consiglio, del 5 aprile 2017, relativo ai dispositivi medici (MDR). Gazzetta Ufficiale dell'Unione europea L 117, 5.5.2017, pp. 1-175. EUR-Lex: http://data.europa.eu/eli/reg/2017/745/oj
27. Medical Device Coordination Group. MDCG 2019-11: guidance on qualification and classification of software in Regulation (EU) 2017/745 (MDR) and Regulation (EU) 2017/746 (IVDR). Brussels: European Commission; 2019. Page of the MDCG documents: https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en
28. European Union Agency for Cybersecurity (ENISA). Health threat landscape. Heraklion: ENISA; 2023 (5 July). Available from: https://www.enisa.europa.eu/publications/health-threat-landscape
29. James G, Witten D, Hastie T, Tibshirani R, Taylor J. An introduction to statistical learning with applications in Python. Cham: Springer; 2023. doi:10.1007/978-3-031-38747-0. Available from: https://www.statlearning.com/
30. Politecnico di Milano, POK (Polimi Open Knowledge). Data, algorithms, and ethical challenges: exploring the AI revolution in medicine [MOOC]. Milano: Politecnico di Milano; 2023-. Available from: https://www.pok.polimi.it/course/view.php?id=177
31. Thirunavukarasu AJ, Ting DSJ, Elangovan K, Gutierrez L, Tan TF, Ting DSW. Large language models in medicine. Nat Med. 2023;29(8):1930-40. doi:10.1038/s41591-023-02448-8. PMID: 37460753.
32. Meskó B. Prompt engineering as an important emerging skill for medical professionals: tutorial. J Med Internet Res. 2023;25:e50638. doi:10.2196/50638. PMID: 37792434.
33. Liang P, Bommasani R, et al. CS324: Large Language Models [course notes]. Stanford (CA): Stanford University; 2022. Available from: https://stanford-cs324.github.io/winter2022/
34. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378. PMID: 38626948.
35. Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK; SPIRIT-AI and CONSORT-AI Working Group. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nat Med. 2020;26(9):1364-74. doi:10.1038/s41591-020-1034-x. PMID: 32908283.
36. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nat Med. 2022;28(5):924-33. doi:10.1038/s41591-022-01772-9. PMID: 35585198.
37. Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW; Topic Group 'Evaluating diagnostic tests and prediction models' of the STRATOS initiative. Calibration: the Achilles heel of predictive analytics. BMC Med. 2019;17(1):230. doi:10.1186/s12916-019-1466-7. PMID: 31842878.
38. World Health Organization. Ethics and governance of artificial intelligence for health: WHO guidance. Geneva: WHO; 2021. Available from: https://www.who.int/publications/i/item/9789240029200
39. World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. Geneva: WHO; 2025. Available from: https://www.who.int/publications/i/item/9789240084759
40. Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale (AI Act). Gazzetta Ufficiale dell'Unione europea L, 2024/1689, 12.7.2024. EUR-Lex: http://data.europa.eu/eli/reg/2024/1689/oj. Commission page: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
41. Goodman CS. HTA 101: introduction to health technology assessment. Bethesda (MD): National Library of Medicine, NICHSR; 2014. Available from: https://wayback.archive-it.org/org-350/https://www.nlm.nih.gov/nichsr/hta101/ta10101.html
42. O'Rourke B, Oortwijn W, Schuller T; International Joint Task Group. The new definition of health technology assessment: a milestone in international collaboration. Int J Technol Assess Health Care. 2020;36(3):187-90. doi:10.1017/S0266462320000215. PMID: 32398176.
43. National Institute for Health and Care Excellence. Evidence standards framework (ESF) for digital health technologies. London: NICE (current version). Available from: https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies
44. Bates DW, Kuperman GJ, Wang S, Gandhi T, Kittler A, Volk L, et al. Ten commandments for effective clinical decision support: making the practice of evidence-based medicine a reality. J Am Med Inform Assoc. 2003;10(6):523-30. doi:10.1197/jamia.M1370. PMID: 12925543.
45. World Health Organization. Digital implementation investment guide (DIIG): integrating digital interventions into health programmes. Geneva: WHO; 2020. ISBN 9789240010567. Available from: https://www.who.int/publications/i/item/9789240010567
46. NHSX / NHS AI Lab. A buyer's guide to AI in health and care. London: NHS; 2020 (page updated on GOV.UK). Available from: https://www.gov.uk/data-ethics-guidance/a-buyers-guide-to-ai-in-health-and-care
47. National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. Gaithersburg (MD): NIST; 2023. doi:10.6028/NIST.AI.100-1. Available from: https://www.nist.gov/itl/ai-risk-management-framework
48. Mandel JC, Kreda DA, Mandl KD, Kohane IS, Ramoni RB. SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. J Am Med Inform Assoc. 2016;23(5):899-908. doi:10.1093/jamia/ocv189. PMID: 26911829.
49. Fedorov A, Beichel R, Kalpathy-Cramer J, Finet J, Fillion-Robin JC, Pujol S, et al. 3D Slicer as an image computing platform for the Quantitative Imaging Network. Magn Reson Imaging. 2012;30(9):1323-41. doi:10.1016/j.mri.2012.05.001. PMID: 22770690.
50. Amugongo LM, Mascheroni P, Brooks S, Doering S, Seidel J. Retrieval augmented generation for large language models in healthcare: a systematic review. PLOS Digit Health. 2025;4(6):e0000877. doi:10.1371/journal.pdig.0000877. PMID: 40498738.
51. Kästner C. Machine learning in production: from models to products. Cambridge (MA): MIT Press; 2025. Available from: https://mlip-cmu.github.io/book/
52. Galaxy Community. The Galaxy platform for accessible, reproducible and collaborative biomedical analyses: 2022 update. Nucleic Acids Res. 2022;50(W1):W345-51. doi:10.1093/nar/gkac247. PMID: 35446428.
53. Conferenza permanente per i rapporti tra lo Stato, le Regioni e le Province autonome di Trento e di Bolzano. Accordo ai sensi dell'art. 4, c. 1, D.Lgs. 281/1997 sul documento «Indicazioni nazionali per l'erogazione di prestazioni in telemedicina». Rep. Atti n. 215/CSR, seduta del 17 dicembre 2020. Available from: https://www.statoregioni.it/it/conferenza-stato-regioni/sedute-2020/seduta-del-17122020/atti/repertorio-atto-n-215csr/

---

## License

© 2026 Diletta Falcone. This curriculum is released under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en) license (Creative Commons Attribution-ShareAlike 4.0 International): you may copy, redistribute and adapt it, including for commercial purposes, giving credit to the author and sharing your changes under the same license. The legal text is in the [LICENSE](LICENSE) file. The third-party courses and documents cited remain subject to their own licenses.
