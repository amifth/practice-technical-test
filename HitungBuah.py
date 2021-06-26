# NamaBuah=["apel", "mangga", "Durian", "Mangga", "Apel", "MANGGA"]

# for i in NamaBuah:
#     len(i)
#     # print(i)
#     if i.isupper()==True and i.islower()==True:
#         len(i)
#         print("A",len(i))

# import collections
# string='apel mangga Durian Mangga Apel MANGGA'
# li=string.split(' ')
# ambil=collections.Counter(li).most_common()

# for kata in ambil:
#     if kata.isupper()==True and kata.islower()==True:
#         print("%s\t: %d"%(kata[0],kata[1]))

import re
import string
from collections import Counter
frequency = {}
document_text = """apel mangga Durian Apel MANGGA Mangga"""
text_string = document_text.lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    if frequency[words] > 1:
        print(words, frequency[words])
    


# text = """apel mangga APEL Durian Apel MANGGA Mangga"""

# # Force to all be lowercase because FISH and fish and Fish are the same
# text = text.lower()

# # Remove anything that isn't a word character or a space
# # We could use .replace(".", "") but regex is a lot easier!
# text = re.sub("[^\w ]", "", text)

# # print("Cleaned sentence is:", text)

# words = text.split(" ")


# if words>=1:
#     print(words)

# a = Counter(words)
# print(a)