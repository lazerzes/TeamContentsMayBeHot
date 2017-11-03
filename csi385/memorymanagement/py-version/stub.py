from memorymanagement import MemoryManager

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
    memory.allocate("Everything", 128)
    memory.free("Everything")
    memory.allocate("Anything", 7)
    memory.top()

if __name__ == "__main__":
    main()
