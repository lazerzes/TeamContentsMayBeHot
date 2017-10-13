#include <iostream>
#include <mutex>
#include <thread>

using namespace std;

const size_t N = 100000; 
const size_t THREAD_COUNT = 50;

class Counter
{
	private:
	thread mThreads[THREAD_COUNT];
	size_t mCounter;
	mutex mtx;

	public:
	Counter()
	{
		mCounter = 0;
	
		for (size_t i = 0; i < THREAD_COUNT; i++)
		{
			mThreads[i] = thread(&Counter::add, this);
		}
	}

	~Counter()
	{
		for (size_t i = 0; i < THREAD_COUNT; i++)
		{
			mThreads[i].join();
		}

		cout << mCounter << endl;
	}

	void add()
	{
		lock_guard<mutex> guard(mtx);
		for (size_t i = 0; i < N; i++)
		{
			mCounter++;
		}
	}
};

int main()
{
	Counter *counter1 = new Counter();
	delete counter1;
}
