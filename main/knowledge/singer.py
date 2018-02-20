from category import Category


class Singer(Category):
    def __init__(self):
        Category.__init__(self)
        self.lexical_form = 'singer'


class Adele:
    def __init__(self):
        self.lexical_form = 'Adele'
