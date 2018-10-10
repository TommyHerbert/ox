class ContextElement:
    def __init__(self):
        pass

    @staticmethod
    def is_expectation():
        return False

    @staticmethod
    def element_type():
        return None


class Expectation(ContextElement):
    def __init__(self, content):
        ContextElement.__init__(self)
        self.content = content

    @staticmethod
    def is_expectation():
        return True

    @staticmethod
    def element_type():
        return 'expectations'


class Proposition(ContextElement):
    def __init__(self):
        ContextElement.__init__(self)

    @staticmethod
    def element_type():
        return 'propositions'

