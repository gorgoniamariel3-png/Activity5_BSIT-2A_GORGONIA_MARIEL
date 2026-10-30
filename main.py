from stack import ArrayStack, LinkedStack
from queue import ArrayQueue, LinkedQueue

def main():
    array_stack = ArrayStack(3)
    linked_stack = LinkedStack()
    array_queue = ArrayQueue(3)
    linked_queue = LinkedQueue()

    while True:
       
        print("   LABORATORY ACTIVITY 5.0: STACKS & QUEUES")
        print("\n\n1. Test ArrayStack (Fixed Capacity: 3)")
        print("2. Test LinkedStack (Dynamic)")
        print("3. Test ArrayQueue (Circular, Capacity: 3)")
        print("4. Test LinkedQueue (Dynamic with Tail)")
        print("5. Run Application: Balanced Parentheses")
        print("6. Run Application: Print Queue Simulation")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            sub_menu_stack(array_stack, "ArrayStack")
        elif choice == '2':
            sub_menu_stack(linked_stack, "LinkedStack")
        elif choice == '3':
            sub_menu_queue(array_queue, "ArrayQueue")
        elif choice == '4':
            sub_menu_queue(linked_queue, "LinkedQueue")
        elif choice == '5':
            check_balanced_parentheses()
        elif choice == '6':
            simulate_print_queue()
        elif choice == '7':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 7.")

def sub_menu_stack(stack_obj, name):
    while True:
        print(f"\n--- {name} Menu ---")
        print(f"Current State: {stack_obj}")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Back to Main Menu")
        
        sub_choice = input("Enter choice (1-4): ").strip()
        try:
            if sub_choice == '1':
                val = input("Enter value to push: ")
                stack_obj.push(val)
                print(f"Pushed '{val}' successfully.")
            elif sub_choice == '2':
                val = stack_obj.pop()
                print(f"Popped value: {val}")
            elif sub_choice == '3':
                val = stack_obj.peek()
                print(f"Top value (Peek): {val}")
            elif sub_choice == '4':
                break
            else:
                print("Invalid choice.")
        except (OverflowError, IndexError) as e:
            print(f"[ERROR CAUGHT]: {e}")

def sub_menu_queue(queue_obj, name):
    while True:
        print(f"\n--- {name} Menu ---")
        print(f"Current State: {queue_obj}")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek Front")
        print("4. Back to Main Menu")
        
        sub_choice = input("Enter choice (1-4): ").strip()
        try:
            if sub_choice == '1':
                val = input("Enter value to enqueue: ")
                queue_obj.enqueue(val)
                print(f"Enqueued '{val}' successfully.")
            elif sub_choice == '2':
                val = queue_obj.dequeue()
                print(f"Dequeued value: {val}")
            elif sub_choice == '3':
                val = queue_obj.peek_front()
                print(f"Front value (Peek): {val}")
            elif sub_choice == '4':
                break
            else:
                print("Invalid choice.")
        except (OverflowError, IndexError) as e:
            print(f"[ERROR CAUGHT]: {e}")


def check_balanced_parentheses():
    expression = input("Enter an expression with parentheses `()[]{}`: ").strip()
    stack = LinkedStack()
    matching_bracket = {')': '(', ']': '[', '}': '{'}
    
    balanced = True
    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                balanced = False
                break
            top_elem = stack.pop()
            if top_elem != matching_bracket[char]:
                balanced = False
                break
                
    if balanced and stack.is_empty():
        print(f"Result: The expression '{expression}' is **BALANCED**.")
    else:
        print(f"Result: The expression '{expression}' is **NOT BALANCED**.")



class PrintJob:
    def __init__(self, job_id, page_count):
        self.job_id = job_id
        self.page_count = page_count

    def __str__(self):
        return f"[Job ID: {self.job_id}, Pages: {self.page_count}]"


def simulate_print_queue():
    print("\n--- Application 2: Print Queue Simulation ---")
    q = LinkedQueue()
    q.enqueue(PrintJob("JOB-001", 4))
    q.enqueue(PrintJob("JOB-002", 12))
    q.enqueue(PrintJob("JOB-003", 2))
    
    print("Initial Print Queue State:")
    print(q)
    
    while not q.is_empty():
        input("\nPress [Enter] to process next print job...")
        job = q.dequeue()
        print(f"-> Printing {job}...")
        print("Remaining Queue:")
        print(q)
    print("\nAll print jobs completed successfully!")


if __name__ == "__main__":
    main()
