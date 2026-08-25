import subprocess as sp

def command():
    print("Enter command or type help: ", end = "")
    line = input()
    return line.split()

#main
print("Welcome to Terminal Music Player!")

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
        sp.run(['touch', 'Playlists/' + " ".join(cmd[1:])])

elif(cmd[0] == "add"):
    if len(cmd) < 3:
        print("Invalid arguments!")
    else:
        sp.run(['mv', cmd[1], 'Music/' + cmd[1]])
        path = cmd[1].split('/')
        fname = 'Music/' + path[len(path) - 1]
        for i in range(2, len(cmd)):
            with open(cmd[i], "a") as file:
                file.write('Music/' + fname)

elif(args[0] == "play"):
    print("placeholder")

elif(args[0] == "pause"):
    print("placeholder")