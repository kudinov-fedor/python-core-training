# multiple assignment
def multiple_assignment(collection):
    a, b, c, d = collection
    return "First will be {3}, then - {1}, then - {2} and in the end - {0}".format(d, b, c, a)


def mult_assignment_tail(collection):
    a, *tail = collection
    return a, tail


def mult_assignment_head(collection):
    *head, d = collection
    return head, d


def sort(data, sort_params, reverse):
    kwargs = {'key': sort_params,
              'reverse': reverse}
    return sorted(data, **kwargs)


def filter_data(collection, filter_name):
    return sorted(list(map(lambda i: i[filter_name], collection)))
