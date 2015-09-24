# Author: Cole Howard
#
# Takes a list of characters and reverses them in place,
# with the constraints of not using .reverse() method
# or a slice operator.


def list_of_chars(list_chars):
    """Take a list of characters and reverses the list

    Args:
        list_chars - a list

    Return:
        a list
    """
    if list_chars:
        for x in range(int(len(list_chars)/2)):
            list_chars[x], list_chars[-x-1] = list_chars[-x-1], list_chars[x]
        return list_chars
    else:
        return None


if __name__ == '__main__':
    assert list_of_chars(None) == None
    assert list_of_chars(['']) == ['']
    assert list_of_chars(['f', 'o', 'o', ' ', 'b', 'a', 'r']) == ['r', 'a', 'b', ' ', 'o', 'o', 'f']
    print(list_of_chars(['f', 'o', 'o']))




