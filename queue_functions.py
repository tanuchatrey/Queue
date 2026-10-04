queue = []

# Insert element into queue
def enqueue():
    value = int(input("Enter element to insert: "))
    queue.append(value)
    print(value, "inserted into queue")


# Delete element from queue
def dequeue():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        value = queue.pop(0)
        print(value, "deleted from queue")


# Display queue
def display():
    if len(queue) == 0:
        print("Queue is empty")
    else:
        print("Queue:", queue)


# Main program
while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
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
        print("Program ended")
        break
    else:
        print("Invalid choice")
