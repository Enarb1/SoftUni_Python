def loading_status(number):
    status = number
    loading = ""

    if status < 100:
        stat = number / 10
        dots = 10 - int(stat)
        loading = ('%' * int(stat)) + ('.' * dots)
        print(f"{number}% [{loading}]\nStill loading...")
    else:
        print("100% Complete!\n[%%%%%%%%%%]")


numb = int(input())
loading_status(numb)




