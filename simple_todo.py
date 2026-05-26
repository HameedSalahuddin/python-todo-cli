import os
tasks = []
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')        
clear_screen()
print('='*30)
print('TO-DO'.center(30))
print('='*30)
print('MENU')
print('view  -> view tasks')
print('add   ->  add tasks')
print('delete-> remove tasks')
print('exit  -> exit app')
def save_file():
    file = open('task.txt','w')
    for i in tasks:
        file.write(i)
        file.write('\n')

    file.close()
def read_file():
    file = open('task.txt','r')
    lst = file.readlines()
    for i in lst:
        tasks.append(i.strip())

'''when the code stops and is run again the task list will be empty 
   so we use the read_file() funtion to read the tasks uploaded into the 
   textfile and add it back into the tasks[] list so the tasks added before
    will be present in it'''
read_file()
while True:
    opt = input('>> ').lower()
    if opt == 'view':
        for num , item in enumerate(tasks,start=1):

            print(num,'.',item)
        done = input('have you done any tasks [y/n] :')
        if done == 'y':
            n = int(input('enter the task which is done : '))
            tasks[n-1]= tasks[n-1]+''+'[DONE]'
            save_file()
            print('GOOD JOB!!!!')


        else:
            continue
        

            
    elif opt == 'add':
        new = input('enter new task :')
        tasks.append(new)
        save_file()

    elif opt=='delete':
        for i,item in enumerate(tasks,start=1):

            print(i,'.',item)
        delete = int(input('enter the task that you want to delete :'))
        tasks.pop(delete-1)
        save_file()
        print('successfully deleted')
    else:
        break 
