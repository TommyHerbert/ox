from main.logical_tree import LogicalTreeLeaf


class Category:
    def __init__(self):
        self.lexical_form = None

    def get_logical_form(self, input_string, reader):
        if input_string == self.lexical_form:
            return LogicalTreeLeaf(self)
        else:
            return None
