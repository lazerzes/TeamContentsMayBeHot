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
#include <stdio.h>

using namespace std;

const string COMMANDS[4] = 
{
    "ps aux",
    "mkdir test",
    "cd ..",
    "kill 1057"
};

int main() {

    FILE *fpipe = NULL;
    char *buf = NULL;
    size_t rb = -1;
    string line;

	for (int i = 0; i < 3; i++)
	{
	    cout << COMMANDS[i] << endl;
	
	    fpipe = (FILE*)popen(COMMANDS[i].c_str(), "r");
	    if (fpipe == NULL)
	    {
	        perror("Problems with pipe");
	        exit(1);
	    }
	    
	    while ( (rb = getline(&buf, &rb, fpipe)) != -1 )
        {
            if (buf == NULL)
            {
                perror("Failed to read line");
                exit(1);
            }
            
            line = buf;
            cout << line;
            
            rb = -1;
            free(buf);
            buf = NULL;
        }
        
        pclose(fpipe);
        
        cout << endl;
    }

	return 0;

}
