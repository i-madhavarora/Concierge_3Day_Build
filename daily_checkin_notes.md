***

**Daily Check-in Notes (`daily_checkins.txt`)**

```text
# DAY 1 CHECK-IN
1. What I finished today: Audited the raw documents, built the baseline TF-IDF chunking/retrieval script, drafted the risk plan, and created the 40-question evaluation set.
2. What I did not finish, and why: Have not integrated the LLM yet. Sticking strictly to the Day 1 goal of ensuring the retrieval baseline works before adding generation logic.
3. The biggest problem I hit and how I handled it: Chunking the messy documents without losing context. Decided to split by double newlines but set a minimum character limit (30 chars) to drop orphaned titles and noise.
4. A decision I made that I am unsure about: Using standard TF-IDF instead of dense embeddings for the baseline. It is faster and transparent, but might struggle with heavy synonyms. 
5. Where I need input, if anywhere: None at the moment.
6. Hours actually spent: 4.5 hours.
7. Plan for tomorrow: Adapt to the Day 2 data update, integrate the LLM for answer generation with citations, connect the mock Order API, and test adversarial inputs.

# DAY 2 CHECK-IN
1. What I finished today: Integrated the LLM generation logic with strict sourcing, connected the mock Order API, and ran adversarial tests against the prompt.
2. What I did not finish, and why: Have not optimized for latency yet, prioritizing safety and accuracy over speed for today's build.
3. The biggest problem I hit and how I handled it: The mock API hangs caused system timeouts. I handled it by implementing a strict failover block that routes the user to a human agent rather than leaving them waiting.
4. A decision I made that I am unsure about: Appending the API output directly into the context window rather than using functional calling, as it was faster to implement but slightly less scalable.
5. Where I need input, if anywhere: None.
6. Hours actually spent: 5 hours.
7. Plan for tomorrow: Build a caching system to hit the latency constraints, implement the human handoff routing, run regression tests, and finalize the decision memo.

# DAY 3 CHECK-IN
1. What I finished today: Implemented a dictionary-based policy cache to cut response time for frequent queries, added a regex-based emotional trigger for human handoff, wrote the regression test script, and finished the final decision memo.
2. What I did not finish, and why: I did not migrate from TF-IDF to dense vector embeddings due to the strict Day 3 latency constraints and the fact that caching solved the immediate speed issue.
3. The biggest problem I hit and how I handled it: Ensuring the cache didn't accidentally serve one user's order data to another. I fixed this by restricting the cache to purely informational, non-PII policy queries.
4. A decision I made that I am unsure about: Using regex for emotional detection (human handoff). It works for explicit anger but might miss passive-aggressive complaints.
5. Where I need input, if anywhere: Ready for the live 30-minute review.
6. Hours actually spent: 4.5 hours.
7. Plan for tomorrow: Project is complete and submitted.