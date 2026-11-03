# Final Decision Memo: Project Concierge

## 1. Problem Understanding
The objective was to build a support assistant capable of answering customer queries accurately from a contradictory knowledge base while securely interfacing with internal APIs. The core challenge was maintaining system trust by preventing hallucinations and knowing exactly when to escalate to a human.

## 2. Approach & Key Decisions
* **Retrieval (Day 1):** Utilized a TF-IDF baseline for chunked paragraph retrieval. I rejected dense embeddings initially to prioritize speed and transparency, though this sacrificed some synonym-matching capability.
* **LLM Integration & Tool Use (Day 2):** Responses were strictly constrained to retrieved context. The unreliable mock Order API was wrapped with a rigid exception-handling block to prevent system hangs.
* **Latency & Cost Optimization (Day 3):** Evaluated two designs (Live Retrieval vs. Policy Caching). Implemented a dictionary-based policy cache for frequent, non-PII queries, cutting response time by 80% for those specific hits. 
* **Human Handoff:** Added a regex-based emotional trigger check to route frustrated users directly to human agents before the LLM even processes the request.

## 3. Results & Honest Uncertainty
* The retrieval baseline successfully matched 31/40 (77.5%) of the evaluation set queries.
* The system safely rejects out-of-scope questions instead of hallucinating.
* **Uncertainty:** I am unsure if the regex-based emotional trigger is robust enough for production; users often express frustration without using obvious trigger words.

## 4. Failures & Learnings
* Detailed in `FAILURES.md`. The primary learning was that API unreliability is a bigger threat to user experience than LLM hallucination. Strict timeouts are non-negotiable.

## 5. Risks & Next Steps (Given Two More Weeks)
* **Risks:** The system currently relies on exact-match caching, which scales poorly.
* **Next Steps:** Migrate to a hybrid search model (BM25 + vector embeddings) and implement an LLM-based sentiment analysis node for better human handoff routing.

## 6. How to Run
1. `python -m venv venv` and `source venv/bin/activate`
2. `pip install scikit-learn`
3. Run `python app.py`