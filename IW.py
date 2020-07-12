class Student():


    def __init__(self, name, address, email,ContactNO,stu_id, balance):
        self.stu_id= stu_id
        self.name = name
        self.address = address
        self.email = email
        self.ContactNo= ContactNO


    def get_info(self):
        import random
        self.stu_id= random.randint(1,100)
        balance = x.balance
        try:
            YourName= input("Enter Your name:")
            Address= input("Enter Your Address:")
            Email= input("Enter Your Email Address:")

            ContactNO = int(input("Enter your ContactNumber:"))

        except:
            print ("Please enter valid contact number. ")

        stu = Student(YourName,Address,Email,ContactNO,self.stu_id,balance)

        ls.append(stu)
        return ls


    def display_info(self,stu):
        print("Your Student Id:", self.stu_id)
        print("name:",stu.name)
        print("Address:", stu.address)
        print("Email:", stu.email)
        print("Your contact number is:", stu.ContactNo)


    def search_info(self,rn):
        for i in range(ls.__len__()):
            for i in range(ls.__len__()):
                if (ls[i].name == rn):
                    return i

    def update(self, rn):
        i = y.search_info(rn)
        secondInstallment = 20000
        amt = int(input("enter the amount you wanna deposit: "))
        if x.balance == 20000:
            print(''' Sorry, we donot accept this amount. You have already cleared your balance.''')
        elif amt == 10000:
            x.balance = secondInstallment
            print(" You have deposited your second installment")
        else:
            print(" Insufficient amount")


    def delete_info(self,rn):
        i= y.search_info(rn)
        del ls[i]


class ProgramDetails():
    def __init__(self, balance,yourChoice):
        self.balance = balance
        print(''' Welcome to Insight Workshop Academy. Input your choices.1. Course of study 
                      2. Registration
                      3. To search your info
                      4. to delete your info''')
        self.yourChoice = yourChoice

    def home(self):
        print('''Now you can see update delete and check your balance:
              3. search your info . "
              4. to delete and leave the workshop"
              5. to check your balance"
              6. to pay your second installment''')



    def CourseOfStudy(self):
        print(
            ''' The available courses for now are:
            1. Python
            2. Javascript
            3.Django'''
            )

    def paymentplan(self):
        self.balance = int(input("Enter the amount you want to deposit:"))

        if self.balance == 20000:
                print(" Hurray, You have cleared your balance"
                  " the amount will be refunded at the end of your course")
        elif self.balance == 10000:
                print("You have sucessfully deposited your first installment")


        elif self.balance != 20000 or 10000:
            print(''' Sorry, the amount you are trying to deposit is not as per our payment option. 
             Our payment options are
             1. Either pay 10k 10k for 2 installment 
                2. Pay 20000 to clear your balance ''')
            exit()

        else:
             self.balance = 0
             print(" The amount to deposit must be equals to Rs 20000 or Rs 10000 ")

    def checkbalance(self):
        print(f'Your current balance is: {self.balance}')



x=ProgramDetails(0,yourChoice=0)
try:
    choice = int(input("Enter your choice : "))
except NameError:
    print("That's not the valid Choice")
except ValueError:
    print ("That is not the valid choice.")

ls=[]
y = Student("","","",0,0,0)


while True:

    try:
        if choice == 1:


            x.CourseOfStudy()
            choice = int(input("Enter 2 to register for course : "))

            continue

        elif choice == 2 :
            y.get_info()
            x.paymentplan()
            print(" You have successfully registered")
            print(" Here is your details.")
            for i in range(ls.__len__()):
                y.display_info(ls[i])
                x.checkbalance()
                x.home()
                choice = int(input("Enter your choice : "))
                continue
            continue
        elif choice == 3:
            try:
                rn = input("Enter your name you wanna search for : ")
                s = y.search_info(rn)
                y.display_info(ls[s])
                x.checkbalance()
            except:
                print(f"{rn} has not registered.")
            break
        elif choice == 4:
            try:
             r = input("Enter Your name to delete your info and leave workshop : ")
             y.delete_info(r)
             print(ls.__len__())

             print("List after deletion")
             for i in range(ls.__len__()):
              y.display_info(ls[i])
            except:
                print(f"{r} has not registered.")

            exit()
        elif choice == 5:
            x.checkbalance()
            break
        elif choice == 6:
            rn = input("What is your name? : ")
            y.update(rn)
            print(ls.__len__())
            print("Thank You. Here is your details.")
            for i in range(ls.__len__()):
                y.display_info(ls[i])
                x.checkbalance()
        else:
            print(" Invalid Input")
        break
    except NameError:
        print("Somthing went wrong...")
        break




















        
