from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review for a place."""

    def __init__(self, *args, **kwargs):
        """Initializes a Review."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""