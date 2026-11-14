queue = []

# Insert element into queue
def enqueue():
    element = int(input("Enter the element: "))
    queue.append(element)
    print(element, "inserted into queue")

# Delete element from queue
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        element = queue.pop(0)
        print(element, "deleted from queue")

# Display queue
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue elements:", queue)


# Main program
while True:
    print("\n--- QUEUE OPERATIONS ---")
    print("1. Enqueue (Insert)")
    print("2. Dequeue (Delete)")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        display()

    elif choice == 4:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
