# Sort Arrays (Ignoring Case)

# Logic: for every item.lower() in words..... get index of that item in new_words and replace the value in new_words

words = ['Long', 'Same', 'that', 'the', 'There', 'They', 'Think', 'Way', 'little']

"""
# Approach 1
new_words = [word.lower() for word in words]
new_words.sort()

for item in words:
    new_words[new_words.index(item.lower())] = item

print(final_words)
"""

print(sorted(words, key=str.lower))
