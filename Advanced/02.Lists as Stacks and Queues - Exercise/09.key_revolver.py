from collections import deque

price_per_bullet = int(input())
barrel_size = int(input())
bullets = [int(n) for n in input().split()]
locks = deque(map(int, input().split()))
payment = int(input())

current_barrel = barrel_size
opened_locks = 0

while bullets and locks:
    if current_barrel > 0:
        shot = bullets.pop()
        current_barrel -= 1
        payment -= price_per_bullet
        if shot <= locks[0]:
            locks.popleft()
            opened_locks += 1
            print('Bang!')
        else:
            print('Ping!')
        if current_barrel == 0 and len(bullets) > 0:
            current_barrel = barrel_size
            print('Reloading!')

if len(locks) == 0:
    print(f'{len(bullets)} bullets left. Earned ${payment}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
