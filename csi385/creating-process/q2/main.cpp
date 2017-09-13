#include <iostream>
#include <string>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

const string BIN_PATH = "/bin/";

string remove_spaces(string data)
{
    size_t position = string::npos;
    while (data.length() > 0)
    {
        position = data.find(' ');
        if (position == string::npos)
        {
            break;
        }
        else
        {
            data.erase(position, 1);
        }
    }
    return data;
}

int main()
{
    pid_t pid;
    string user_input = "";
    string program_name = "";
    string program_arguments = "";
    string *program_arguments_array;
    size_t position = string::npos;

    getline(cin, user_input);
    position = user_input.find(' ');
    if (position == string::npos)
    {
        program_name = user_input;
        program_arguments = "";
    }
    else
    {
        program_name = user_input.substr(0, position);
        program_arguments = user_input.substr(position+1, user_input.length());
    }

    pid = fork();
    if (pid > 0)
    {
        // Parent process
        wait(NULL);
    }
    else if (pid == 0)
    {
        // Child process
        //execv(BIN_PATH + program_name);
        exit(1);
    }
    else
    {
        // Error
        perror("Fork failed with the following error");
        exit(1);
    }

    return 0;
}
