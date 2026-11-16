todo_list =[]

def show_menu():
    print("\n--- TODO LIST ---")
    print("1.Task dikhayein")
    print("2.Task add karna")
    print("3.Task delete karna")
    print("4.task total price")
    print("5.Exit")

while True:
    show_menu()
    choice =input("Apna choice dijiye (1/2/3/4):")

    if choice =='1':
        if not todo_list:
            print("list khaali hai.")
        else:
            print("\nApna To-DO list:")
            for i,task in enumerate(todo_list,start=1):
                print(f"{i}.{task}")
    elif  choice =='2':
             task =input("kya kaam add karna chahte hain?")
             todo_list.append(task)
             print("task add ho gya.")
    elif choice =='3':
         if not todo_list:
              print("kuch del nahi karna.")
         else:
               for i,task in enumerate(todo_list,start=1):
                print(f"{i}.{task}")
         try:
                task_num = int(input("Kaunsa task delete karna chahte hain (number likhein): "))
                if 1 <= task_num <= len(todo_list):
                    removed = todo_list.pop(task_num - 1)
                    print(f"Task '{removed}' delete ho gaya.")
                else:
                    print("Galat number.")
         except ValueError:
                print("Sirf number likhein.")
    elif  choice =='4':
         total= sum(task['price']for task in todo_list)
         print(f"Total price: RS.{total:.2f}")          

    elif choice =='5':
         print("shukariya!list band ho gai.")

    else:
         print("try again.")          
              
                            