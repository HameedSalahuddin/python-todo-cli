tasks = []
print('MENU')
print('1.view tasks')
print('2.add tasks')
print('3.remove tasks')
print('4.exit')
while True:
    opt = input('enter operation :')
    if opt == '1':
        for num , item in enumerate(tasks,start=1):

            print(num,'.',item)

            
    elif opt == '2':
        new = input('enter new task :')
        tasks.append(new)

    elif opt=='3':
        for i in tasks:
            print(i)
        item = input('enter the task that you want to delete :')
        x = tasks.index(item)
        tasks.pop(x)
        print('successfully deleted')
    else:
        break

