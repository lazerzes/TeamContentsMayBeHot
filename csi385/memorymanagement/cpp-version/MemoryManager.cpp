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

Node::Node(uint start, uint size, string name, bool isEmpty)
{
    mPrevious = NULL;
    mNext = NULL;

    mStart = start;
    mSize = size;

    mName = name;
    mIsEmpty = isEmpty;
}

Node::~Node()
{
    mPrevious = NULL;
    mNext = NULL;
}

MemoryManager::MemoryManager(uint capacity)
{
    mHead = new Node(0, capacity, EMPTY, true);
    mAvailable = capacity;
    mTotal = capacity;
}

MemoryManager::~MemoryManager()
{
    mHead = NULL;
}

/* Purpose: Find the first block that has the specified size
 * Pre: Size
 * Post: Returns pointer to suitable block, or NULL
 ******************************************************************************/
Node *MemoryManager::findFirstFit(uint size)
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

/* Purpose: Helper function for searching the linked list for a particular node
 * Pre: Name of target node
 * Post: Returns pointer to matching node, or NULL if no match is found
 ******************************************************************************/
Node *MemoryManager::findNodeByName(string name)
{
    Node *temp = mHead;
    while (temp != NULL)
    {
        if (temp->mName == name)
        {
            return temp;
        }
        temp = temp->mNext;
    }
    return NULL;
}

/* Purpose: Allocate memory block for node with specified name and size
 * Pre: Name and size requirement
 * Post: Block allocated if possible
 ******************************************************************************/
void MemoryManager::allocate(string name, uint size)
{
    cout << "Allocating block of size " << size << " for " << name << endl;
    Node *freespace = findFirstFit(size);

    // Case 1: Failed to find free space
    if (freespace == NULL)
    {
        cout << "Memory allocation failure. Insufficient memory." << endl;
        return;
    }

    freespace->mName = name;
    freespace->mIsEmpty = false;
    mAvailable -= size;

    // Case 2: Free space is an exact fit
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
    freespace = NULL;
}

/* Purpose: Display info about memory usage
 * Pre: None
 * Post: Info about each block of memory printed to the console
 ******************************************************************************/
void MemoryManager::display()
{
    cout << "Available: " << mAvailable << "/" << mTotal << endl;

    Node *temp = mHead;
    while (temp != NULL)
    {
        cout << temp->mName << ": " << temp->mStart << " (" << temp->mSize << ")"<< endl;
        temp = temp->mNext;
    }
    temp = NULL;
}

/* Purpose: Free memory block with specified name
 * Pre: Name of memory block
 * Post: Memory block freed and merged with adjacent free space if possible
 ******************************************************************************/
void MemoryManager::free(string name)
{
    cout << "Freeing block with name " << name << endl;
    Node *temp = findNodeByName(name);

    // Case 1: Failed to find node
    if (temp == NULL)
    {
        cout << "Failed to free block. Block does not exist." << endl;
        return;
    }

    mAvailable += temp->mSize;
    temp->mName = EMPTY;
    temp->mIsEmpty = true;

    Node *previous = temp->mPrevious;
    Node *next = temp->mNext;

    // Case 2-A: Merge with previous
    if (previous != NULL && previous->mIsEmpty)
    {
        previous->mNext = next;
        if (next != NULL)
        {
            next->mPrevious = previous;
        }
        previous->mSize += temp->mSize;
        delete temp;
        temp = previous;
        previous = temp->mPrevious;
    }

    // Case 2-B: Merge with next
    if (next != NULL && next->mIsEmpty)
    {
        next->mPrevious = previous;
        if (previous != NULL)
        {
            previous->mNext = next;
        }
        next->mSize += temp->mSize;
        next->mStart = temp->mStart;
        delete temp;
    }

    previous = NULL;
    next = NULL;
    temp = NULL;
}
