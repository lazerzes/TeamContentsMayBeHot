#include "MemoryManager.h"


Node::Node(uint start, uint size, string name, bool isEmpty) {

	mStart = start;
	mSize = size;
	mName = name;
	mIsEmpty = isEmpty;

}

MemoryManager::MemoryManager(uint capacity)
{
    mHead = new Node(0, capacity, EMPTY, true);
}

Node* MemoryManager::findEmptySpaceForProcess(uint size)
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

void MemoryManager::allocate(string name, uint size)
{
    Node* freespace = findEmptySpaceForProcess(size);

    if(freespace == NULL)
	{
        //out error not enought space
        return;
    }

    Node* newNode = new Node(freespace->mStart, size, name, false);

	if (freespace->mSize - size == 0)
	{
		newNode->mNext = freespace->mNext;
		newNode->mPrevious = freespace->mPrevious;

		if (newNode->mPrevious != NULL) {
			newNode->mPrevious->mNext = newNode;
		}

		delete freespace;

	}
	else
	{
		newNode->mNext = freespace;
		newNode->mPrevious = freespace->mPrevious;

		freespace->mStart = (newNode->mStart + (newNode->mSize - 1));
		freespace->mSize -= newNode->mSize;

		if (newNode->mPrevious != NULL) {
			newNode->mPrevious->mNext = newNode;
		}

	}

	if (newNode->mStart == 0) {
		mHead = newNode;
	}

}

void MemoryManager::display()
{
    Node *current = mHead;

    while (current != NULL)
    {
        cout << current->mName << ": " << current->mStart << " (" << current->mSize << ")"<< endl;
        current = current->mNext;
    }
}
