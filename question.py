from functools import partial


class Expectation:
    def __init__(self, content):
        self.content = content


class Question:
    def __init__(self):
        pass

    def get_logical_form(self, input_string, reader):
        return Expectation(self.get_question_logic(input_string, reader))

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
        return partial(self.find_favourite, reader), [category]

    @staticmethod
    def get_category_string(input_string):
        # probably there's a neater way to do this with regular expressions
        start_string = "What's your favourite "
        end_string = "?"
        if not input_string.startswith(start_string):
            return None
        if not input_string.endswith(end_string):
            return None
        return input_string[len(start_string):0 - len(end_string)]

    def find_favourite(self, reader, category):
        relations = reader.get_relations()
        # bit long
        instances = [r.arguments[0] for r in relations if r.type == 'is_a' and r.arguments[1] == category]
        ox_likes = \
            [r for r in relations if r.type == 'likes' and r.arguments[0] == self.ox and r.arguments[1] in instances]
        if len(ox_likes) == 0:
            return None
        biggest_like = ox_likes[0]
        for like in ox_likes[1:]:
            if like.arguments[2] > biggest_like.arguments[2]:
                biggest_like = like
        return biggest_like.arguments[1]
