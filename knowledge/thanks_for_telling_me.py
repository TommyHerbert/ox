from knowledge.concept import Thing


class ThanksForTellingMe(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = "Oh, I didn't know that. Thanks for telling me."

