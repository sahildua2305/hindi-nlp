import re

def unichrWord(word):
    return [unichr(ord(i)) for i in word]

def ordWord(word):
    return [str(ord(i)) for i in word]

def unichrOrd(ord_list):
    return [unichr(i) for i in ord_list]

#Initialization of variables
separators = [u"|"]
ending_words = []
decoded_ending_words = []
hyponyms = []
words_for_relations=[]
related_words=[]
count=0
count_diff=0
index=0
output=''
#...........................

# Preprocessing
words_for_relations.append([unichr(i) for i in [2344,2366,2350,2325]]) #naamak
words_for_relations.append([unichr(i) for i in [2332,2376,2360,2375]]) #jaise
#.........................

# Read the file containing Hindi text
file = open('sample-files/sample.txt', 'r')
data = file.read().decode('utf-8')
words = data.split()
#.................................

for word in words:
    curr_word = unichrWord(word)
    if curr_word in words_for_relations:
        related_words.append([words[index-1], words[index+1]])
        print (ordWord(words[index-1]))
        print words[index-1], words[index+1]
        if curr_word == words_for_relations[0]:
            with open('results/hyponyms.txt', 'a') as file:
                file.write('[('+",".join(ordWord(words[index+1]))+'),('+",".join(ordWord(words[index-1]))+")]")
        elif curr_word == words_for_relations[1]:
            with open('results/hyponyms.txt', 'a') as file:
                file.write('[('+",".join(ordWord(words[index-1]))+'),('+",".join(ordWord(words[index+1]))+")]")

    #Used for calculating number of sentences in the file
    # 2404 is the code for '|'.
    # 63 is the code for '?'.
    if ord(word[-1])==2404 or ord(word[-1])==63:
        count+=1
        temp_ending_list = [ord(i) for i in word[:-1]]
        if temp_ending_list not in ending_words:
            ending_words.append(temp_ending_list)
            count_diff+=1
    #............................................
    index+=1

print "Total number of sentences: "+str(count)
print "Total different ending words: "+str(count_diff)
print "Hyponyms found: ", related_words
