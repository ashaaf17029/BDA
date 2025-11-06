#Aim: Count how many times each word appears in input.txt

count = {}  # store word-frequency pairs

f = open("input.txt", "r")  # open file in read mode
text = f.read()  # read file content

words = text.lower().split()  # convert to lowercase & split into words

for word in words:
    word = word.strip(".,")  # remove commas and periods
    if word in count:
        count[word] += 1  # increase count if word exists
    else:
        count[word] = 1  # add new word with count 1

for word, freq in count.items():
    print(word, ":", freq)  # print word and its count

f.close()  # close file
