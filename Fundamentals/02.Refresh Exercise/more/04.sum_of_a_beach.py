text = input().lower()
words_to_count = ["Sand", "Water", "Fish", "Sun"]

total_count = 0

for word in words_to_count:
    total_count += text.count(word.lower())
print(total_count)