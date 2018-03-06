import re
from functools import partial
from concept import Category
from main.conversation.context import Expectation
from main.knowledge.logical_tree import LogicalTreeBranch


class Question(Category):
    def __init__(self):
        Category.__init__(self)

    def get_logical_form(self, input_string=None, reader=None):
        if None in [input_string, reader]:
            return None
        question_logic = self.get_question_logic(input_string, reader)
        return Expectation(question_logic) if question_logic else None

    def get_question_logic(self, input_string, reader):
        return None


class FavouriteQuestion(Question):
    def __init__(self, ox):
        Question.__init__(self)
        self.ox = ox

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

    def find_favourite_in_list(self, relations, candidates):
        ox_likes = []
        for r in relations:
            if r.relation_type == 'likes' and r.arguments[0] == self.ox and r.arguments[1] in candidates:
                ox_likes.append(r)
        if len(ox_likes) == 0:
            return None
        biggest_like = ox_likes[0]
        for like in ox_likes[1:]:
            if like.arguments[2] > biggest_like.arguments[2]:
                biggest_like = like
        return biggest_like.arguments[1]
