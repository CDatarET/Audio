#define MINIAUDIO_IMPLEMENTATION
#include <miniaudio/miniaudio.h>
#include <iostream>
#include <fstream>
#include <filesystem>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
    vector<string> args;
    for(int i = 0; i < argc; i++){
        string s = argv[i];
        args.push_back(s);
    }
    

    if(args[1] == "help"){
        cout << "Available commands-\n";
        cout << "play <playlist>\n";
        cout << "pause\n";
        cout << "create <playlist>\n";
        cout << "add <song> <playlist>\n";
    }
    else if(args[1] == "create"){
        filesystem::create_directory(args[2]);
        cout << "Successfully created " << args[2] << endl;
    }
    else if(args[1] == "play"){
        ma_engine engine;
        if (ma_engine_init(nullptr, &engine) != MA_SUCCESS) return -1;
        ma_engine_play_sound(&engine, argv[2], nullptr);
        getchar();
        ma_engine_uninit(&engine);
    }

    return 0;
}