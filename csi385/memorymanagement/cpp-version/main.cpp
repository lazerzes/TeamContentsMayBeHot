/*       Authors: Rei Armenia, Matthew James Harrison
 *         Class: CSI-385 Operating Systems Architecture
 *    Assignment: Memory Allocation and Deallocation using LinkedLists
 *      Due Date: November 11, 2017
 *
 * Description:
 *   This C++ program models memory allocation.
 *
 * Certication of Authenticity:
 *   I certify that this is entirely my own work, except where I have given
 *   fully-documented references to the work of others. I understand the
 *   definition and consequences of plagiarism and acknowledge that the
 *   assessor of this assignment may, for the purpose of assessing this
 *   assignment:
 *     -  Reproduce this assignment and provide a copy to another member of
 *        academic staff; and/or
 *     -  Communicate a copy of this assignment to a plagiarism checking service
 *        (which may then retain a copy of this assignment on its database for
 *        the purpose of future plagiarism checking)
 ******************************************************************************/

#include "MemoryManager.h"

using namespace std;

int main()
{
    MemoryManager mem = MemoryManager(64);

    mem.allocate("Init", 16);
    mem.allocate("Foo", 2);
    mem.allocate("Baz", 4);
    mem.allocate("Yes", 1);
    mem.allocate("Stuff", 12);
    mem.display();
    mem.free("Baz");
    mem.free("Yes");
    mem.display();
    mem.allocate("Everything", 128);
    mem.free("Everything");
    mem.allocate("Anything", 7);
    mem.display();
    return 0;
}
