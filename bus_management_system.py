class User:
    def __init__(self,username,password) -> None:
        self.username = username
        self.password = password

class Bus:
    def __init__(self,coach,driver,arrival,departure,from_des,to) -> None:
        self.coach = coach
        self.driver = driver
        self.arrival = arrival
        self.departure = departure
        self.from_des = from_des
        self.to = to
        self.seat = ['Empty' for i in range(20)]

class Ms_Delux:
    total_bus = 10
    total_bus_lst = []
    def install(self):
        bus_no = int(input('Enter Bus No : '))
        flag = 1
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                print('Bus already installed')
                flag = 0
                break
        if flag:
            bus_driver = input('Enter Bus Driver Name : ')
            bus_arrival = input('Enter Bus Arrival Time : ')
            bus_departure = input('Enter Bus Departure Time : ')
            bus_from =  input('Enter Bus Start From : ')
            bus_to = input('Enter Bus Destination To : ')
            self.new_bus = Bus(bus_no,bus_driver,bus_arrival,bus_departure,bus_from,bus_to)
            self.total_bus_lst.append(vars(self.new_bus))
            print('\n Bus installed successfully\n')

class BusCounter(Ms_Delux):
    user_lst = [] #user database
    bus_seat = 20
    def revervation(self):
        bus_no = int(input('Enter Bus Number : '))
        flag = 1
        for bus in self.total_bus_lst:
            if bus_no == bus['coach']:
                passenger = input('Enter Your Name : ')
                seat_no = int(input('Enter Your Seat Number : '))
                if seat_no - 1 > self.bus_seat:
                    print('Only 20 seats are available')
                elif bus['seat'][seat_no - 1] != 'Empty':
                    print('Seat Already Booked')
                else:
                    bus['seat'][seat_no - 1] = passenger
            else:
                flag = 0
                break
        if flag == 0:
            print('No Bus available')
    def showBusInfo(self):
        bus_no = int(input('Enter Bus No : '))
        for bus in self.total_bus_lst:
            if bus['coach'] == bus_no:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {'#'*10}")
                print(f"Bus Number : {bus_no} \t\t Driver : {bus['driver']}")
                print(f"Arrive : {bus['arrival']} \t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']} \t\t  To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}",end="\t")
                        a+=1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}",end="\t")
                        a+=1
                    print()
    def get_users(self):
        return self.user_lst
    def creat_account(self):
        name = input('Enter your name : ')
        flag = 0
        for user in self.get_users():
            if user.username == name:
                print('Username already Exists')
                flag = 1
                break
        if flag == 0:
            password = input('Enter your password : ')
            self.new_user = User(name,password)
            self.user_lst.append(vars(self.new_user))
            print('Account Creat Successfully')
    def available_buses(self):
        if len(self.total_bus_lst) == 0:
            print('No Bus Available')
        else:
            for bus in self.total_bus_lst:
                print('*'*50)
                print()
                print(f"{' '*10} {'#'*10} BUS INFO {bus['coach']}{'#'*10}")
                print(f"Bus Number : {bus['coach']}\t\t Driver : {bus['driver']}")
                print(f"Arrive : {bus['arrival']}\t\t Departure : {bus['departure']}")
                print(f"From : {bus['from_des']}\t\t  To : {bus['to']}")
                print()
                a = 1
                for i in range(5):
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}",end="\t")
                        a+=1
                    print("\t", end="")
                    for j in range(2):
                        print(f"{a}. {bus['seat'][a-1]}",end="\t")
                        a+=1
                    print()



while True:
    counter = BusCounter()
    print('1. Creat An Account\n2. Login To Your Account \n3. Exit')
    user_input = int(input('Enter Your Choice : '))
    if user_input == 3:
        break
    elif user_input == 1:
        counter.creat_account()
    elif user_input == 2:
        name = input('Enter Your Name : ')
        password = input('Enter Your Password : ')
        isAdmin = False
        flag = 0
        if name == 'Admin' and password == '12ab34':
            isAdmin = True
        if isAdmin == False:
            for user in counter.get_users():
                if user['username'] == name and user['password'] == password:
                    flag = 1
                    break
            if flag:
                while True:
                    print(f"1. Available Buses \n2. Show Bus Info \n3. Reservation \n4.EXIT")
                    a = int(input('Enter Your Choice : '))
                    if a == 4:
                        break
                    elif a == 1:
                        counter.available_buses()
                    elif a == 2:
                        counter.showBusInfo()
                    elif a == 3:
                        counter.revervation()
            else:
                print('Who are you?')
        else:
            while True:
                print(f"Hello Admin, welcome back")
                print(f"1. Install Bus \n2. Available Buses \n3. Show Bus \n4. Show User list \n5. EXIT")
                a = int(input('Enter Your Choice : '))
                if a == 5:
                    break
                elif a == 1:
                    counter.install()
                elif a == 2:
                    counter.available_buses()
                elif a == 3:
                    counter.showBusInfo()
                elif a == 4:
                    counter.get_users()





# company = Ms_Delux()
# company.install()

# b=BusCounter()
# b.install()
# b.install()
# b.revervation()
# b.showBusInfo()
# b.available_buses()
# b.creat_account()

# admin->Admin
# password->12ab34
