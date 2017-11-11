#include "MemoryManager.h"

using namespace std;

int main()
{
    MemoryManager mem = MemoryManager(500);

    mem.display();
    mem.allocate("Test", 100);
    mem.allocate("dark souls is the cuphead of dark souls", 4);
    mem.allocate("static abstract", 396);
    mem.display();
    return 0;
}
