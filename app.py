import time
import os
from openai import OpenAI 

# Drop your API key here (or use Anthropic/Gemini)
client = OpenAI(api_key="I_DONT_HAVE_A_KEY")  # Replace with actual API key

class MockOrderAPI:
    @staticmethod
    def get_order_status(order_id):
        time.sleep(1)
        if order_id == "ERROR":
            raise TimeoutError("Order service unavailable")
        return {"order_id": order_id, "status": "Shipped", "delivery_date": "Tomorrow"}

class ConciergeAssistant:
    def __init__(self, retriever):
        self.retriever = retriever
        self.policy_cache = {}

    def is_emotional_or_complex(self, user_query):
        trigger_words = ['angry', 'sue', 'lawyer', 'stolen', 'ruined', 'worst']
        return any(word in user_query.lower() for word in trigger_words)

    def generate_response(self, user_query, order_id=None):
        if self.is_emotional_or_complex(user_query):
            return "Escalating to a human agent immediately. Please hold.", "Human Support"

        if user_query in self.policy_cache:
            return self.policy_cache[user_query], "Cache"

        order_context = ""
        if order_id:
            try:
                order_data = MockOrderAPI.get_order_status(order_id)
                order_context = f"Order {order_data['order_id']} is {order_data['status']}."
            except Exception:
                return "Our order system is currently down. Transferring to an agent.", "Human Support"

        docs = self.retriever.search(user_query, top_k=1)
        if not docs and not order_context:
            return "I don't have that information in my current documents. Let me connect you to an agent.", "Fallback"

        source = docs[0]['source'] if docs else "Order API"
        context_text = docs[0]['text'] if docs else ""
        
        # Real LLM Call
        prompt = f"Answer the user based strictly on this context: '{context_text}'. {order_context}\nUser: {user_query}"
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=100
            )
            final_answer = response.choices[0].message.content
        except Exception:
            final_answer = f"Based on {source}, I found relevant policy but the AI generation timed out."

        if not order_id:
            self.policy_cache[user_query] = final_answer
            
        return final_answer, source