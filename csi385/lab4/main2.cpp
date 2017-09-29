#include <unistd.h>
#include <sys/wait.h>
#include <iostream>

int main()
{
    pid_t pid;
    int pipefd[2];
    char buf[256];

    pipe(pipefd);

    pid = fork();

    if (pid == 0)
    {
        close(pipefd[0]);
	dup2(pipefd[1], 1);
        write(1, "Hello World\n\0", 256);
        close(pipefd[1]);
    }
    else if (pid > 0)
    {
        close(pipefd[1]);
	dup2(pipefd[0], 0);
        read(0, &buf, 256);
        std::cout << buf;
        close(pipefd[0]);
    }
    return 0;
}
