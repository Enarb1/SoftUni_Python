import re

text = input()
title_pattern = r'<title>(.*?)<\/title>'
body_pattern = r'<body>(.*?)<\/body>'

title_match = re.findall(title_pattern, text)
body_match = re.findall(body_pattern, text)
for title in title_match:
    title_text = re.sub(r'<.*?>', "", title).replace('\\n','').strip()
    for body in body_match:
        body_text = re.sub(r'<.*?>', "", body).replace('\\n','').strip()
        print(f'Title: {title_text}')
        print(f'Content: {body_text}')

