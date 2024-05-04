task_list = []

def add(task):
	task_list.append(task)
	print(task ," task added sucessfully!")

def view():
	if task_list:
		print("Your tasks:")
		for index, task in enumerate(task_list, start=1):
			print(f"{index}. {task}")
	else:
		print("task folder is empty!")
def complete(c_index):
	if 1 <= c_index <= len(task_list):
		completed_task =  task_list.pop(c_index - 1)
		print("Task completed: " + completed_task)
	else:
		print("Invalid task index!")

def delete(d_index):
	if 1 <= d_index <= len(task_list):
		deleted_task =  task_list.pop(d_index - 1)
		print("Task deleted: " + deleted_task)
	else:
		print("Invalid task index!")

def main():
	while True:
		print("\n \t Enter your choice according to your requirement!")
		print("'1' For add task")
		print("'2' For view task")
		print("'3' For complete task")
		print("'4' For delete task")
		print("'5' For exit")
		choice = input("Enter your choice: ")
		if choice == "1":
			task = input("Enter your task: ")
			add(task)
		elif choice == "2":
			view()
		elif choice == "3":
			c_index = int(input("enter the task index to mar as complete: "))
			complete(c_index)
		elif choice == "4":
			d_index = int(input("enter the task index to delete: "))
			delete(d_index)
		elif choice == "5":
			print("Exit...")
			break
		else:
			print("Invalid choice. Try again please!")
if __name__ == "__main__":
	main()