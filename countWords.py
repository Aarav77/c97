introString=input("Please introduce yourself: ")
charCount=0
wordCount=1
for i in introString:
    charCount=charCount+1
    if(i==' '):
        wordCount=wordCount+1
print("number of words: ")
print(wordCount)
print("number of characters: ")
print(charCount)