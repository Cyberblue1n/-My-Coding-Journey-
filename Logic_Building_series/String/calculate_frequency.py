#Calculate frequency of characters in a string
def calculate_freq(word):
    count_char = {}
    for i in word:
        if i in count_char:
            count_char[i] = count_char.get(i, 0)+1
        else:
            count_char[i] = 1

    return count_char


a = input("Enter a string: ")
print(calculate_freq(a))
