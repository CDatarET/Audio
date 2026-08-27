import subprocess as sp
import shlex
import os

def command():
    print("Enter command or type help: ", end = "")
    line = input()
    return shlex.split(line)

#main
print("Welcome to Terminal Music Player!")

cmd = command()
print(cmd)

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

elif(cmd[0] == "add"):
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
            

elif(cmd[0] == "play"):
    if len(cmd) < 2:
        print("Invalid arguments!")
    else:
        with open('Playlists/' + cmd[1], "r") as file:
            lines = file.readlines()

        for line in lines[1:]:
            print(line[:len(line) - 1])
            sp.run(['mpv', str(line[:len(line) - 1])])

elif(cmd[0] == "pause"):
    print("placeholder")