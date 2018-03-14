import re
from functools import partial

import main.ox
from main.knowledge.logical_tree import LogicalTreeBranch
from main.knowledge.question import Question


class FavouriteQuestion(Question):
    def __init__(self):
        Question.__init__(self)

    def get_question_logic(self, input_string, reader):
        category_string = self.get_category_string(input_string)
        if not category_string:
            return None
        category = reader.parse(category_string)
        return LogicalTreeBranch(partial(self.find_favourite, reader), [category])

    @staticmethod
    def get_category_string(input_string):
        match = re.match("What's your favourite (.+)\?", input_string)
        return match.group(1) if match else None

    def find_favourite(self, reader, category):
        relations = reader.get_relations()
        instances = category
        if type(instances) != list:
            instances = [r.arguments[0] for r in relations if r.relation_type == 'is_a' and r.arguments[1] == category]
        return self.find_favourite_in_list(relations, instances)

    @staticmethod
    def find_favourite_in_list(relations, candidates):
        ox_likes = []
        for r in relations:
            if r.relation_type == 'likes' and r.arguments[0].__class__ == main.ox.Ox and r.arguments[1] in candidates:
                ox_likes.append(r)
        if len(ox_likes) == 0:
            return None
        biggest_like = ox_likes[0]
        for like in ox_likes[1:]:
            if like.arguments[2] > biggest_like.arguments[2]:
                biggest_like = like
        return biggest_like.arguments[1]