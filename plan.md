# Plan for Days 2 & 3

## Upcoming Roadmap
* **Day 2:** Integrate the LLM (OpenAI/Anthropic API) with the TF-IDF retriever to form a complete RAG pipeline. Connect the mock Order API and build error-handling wrappers around it. Run the evaluation set and analyze the adversarial attacks.
* **Day 3:** Optimize latency by caching frequent queries and trimming context size. Implement the human-handoff routing logic. Write the final decision memo.

## Top 3 Risks
1. **API Timeout and Flakiness:** The mock order service is intentionally slow and unreliable. If it hangs, the chatbot will hang. I will need to implement strict timeout wrappers and fallback responses (e.g., "The system is currently busy, transferring to a human").
2. **Adversarial Jailbreaks:** Users might try to manipulate the bot into issuing unauthorized refunds. The system prompt needs strong boundary constraints and a secondary validation check before executing any API action.
3. **Latency Constraints:** Adding LLM generation on top of retrieval can easily push response times past acceptable limits for customer support. I might have to trade off using a smaller, faster model for simple queries and only route to a larger model for complex issues.