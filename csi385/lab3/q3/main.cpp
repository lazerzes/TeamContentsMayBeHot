/*       Authors: Rei Armenia, Matthew James Harrison
 *         Class: CSI-385 Operating Systems Architecture
 *    Assignment: Creating Processes
 *      Due Date: September 24, 2017
 *
 * Description:
 *   This C++ program demonstrates using pipes with fork and exec.
 *
 * Research:
 *   Creating pipes in C: http://tldp.org/LDP/lpg/node11.html
 *   Using dup2 for Redirection and Pipes: http://www.cs.loyola.edu/~jglenn/702/
 *     S2005/Examples/dup2.html
 *   Example - exec and pipes: http://www.minek.com/files/unix_examples/execill.
 *     html
 *   Mapping UNIX pipe descriptors to stdin and stdout in C: http://www.unixwiz.
 *     net/techtips/remap-pipe-fds.html
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
#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

using namespace std;

void pipe_fork_exec(char *argv[])
{
    char buf;
    int pipefd[2];
    pid_t pid;
    int rb;

    pipe(pipefd);
    pid = fork();
    
    if (pid == 0)
    {
        close(pipefd[0]);
        dup2(pipefd[1], 1);
        
        execv(argv[0], argv);
        
        close(pipefd[1]);
        perror("Failed to execute");
    }
    else if (pid > 0)
    {
        close(pipefd[1]);
        
        while (rb = read(pipefd[0], &buf, 1))
        {
            cout << buf;
        }
        
        close(pipefd[0]);
    }
    else
    {
        perror("Failed to fork");
        exit(1);
    }
}

int main() 
{
    char *argv_ps[] = 
    {
        "/bin/ps",
        "-aux",
        NULL
    };
    char *argv_mkdir[] = 
    {
        "/bin/mkdir",
        "test",
        NULL
    };
    char *argv_cd[] = 
    {
        "/bin/cd",
        "test",
        NULL
    };
    char *argv_kill[] = 
    {
        "/bin/kill",
        "1057",
        NULL
    };
    
    pipe_fork_exec(argv_ps);
    pipe_fork_exec(argv_mkdir);
    pipe_fork_exec(argv_cd);
    pipe_fork_exec(argv_kill);
    
	return 0;

}
