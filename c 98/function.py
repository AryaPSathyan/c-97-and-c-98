def countWordsFromFile():
    filename = input("enter the filepath:")
    noOfWords = 0
    file = open(filename,'r')
    for line in file :
        words = line.split()
        noOfWords=noOfWords+len(words)
    print("no of words in the file:",noOfWords)

countWordsFromFile()   

