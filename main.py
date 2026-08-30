import subprocess as sp
import shlex
import os

def command():
    print("Enter command or type help: ", end = "")
    line = input()
    return shlex.split(line)

def display(name):
    print("╭──────────────────────────────────────╮")
    print("│  Terminal Music Player               │")
    print("├──────────────────────────────────────┤")
    print("│                                      │")
    print("│  ▶ " + name + "                 │")
    print("│    ━━━━━━━━━━━━━━━━──────  03:21     │")
    print("│                                      │")
    print("│  [p] Pause  [n] Next  [b] Previous   │")
    print("│  [s] Shuffle [q] Quit                │")
    print("╰──────────────────────────────────────╯")

#main
print("Welcome to Terminal Music Player!")

while True:
    cmd = command()
    if len(cmd) == 0 or cmd[0] == "help":
        print("Available commands-")
        print("create <playlist>")
        print("add <song path> <playlist>")
        print("play <playlist> <optional loop and/or shuffle>")
        print("pause")
        print("skip")

    elif cmd[0] == "create":
        if len(cmd) < 2:
            print("Invalid arguments!")
        else:
            for i in range(1, len(cmd)):
                sp.run(['touch', 'Playlists/' + cmd[i]])
                with open('Playlists/' + cmd[i], "a") as file:
                    file.write('0\n')

    elif cmd[0] == "add":
        if len(cmd) < 3:
            print("Invalid arguments!")
        else:
            cmd[1] = os.path.expanduser(cmd[1])
            fname = cmd[1][cmd[1].rfind('/') + 1:]
            sp.run(['mv', cmd[1], './Music/' + fname])
            print(fname)
            for i in range(2, len(cmd)):
                with open('Playlists/' + cmd[i], "a") as file:
                    file.write('Music/' + fname + '\n')
                
                with open('Playlists/' + cmd[i], "r") as file:
                    lines = file.readlines()

                lines[0] = str(int(lines[0]) + 1) + '\n'

                with open('Playlists/' + cmd[i], "w") as file:
                    file.writelines(lines)
                
    elif cmd[0] == "play":
        if len(cmd) < 2:
            print("Invalid arguments!")
        else:
            with open('Playlists/' + cmd[1], "r") as file:
                lines = file.readlines()

            for line in lines[1:]:
                display(line[6:len(line) - 1])
                sp.Popen(['mpv', line.strip()])

    elif cmd[0] == "pause":
        sp.run(['kill', 'mpv'])
    
    elif cmd[0] == 'exit':
        break

    else:
        print("Command not recognized")