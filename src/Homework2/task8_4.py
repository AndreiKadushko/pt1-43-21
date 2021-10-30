def iq_test(numbers):
    # Bob is preparing to pass IQ test. The most frequent task in this test
    # is to find out which one of the given numbers differs from the others.
    # Bob observed that one number usually differs from the others in evenness.
    # Help Bob — to check his answers, he needs a program that among the given
    # numbers finds one that is different in evenness, and return a position of this number.
    # ! Keep in mind that your task is to help Bob solve a real IQ test, which
    # means indexes of the elements start from 1 (not 0)
    # Examples:
    # iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even
    # iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd

    numb = [int(i) for i in numbers.split()]
    evn = []
    odd = []
    for i in range(len(numb)):
        if numb[i] % 2 == 0:
            evn.append(i + 1)
        else:
            odd.append(i + 1)
    if len(evn) > 1:
        return odd[0]
    else:
        return evn[0]


numb_str = input()
print(iq_test(numb_str))
