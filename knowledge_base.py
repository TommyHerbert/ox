from question import FavouriteQuestion

class KnowledgeBase:
    def __init__(self, ox):
        self.ox = ox
        self.categories = []
        self.categories.append(FavouriteQuestion(self.ox))
