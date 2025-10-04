# app.py
import os
import json

from modules.document_loader import load_all_documents
from modules.embedder import build_faiss_index, load_faiss_index, save_index, get_embedding_model
from modules.summarizer import summarize_with_rag
from modules.planner import generate_survey_plan
from modules.human_feedback import review_plan, rerun_flagged_sections
from modules.web_loader import search_articles  # optional live data fetch

LOCAL_DOCS_PATH = "data/local_docs"
INDEX_PATH = "vectorstore"
META_PATH = os.path.join(INDEX_PATH, "meta.pkl")
PLAN_PATH = "survey_plan.json"
REVIEWED_PLAN_PATH = "survey_plan_reviewed.json"
UPDATED_PLAN_PATH = "survey_plan_reviewed_updated.json"

def main():
    print("🔹 Starting Pharma Literature GenAI Survey Tool Pipeline")

    # Step 1: Load and chunk local pharma documents
    print("📂 Loading local documents...")
    documents = load_all_documents(LOCAL_DOCS_PATH)
    print(f"✅ Loaded and chunked {len(documents)} document chunks.")

    # Step 2: Setup embedding model
    embedding_model = get_embedding_model()

    # Step 3: Build or load FAISS index of documents
    if os.path.exists(INDEX_PATH):
        print("📦 Loading existing FAISS index...")
        vectorstore = load_faiss_index(INDEX_PATH, embedding_model)
    else:
        print("🧠 Building new FAISS index...")
        vectorstore = build_faiss_index(documents, embedding_model)
        save_index(vectorstore, metadata={"source": "local_docs"}, index_path=INDEX_PATH, meta_path=META_PATH)
    if not vectorstore:
        print("❌ Failed to load or build vectorstore index. Exiting.")
        return

    # Step 4: Generate initial research plan/questions (automatic or user-driven)
    print("📝 Generating initial research plan...")
    topic = input("Enter research topic: ")
    plan = generate_survey_plan(topic)
    with open(PLAN_PATH, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)
    print(f"✅ Research plan saved to {PLAN_PATH}")

    # Optional Step 5: Fetch relevant live web data for broader context
    print("🌐 Fetching live web data (optional)...")
    web_docs = []
    try:
        web_docs = search_articles(topic, source="all", max_results=5)
  # expects list of documents
        if web_docs:
            print(f"✅ Fetched {len(web_docs)} live web documents.")
            # Optionally embed and add web docs to vectorstore (not implemented here)
    except Exception as e:
        print(f"⚠️ Skipping web data fetch due to error: {e}")

    # print("Type of web dosc is ",type(web_docs))
    # print(web_docs[0])
    # Step 6: For each question, run summarization with RAG (retrieval augmented generation)
    print("🤖 Running summarization for each question in the plan...")
    for section in plan.get("sections", []):
        question = section.get("question", "")
        if not question:
            continue
        print(f"🔍 Summarizing: {question}")
        try:
        # print('Muttukudi is ')
            result = summarize_with_rag(question, vectorstore=vectorstore, k=1, web_sources=web_docs , debug=True)
            # print('Final Result is ',result)
            section["answer"] = result.get("answer", "")
            section["sources"] = result.get("sources", [])
            section["status"] = "generated"
        except Exception as e:
            section["answer"] = f"❌ Error: {e}"
            section["sources"] = []
            section["status"] = "error"

    # Save updated plan with answers
    with open(PLAN_PATH, "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=2)
    print(f"✅ Updated plan with answers saved to {PLAN_PATH}")

    # Step 7: Human feedback loop - review, edit, flag for rerun, add questions
    review_plan(PLAN_PATH)  # interactive CLI loop saves to REVIEWED_PLAN_PATH

    # Step 8: Rerun flagged sections to improve answers
    rerun_flagged_sections(REVIEWED_PLAN_PATH)  # saves to UPDATED_PLAN_PATH

    print("🎉 Pipeline execution complete.")
    print(f"🗂️ Final reviewed and updated plan saved at: {UPDATED_PLAN_PATH}")

if __name__ == "__main__":
    main()
