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
        write(pipefd[1], "Hello World\n\0", 256);
        close(pipefd[1]);
    }
    else if (pid > 0)
    {
        close(pipefd[1]);
        read(pipefd[0], &buf, 256);
        std::cout << buf;
        close(pipefd[0]);
    }
    return 0;
}
