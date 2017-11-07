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
    uint mEnd;

    string name;
}

class MemoryManager
{
    public:
    uint mSize;
    Node *mHead;

    MemoryManager();
    vector<Node*>findEmptySpaceForProcess();
    void allocate(char name, uint size);
};

#endif
