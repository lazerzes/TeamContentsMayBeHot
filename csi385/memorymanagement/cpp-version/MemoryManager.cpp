#include "MemoryManager.h"

Node::Node(uint start, uint size, string name, bool isEmpty)
{
    mPrevious = NULL;
    mNext = NULL;

    mStart = start;
    mSize = size;

    mName = name;
    mIsEmpty = isEmpty;

}

MemoryManager::MemoryManager(uint capacity)
{
    mHead = new Node(0, capacity, EMPTY, true);
    mAvailable = capacity;
    mTotal = capacity;
}

Node *MemoryManager::findEmptySpaceForProcess(uint size)
{
    if (mHead != NULL)
    {
        if (mHead->mIsEmpty && mHead->mSize >= size)
        {
            return mHead;
        }

        Node* temp = mHead->mNext;
        while (temp != NULL)
        {
            if (temp->mIsEmpty && temp->mSize >= size)
            {
                return temp;
            }
            temp = temp->mNext;
        }
    }
    return NULL;
}

Node *MemoryManager::findNodeByName(string name)
{
    Node *temp = mHead;
    while (temp != NULL)
    {
        if (temp->mName == name)
        {
            break;
        }
        temp = temp->mNext;
    }
    return temp;
}

void MemoryManager::allocate(string name, uint size)
{
    cout << "Allocating block of size " << size << " for " << name << endl;
    Node* freespace = findEmptySpaceForProcess(size);

    // Case 1: Failed to find free space
    if (freespace == NULL)
    {
        cout << "Memory allocation failure. Insufficient memory." << endl;
        return;
    }

    freespace->mName = name;
    freespace->mIsEmpty = false;
    mAvailable -= size;

    // Case 2: Free space is an exact fit, meaning we are done
    if (freespace->mSize == size)
    {
        return;
    }
    // Case 3: Free space is larger than necessary
    else
    {
        Node* newNode = new Node(freespace->mStart + size, freespace->mSize - size, EMPTY, true);
        freespace->mSize = size;
        newNode->mNext = freespace->mNext;
        newNode->mPrevious = freespace;
        freespace->mNext = newNode;
    }
}

void MemoryManager::display()
{
    cout << "Available: " << mAvailable << "/" << mTotal << endl;

    Node *current = mHead;
    while (current != NULL)
    {
        cout << current->mName << ": " << current->mStart << " (" << current->mSize << ")"<< endl;
        current = current->mNext;
    }
}

void MemoryManager::free(string name)
{
    cout << "Freeing block with name" << name << endl;
}
