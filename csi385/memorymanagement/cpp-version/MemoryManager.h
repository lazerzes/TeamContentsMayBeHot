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

#ifndef HEADER_HPP
#define HEADER_HPP

#include <iostream>
#include <string>

#define uint size_t

using namespace std;

const string EMPTY = "empty block";

struct Node
{
    Node *mPrevious;
    Node *mNext;

    uint mStart;
    uint mSize;

    string mName;
    bool mIsEmpty;

    Node(uint start, uint size, string name, bool isEmpty);
    ~Node();
};

class MemoryManager
{
    private:
    Node *mHead;
    uint mAvailable;
    uint mTotal;

    public:
    MemoryManager(uint capacity);
    ~MemoryManager();
    Node *findFirstFit(uint size);
    Node *findNodeByName(string name);
    void allocate(string name, uint size);
    void display();
    void free(string name);
};

#endif
