#include <alsa/asoundlib.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
//g++ main.cpp -lasound

vector<string> command(){
    cout << "Enter command or type help: ";
    string line;
    getline(cin, line);
    stringstream ss(line);
    vector<string> v;
    string word;

    while(ss >> word) {
        v.push_back(word);
    }

    return v;
}

void display(string name){
    cout << "╭──────────────────────────────────────╮\n";
    cout << "│  Terminal Music Player               │\n";
    cout << "├──────────────────────────────────────┤\n";
    cout << "│                                      │\n";
    cout << "│  ▶ " << name << "                 │\n";
    cout << "│    ━━━━━━━━━━━━━━━━──────  03:21     │\n";
    cout << "│                                      │\n";
    cout << "│  [p] Pause  [n] Next  [b] Previous   │\n";
    cout << "│  [s] Shuffle [q] Quit                │\n";
    cout << "╰──────────────────────────────────────╯\n";
}

void play(string playlist){
    
}

int main(){
    cout << "Welcome to Audio Player\n";
    
    vector<string> args = command();
    if(args.size() == 0 || args[0] == "help"){
        cout << "Available commands-\n";
        cout << "create <playlist>\n";
        cout << "add <song path> <playlist>\n";
        cout << "play <playlist> <optional loop and/or shuffle>\n";
        cout << "pause\n";
        cout << "skip\n";
    }
    else if(args[0] == "create"){
        if(args.size() != 2){
            cout << "Invalid arguments!\n";
            return 1; //change later
        }

        filesystem::create_directory(args[1]);
        cout << "Successfully created " << args[1] << endl;
    }
    else if(args[0] == "add"){
        if(args.size() != 3){
            cout << "Invalid arguments!\n";
            return 1; //change later
        }

        filesystem::path music = "Music";
        filesystem::path name = args[1];
        filesystem::rename(args[1], music / name.filename());
    }
    else if(args[0] == "play"){
        
    }
    else if(args[0] == "pause"){

    }

    return 0;
}