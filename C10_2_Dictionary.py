def decode(word):
    kb= {"A":"Apples","O":"Oranges"}

    result = ""
    for i in range(0,len(word)):
        result = result + kb[word[i]]+"/"
    
    print(result)

word_1 = "AO"
decode(word_1)

