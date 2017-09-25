/*       Authors: Rei Armenia, Matthew James Harrison
 *         Class: CSI-385 Operating Systems Architecture
 *    Assignment: Creating Processes
 *      Due Date: September 24, 2017
 *
 * Description:
 *   This C++ program runs "ps -ax" via a child process whose output has been
 *   redirected to a pipe.
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

