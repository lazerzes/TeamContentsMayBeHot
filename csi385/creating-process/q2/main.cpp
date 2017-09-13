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

    // Get the program path via prompt
    cout << "What program would you like to run? ";
    cin >> data;
    data = BIN_PATH + data;

    // Generate cstring in heap for program path
    length = data.length();
    program = (char*)malloc(length+1);
    data.copy(program, length);
    program[length+1] = '\0';

    // Get argument count via prompt
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

    // Allocate heap for arguments list
    argument_count = stoi(data);
    argument_count++; // need an extra argument for program path
    arguments = (char**)malloc(sizeof(char*) * (argument_count+1));

    // Get argument via prompt and allocate heap pointed from arguments list
    arguments[0] = program; // first argument is program name
    for (size_t i = 1; i < argument_count; i++)
    {
        cout << "Please enter argument [" << i << "]: ";
        cin >> data;
        length = data.length();
        arguments[i] = (char*)malloc(length+1);
        data.copy(arguments[i], length);
        arguments[i][length+1] = '\0';
    }
    arguments[argument_count+1] = NULL; // null terminate arguments list

    pid = fork();
    if (pid > 0)
    {
        // Parent process
        cout << "Parent: Waiting for child process to finish execution..."
             << endl << endl;
        wait(NULL);
        cout << endl << "Parent: Wait concluded. Terminating process." << endl;
    }
    else if (pid == 0)
    {
        // Child process
        execv(arguments[0], arguments);

        // The following code will only run if execv fails on child process
        cout << "Child: Execution failed. Program not found." << endl;

        // Free heap
        for (size_t i = 0; i < argument_count; i++)
        {
            cout << "Freeing: " << arguments[i] << endl;
            if (arguments[i] != NULL)
            {
                free(arguments[i]);
                arguments[i] = NULL;
            }
        }
        cout << "Freeing array." << endl;
        if (arguments != NULL)
        {
            free(arguments);
            arguments = NULL;
        }
        return 0;
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
