#include "MemoryManager.h"

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

        temp = mHead->next;
        while(temp != NULL){
            temp->mIsEmpty && size <= temp->size ? return temp : temp = temp->mNext;
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

    Node* newNode = new Node(freespace->start, size, name, false);

    if(size < freespace->size){
        freespace->size -= (size);
        freespace->start = (size - 1);

        if(frees)

    }



}
