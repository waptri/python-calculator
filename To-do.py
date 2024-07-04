# Adding tasks
task = []

def add_task(task_description):
   task = {
      'id': len(tasks) + 1,
      'description': task_description,
      'completed': False 
   } 
   tasks.append(task)
   print(f"task added: {task_description}")
   
   # adding viewing task
   
   def view_tasks():
       for task in tasks:
           status = "Tick" if task['completed'] else"wrong"
           print(f"{task['id']}. {task['description']} [{status}]")
         
 # Marking Tasks as Complete 
  
def mark_task_complete(task_id):
      for task in tasks:
          if task['id'] == task_id:
              task['completed'] = True
              print(f"task {task_id} marked as complete.")
              break
          else:
               print(f"task {task_id} not found.")
          
 # Deleting tasks
 
def delete_task(task_id):
     global tasks
     tasks = [task for task in tasks if task['id'] != task_id]
     print(f"task {task_id} deleted.")
     
 
 # user interface for simple interaction with the user
 
def main():
     while True:
         print("\n1. add task")
         print("2. view task")
         print("3. complete task")
         print("4. delete task")
         print("5. exit") 
         choice = input("Enter your choice: ")
         
         if choice == '1':
             task_description = input("Enter task descrition")
             add_task(task_description)
         elif choice == '2':   
           view_task()
         elif choice == '3':
            task_id = int(input("Enter task ID to complete. "))
         elif choice == '4':
             task_id = int(input("Enter task ID to delete. ")) 
             delete_task(task_id)
         elif choice == '5':
             print("Goodbye!")
             break
         else:
             print("invalid choice please try again. ")
     if __name__ == "__main__":
         main()        
          
         
            
     
              
          
                  
   