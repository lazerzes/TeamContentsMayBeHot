#include <iostream>
#include <thread>

const size_t COUNT = 1000;

void call_from_thread(int array[])
{
	for (size_t i = 0; i < COUNT; i++)
	{
		if (i % 2 == 0)
		{
			array[i] = 0;
		}
		else
		{
			array[i] = 1;
		}
	}
}

int main()
{
	int array[COUNT];
	std::thread my_threads[COUNT];

	for (size_t i = 0; i < COUNT; i++)
	{
		my_threads[i] = std::thread(call_from_thread, array);
	}

	for (size_t i = 0; i < COUNT; i++)
	{
		my_threads[i].join();
	}

	return 0;
}
