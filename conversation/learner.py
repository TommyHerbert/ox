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
    longer_term_base.add_categories(to_learn[0])
    longer_term_base.add_things(to_learn[1])
    longer_term_base.add_relations(to_learn[2])
    # TODO


def get_new_elements(new_base, old_base):
    '''
    Return a tuple of knowledge elements that are in the new knowledge
    base but not in the old one. The members of the tuple are
    themselves tuples: the first contains categories, the second things
    and the third relations.
    '''
    categories = \
        [c for c in new_base.categories if c not in old_base.categories]
    things = [t for t in new_base.things if t not in old_base.things]
    relations = [r for r in new_base.relations if r not in old_base.relations]
    return (tuple(categories), tuple(things), tuple(relations))

