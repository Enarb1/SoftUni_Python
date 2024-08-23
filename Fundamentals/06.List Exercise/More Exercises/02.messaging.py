numbers = input().strip().split()
text = input().strip()

# Initialize the final message
message = []

# Process each number
for number in numbers:
    # Calculate the sum of digits of the current number
    digit_sum = sum(int(digit) for digit in number)

    # Determine the index in the current text
    index = digit_sum % len(text)

    # Append the character at this index to the message
    message.append(text[index])

    # Remove the character at this index from the text
    text = text[:index] + text[index + 1:]

# Print the final message
print(''.join(message))