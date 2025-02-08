word_freq={}
word=input("Enter Word: ")
for letter in word:
    if letter in word_freq:
        word_freq[letter] += 1
    else:
        word_freq[letter] = 1

print(word_freq)