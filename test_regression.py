import json
from day1_retrieval import ConciergeRetriever
from app import ConciergeAssistant

def run_automated_tests():
    print("Starting automated regression tests...")
    
    # Load retrieval system
    retriever = ConciergeRetriever("data/raw_documents")
    retriever.load_and_chunk()
    bot = ConciergeAssistant(retriever)
    
    # Load evaluation set
    with open("data/eval_set.json", "r") as f:
        eval_data = json.load(f)
        
    passed = 0
    # Test a quick sample of 5 questions to save API costs
    for item in eval_data[:5]:
        query = item['question']
        print(f"\nTesting Q: {query}")
        try:
            answer, source = bot.generate_response(query)
            print(f"Result: SUCCESS (Source: {source})")
            passed += 1
        except Exception as e:
            print(f"Result: FAILED -> {e}")
            
    print(f"\nRegression Test Complete: {passed}/5 passed without crashing.")

if __name__ == "__main__":
    run_automated_tests()