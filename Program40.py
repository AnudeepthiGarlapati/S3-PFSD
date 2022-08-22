class TrainTicket1:
    def details(self,name,id,tickets):
        self.name=name
        self.id=id
        self.tickets=tickets

class TrainTicket2:
    def selection(self,class):
        if(class==1)



t=TrainTicket2()
name=input("enter your name")
id=input("enter your id")
t.details(name,id,50)
class=input("enter the class")
t.selection(class)
