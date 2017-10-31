class Block:
    def __init__(self, starting_address, size, name="Empty"):
        self.starting_address = starting_address
        self.size = size
        self.next = None
        self.is_empty = True
        self.name = name

    def load(self, name):
        self.name = name
        self.is_empty = False

class MemoryManager:
    def __init__(self, total_memory):
        self.used_memory = 0
        self.total_memory = total_memory
        self.root = Block(0, total_memory)
        self.blocks = 1

    def allocate(self, name, memory_requirement):
        print("Attempting to allocate", memory_requirement, "memory units for", name)

        block = self.root
        address = 0
        while block is not None:
            if block.is_empty and block.size >= memory_requirement:
                break
            block = block.next
            address += 1

        # Case 1: Failed to find block
        if block is None:
            print("Memory allocation failure. Insufficient memory.")
            return

        self.used_memory += memory_requirement

        # Case 2: Block is a perfect fit
        if block.size is memory_requirement:
            block.load(name)
            return

        # Case 3: Block is an imperfect fit
        # Resize existing block
        new_block_size = block.size - memory_requirement
        block.size = memory_requirement
        block.load(name)

        # Create and link new block
        new_block = Block(address+1, new_block_size)
        new_block.next = block.next
        block.next = new_block

    def free(self, block_index):
        pass

    def top(self):
        print("Using:", self.used_memory, "out of", self.total_memory)
        block = self.root
        while block is not None:
            print(block.starting_address, block.name, block.size)
            block = block.next


def main():
    memory = MemoryManager(64)
    memory.allocate("Init", 16)
    memory.allocate("Calculator", 2)
    memory.top()

if __name__ == "__main__":
    main()
