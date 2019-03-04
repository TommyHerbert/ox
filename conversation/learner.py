from conversation import naive_learning_strategy as strategy


def update(longer_term_base, temporary_base, output_path):
    '''
    When a conversation introduces a novel concept or relation, ask the
    learning strategy whether this information is worth preserving. If
    so, update the longer-term knowledge base and write it out as
    source code that can be imported by other instances of Ox.
    '''
    new_elements = get_new_elements(temporary_base, longer_term_base)
    to_learn = strategy.select(new_elements, longer_term_base)
    


def get_new_elements():
    pass # TODO

