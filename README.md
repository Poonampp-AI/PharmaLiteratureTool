# GenAI Pharma Literature Intelligence Tool
🚀 Overview

The GenAI Pharma Literature Intelligence Tool is a multi-agent RAG-based research system built using LangGraph, LangChain, OpenAI, and Python.
It automates scientific and regulatory literature review for the pharma domain by integrating semantic search, summarization, auto-tagging, and citation-aware generation.

The tool enables users to query across scientific journals, clinical trials, pharmacopoeias, and internal regulatory documents, bringing together multi-source insights in a single intelligent interface.

🧩 Tech Stack

Frameworks: LangChain, LangGraph, Python (Multi-Agent architecture)

LLM Backend: Azure OpenAI (GPT-4 / GPT-4-Turbo)

Retrieval Engine: FAISS / Azure Cognitive Search (Vector DB)

UI Layer: Streamlit (interactive dashboard)

Data Sources: PubMed, ClinicalTrials.gov, Drugs.com, WHO, EMA, Internal Repositories

Storage: Local document store + citation embedding

Version Control: GitHub

✨ Key Features

🔍 Hybrid Semantic Search: Combines keyword + vector-based retrieval for highly relevant results.

🧠 Multi-Agent Workflow: Planner, Retriever, Summarizer, and Validator agents work in parallel for efficiency.

📚 Citation-Aware Summarization: Each generated output includes proper citations to original sources.

🧾 Auto-Tagging Engine: Dynamically labels documents by type (scientific, regulatory, internal, etc.).

🗂 Dynamic Data Ingestion: Supports local uploads, web scraping, and database ingestion.

🎙 Speech-to-Text Input: Voice-based query support for faster research interaction.

📊 Insights Dashboard: Displays document summaries, key metrics, and search history.

🧑‍💼 Human-in-the-Loop: Allows expert feedback to refine and improve generated insights.

💬 Contextual Query Understanding: Handles complex natural language and multi-part scientific questions.

⚙️ Modular Architecture: Clean separation of modules—loader, embedder, search, summarizer—for easy scaling and updates.

🧠 Current Capabilities

Semantic retrieval from multiple pharma-relevant sources

Automated literature summarization with citations

Interactive Streamlit UI for querying and reviewing results

Configurable pipeline for scientific, regulatory, and internal document categories

🔮 Future Enhancements

🚢 Deployment on Azure Kubernetes Service (AKS): For scalable multi-user handling and auto-load balancing.

🧾 Advanced PDF/Docx parsing: Improve support for complex tables and scientific notations.

📈 Analytics Dashboard: Trends, frequency analysis, and keyword visualization.

🤖 LLM Fine-Tuning: On domain-specific corpora (e.g., ICH, FDA, WHO) for better accuracy.

🔐 Enterprise Integration: Integration with internal pharma databases and role-based access control.

🗣 Voice-Driven Summarization: Generate summaries directly from voice queries.

🌐 Multi-Language Support: Extend support to EMA and WHO multilingual publications.

📦 Repository Structure
genai_lit_survey_tool/
├── app.py
├── config/
│   └── settings.py
├── modules/
│   ├── planner.py
│   ├── document_loader.py
│   ├── web_loader.py
│   ├── embedder.py
│   ├── search.py
│   ├── summarizer.py
│   ├── human_feedback.py
│   └── speech_to_text.py
├── ui/
│   └── ui.py
├── data/
│   ├── local_docs/
│   └── uploads/
└── vectorstore/

🧾 Example Query

“Summarize recent EMA and WHO guidance on the impurity limits of oncology drugs and include citations.”
