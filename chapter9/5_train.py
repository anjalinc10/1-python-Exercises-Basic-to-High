class Train():
    railway='Indian Railway'

    def __init__(self,name,fare,seat=10):
        self.name=name
        self.fare=fare
        self.seat=seat

    def GetStatus(self):
        print(f'The name of the train is {self.name}')
        print(f'The available seats are: {self.seat}')
        print(f'The price of ticket is: {self.fare}')
        print("*************************************")

    def BookTicket(self):
        if(self.seat>0):
            print(f'your ticket has been booked! your seat is {self.seat}')
            self.seat = self.seat - 1
        else:
            print(f'sorry this train is full!kindly try to tatkal')

    def ToGetFare(self):
        print(f'The price of ticket is: {self.fare}')

    def ToCancel(self):
        self.seat = self.seat + 1
        print(f'cancel the Ticket: {self.seat}')
 
travel_train = Train("Rajadhani Express",500,10)
travel_train.GetStatus()
travel_train.BookTicket()
travel_train.GetStatus()
travel_train.ToCancel()
travel_train.GetStatus()




