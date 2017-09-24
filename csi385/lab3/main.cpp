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

int main()
{
    FILE *fpipe = NULL;
    char *command = (char*)"ps -ax";
    char *buf = NULL;
    size_t rb = 0;
    size_t pos = 0;
    int i = 0;
    string line = "";
    
    if (!(fpipe = (FILE*)popen(command, "r")))
    {
        perror("Problems with pipe");
        exit(1);
    }
    
    while ( (rb = getline(&buf, &rb, fpipe)) != -1 )
    {
        line = buf;
        
        if (i == 0)
        {
            pos = line.find("COMMAND");
        }
        else if (i == 1)
        {
            line.replace(pos, rb-1, "REDACTED\n");
        }
        
        cout << line;

        rb = 0;
        free(buf);
        buf = NULL;
        i++;
    }
    pclose(fpipe);
}
