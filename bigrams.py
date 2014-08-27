from functions import *

#Read the file containing Hindi text
file = open('sample-files/temp.txt', 'r')
data = file.read().decode('utf-8')
words = data.split()
#...................................

for word in words:
    temp_list = words
    print word.encode('utf-8')
    while word in temp_list:
        index = temp_list.index(word)
        print index
        temp_list = temp_list[index+1:]
        print temp_list
    break
