def countingWords_fromFile():
    f = input("Enter a File Name: ")
    fOpen = open(f, "r")
    num_ofWords = 0
    for line in fOpen:
        words = line.split()
        num_ofWords = num_ofWords + len(words)
    print(num_ofWords)
        

countingWords_fromFile()

