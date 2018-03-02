from concept import Category, Thing


class Song(Category):
    def __init__(self):
        Category.__init__(self)
        self.lexical_form = 'song'


class Hello(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Hello'

class SomeoneLikeYou(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Someone Like You'
