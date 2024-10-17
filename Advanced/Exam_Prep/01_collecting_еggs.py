from collections import deque

BOX_SIZE = 50

eggs= deque([int(e) for e in input().split(", ") if int(e) > 0])
papers = deque([int(p) for p in input().split(", ")])

filled_boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()
    if egg == 13:
        first_paper = papers.popleft()
        papers.append(first_paper)
        papers.appendleft(paper)
        continue

    if sum([egg, paper]) <= BOX_SIZE:
        filled_boxes += 1

if filled_boxes:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(map(str, eggs))}")
if papers:
    print(f"Pieces of paper left: {', '.join(map(str, papers))}")