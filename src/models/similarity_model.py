from sentence_transformers import SentenceTransformer

class SimilarityModel:
    """Handles SentenceTransformer model loading and caching"""
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SimilarityModel, cls).__new__(cls)
            cls._instance.model = SentenceTransformer('all-MiniLM-L6-v2')
        return cls._instance
    
    def get_model(self):
        """Return the loaded model"""
        return self.model