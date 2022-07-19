# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u":
#         count += 1

# print(count)

# 12

word = "HappyHacking"

count = 0

for char in word:
    if char in 'aeiou':
        count += 1

print(count)