time = int(input())
weekday= input()

if weekday != "Sunday":
    if  10 <= time <= 18 :
        print('open')
    else:
        print('closed')
else:
    print('closed')