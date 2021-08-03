Sentence = input("Write your sentence here")
Count = 0
wordCount = 0 
for i in Sentence: 
    Count = Count + 1
    if (i == ' '):
        wordCount = wordCount + 1


print(Count)
print(wordCount)