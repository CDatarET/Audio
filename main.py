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

elif(cmd[0] == "add"):
    if len(cmd) < 3:
        print("Invalid arguments!")
    else:
        cmd[1] = os.path.expanduser(cmd[1])
        fname = cmd[1][cmd[1].rfind('/') + 1:]
        sp.run(['mv', cmd[1], './Music/' + fname])
        '''
        path = cmd[1].split('/')
        fname = 'Music/' + path[len(path) - 1]
        for i in range(2, len(cmd)):
            with open(cmd[i], "a") as file:
                file.write('Music/' + fname)
        '''

elif(args[0] == "play"):
    print("placeholder")

elif(args[0] == "pause"):
    print("placeholder")