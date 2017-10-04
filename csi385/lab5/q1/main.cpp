#include <iostream>
#include <thread>

const size_t COUNT = 1000;

void call_from_thread()
{
	std::cout << "Hello" << std::endl;
}

int main()
{
	std::thread my_threads[COUNT];

	for (size_t i = 0; i < COUNT; i++)
	{
		my_threads[i] = std::thread(call_from_thread);
	}

	for (size_t i = 0; i < COUNT; i++)
	{
		my_threads[i].join();
	}

	return 0;
}
