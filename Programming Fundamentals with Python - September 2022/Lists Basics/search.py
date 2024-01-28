n = int(input())
word = input()

strings = []
filtered_lst = []

for i in range(n):
    sentence = input()
    strings.append(sentence)

    if word in sentence:
        filtered_lst.append(sentence)

print(strings)
print(filtered_lst)

