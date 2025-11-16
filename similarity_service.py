from sentence_transformers import util
from src.models.similarity_model import SimilarityModel

class SimilarityService:
    """Service for calculating text similarity"""
    
    def __init__(self):
        self.model = SimilarityModel().get_model()
    
    def check_similarity(self, new_idea, existing_ideas):
        """Check similarity between new idea and existing ideas"""
        if not new_idea or not existing_ideas:
            raise ValueError("Missing newIdea or existingIdeas")
        
        new_emb = self.model.encode(new_idea, convert_to_tensor=True)
        old_embs = self.model.encode(existing_ideas, convert_to_tensor=True)
        scores = util.cos_sim(new_emb, old_embs)[0]
        
        best_index = scores.argmax().item()
        best_score = scores[best_index].item()
        
        return {
            "bestScore": float(best_score),
            "bestIdea": existing_ideas[best_index],
            "isSimilar": best_score >= 0.80
        }