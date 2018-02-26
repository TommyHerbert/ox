from concept import Category, Thing


class Singer(Category):
    def __init__(self):
        Category.__init__(self)
        self.lexical_form = 'singer'


class Adele(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Adele'
