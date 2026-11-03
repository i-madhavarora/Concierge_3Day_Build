import os
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ConciergeRetriever:
    def __init__(self, doc_directory):
        self.doc_directory = doc_directory
        self.chunks = []
        self.chunk_sources = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None

    def load_and_chunk(self):
        """Reads text files and chunks them by paragraph."""
        for filename in os.listdir(self.doc_directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(self.doc_directory, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    text = f.read()
                    
                # Simple splitting by double newline for paragraphs
                paragraphs = [p.strip() for p in text.split('\n\n') if len(p.strip()) > 30]
                
                for i, para in enumerate(paragraphs):
                    self.chunks.append(para)
                    self.chunk_sources.append(f"{filename} - Section {i+1}")
        
        # Fit the baseline TF-IDF model
        self.tfidf_matrix = self.vectorizer.fit_transform(self.chunks)
        print(f"Loaded {len(self.chunks)} chunks from {len(os.listdir(self.doc_directory))} documents.")

    def search(self, query, top_k=3):
        """Returns the most relevant text chunks for a given query."""
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Basic threshold to filter noise
                results.append({
                    "source": self.chunk_sources[idx],
                    "text": self.chunks[idx],
                    "score": round(similarities[idx], 3)
                })
        return results

# Quick test execution
if __name__ == "__main__":
    # Assuming documents are placed in data/raw_documents
    retriever = ConciergeRetriever("data/raw_documents")
    retriever.load_and_chunk()
    
    test_query = "What is the policy for late refunds?"
    print(f"\nSearching for: '{test_query}'")
    for res in retriever.search(test_query, top_k=1):
        print(f"\nBest Match [{res['source']}]:\n{res['text']}")