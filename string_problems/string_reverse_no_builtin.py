x = "Let's solve the question"

# s'tel evlos eht noitseuq


def reverse(word):
    rev_word = ""
    word_len = len(word) - 1
    for indx in range(0, word_len + 1):
        rev_word += word[word_len - indx]
    return rev_word


# print(reverse("Hello"))

# y = ""
# for word in x.split():
#     y = y + " " + reverse(word)
#     print(" ")

# print(y)


word = "Hello"

x = word[0]
word = word[1:] + x
print(word)
