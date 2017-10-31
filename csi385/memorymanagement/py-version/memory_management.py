class Block:
    def __init__(self, starting_address, size, name="Empty"):
        self.starting_address = starting_address
        self.size = size
        self.name = name
        self.is_empty = True
        self.next = None
        self.id = None

    def load(self, name):
        self.name = name
        self.is_empty = False

    def unload(self):
        self.name = "Empty"
        self.is_empty = True

class MemoryManager:
    def __init__(self, total_memory):
        self.used_memory = 0
        self.total_memory = total_memory
        self.root = Block(0, total_memory)

    def allocate(self, name, memory_requirement):
        print("Allocating block of size", memory_requirement, "for", name)

        # Find first fit
        block = self.root
        current_address = 0
        while block is not None:
            if block.is_empty and block.size >= memory_requirement:
                break
            current_address += block.size
            block = block.next

        # Case 1: Failed to find block
        if block is None:
            print("Memory allocation failure. Insufficient memory.")
            return

        self.used_memory += memory_requirement
        block.load(name)

        # Case 2: Block is a perfect fit
        if block.size is memory_requirement:
            return

        # Case 3: Block is an imperfect fit
        # Resize existing block
        new_block_size = block.size - memory_requirement
        block.size = memory_requirement
        block.load(name)

        # Create and link new block
        new_block = Block(current_address + memory_requirement, new_block_size)
        new_block.next = block.next
        block.next = new_block

        self.__recalculate_block_ids__()

    def free(self, name_to_free):
        print("Freeing block with name", name_to_free)
        block = self.root
        previous_block = None
        while block is not None:
            if block.name is name_to_free:
                break
            previous_block = block
            block = block.next

        # Case 1: Failed to find block
        if block is None:
            print("Failed to free block. Block does not exist.")
            return

        self.used_memory -= block.size
        block.unload()

        # Case 2-A: Block has predecessor
        if previous_block is not None:
            if previous_block.is_empty:
                previous_block.next = block.next
                previous_block.size += block.size

        # Case 2-B: Block has successor
        next_block = block.next
        if next_block is not None:
            if next_block.is_empty:
                block.next = next_block.next
                block.size += next_block.size

        self.__recalculate_block_ids__()

    def top(self):
        print("Using:", self.used_memory, "out of", self.total_memory)
        block = self.root
        while block is not None:
            print(block.id, block.starting_address, block.name, block.size)
            block = block.next

    def __recalculate_block_ids__(self):
        current_id = 0
        block = self.root
        while block is not None:
            block.id = current_id
            current_id += 1
            block = block.next


def main():
    memory = MemoryManager(64)
    memory.allocate("Init", 16)
    memory.allocate("Foo", 2)
    memory.allocate("Baz", 4)
    memory.allocate("Yes", 1)
    memory.allocate("Stuff", 12)
    memory.top()
    memory.free("Baz")
    memory.free("Yes")
    memory.top()

if __name__ == "__main__":
    main()
