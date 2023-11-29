def isAnagram(word):
    word_listed = {}
    for key, value in enumerate(word):
        word_listed[key] = value
    print(word_listed)

x = "Anaconda"

isAnagram(x)