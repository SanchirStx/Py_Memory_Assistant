import json 

def Memory_Assistant():
    memory = {}
    print("Welcome to Memory Assistant!")
    while True:
        action = input("\nMemory assistant: [s] Store Memory, [r] Retrieve Memory, [d] Delete Memory, [v] View All Memories, [q] Quit\nChoose an option: ").strip().lower()
        if action == 'q':
            print("Exiting Memory Assistant.")
            break
        if action == 's':
            key = input("enter a key to story memory: ").strip()
            value = input("enter the memory to store: ").strip()
            memory[key] = value
            with open('memory.json', 'w') as f:
                json.dump(memory, f)
            print(f"Memory stored under key '{key}'.")
        elif action == 'r':
            if not memory:
                print("No memories stored.")
                continue
            key = input('Enter the key to retrieve memory: ').strip()
            value = memory.get(key)
            if value:
                print(f"Memory for '{key}': {value}")
            else:
                print(f"No memory found for key '{key}'.")
        elif action == 'd':
            if not memory:
                print("No memories to delete.")
                continue
            key = input("Enter the key to delete memory: ").strip()
            if key in memory:
                del memory[key]
                with open('memory.json', 'w') as f:
                    json.dump(memory, f)
                print(f"Memory for key '{key}' deleted.")
        elif action == 'v':
            if not memory:
                print("No memories stored.")
                continue
            elif memory:
                print("All Stored Memories:")
                for key, value in memory.items():
                    print(f"{key}: {value}")
        else:
            print("Invalid option. Please try again.")
            with open('memory.json', 'r') as f:
                memory = json.load(f)
Memory_Assistant()
            
