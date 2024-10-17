from collections import deque

tools = deque(map(int,input().split()))
substances = [int(x) for x in input().split()]

challenges = [int(c) for c in input().split()]


while tools and substances and challenges:
    tool = tools.popleft()
    substance = substances.pop()
    power = tool * substance

    if power in challenges:
        challenges.remove(power)
    else:
        tool += 1
        tools.append(tool)
        substance -= 1
        if substance > 0:
            substances.append(substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print('Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f"Tools: {', '.join(str(t) for t in tools)}")

if substances:
    print(f"Substances: {', '.join(str(s) for s in substances)}")

if challenges:
    print(f"Challenges: {', '.join(str(c) for c in challenges)}")

