//
//  main.cpp
//  lab03
//
//  Created by Armenia, Rei on 9/22/17.
//  Copyright © 2017 reiarmenia. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
    
    FILE* fpipe;
    char* command = (char*)"ps -ax";
    char line[256];
    string str;
    
    if(!(fpipe = (FILE*)popen(command, "r"))){
        perror("Problems with pipe");
        exit(1);
    }
    
    int t = 0;
    
    while( fgets(line, sizeof(line), fpipe)){
        str = line;
        if( t == 1){
            str.replace(0, 7, "REDACTED");
        }
        cout << str;
        t++;
    }
    pclose(fpipe);
    
    
}
