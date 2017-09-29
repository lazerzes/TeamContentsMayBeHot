#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <string>

int main()
{
    pid_t pid;
    int pipefd[2];
	string buffer;
	char *args[] =
	{
		"/bin/ls",
		NULL
	};

    pipe(pipefd);

    pid = fork();

    if (pid == 0)
    {
        close(pipefd[0]);
		dup2(pipefd[1], 1);
        execv(args[0], args);
        close(pipefd[1]);
    }
    else if (pid > 0)
    {
        close(pipefd[1]);
		dup2(pipefd[0], 0);
        std::getline(std::cin, buffer);
		std::cout << buffer;
        close(pipefd[0]);
    }
    return 0;
}
