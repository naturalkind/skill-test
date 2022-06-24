
#def func(x, start, end, last):
#    for ix, o in enumerate(list(x.keys())):
#        if x[o].get(start) != None:
#            x[o][start].update({end:{}})
#            break
#        else:
#            func(x[o], start, end, last)


def func(x, start, end, last):
    if x[last].get(start) != None:
        x[last][start].update({end:{}})
    elif not x[last]:
        x[last].update({end:{}})
    else:
        for o in list(x[last].keys()):
            func(x[last][o], start, end, start)

def to_tree(x):
    temp_dict = {}
    last = None
    for start, end in x:
        if start == None:
            temp_dict[end] = {}
        else:
            try:
                temp_dict[start].update({end:{}})
                last = start
            except KeyError:
                func(temp_dict, start, end, last)
    return temp_dict


if __name__ == '__main__':
    #Write a function that builds a tree based on a list of tuples of id (parent id, offspring id),
    #where None is the id of the root node.
    #How this should work:

    #Написать функцию, строящую дерево по списку пар id (id родителя, id потомка),
    #где None - id корневого узла.
    #Пример работы:

    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
    
    assert to_tree(source) == expected





