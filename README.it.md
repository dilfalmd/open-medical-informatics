[English version](README.md) · [Pagina web con caselle di avanzamento](https://dilettafalcone.it/open-health-informatics/)

# Open Health Informatics

**Un curriculum gratuito di informatica sanitaria per medici e professionisti della salute.**

Sul modello di [OSSU Computer Science](https://github.com/ossu/computer-science), per chi parte da zero in informatica: un tronco comune (livelli 0–5), poi un indirizzo a scelta, *Ponte* (guida i progetti, scrive poco codice), *Sviluppatore* (programma e analizza) o *Bioinformatica traslazionale* (genomica applicata alla clinica).

**A chi si rivolge.** A medici e professionisti sanitari (infermieri, ostetriche, tecnici sanitari, farmacisti, professioni della riabilitazione), che possono seguirlo così com'è. Biologi e chi lavora in laboratorio trovano il loro percorso nell'indirizzo C. Statistici sanitari ed epidemiologi partono dall'altro lato: possono saltare il Livello 2 e trovano naturale l'indirizzo B, ma la guida dà per scontata una conoscenza di base del lavoro clinico.

Revisione: 22/11/2026

## Principi

- **Gratuito:** solo risorse gratuite (i corsi «in audit» sono segnalati nelle Note).
- **Fonti autorevoli, sempre citate:** ogni voce rinvia alla Bibliografia; le regole per proporre una voce sono in [CONTRIBUTING.md](CONTRIBUTING.md).
- **Da zero in informatica, non in clinica:** si programma in **Python** e a ogni livello si costruisce qualcosa, mai con dati di pazienti reali.
- **AI come tutor:** verificare sempre ogni fatto su una fonte primaria [1], non incollare mai dati di pazienti [2], scrivere da sé il codice degli esercizi.

## Come usare questa guida

I livelli 0–5 si fanno in ordine, poi si sceglie un indirizzo (A, B o C). I numeri tra parentesi quadre rinviano alla Bibliografia.

---

## Livello 0 · Introduzione

**Obiettivo:** capire che cos'è l'informatica biomedica, quali ruoli esistono e com'è fatto il sistema sanitario digitale italiano. **Totale: ~15 ore.**

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Definizione di informatica biomedica e competenze in informatica medica | AMIA (Kulikowski et al., 2012) [3] e IMIA (Mantas et al., 2010) [4]. [PubMed 22683918](https://pubmed.ncbi.nlm.nih.gov/22683918/), [PubMed 20054502](https://pubmed.ncbi.nlm.nih.gov/20054502/) | Società scientifica, Peer-reviewed | EN | ~4 h (stima) | Nessuno | Due articoli di riferimento su che cos'è la disciplina e quali competenze servono. |
| Introduction to Biomedical Informatics | CHOP OPEN, Children's Hospital of Philadelphia (Bonafide, seminario 2022). [Link](https://open.chop.edu/?p=8933) | Istituzione (ospedale universitario) | EN | ~1 h | Nessuno | Gratuito con account. Una sola lezione, la pagina avverte che può essere datata. |
| Global strategy on digital health 2020–2025 | OMS, 2021. [Link](https://www.who.int/publications/i/item/9789240020924) [5] | Istituzione | EN | ~3 h (stima) | Nessuno | PDF gratuito (CC BY-NC-SA 3.0 IGO). Sintesi e principi. |
| Sanità digitale in Italia: FSE 2.0, Ecosistema Dati Sanitari, PNRR Missione 6 | Ministero della Salute: [Sanità digitale](https://www.salute.gov.it/new/it/sanita-digitale/), [PNRR Missione Salute](https://www.pnrr.salute.gov.it/); portale nazionale [fascicolosanitario.gov.it](https://www.fascicolosanitario.gov.it/); decreti [6] [7] | Istituzione | IT | ~4 h (stima) | Nessuno | Lettura guidata, non un corso. Il decreto FSE 2.0 è del 7 settembre 2023 [6]; l'EDS è istituito dal decreto del 31 dicembre 2024 [7]. |
| Collaborative Data Science for Healthcare (HST.953, 2020), lezioni introduttive | MIT OpenCourseWare / MIT Critical Data. [Link](https://ocw.mit.edu/courses/hst-953-collaborative-data-science-for-healthcare-fall-2020) | Università | EN | ~3 h (stima) | Nessuno | Solo le prime lezioni, per una panoramica; il resto torna nei livelli 3 e 5. |

---

## Livello 1 · Basi di informatica

**Obiettivo (minimo indispensabile):** scrivere piccoli programmi in Python, lavorare da riga di comando con git e interrogare un database con SQL. **Totale: ~65 ore.** Il corso CS50P completo e gli algoritmi sono spostati nell'indirizzo B.

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Python for Everybody | C. R. Severance, [py4e.com](https://www.py4e.com/) [8] | Materiali aperti | EN | ~35 h (stima) | Nessuno | Materiali gratuiti (libro, video, esercizi); i certificati sono altrove. Capitoli su variabili, cicli, funzioni, stringhe, file, liste, dizionari: basta per il tronco comune. |
| The Missing Semester of Your CS Education | MIT (CSAIL / MIT Open Learning). [Link](https://missing.csail.mit.edu/) | Università | EN | ~10 h (stima) | Python di base | Note con licenza aperta CC BY-NC-SA. Si seguono solo le lezioni su shell, editor e controllo di versione (git). |
| CS50's Introduction to Databases with SQL (prime lezioni) | Harvard University (CS50). [Link](https://cs50.harvard.edu/sql/) | Università | EN | ~20 h (stima) | Nessuno | Gratuito via OpenCourseWare; qui solo le prime lezioni: SQLite, join, normalizzazione. |

---

## Livello 2 · Dati e statistica (in Python)

**Obiettivo (minimo indispensabile):** leggere e scrivere un'analisi statistica corretta su dati clinici, pulire dati, fare grafici onesti. **Totale: ~60 ore.**

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Think Stats: Exploratory Data Analysis in Python (3a ed.) | A. B. Downey [9]. [Link](https://allendowney.github.io/ThinkStats/) | Materiali aperti | EN | ~30 h (stima) | Livello 1 | Gratuito online (licenza Creative Commons), con notebook eseguibili su Google Colab. Probabilità, distribuzioni, stima, test d'ipotesi, regressione, analisi di sopravvivenza. |
| Python Data Science Handbook (NumPy, pandas, Matplotlib) | J. VanderPlas [10]. [Link](https://jakevdp.github.io/PythonDataScienceHandbook/) | **Industria** (editore O'Reilly; testo gratuito online, licenza CC-BY-NC-ND) | EN | ~20 h (stima) | Livello 1 | Solo i capitoli 2–4. |
| Analisi guidata su dati clinici reali anonimi: MIMIC-IV demo | PhysioNet / MIT Laboratory for Computational Physiology. [Demo](https://physionet.org/content/mimic-iv-demo/); articolo [11] | Istituzione, Peer-reviewed | EN | ~10 h (stima) | Le due voci precedenti | Il demo è a libero accesso. Esercizio: coorte, statistiche descrittive, un modello di regressione. |
| *(facoltativo, per chi fa ricerca clinica)* Introduction to Statistics for the Life and Biomedical Sciences, con esercitazioni in **R** | OpenIntro [12]. [Link](https://www.openintro.org/book/biostat/) | Materiali aperti | EN | ~50 h (stima) | Livello 1 | PDF gratuito (si può mettere il prezzo a 0 $). Regressione lineare e logistica, sopravvivenza. È l'unica voce in R; esclusa dal totale. |

---

## Livello 3 · Informatica sanitaria

**Obiettivo (minimo indispensabile):** capire come si rappresentano e si scambiano i dati clinici (standard e terminologie), usare FHIR e OMOP a livello di base, e riconoscere come supporto alle decisioni e fattore umano determinino l'uso reale di un sistema. **Totale: ~65 ore.** I materiali sono quelli pubblicati gratuitamente dagli enti di standard.

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Terminologie: SNOMED CT, LOINC, ICD-11 (con panoramica sugli standard) | **SNOMED International**: [education](https://www.snomed.org/education) (tutorial iniziali accessibili senza account); **Regenstrief**: [LOINC](https://www.regenstrief.org/real-world-solutions/loinc/) (LOINC è gratuito); **OMS**: [ICD-11 Training Package](https://icdcdn.who.int/icd11training/index.html) [13]; **NLM**: [tutorial standard e terminologie](https://www.nlm.nih.gov/oet/ed/healthdatastandards/index.html) [14] | Ente di standard (SNOMED, Regenstrief, OMS); Istituzione (NLM) | EN | ~19 h (stima) | Livello 0 | **L'Italia non risulta tra i Paesi membri di SNOMED International** (elenco di 54–55 membri, consultato il 22/11/2026) [15]: i corsi ufficiali sono gratuiti per i membri e a pagamento fuori dai membri [16], quindi qui si usano i tutorial iniziali e il tutorial NLM. |
| HL7 FHIR: concetti, risorse, REST e ricerca | HL7 International, specifica FHIR [17]: [panoramica clinica](https://www.hl7.org/fhir/overview-clinical.html), [panoramica per sviluppatori](https://www.hl7.org/fhir/overview-dev.html), [elenco risorse](https://www.hl7.org/fhir/resourcelist.html), [ricerca](https://www.hl7.org/fhir/search.html); NIH (NCPI), notebook [fhir-101](https://github.com/NIH-NCPI/fhir-101); HL7 Italia, [hl7.it](https://hl7.it/) | Ente di standard, Istituzione | EN (HL7 Italia IT) | ~12 h (stima) | Livello 1 | I corsi HL7 ufficiali non sono gratuiti: si studia il materiale didattico della specifica, con gli esercizi del notebook NIH. |
| DICOM: modello dei dati e flusso immagini | NEMA/MITA, DICOM Standard, Parte PS3.1 [18]: [PS3.1](https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html), [presentazione dello standard](https://www.dicomstandard.org/about) | Ente di standard | EN | ~4 h (stima) | Livello 1 | Solo introduzione e panoramica, non l'intero standard. |
| OMOP CDM e OHDSI | OHDSI, *The Book of OHDSI* [19] (CC0): [link](https://ohdsi.github.io/TheBookOfOhdsi/); EHDEN Academy (consorzio europeo): [link](https://academy.ehden.eu/) | Ente di standard (OHDSI) | EN | ~12 h (stima) | Livelli 1–2 (SQL) | EHDEN Academy: gratuita, con account (confermato da fonti dell'EHDEN). Capitoli 4–6 del libro (CDM, vocabolari, ETL). Articolo di riferimento: Hripcsak et al. [20]. |
| Cartelle cliniche elettroniche e analisi secondaria dei dati | MIT Critical Data, *Secondary Analysis of Electronic Health Records* (Springer, 2016, open access) [21]. [Link](https://www.ncbi.nlm.nih.gov/books/NBK543627/) | Università (libro open access) | EN | ~10 h (stima) | Livello 2 | Si scelgono i capitoli su pulizia dei dati, bias e progettazione di studi. |
| Supporto alle decisioni cliniche, fattore umano e flussi di lavoro | Sutton et al. 2020 [22]; Zhang e Walji (TURF) 2011 [23]; NIST, NISTIR 7741 [24]: [link](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7741.pdf); HL7, [CDS Hooks](https://cds-hooks.org/) | Peer-reviewed, Istituzione | EN | ~8 h (stima) | Livello 0 | Due articoli e una guida NIST sull'usabilità delle cartelle cliniche; CDS Hooks per integrare il supporto alle decisioni nel flusso clinico. |

---

## Livello 4 · Regole, privacy e sicurezza informatica in sanità

**Obiettivo:** sapere che cosa si può fare con i dati sanitari, quando un software è un dispositivo medico, e i fondamenti della sicurezza informatica in sanità. **Totale: ~35 ore.**

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| GDPR e dati sanitari (art. 9) | Regolamento (UE) 2016/679 [2]: [testo e pagina del Garante](https://www.garanteprivacy.it/regolamentoue); Garante, [Sanità e ricerca scientifica](https://www.garanteprivacy.it/temi/sanita-e-ricerca-scientifica) | Istituzione | IT | ~6 h (stima) | Livello 0 | Lettura dell'art. 9 (categorie particolari di dati, tra cui quelli relativi alla salute) e dei provvedimenti del Garante per la sanità. |
| FSE 2.0 ed Ecosistema Dati Sanitari: regole e privacy | Decreto 7 settembre 2023 (GU n. 249 del 24/10/2023) [6]: [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/gu/2023/10/24/249/sg/pdf); decreto 31 dicembre 2024 (GU n. 53 del 5/3/2025) [7]: [Gazzetta Ufficiale](https://www.gazzettaufficiale.it/eli/gu/2025/03/05/53/sg/pdf); Garante, [FAQ sul fascicolo sanitario](https://www.garanteprivacy.it/faq/fascicolo-sanitario) | Istituzione | IT | ~6 h (stima) | Livello 0 | Il decreto del 2023 è modificato da decreti successivi: leggere sempre il testo consolidato più recente. |
| Spazio europeo dei dati sanitari (EHDS) | Regolamento (UE) 2025/327 [25]; Commissione europea, [pagina EHDS](https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en) | Istituzione | EN/IT | ~4 h (stima) | Livello 0 | Pubblicato in Gazzetta Ufficiale UE il 5 marzo 2025. Le date di applicazione sono scaglionate: controllare la pagina della Commissione. |
| Software come dispositivo medico (MDR) | Regolamento (UE) 2017/745 [26]; Commissione europea, MDCG 2019-11 (qualificazione e classificazione del software) [27]: [pagina MDCG](https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en); Ministero della Salute, [dispositivi medici](https://www.salute.gov.it/new/it/tema/dispositivi-medici/) | Istituzione | EN/IT | ~5 h (stima) | Livello 0 | Quando un software è un dispositivo medico e come si classifica. |
| Sicurezza informatica: fondamenti e minacce alla sanità | Harvard University (CS50), [CS50's Introduction to Cybersecurity](https://cs50.harvard.edu/cybersecurity/); ENISA, *Health Threat Landscape* (2023) [28]: [pagina](https://www.enisa.europa.eu/publications/health-threat-landscape) | Università, Istituzione | EN | ~14 h (stima) | Nessuno | Del corso CS50 si seguono account, dati e privacy. Il rapporto ENISA analizza gli incidenti informatici nel settore sanitario UE da gennaio 2021 a marzo 2023. |

---

## Livello 5 · AI in medicina (pilastro)

**Obiettivo:** capire come funzionano ML, deep learning e LLM, quali sono i loro limiti (allucinazioni incluse), saper valutare clinicamente un modello (validazione, calibrazione, bias, linee guida di reporting) e conoscere etica e regole (AI Act, MDR, OMS). **Totale: ~87 ore.** Dove possibile, in italiano.

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Fondamenti dell'AI (in italiano) | Università di Helsinki con MinnaLearn, *Elements of AI*, versione italiana promossa dal Dipartimento per la trasformazione digitale: [link](https://www.elementsofai.it/). *(alternativa)* Federica Web Learning, *Intelligenza artificiale e scienza dei dati - le basi*: [catalogo AI](https://www.federica.eu/intelligenza-artificiale/) | Università | **IT** | ~20 h (stima) | Nessuno | Entrambi gratuiti (Federica dichiara «100% gratuiti» tutti i corsi). Federica richiede registrazione per aprire i corsi; durata non indicata. |
| Fondamenti di machine learning e deep learning | G. James, D. Witten, T. Hastie, R. Tibshirani, J. Taylor, *An Introduction to Statistical Learning with Applications in Python* (Springer, 2023) [29]: [link](https://www.statlearning.com/). *(alternativa in italiano)* Federica Web Learning, *Machine Learning* (F. Stella): [catalogo AI](https://www.federica.eu/intelligenza-artificiale/). *(facoltativo)* Google, [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course) | Università (libro, PDF gratuito); la voce facoltativa è **Industria** | EN (alternativa IT) | ~20 h (stima) | Livelli 1–2 | Si scelgono i capitoli su regressione, classificazione, valutazione dei modelli, alberi e un'introduzione alle reti neurali. |
| Machine learning per la sanità | MIT 6.S897 / HST.956, *Machine Learning for Healthcare* (Sontag, Szolovits, 2019). [Link](https://ocw.mit.edu/courses/6-s897-machine-learning-for-healthcare-spring-2019/) | Università | EN | ~10 h (stima) | ML di base | Appunti e video gratuiti. Si seguono solo poche lezioni (stratificazione del rischio, bias, interpretabilità); il corso intero presuppone ML universitario. |
| AI generativa e LLM: come funzionano, limiti, allucinazioni, prompting | Politecnico di Milano, POK, *Data, Algorithms, and Ethical Challenges: Exploring the AI Revolution in Medicine* (gratuito, 12 ore): [link](https://www.pok.polimi.it/course/view.php?id=177) [30]. Articoli: Thirunavukarasu et al. 2023 (LLM in medicina) [31]; Meskó 2023 (prompting per professionisti sanitari) [32]; Ji et al. 2023 (allucinazioni) [1]. *(facoltativo)* Stanford, CS324 *Large Language Models* (note delle lezioni): [link](https://stanford-cs324.github.io/winter2022/) [33] | Università, Peer-reviewed | EN | ~19 h (12 h dichiarate dal corso POK + 7 h di articoli, stima) | Livello 2 | Le note CS324 non citano le allucinazioni: per quelle ci sono gli articoli. |
| Valutazione clinica dei modelli | TRIPOD+AI [34], CONSORT-AI [35], DECIDE-AI [36] (EQUATOR Network: [TRIPOD](https://www.equator-network.org/reporting-guidelines/tripod-statement/), [CONSORT-AI](https://www.equator-network.org/reporting-guidelines/consort-artificial-intelligence/), [DECIDE-AI](https://www.equator-network.org/reporting-guidelines/decide-ai/)); Van Calster et al. 2019, calibrazione [37] | Peer-reviewed, Società scientifica (EQUATOR) | EN | ~8 h (stima) | Livello 2 | Validazione esterna, calibrazione, bias e liste di controllo per riportare studi con AI. Si applica una lista a uno studio reale. |
| Etica e regolazione dell'AI in sanità | OMS, *Ethics and governance of AI for health* (2021) [38]: [link](https://www.who.int/publications/i/item/9789240029200); OMS, guida sui *large multi-modal models* (2025) [39]: [link](https://www.who.int/publications/i/item/9789240084759); Regolamento (UE) 2024/1689 (AI Act) [40]: [pagina della Commissione](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) | Istituzione | EN/IT | ~10 h (stima) | Livello 4 | Documenti OMS in PDF gratuito (CC BY-NC-SA 3.0 IGO). Per l'AI Act e il suo rapporto con l'MDR usare il testo ufficiale in Gazzetta UE. |

---

## Indirizzo A · Ponte

**Per chi:** guida i progetti di sanità digitale, valuta e acquista tecnologie, governa l'AI in ospedale; scrive poco codice. **Ore: ~118.**

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Governance e valutazione delle tecnologie (HTA) | C. S. Goodman, *HTA 101* (NICHSR / National Library of Medicine, 2014) [41]: [archivio](https://wayback.archive-it.org/org-350/https://www.nlm.nih.gov/nichsr/hta101/ta10101.html); O'Rourke et al. 2020, definizione di HTA [42]; NICE, [Evidence standards framework](https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies) [43] | Istituzione, Peer-reviewed | EN | ~26 h (stima) | Livello 3 | La pagina originale NLM è archiviata: si usa la copia. Materiale italiano (AGENAS) non trovato. |
| Progettazione dei sistemi di supporto alle decisioni e usabilità | Sutton 2020 [22]; Bates 2003 [44]; Zhang e Walji 2011 [23]; NIST NISTIR 7741 [24]; HL7 [CDS Hooks](https://cds-hooks.org/) | Peer-reviewed, Istituzione | EN | ~20 h (stima) | Livello 3 | Dalla lettura alla progettazione: ogni studente disegna un flusso decisionale con i criteri letti. |
| Gestione dei progetti e del cambiamento | OMS, *Digital Implementation Investment Guide* [45]: [link](https://www.who.int/publications/i/item/9789240010567); MIT OpenCourseWare, HST.921, *Information Technology in the Health Care System of the Future* (2009): [link](https://ocw.mit.edu/courses/hst-921-information-technology-in-the-health-care-system-of-the-future-spring-2009/) | Istituzione, Università | EN | ~45 h (stima) | Livello 3 | Il materiale MIT è del 2009: metodo valido, esempi datati. |
| Acquisto e valutazione di prodotti AI | NHS AI Lab, *A buyer's guide to AI in health and care* [46]: [link](https://www.gov.uk/data-ethics-guidance/a-buyers-guide-to-ai-in-health-and-care); NICE, Evidence standards framework (link sopra); Regolamenti [26] e [40] | Istituzione | EN | ~12 h (stima) | Livelli 4–5 | Dieci domande per chi acquista AI. Documento britannico: si adatta al contesto italiano con MDR e AI Act. |
| Governance dell'AI in ospedale | NIST, *AI Risk Management Framework 1.0* [47]: [link](https://www.nist.gov/itl/ai-risk-management-framework); OMS [38] [39] | Istituzione | EN | ~15 h (stima) | Livello 5 | Quadro di gestione del rischio dell'AI. Non specifico per la sanità: si integra con i documenti OMS. |

## Indirizzo B · Sviluppatore

**Per chi:** programma, analizza dati, costruisce modelli e applicazioni. **Ore: ~524.** Qui stanno le voci più pesanti spostate dal tronco comune.

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Python completo | Harvard University, [CS50P](https://cs50.harvard.edu/python/) (qui il completamento oltre Python for Everybody) | Università | EN | ~50 h (stima: ore residue) | Livello 1 | Corso universitario impegnativo. |
| Informatica e algoritmi | Harvard University, [CS50x](https://cs50.harvard.edu/x/), CS50's Introduction to Computer Science; MIT OpenCourseWare, [6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) (primavera 2020) | Università | EN | ~165 h (stima: 11 settimane da 10–20 h ciascuna, secondo le FAQ di CS50x; 6.006 escluso) | Livello 1 | Tutte le settimane in C restano: impegnative ma formative (memoria e strutture dati); poi 6.006 come approfondimento rigoroso, che richiede matematica discreta. |
| Sviluppo web e app FHIR (SMART on FHIR) | Università di Helsinki, [Full Stack Open](https://fullstackopen.com/en/) (parti 0–5); HL7, [SMART App Launch](https://www.hl7.org/fhir/smart-app-launch/); SMART Health IT (Boston Children's Hospital), [docs](https://docs.smarthealthit.org/); Mandel et al. 2016 [48] | Università, Ente di standard, Peer-reviewed | EN | ~75 h (stima) | Livelli 1 e 3 | Full Stack Open è gratuito (CC BY-NC-SA). L'App Launcher SMART è utilizzabile senza registrazione. |
| ML e deep learning approfonditi | Stanford University, [CS229 Machine Learning](https://cs229.stanford.edu/). *(facoltativo)* fast.ai, [Practical Deep Learning](https://course.fast.ai/) | Università; la voce facoltativa è **Industria** | EN | ~65 h (stima; fast.ai dichiara 9 lezioni, ~13,5 h) | Livelli 2 e 5 | fast.ai richiede circa un anno di Python. |
| Imaging medico | 3D Slicer (finanziato dai NIH; Fedorov et al. 2012) [49]: [training](https://training.slicer.org/); Stanford, [CS231n](https://cs231n.stanford.edu/). *(facoltativo)* MONAI, [tutorials](https://github.com/Project-MONAI/tutorials) | Università, Peer-reviewed; MONAI è **Industria** | EN | ~35 h (stima) | Livello 3 (DICOM), 5 | MONAI è un progetto open source con forte partecipazione industriale. |
| NLP clinico e LLM | Stanford University, [CS224N NLP with Deep Learning](https://web.stanford.edu/class/cs224n/). Hugging Face, [LLM Course](https://huggingface.co/learn/llm-course/chapter1/1) (gratuito). Rassegna sistematica sul RAG (retrieval-augmented generation) in sanità: Amugongo et al. 2025 [50], [PubMed 40498738](https://pubmed.ncbi.nlm.nih.gov/40498738/) | Università, Peer-reviewed; il corso HF è **Industria** | EN | ~83 h (stima, compresa la rassegna, ~3 h) | Livello 5; Python buono | Il corso HF copre transformer, fine-tuning e LLM, non RAG né inferenza locale: per il RAG in medicina si legge la rassegna [50]. |
| Agenti AI di base | Hugging Face, [AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) (gratuito; framework smolagents, LlamaIndex, LangGraph) | **Industria** | EN | ~21 h (stima) | NLP/LLM e ML | Gratuito. |
| MLOps: dai modelli ai prodotti | C. Kästner (Carnegie Mellon University), *Machine Learning in Production: From Models to Products* (MIT Press, 2025) [51]: [libro online](https://mlip-cmu.github.io/book/) | Università | EN | ~30 h (stima) | Livelli 1 e 5 | Testo online ad accesso libero (licenza CC BY-NC-ND 4.0). Si scelgono i capitoli su architettura e distribuzione, automazione della pipeline, controllo della qualità e ingegneria responsabile. |

## Indirizzo C · Bioinformatica traslazionale

**Per chi:** viene dalla biologia o dal laboratorio e vuole lavorare con dati genomici in clinica (analisi, interpretazione e scambio dei dati genetici dei pazienti). **Ore: ~125.** Restano fuori la bioinformatica pura (filogenesi, biologia strutturale, algoritmi sulle sequenze).

| Corso | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Fondamenti di genomica computazionale | MIT OpenCourseWare, 7.91J, *Foundations of Computational and Systems Biology* (primavera 2014) [54]: [link](https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/) | Università | EN | ~25 h (stima) | Livelli 1 e 2 | Appunti, video ed esercizi gratuiti (CC BY-NC-SA 4.0). Corso di un semestre: si scelgono le lezioni sull'analisi di sequenze genomiche e sull'espressione genica; si lasciano fuori filogenesi e biologia strutturale. |
| Analisi dei dati NGS e formato VCF | Galaxy Training Network, percorsi *Sequence analysis* e *Variant analysis* [52]: [link](https://training.galaxyproject.org/training-material/topics/variant-analysis/); EMBL-EBI Training, corsi on demand [56]: [link](https://www.ebi.ac.uk/training/on-demand); Danecek et al. 2011, formato VCF [55] | Peer-reviewed, Istituzione | EN | ~30 h (stima) | Livello 1 | Galaxy: materiale aperto e gratuito, esercizi su un server Galaxy pubblico. EMBL-EBI: corsi on demand gratuiti, account facoltativo (serve solo per tenere traccia dei progressi). Si scelgono allineamento, chiamata delle varianti e annotazione; Biopython o Python per leggere i file VCF. |
| Interpretazione clinica delle varianti | Richards et al. 2015, linee guida ACMG/AMP [57]; ClinGen [58]: [sito](https://clinicalgenome.org/); ClinVar (NCBI) [59]: [sito](https://www.ncbi.nlm.nih.gov/clinvar/) | Società scientifica, Peer-reviewed, Istituzione | EN | ~20 h (stima) | Livello 3 | Dati ClinGen (CC0) e ClinVar liberamente consultabili. Si classifica una variante di esempio con i criteri ACMG/AMP e si confronta con ClinVar. |
| Standard dei dati genomici | GA4GH [60]: [prodotti](https://www.ga4gh.org/) (VCF e htsget, [Phenopackets](https://www.ga4gh.org/product/phenopackets/) [61], [Beacon](https://www.ga4gh.org/product/beacon/)); HL7, [Genomics Reporting IG](https://build.fhir.org/ig/HL7/genomics-reporting/) [62] | Ente di standard, Peer-reviewed | EN | ~25 h (stima) | Livelli 1, 2 e 3 | Prodotti GA4GH dichiarati gratuiti e open source. Si segue la guida HL7 per riportare una variante in FHIR; i dati sono sempre di esempio. |
| Farmacogenomica | CPIC [63]: [linee guida](https://www.clinpgx.org/cpic/guidelines); ClinPGx (ex PharmGKB) [64]: [sito](https://www.clinpgx.org/) | Società scientifica, Istituzione | EN | ~15 h (stima) | Livello 3 | Linee guida CPIC liberamente accessibili; dati ClinPGx con licenza CC BY-SA 4.0 e senza registrazione. Si leggono 2–3 linee guida (gene e farmaco). |
| Dati genetici: regole e privacy | GDPR, art. 9 [2]; Garante per la protezione dei dati personali, Provvedimento n. 146 del 5 giugno 2019, par. 4 sui dati genetici [65]: [link](https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9124510) | Istituzione | IT | ~10 h (stima) | Livello 4 | Il provvedimento resta in vigore (modificato il 13 febbraio 2025, n. 66) fino all'adozione delle misure di garanzia previste dall'art. 2-septies del Codice privacy. |

La bioinformatica pura (filogenesi, biologia strutturale, algoritmi sulle sequenze) è fuori perimetro di questo curriculum.

---

## Approfondimenti a scelta (circa 25 ore ciascuno)

| Tema | Fonte | Tipo di fonte | Lingua | Impegno | Prerequisiti | Note |
|---|---|---|---|---|---|---|
| Genomica e bioinformatica | Galaxy Community [52]: [Galaxy Training Network](https://training.galaxyproject.org/) | Peer-reviewed | EN | ~25 h (stima) | Livello 1 | Percorsi del Galaxy Training Network sull'analisi di dati biologici. Chi segue l'indirizzo C lo trova già nel percorso. |
| Sanità pubblica digitale ed epidemiologia computazionale | OMS, [OpenWHO](https://openwho.org/); ISS, [EpiCentro](https://www.epicentro.iss.it/) e [EDUISS](https://www.eduiss.it/) (FAD gratuita dell'ISS, cataloghi su salute pubblica e SABiC) | Istituzione | EN/IT | ~25 h (stima) | Livello 2 | Scelta dei corsi OpenWHO su epidemiologia e dati; EDUISS e EpiCentro per il contesto italiano (registrazione richiesta). |
| Imaging avanzato | Vedi Indirizzo B (3D Slicer, CS231n, MONAI) e [PS3.1 DICOM](https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html) [18]. | Università, Ente di standard | EN | ~25 h (stima) | Livello 3 | Per chi sceglie l'indirizzo A: solo concetti, senza codice. |
| Telemedicina | Conferenza Stato-Regioni, *Indicazioni nazionali per l'erogazione di prestazioni in telemedicina*, Accordo del 17 dicembre 2020, Rep. Atti n. 215/CSR [53]: [atto](https://www.statoregioni.it/it/conferenza-stato-regioni/sedute-2020/seduta-del-17122020/atti/repertorio-atto-n-215csr/), [PDF](https://www.statoregioni.it/media/3221/p-3-csr-rep-n-215-17dic2020.pdf) | Istituzione | IT | ~25 h (stima) | Livello 4 | Testo ufficiale dell'accordo verificato sul sito della Conferenza (PDF raggiungibile). |

---

## Contribuire

Proposte e correzioni con issue o pull request, secondo [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Bibliografia

(Stile Vancouver. Le citazioni del testo rinviano ai numeri qui sotto, in ordine di prima comparsa. Data di accesso a tutti i link: 22/11/2026.)

1. Ji Z, Lee N, Frieske R, Yu T, Su D, Xu Y, et al. Survey of hallucination in natural language generation. ACM Comput Surv. 2023;55(12):Art. 248. doi:10.1145/3571730.
2. Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016, relativo alla protezione delle persone fisiche con riguardo al trattamento dei dati personali (GDPR). Gazzetta Ufficiale dell'Unione europea L 119, 4.5.2016, pp. 1-88. EUR-Lex: http://data.europa.eu/eli/reg/2016/679/oj. Testo italiano anche su: https://www.garanteprivacy.it/regolamentoue
3. Kulikowski CA, Shortliffe EH, Currie LM, Elkin PL, Hunter LE, Johnson TR, et al. AMIA Board white paper: definition of biomedical informatics and specification of core competencies for graduate education in the discipline. J Am Med Inform Assoc. 2012;19(6):931-8. doi:10.1136/amiajnl-2012-001053. PMID: 22683918.
4. Mantas J, Ammenwerth E, Demiris G, Hasman A, Haux R, Hersh W, et al. Recommendations of the International Medical Informatics Association (IMIA) on education in biomedical and health informatics. Methods Inf Med. 2010;49(2):105-20. doi:10.3414/ME5119. PMID: 20054502.
5. World Health Organization. Global strategy on digital health 2020-2025. Geneva: WHO; 2021. Disponibile su: https://www.who.int/publications/i/item/9789240020924
6. Italia. Ministero della Salute. Decreto 7 settembre 2023. Fascicolo sanitario elettronico 2.0. Gazzetta Ufficiale della Repubblica Italiana, Serie Generale n. 249, 24 ottobre 2023 (23A05829). Disponibile su: https://www.gazzettaufficiale.it/eli/gu/2023/10/24/249/sg/pdf. Modificato da decreti successivi (tra cui quello dell'11 novembre 2025, GU n. 286 del 10 dicembre 2025).
7. Italia. Ministero della Salute. Decreto 31 dicembre 2024. Istituzione dell'Ecosistema dati sanitari (EDS). Gazzetta Ufficiale della Repubblica Italiana, Serie Generale n. 53, 5 marzo 2025 (25A01321). Disponibile su: https://www.gazzettaufficiale.it/eli/gu/2025/03/05/53/sg/pdf
8. Severance CR. Python for Everybody (py4e). Disponibile su: https://www.py4e.com/
9. Downey AB. Think Stats: exploratory data analysis in Python. 3rd ed. Green Tea Press. Disponibile su: https://allendowney.github.io/ThinkStats/
10. VanderPlas J. Python data science handbook. Sebastopol (CA): O'Reilly Media; 2016. Disponibile su: https://jakevdp.github.io/PythonDataScienceHandbook/
11. Johnson AEW, Bulgarelli L, Shen L, Gayles A, Shammout A, Horng S, et al. MIMIC-IV, a freely accessible electronic health record dataset. Sci Data. 2023;10(1):1. doi:10.1038/s41597-022-01899-x. PMID: 36596836.
12. OpenIntro. Introduction to statistics for the life and biomedical sciences. 1st ed.. Disponibile su: https://www.openintro.org/book/biostat/
13. World Health Organization. ICD-11 training package. Geneva: WHO. Disponibile su: https://icdcdn.who.int/icd11training/index.html
14. National Library of Medicine. Health data standards and terminologies: a tutorial. Bethesda (MD): NLM. Disponibile su: https://www.nlm.nih.gov/oet/ed/healthdatastandards/index.html
15. SNOMED International. Members [Internet]. Disponibile su: https://www.snomed.org/members (consultato il 22/11/2026: elenco di 54-55 Paesi e territori; l'Italia non compare).
16. National Library of Medicine. SNOMED CT overview [Internet]. Bethesda (MD): NLM. Disponibile su: https://www.nlm.nih.gov/healthit/snomedct/snomed_overview.html (l'NLM distribuisce SNOMED CT senza costi ai suoi utenti statunitensi in quanto membro; possono applicarsi tariffe fuori dai Paesi membri).
17. HL7 International. HL7 FHIR: Fast Healthcare Interoperability Resources (specifica). Disponibile su: https://www.hl7.org/fhir/
18. National Electrical Manufacturers Association (NEMA). DICOM PS3.1: Introduction and overview. In: Digital Imaging and Communications in Medicine (DICOM) Standard. Rosslyn (VA): NEMA. Disponibile su: https://dicom.nema.org/medical/dicom/current/output/chtml/part01/PS3.1.html
19. OHDSI Collaborative. The Book of OHDSI: Observational Health Data Sciences and Informatics. 2019 (aggiornamento continuo). Disponibile su: https://ohdsi.github.io/TheBookOfOhdsi/
20. Hripcsak G, Duke JD, Shah NH, Reich CG, Huser V, Schuemie MJ, et al. Observational Health Data Sciences and Informatics (OHDSI): opportunities for observational researchers. Stud Health Technol Inform. 2015;216:574-8. PMID: 26262116.
21. MIT Critical Data. Secondary analysis of electronic health records. Cham: Springer; 2016. doi:10.1007/978-3-319-43742-2. Accesso aperto su: https://www.ncbi.nlm.nih.gov/books/NBK543627/
22. Sutton RT, Pincock D, Baumgart DC, Sadowski DC, Fedorak RN, Kroeker KI. An overview of clinical decision support systems: benefits, risks, and strategies for success. NPJ Digit Med. 2020;3:17. doi:10.1038/s41746-020-0221-y. PMID: 32047862.
23. Zhang J, Walji MF. TURF: toward a unified framework of EHR usability. J Biomed Inform. 2011;44(6):1056-67. doi:10.1016/j.jbi.2011.08.005. PMID: 21867774.
24. Schumacher RM, Lowry SZ. NIST guide to the processes approach for improving the usability of electronic health records. NISTIR 7741. Gaithersburg (MD): National Institute of Standards and Technology; 2010. Disponibile su: https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7741.pdf
25. Regolamento (UE) 2025/327 del Parlamento europeo e del Consiglio, dell'11 febbraio 2025, sullo spazio europeo dei dati sanitari (EHDS). Gazzetta Ufficiale dell'Unione europea L, 2025/327, 5.3.2025. EUR-Lex: https://eur-lex.europa.eu/eli/reg/2025/327/oj. Pagina della Commissione: https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space_en
26. Regolamento (UE) 2017/745 del Parlamento europeo e del Consiglio, del 5 aprile 2017, relativo ai dispositivi medici (MDR). Gazzetta Ufficiale dell'Unione europea L 117, 5.5.2017, pp. 1-175. EUR-Lex: http://data.europa.eu/eli/reg/2017/745/oj
27. Medical Device Coordination Group. MDCG 2019-11: guidance on qualification and classification of software in Regulation (EU) 2017/745 (MDR) and Regulation (EU) 2017/746 (IVDR). Brussels: European Commission; 2019. Pagina dei documenti MDCG: https://health.ec.europa.eu/medical-devices-sector/new-regulations/guidance-mdcg-endorsed-documents-and-other-guidance_en
28. European Union Agency for Cybersecurity (ENISA). Health threat landscape. Heraklion: ENISA; 2023 (5 luglio). Disponibile su: https://www.enisa.europa.eu/publications/health-threat-landscape
29. James G, Witten D, Hastie T, Tibshirani R, Taylor J. An introduction to statistical learning with applications in Python. Cham: Springer; 2023. doi:10.1007/978-3-031-38747-0. Disponibile su: https://www.statlearning.com/
30. Politecnico di Milano, POK (Polimi Open Knowledge). Data, algorithms, and ethical challenges: exploring the AI revolution in medicine [MOOC]. Milano: Politecnico di Milano; 2023-. Disponibile su: https://www.pok.polimi.it/course/view.php?id=177
31. Thirunavukarasu AJ, Ting DSJ, Elangovan K, Gutierrez L, Tan TF, Ting DSW. Large language models in medicine. Nat Med. 2023;29(8):1930-40. doi:10.1038/s41591-023-02448-8. PMID: 37460753.
32. Meskó B. Prompt engineering as an important emerging skill for medical professionals: tutorial. J Med Internet Res. 2023;25:e50638. doi:10.2196/50638. PMID: 37792434.
33. Liang P, Bommasani R, et al. CS324: Large Language Models [note del corso]. Stanford (CA): Stanford University; 2022. Disponibile su: https://stanford-cs324.github.io/winter2022/
34. Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Van Calster B, et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378. doi:10.1136/bmj-2023-078378. PMID: 38626948.
35. Liu X, Cruz Rivera S, Moher D, Calvert MJ, Denniston AK; SPIRIT-AI and CONSORT-AI Working Group. Reporting guidelines for clinical trial reports for interventions involving artificial intelligence: the CONSORT-AI extension. Nat Med. 2020;26(9):1364-74. doi:10.1038/s41591-020-1034-x. PMID: 32908283.
36. Vasey B, Nagendran M, Campbell B, Clifton DA, Collins GS, Denaxas S, et al. Reporting guideline for the early-stage clinical evaluation of decision support systems driven by artificial intelligence: DECIDE-AI. Nat Med. 2022;28(5):924-33. doi:10.1038/s41591-022-01772-9. PMID: 35585198.
37. Van Calster B, McLernon DJ, van Smeden M, Wynants L, Steyerberg EW; Topic Group 'Evaluating diagnostic tests and prediction models' of the STRATOS initiative. Calibration: the Achilles heel of predictive analytics. BMC Med. 2019;17(1):230. doi:10.1186/s12916-019-1466-7. PMID: 31842878.
38. World Health Organization. Ethics and governance of artificial intelligence for health: WHO guidance. Geneva: WHO; 2021. Disponibile su: https://www.who.int/publications/i/item/9789240029200
39. World Health Organization. Ethics and governance of artificial intelligence for health: guidance on large multi-modal models. Geneva: WHO; 2025. Disponibile su: https://www.who.int/publications/i/item/9789240084759
40. Regolamento (UE) 2024/1689 del Parlamento europeo e del Consiglio, del 13 giugno 2024, che stabilisce regole armonizzate sull'intelligenza artificiale (AI Act). Gazzetta Ufficiale dell'Unione europea L, 2024/1689, 12.7.2024. EUR-Lex: http://data.europa.eu/eli/reg/2024/1689/oj. Pagina della Commissione: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
41. Goodman CS. HTA 101: introduction to health technology assessment. Bethesda (MD): National Library of Medicine, NICHSR; 2014. Disponibile su: https://wayback.archive-it.org/org-350/https://www.nlm.nih.gov/nichsr/hta101/ta10101.html
42. O'Rourke B, Oortwijn W, Schuller T; International Joint Task Group. The new definition of health technology assessment: a milestone in international collaboration. Int J Technol Assess Health Care. 2020;36(3):187-90. doi:10.1017/S0266462320000215. PMID: 32398176.
43. National Institute for Health and Care Excellence. Evidence standards framework (ESF) for digital health technologies. London: NICE (versione corrente). Disponibile su: https://www.nice.org.uk/what-nice-does/digital-health/evidence-standards-framework-esf-for-digital-health-technologies
44. Bates DW, Kuperman GJ, Wang S, Gandhi T, Kittler A, Volk L, et al. Ten commandments for effective clinical decision support: making the practice of evidence-based medicine a reality. J Am Med Inform Assoc. 2003;10(6):523-30. doi:10.1197/jamia.M1370. PMID: 12925543.
45. World Health Organization. Digital implementation investment guide (DIIG): integrating digital interventions into health programmes. Geneva: WHO; 2020. ISBN 9789240010567. Disponibile su: https://www.who.int/publications/i/item/9789240010567
46. NHSX / NHS AI Lab. A buyer's guide to AI in health and care. London: NHS; 2020 (pagina aggiornata su GOV.UK). Disponibile su: https://www.gov.uk/data-ethics-guidance/a-buyers-guide-to-ai-in-health-and-care
47. National Institute of Standards and Technology. Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1. Gaithersburg (MD): NIST; 2023. doi:10.6028/NIST.AI.100-1. Disponibile su: https://www.nist.gov/itl/ai-risk-management-framework
48. Mandel JC, Kreda DA, Mandl KD, Kohane IS, Ramoni RB. SMART on FHIR: a standards-based, interoperable apps platform for electronic health records. J Am Med Inform Assoc. 2016;23(5):899-908. doi:10.1093/jamia/ocv189. PMID: 26911829.
49. Fedorov A, Beichel R, Kalpathy-Cramer J, Finet J, Fillion-Robin JC, Pujol S, et al. 3D Slicer as an image computing platform for the Quantitative Imaging Network. Magn Reson Imaging. 2012;30(9):1323-41. doi:10.1016/j.mri.2012.05.001. PMID: 22770690.
50. Amugongo LM, Mascheroni P, Brooks S, Doering S, Seidel J. Retrieval augmented generation for large language models in healthcare: a systematic review. PLOS Digit Health. 2025;4(6):e0000877. doi:10.1371/journal.pdig.0000877. PMID: 40498738.
51. Kästner C. Machine learning in production: from models to products. Cambridge (MA): MIT Press; 2025. Disponibile su: https://mlip-cmu.github.io/book/
52. Galaxy Community. The Galaxy platform for accessible, reproducible and collaborative biomedical analyses: 2022 update. Nucleic Acids Res. 2022;50(W1):W345-51. doi:10.1093/nar/gkac247. PMID: 35446428.
53. Conferenza permanente per i rapporti tra lo Stato, le Regioni e le Province autonome di Trento e di Bolzano. Accordo ai sensi dell'art. 4, c. 1, D.Lgs. 281/1997 sul documento «Indicazioni nazionali per l'erogazione di prestazioni in telemedicina». Rep. Atti n. 215/CSR, seduta del 17 dicembre 2020. Disponibile su: https://www.statoregioni.it/it/conferenza-stato-regioni/sedute-2020/seduta-del-17122020/atti/repertorio-atto-n-215csr/
54. MIT OpenCourseWare. 7.91J Foundations of Computational and Systems Biology [corso]. Cambridge (MA): Massachusetts Institute of Technology; primavera 2014. Disponibile su: https://ocw.mit.edu/courses/7-91j-foundations-of-computational-and-systems-biology-spring-2014/
55. Danecek P, Auton A, Abecasis G, Albers CA, Banks E, DePristo MA, et al. The variant call format and VCFtools. Bioinformatics. 2011;27(15):2156-8. doi:10.1093/bioinformatics/btr330. PMID: 21653522.
56. EMBL-EBI Training. On-demand training [corsi online]. Hinxton: European Bioinformatics Institute (EMBL-EBI). Disponibile su: https://www.ebi.ac.uk/training/on-demand. Gratuità dichiarata su: https://www.embl.org/training/self-paced-learning/
57. Richards S, Aziz N, Bale S, Bick D, Das S, Gastier-Foster J, et al. Standards and guidelines for the interpretation of sequence variants: a joint consensus recommendation of the American College of Medical Genetics and Genomics and the Association for Molecular Pathology. Genet Med. 2015;17(5):405-24. doi:10.1038/gim.2015.30. PMID: 25741868.
58. Rehm HL, Berg JS, Brooks LD, Bustamante CD, Evans JP, Landrum MJ, et al. ClinGen: the Clinical Genome Resource. N Engl J Med. 2015;372(23):2235-42. doi:10.1056/NEJMsr1406261. PMID: 26014595. Condizioni d'uso dei dati (CC0): https://clinicalgenome.org/docs/terms-of-use/
59. Landrum MJ, Lee JM, Benson M, Brown GR, Chao C, Chitipiralla S, et al. ClinVar: improving access to variant interpretations and supporting evidence. Nucleic Acids Res. 2018;46(D1):D1062-7. doi:10.1093/nar/gkx1153. PMID: 29165669.
60. Rehm HL, Page AJH, Smith L, Adams JB, Alterovitz G, Babb LJ, et al. GA4GH: international policies and standards for data sharing across genomic research and healthcare. Cell Genom. 2021;1(2):100029. doi:10.1016/j.xgen.2021.100029. PMID: 35072136.
61. Jacobsen JOB, Baudis M, Baynam GS, Beckmann JS, Beltran S, Buske OJ, et al. The GA4GH Phenopacket schema defines a computable representation of clinical data. Nat Biotechnol. 2022;40(6):817-20. doi:10.1038/s41587-022-01357-4. PMID: 35705716.
62. HL7 International. HL7 FHIR Genomics Reporting Implementation Guide [guida di implementazione]. Ann Arbor (MI): HL7 International (versione corrente). Disponibile su: https://build.fhir.org/ig/HL7/genomics-reporting/
63. Relling MV, Klein TE. CPIC: Clinical Pharmacogenetics Implementation Consortium of the Pharmacogenomics Research Network. Clin Pharmacol Ther. 2011;89(3):464-7. doi:10.1038/clpt.2010.279. PMID: 21270786.
64. Whirl-Carrillo M, McDonagh EM, Hebert JM, Gong L, Sangkuhl K, Thorn CF, et al. Pharmacogenomics knowledge for personalized medicine. Clin Pharmacol Ther. 2012;92(4):414-7. doi:10.1038/clpt.2012.96. PMID: 22992668.
65. Garante per la protezione dei dati personali. Provvedimento recante le prescrizioni relative al trattamento di categorie particolari di dati, ai sensi dell'art. 21, comma 1 del d.lgs. 10 agosto 2018, n. 101, n. 146 del 5 giugno 2019 (Gazzetta Ufficiale n. 176 del 29 luglio 2019), doc. web n. 9124510; par. 4 sui dati genetici, modificato dal provvedimento n. 66 del 13 febbraio 2025 (doc. web n. 10112364). Disponibile su: https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9124510

---

## Licenza

© 2026 Diletta Falcone. Questo curriculum è distribuito con licenza [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.it) (Creative Commons Attribuzione - Condividi allo stesso modo 4.0 Internazionale): puoi copiarlo, ridistribuirlo e modificarlo, anche per scopi commerciali, citando l'autrice e distribuendo le modifiche con la stessa licenza. Il testo legale è nel file [LICENSE](LICENSE). I corsi e i documenti di terzi citati restano soggetti alle rispettive licenze.
