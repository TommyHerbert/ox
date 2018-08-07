from main.knowledge.concept import Thing


class AlreadyKnow(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = "Yes, I know."

