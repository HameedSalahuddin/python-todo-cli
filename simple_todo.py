tasks = []
print('MENU')
print('1.view tasks')
print('2.add tasks')
print('3.remove tasks')
print('4.exit')
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
    opt = input('enter operation :')
    if opt == '1':
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
        

            
    elif opt == '2':
        new = input('enter new task :')
        tasks.append(new)
        save_file()

    elif opt=='3':
        for i,item in enumerate(tasks,start=1):

            print(i,'.',item)
        delete = int(input('enter the task that you want to delete :'))
        tasks.pop(delete-1)
        save_file()
        print('successfully deleted')
    else:
        break 
