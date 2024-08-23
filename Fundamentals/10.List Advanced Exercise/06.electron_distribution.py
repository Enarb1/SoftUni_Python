def electrons_final(electrons):
    shells = []
    shell_position = 1

    while electrons > 0:
        shell_space = 2 * (shell_position ** 2)
        if electrons >= shell_space:
            shells.append(shell_space)
            electrons -= shell_space
        else:
            shells.append(electrons)
            electrons = 0
        shell_position += 1
    return shells


total_electrons = int(input())
final_shells = electrons_final(total_electrons)
print(final_shells)







