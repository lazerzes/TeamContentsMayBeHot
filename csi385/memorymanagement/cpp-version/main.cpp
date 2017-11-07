struct Node {

	Node* previous;
	Node* next;

	uint start;
	uint size;

	string name;

	Node(uint start, uint size, string name) {
		this->start = start;
		this->size = size;
		this->name = name;

	}

};

class MemoryManager {

public:
	uint size;
	Node* head;

	MemoryManager(uint size) {
		this->size = size;
		head = new Node(0, this->size, "unused");
	}

	vector<Node*> findEmptySpaceForProcess(uint size) {
		vector<Node*> list;

		Node* temp = head;
		while (temp != NULL) {
			if (temp->name == "unused" && size <= temp->size) {
				list.push_back(temp);
			}
		}

		return list;

	}

	void allocate(string name, uint size) {

		vector<Node*> list = this->findEmptySpaceForProcess(size);

	}


};

int main() {



	return 0;

}
