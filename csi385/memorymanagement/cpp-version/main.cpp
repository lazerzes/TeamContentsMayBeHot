#include "MemoryManager.h"

using namespace std;

int main()
{
    MemoryManager mem = MemoryManager(500);

    mem.allocate("Test", 100);
    mem.allocate("dark souls is the cuphead of dark souls", 4);
}
