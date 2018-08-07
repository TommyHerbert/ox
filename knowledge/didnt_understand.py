from knowledge.concept import Thing


class DidntUnderstand(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = "Sorry, I didn't understand that."

