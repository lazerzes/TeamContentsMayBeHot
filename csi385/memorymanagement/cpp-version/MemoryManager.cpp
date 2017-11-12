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

MemoryManager::MemoryManager(uint capacity)
{
    mHead = new Node(0, capacity, EMPTY, true);
    mAvailable = capacity;
    mTotal = capacity;
}

/* Purpose:
 * Pre:
 * Post:
 ******************************************************************************/
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

/* Purpose:
 * Pre:
 * Post:
 ******************************************************************************/
void MemoryManager::allocate(string name, uint size)
{
    cout << "Allocating block of size " << size << " for " << name << endl;
    Node *freespace = findEmptySpaceForProcess(size);

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

/* Purpose: Display info about memory usage
 * Pre: None
 * Post: Info about each block of memory printed to the console
 ******************************************************************************/
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

/* Purpose:
 * Pre:
 * Post:
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

    // Case 2-A: Merge with previous
    if (temp->mPrevious != NULL)
    {

    }

    // Case 2-B: Merge with next
    if (temp->mNext != NULL)
    {

    }
}
