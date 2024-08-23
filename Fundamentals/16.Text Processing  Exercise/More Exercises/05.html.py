line_counter = 0
while True:
    command = input()
    if command == 'end of comments':
        break
    text = command
    if line_counter == 0:
        print(f'<h1>\n\t{text}\n</h1>')
    elif line_counter == 1:
        print(f"<article>\n\t{text}\n</article>")
    else:
        print(f'<div>\n\t{text}\n</div>')
    line_counter += 1