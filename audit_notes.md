# Document Audit & Strategy

## Identified Issues in Knowledge Base
1. **Contradictions:** Standard return policy states a 30-day window, but a separate holiday addendum states 15 days.
   * **Decision:** We will inject a metadata tag for "active dates" during the chunking phase. If the current date falls outside the holiday window, the holiday document is heavily penalized in the retrieval score.
2. **Outdated Content:** There are legacy files (e.g., `shipping_faq_2024.txt`) that conflict with current SLA times.
   * **Decision:** Instead of deleting them, we will filter them out at the directory loading level by checking for "deprecated" or old year markers in the filename/header, ensuring the retriever only sees current documents.
3. **Gaps:** There is zero mention of digital gift card refunds in any document. 
   * **Decision:** The system prompt will be strictly instructed to return "I don't have that information" rather than attempting to guess or hallucinate a policy.
4. **Duplicates:** Exact paragraphs are repeated across the internal support wiki and customer-facing FAQ.
   * **Decision:** TF-IDF naturally handles this, but to avoid flooding the top-K results with the exact same text, we will implement a basic deduplication check (cosine similarity > 0.95 between chunks) during the loading phase.