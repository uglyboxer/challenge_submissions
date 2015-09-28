""" Written by Cole Howard
Examines the text of alice.txt counts the number of occurances of 
each word and then sorts them by most frequent to least and writes that
result to a file alice_words.txt

It then prints the longest word it found
and the total count of words in the dictionary it created.
"""


def add_word(inventory, word):
    """ Takes a dictionary and a word
    adds the word to the dictionary or just ups its count of that word
    Returns the dictionary
    """
    word = strip_word(word)
    inventory[word] = inventory.get(word, 0) + 1
    return inventory

def strip_word(word):
    """ Takes a word and strips it of spaces, numbers and puncs
    Returns what is left
    """

    punc = '!@#$%^&*()_-=+}{[]|;:<".,>?/0123456789\t\n '
    temp_word = ''
    for char in word:
        if char not in punc:
            temp_word += char
    return temp_word.lower()


def main():
    f = open('alice.txt', 'r')
    out_file = open('alice_words.txt', 'w')
    inventory = {}
    # Parse the text, build dictionary and add counts as you go
    for line in f:
        line.strip()
        if line:
            temp = line.split(' ')
            [add_word(inventory, word) for word in temp]
    ans = [(val, k) for k, val in inventory.items()] 
    ans.sort(reverse = True)
    [out_file.write('{} \t\t {}\n'.format(elem[1], elem[0])) for elem in ans]
    answer = ''
    word_count = 0
    for elem, val in inventory.items():
        word_count += val
        if len(elem) > len(answer):
            answer = elem
    print(answer)
    print(word_count)

if __name__ == '__main__':
    assert add_word({}, 'hi') == {'hi': 1}
    assert strip_word('sdBD#$!@#$') == 'sdbd'
    main()