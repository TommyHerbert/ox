from category import Category


class Song(Category):
    def __init__(self):
        Category.__init__(self)
        self.lexical_form = 'song'


class Hello:
    def __init__(self):
        self.lexical_form = 'Hello'
