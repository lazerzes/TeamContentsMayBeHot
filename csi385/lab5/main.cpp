#include <iostream>
#include <thread>

const int COUNT = 1000;

void call_from_thread()
{
	std::cout << "Hello" << endl;
}

int main()
{
	std::thread my_threads[COUNT];

	for (int i = 0; i < COUNT: i++)
	{
		my_threads[i] = std::thread(call_from_thread);
	}

	for (int i = 0; i < COUNT; i++)
	{
		my_threads[i].join();
	}

	return 0;
}
