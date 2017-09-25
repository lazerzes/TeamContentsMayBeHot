/*       Authors: Rei Armenia, Matthew James Harrison
 *         Class: CSI-385 Operating Systems Architecture
 *    Assignment: Creating Processes
 *      Due Date: September 24, 2017
 *
 * Description:
 *   This C++ program runs "ps -ax" via a child process whose output has been
 *   redirected to a pipe.
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

int main()
{
    char *argv_ps[] = 
    {
        "/bin/ps",
        "-ax",
        NULL
    };
    char buf;
    size_t i = 0;
    string line = "";
    pid_t pid;
    int pipefd[2];
    size_t pos = string::npos;
    int rb = -1;
    
    // Create a new pipe
    if (pipe(pipefd) == -1)
    {
        perror("Failed to pipe");
    }

    // Fork program into two processes
    if ((pid = fork()) == -1)
    {
        perror("Failed to fork");
    }
    
    // Child process
    if (pid == 0)
    {
        close(pipefd[0]); // Close STDIN
        dup2(pipefd[1], 1); // Redirect STDOUT to pipe output
        
        execv(argv_ps[0], argv_ps);
        
        perror("Failed to execute program");
        exit(1);
    }
    // Parent process
    else
    {
        close(pipefd[1]); // Close pipe input
        
        // Read pipe output character-by-character
        i = 0;
        while ( (rb = read(pipefd[0], &buf, 1)) == 1 )
        {
            // Append character to line
            line.push_back(buf);
            
            // Detect end of line
            if (buf == '\n')
            {
                // Scan header
                if (i == 0)
                {
                    // Column we want is always aligned with the C in COMMAND
                    if ((pos = line.find("COMMAND")) == -1)
                    {
                        perror("Unable to parse ps header");
                        exit(1);
                    }
                }
                // Redact first process name
                else if (i == 1)
                {
                    line.replace(pos, line.length(), "REDACTED\n");
                }
            
                // Display and clear the line
                cout << line;
                line = "";
                
                i++;
            }
        }
        wait(NULL);
    }
    return 0;
}
