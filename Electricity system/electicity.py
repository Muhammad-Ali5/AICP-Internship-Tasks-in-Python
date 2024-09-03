import numpy as np

class Electricity:
    def __init__(self, id):
        self.id = id
        print(f"My sudent ID is { self.id}")
        matrix=[[55,65,75],[120,150,170],[210,230,240]]
        # print(matrix)
    def costSlab1(self):
        # self.result = [55*10 , 65*10 , 75*10]
        matrix = np.array([[55 , 65 , 75],[120,150,170],[210,230,240]])
        multiplier = 10
        matrix[0, :] *=multiplier
        print(f"Bill for Slab 1 is \n {matrix[0]}")

    def costSlab2(self):
        matrix = np.array([[55,65,75],[120,150,170],[210,230,240]])
        multiplier = 15
        matrix[1, :] *=multiplier
        print(f"Bill for Slab 2 is \n {matrix[1]}")
    def costSlab3(self):
        matrix = np.array([[55,65,75],[120,150,170],[210,230,240]])
        multiplier = 20
        matrix[2, :] *=multiplier
        print(f"Bill for Slab 1 is \n {matrix[2]}")


print("  WELCOME TO WABDA BILLING SYSTEM  ")
print('====================================')
std = Electricity("XY12345678")
while True:
    print("Press 1 to display the bill of slab 1 and slab 2")
    print("Press 2 to display the bill of slab 3 ")
    print("Press any other key to exit...")
    print('====================================')
    choice=int(input("Enter Your choice..."))
    print('====================================')
    if choice==1:
        std.costSlab1()
        std.costSlab2()
    elif choice==2:
        std.costSlab3()
    else:
        print("you exit the program...")
        break
