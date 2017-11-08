#ifndef HEADER_HPP
#define HEADER_HPP

#include <iostream>
#include <string>
#include <vector>

#define uint unsigned int

using namespace std;

struct Node
{
    Node *mPrevious;
    Node *mNext;

    uint mStart;
    uint mSize;

    bool mIsEmpty;

    string name;
}

class MemoryManager
{
    public:

    Node *mHead;

    MemoryManager(uint capacity);
    Node* findEmptySpaceForProcess(uint size);
    void allocate(string name, uint size);
    void free(string name);
};

#endif
