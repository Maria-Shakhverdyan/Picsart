class Review:
    __slots__ = ['customer_name', 'order', 'rating', 'comments']

    def __init__(self, customer_name, order, rating, comments):
        self.customer_name = customer_name
        self.order = order
        self.rating = rating
        self.comments = comments

    def display_review(self):
        return f"Review by {self.customer_name}: Rating: {self.rating}/5, Comments: {self.comments}"