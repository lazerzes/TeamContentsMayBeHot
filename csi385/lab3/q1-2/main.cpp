/*       Authors: Rei Armenia, Matthew James Harrison
 *         Class: CSI-385 Operating Systems Architecture
 *    Assignment: Creating Processes
 *      Due Date: September 24, 2017
 *
 * Description:
 *   This C++ program...
 *
 * Certication of Authenticity:
 *   I certify that this is entirely my own work, except where I have given
 *   fully-documented references to the work of others. I understand the
 *   definition and consequences of plagiarism and acknowledge that the
 *   assessor of this assignment may, for the purpose of assessing this
 *   assignment:
 *     -  Reproduce this assignment and provide a copy to another member of
 *        academic staff; and/or
 *     -  Communicate a copy of this assignment to a plagiarism checking service
 *        (which may then retain a copy of this assignment on its database for
 *        the purpose of future plagiarism checking)
 ******************************************************************************/
 
#include <iostream>
#include <string>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>

using namespace std;

const int CHILD_ARGC = 2;
const string CHILD_ARGV[CHILD_ARGC] = 
{
    "/bin/ps",
    "-ax"
};
const bool VERBOSE = true;

int main()
{
    // process management
    int pipefd[2];
    char **cargv;
    char *command = (char*)"ps -ax";
    
    // string parsing
    char *buf = NULL;
    size_t rb = -1;
    size_t pos = string::npos;
    size_t len = string::npos;
    pid_t cpid;
    int i;
    string data;
    
    if (VERBOSE) { cout << "Creating pipe" << endl; }
    if ( pipe(pipefd) == -1 )
    {
        perror("Failed to pipe");
        exit(1);
    }
    
    if (VERBOSE) { cout << "Forking process" << endl; }
    cpid = fork();
    if (cpid == -1)
    {
        perror("Failed to fork");
        exit(1);
    }
    // Child process will write to pipe
    else if (cpid == 0)
    {
        if (VERBOSE) { cout << "Child: Fork successful" << endl; }
    
        // Close read fd from pipe
        close(pipefd[0]);
        
        if (VERBOSE) { cout << "Child: Closed unused read end" << endl; }

        // Allocate heap for list of arguments
        cargv = (char**)malloc(sizeof(char*) * CHILD_ARGC);
        
        if (VERBOSE) { cout << "Child: Allocated memory for argv" << endl; }
        
        // Allocate heap for program path and load data it
        data = CHILD_ARGV[0];
        len = data.length();
        cargv[0] = (char*)malloc(len+1);
        data.copy(cargv[0], len);
        cargv[0][len+1] = '\0';
        
        if (VERBOSE) { cout << "Child: Allocated memory for argv[0]" << endl; }
        
        // Allocate heap for program argument(s) and load it
        data = CHILD_ARGV[1];
        len = data.length();
        cargv[0] = (char*)malloc(len+1);
        data.copy(cargv[1], len);
        cargv[1][len+1] = '\0';

        if (VERBOSE) { cout << "Child: Allocated memory for argv[1]" << endl; }

        // Replace STDOUT with write fd from pipe
        dup2(pipefd[1], STDOUT_FILENO);

        if (VERBOSE) { cout << "Child: Executing program" << endl; }

        execv(cargv[0], cargv);
        
        perror("Failed to execv");
        exit(1);
    }
    // Parent process will read from pipe
    else
    {
        // Close write fd from pipe
        close(pipefd[1]);
        
        if (VERBOSE) { cout << "Parent: Initiated read loop" << endl; }
        i = 0;
        while ( rb = read(pipefd[0], &buf, 256) > 0 )
        {
            if (buf == NULL)
            {
                perror("Failed to read pipe");
                exit(1);
            }
            
            data = buf;
            
            // If first line, find the column where "COMMAND" starts
            if (i == 0)
            {
                if (VERBOSE) { cout << "Parent: Identified headers" << endl; }
                pos = data.find("COMMAND");
            }
            // If second line, replace the command string
            else if (i == 1)
            {
                if (VERBOSE) { cout << "Parent: Redacting" << endl; }
                data.replace(pos, rb-1, "REDACTED\n");
            }
            
            cout << data;
            
            rb = -1;
            free(buf);
            buf = NULL;
            i++;
            
            if (VERBOSE) { cout << "Parent: Read " << i << " lines" << endl; }
        }
        
        close(pipefd[0]);
        
        if (VERBOSE) { cout << "Parent: Waiting for child to end" << endl; }
        wait(NULL);
    }
    
    return 0;
}
