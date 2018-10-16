class ContextElement:
    def __init__(self, content):
        self.content = content

    @staticmethod
    def is_expectation():
        return False

    @staticmethod
    def element_type():
        return None


class Expectation(ContextElement):
    @staticmethod
    def is_expectation():
        return True

    @staticmethod
    def element_type():
        return 'expectations'


class Proposition(ContextElement):
    @staticmethod
    def element_type():
        return 'propositions'

