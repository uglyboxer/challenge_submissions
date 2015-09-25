# wk1_quiz
# Author: Cole Howard


def main():
    eight = 8
    b = eight
    print(b)
    x = 3
    print(x == 'a' or x == 'b')
    print(x > 10 and x % 2 != 0)


def no_change(n):
    return n


def tripler(str1):
    for x in range(3):
        print(str1)
    return None 


def pay_calc():
    hrs = eval(input("Enter Hours: "))
    rate = eval(input("Enter Rate: "))
    print("Pay: ", hrs * rate)
    return None 

def main_cont():
    str1 = "Hello"
    str2 = "World"
    str3 = str1 + str2
    print(str1[-1], str1[4])
    str1 = "Hi"
    print(str1*3)
    lst = [x for x in range(11)]
    lst.append('hi')
    lst.remove(4)
    print(5 in lst)
    [print(x) for x in range(10)]
    [print(y) for y in lst]
    [print(x * 2) for x in range(10)]

def infinity():
    count = 0
    while True:
        count += 1

def main_still_cont():
    var = None
    print(bool(var))
    tup = 'a',
    tup2 = 'a', 'b'
    tup3 = 'Dicaprio', 43
    name, age = tup3
    dct = {}
    dct['one'] = 1
    dct['two'] = 2
    dct['three'] = 3
    dct['four'] = 4
    dct['three'] = 'tres'
    del dct['two']
    keys_list = [x for x in dct]
    vals_list = [y for y in dct.values()]
    [print(a, ' ', b) for a, b in dct.items()]

    # We might use a dictionary over tuples for faster lookup of values

    # Definitions:
    # Mutability/immutability - describes whether or not something can be
    #                           altered (mutable) 
    # Homogenous/Heterogenous datatypes - Homogenous would be a datatype
    #                                   that can only hold like datatypes
    #                                - Heterogenous one can hold any
    #                                  data regardless of other types of entries
    #                                  in the structure.
    # Overflow - The state when all storage elements are filled and input is
    #            added.  In computing specifically relates to memory and/or
    #            the "bit buckets" with regards to a specific piece of data
    # Abstraction - The process of working back from a specific case to a 
    #               a more generalized one.  
    # Modularization - The practice of breaking a problem into smaller parts
    #                  whose solutions are, ideally, repurposable and easier
    #                  to troubleshoot.

    # Datatypes:
    # string: IHO
    # list: MHE
    # tuple: IHE
    # dictionary: IHE

    # Difference: Printing output from a function displays it in the terminal
    #             Returning output sends the result back to it calling
    #             statement.


if __name__ == '__main__':
    main()
    no_change(3)
    tripler('Hi there.')
    pay_calc()
    main_cont()
    # infinity()  # Commented out for reasons.
    main_still_cont()
