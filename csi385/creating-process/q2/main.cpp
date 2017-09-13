#include <iostream>
#include <string>
#include <unistd.h>
#include <sys/wait.h>

using namespace std;

const string BIN_PATH = "/bin/";

int main()
{
    pid_t pid;
    string data = "";
    size_t length = 0;
    size_t argument_count = 0;
    char *program;
    char **arguments;

    // Get the path of the program
    cout << "What program would you like to run? ";
    cin >> data;
    data = BIN_PATH + data;
    length = data.length();
    program = new char[length+1];
    data.copy(program, length);
    program[length+1] = '\0';

    // Get argc
    cout << "How many arguments? ";
    cin >> data;
    for (size_t i = 0; i < data.length(); i++)
    {
        if (!isdigit(data[i]))
        {
            cout << "Error: NaN\n";
            exit(1);
        }
    }
    argument_count = stoi(data);
    arguments = new char*[argument_count+1];

    // Get arguments
    for (size_t i = 0; i < argument_count; i++)
    {
        cout << "Please enter argument [" << i+1 << "]: ";
        cin >> data;
        length = data.length();
        arguments[i] = new char[length+1];
        data.copy(arguments[i], length);
        arguments[i][length+1] = '\0';
    }
    arguments[argument_count] = NULL;

    pid = fork();
    if (pid > 0)
    {
        // Parent process
        wait(NULL);
    }
    else if (pid == 0)
    {
        // Child process
        execv(program, arguments);
        exit(1);
    }
    else
    {
        // Error
        perror("Fork failed with the following error");
        exit(1);
    }

    for (size_t i = 0; i < argument_count; i++)
    {
        delete arguments[i];
    }
    delete [] arguments;

    return 0;
}
