class Reasoner:
    def __init__(self):
        pass

    def take_move(self, logical_tree):
        return self.resolve(logical_tree)

    def resolve(self, logical_tree):
        if logical_tree.is_leaf():
            return logical_tree.content
        resolved_args = [self.resolve(a) for a in logical_tree.args]
        return logical_tree.func(*resolved_args)
