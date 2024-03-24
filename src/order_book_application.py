class Task:
    id = 0

    def __init__(self, description: str, programmer: str, workload: int) -> None:
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False

    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True

    def __str__(self) -> str:
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'NOT ' if not self.is_finished() else ''}FINISHED"
    

class OrderBook:
    def __init__(self) -> None:
        self.__orders = []

    def add_order(self, description: str, programmer: str, workload: int):
        self.__orders.append(Task(description, programmer, workload))

    def all___orders(self):
        return self.__orders
    
    def programmers(self):
        arr = []

        for order in self.__orders:
            arr.append(order.programmer)

        return list(set(arr))
    
    def mark_finished(self, id: int):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError('id not found')
    
    def finished___orders(self):
        return [order for order in self.__orders if order.is_finished()]
    
    def unfinished___orders(self):
        return [order for order in self.__orders if not order.is_finished()]
    
    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError
        
        finished_count = len([order for order in self.finished___orders() if order.programmer == programmer])
        unfinished_count = len([order for order in self.unfinished___orders() if order.programmer == programmer])

        finished_hour_total = sum([order.workload for order in self.finished___orders() if order.programmer == programmer])
        unfinished_hour_total = sum([order.workload for order in self.unfinished___orders() if order.programmer == programmer])

        return (finished_count, unfinished_count, finished_hour_total, unfinished_hour_total)
    

class OrderApplication:
    def __init__(self) -> None:
        self.__order_book = OrderBook()

    def __help(self):
        print('commands:')
        print('0 exit')
        print('1 add order')
        print('2 list finished tasks')
        print('3 list unfinished tasks')
        print('4 mark task as finished')
        print('5 programmers')
        print('6 status of programmer')

    def __add_order(self):
        desc = input('description: ')
        programmer_and_workload = input('programmer and workload estimate: ')
        programmer_and_workload = programmer_and_workload.split()
        programmer = programmer_and_workload[0]
        workload = int(programmer_and_workload[1])

        self.__order_book.add_order(desc, programmer, workload)
        print('added!')

    def __list_finished_tasks(self):
        tasks = self.__order_book.finished___orders()

        if len(tasks) == 0:
            print('no finished tasks')
            return
        
        for task in tasks:
            print(task)

    def __list_unfinished_tasks(self):
        tasks = self.__order_book.unfinished___orders()

        if len(tasks) == 0:
            print('no unfinished tasks')
            return
        
        for task in tasks:
            print(task)

    def __mark_task(self):
        id = int(input('id: '))
        self.__order_book.mark_finished(id)

        print('marked as finished')

    def __get_programmers(self):
        programmers = self.__order_book.programmers()
        for programmer in programmers:
            print(programmer)

    def __get_programmer_detail(self):
        programmer = input('programmer: ')
        details = self.__order_book.status_of_programmer(programmer)
        (finished, not_finished, finish_hour, non_finish_hour) = details

        print(f'tasks: finished {finished} not finished {not_finished}, hours: done {finish_hour} scheduled {non_finish_hour}')

    def execute(self):
        self.__help()

        while True:
            print()
            try:
                cmd = input('command: ')

                if cmd == '0':
                    break
                elif cmd == '1':
                    self.__add_order()
                elif cmd == '2':
                    self.__list_finished_tasks()
                elif cmd == '3':
                    self.__list_unfinished_tasks()
                elif cmd == '4':
                    self.__mark_task()
                elif cmd == '5':
                    self.__get_programmers()
                elif cmd == '6':
                    self.__get_programmer_detail()
            except:
                print('erroneous input')


OrderApplication().execute()