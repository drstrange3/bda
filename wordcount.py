text = input()
text = text.strip()
words = text.split(" ")
for word in words:
    print(word, "1")

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)
