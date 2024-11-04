


def concat_tuples(tuple1, tuple2):
    #Check inputs being tuples
    if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
        raise ValueError("Both inputs must be tuples.")

    results = tuple1 + tuple2
    return results

try:
    tuplea = (1,2,3,4)
    tupleb = (5,6,7,8)

    results = concat_tuples(tuplea, tupleb)
    print(results)
except ValueError as e:
    print(e)