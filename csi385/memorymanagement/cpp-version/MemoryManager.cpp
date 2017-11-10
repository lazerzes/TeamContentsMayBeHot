#include "MemoryManager.h"

Node::Node(uint start, uint size, string name, bool isEmpty) {

	mStart = start;
	mSize = size;
	mName = name;
	mIsEmpty = isEmpty;

}

MemoryManager::MemoryManager()
{
    mHead = new Node(0, 500, "free memory", true);
}

Node* MemoryManager::findEmptySpaceForProcess(uint size)
{

    if(mHead != NULL){
        if(mHead->mIsEmpty){
            return mHead;
        }
		
        Node* temp = mHead->mNext;
        while(temp != NULL){
			if (temp->mIsEmpty && size <= temp->mSize) {
				return temp;
			}
			else {
				temp = temp->mNext;
			}
        }

        return NULL;
    }

}

void MemoryManager::allocate(string name, uint size)
{
    Node* freespace = findEmptySpaceForProcess(size);

    if(freespace == NULL){
        //out error not enought space
        return;
    }

    Node* newNode = new Node(freespace->mStart, size, name, false);



}
