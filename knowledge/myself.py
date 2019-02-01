from knowledge.concept import Thing


class Myself(Thing):
    def __init__(self):
        Thing.__init__(self)
        self.lexical_form = 'Ox'

        # Nothing is using this yet, and anyway Ox can't yet understand
        # it. But it seems like a good way to set out our stall.
        self.goal = 'do good by teaching'

    def overwrite_copy(self, source_directory, relative_path):
        pass # don't generate this concept from the default template

