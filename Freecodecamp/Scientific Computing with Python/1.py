#Introduction : Why Program?
#

'''
Sakai software. 
Computer = Hardware + Software -> Data, Information...Networks. 
Code - Sequence of stored instructions.
Computer needs precision and accuracy.
  
  
'''
name = raw_imput('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for words in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is none or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) 
'''
Output - 
Enter file : words.txt
'''



