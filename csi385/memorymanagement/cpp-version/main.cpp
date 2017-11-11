#include "MemoryManager.h"

using namespace std;

int main()
{
    MemoryManager mem = MemoryManager(500);

    cout  << "Testing 1 2 3" << endl;
    mem.display();
    mem.allocate("Test", 100);
    mem.allocate("dark souls is the cuphead of dark souls", 4);
    mem.display();
    cout << "Testing 4 5 6" << endl;
}
