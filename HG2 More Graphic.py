import random
import tkinter



'''with open('HiGuys.xls',"r") as file:
    HG = file.read()
print(HG.row[0]) '''

topping = ['Pearls','Coconut','Pudding','Red Bean', 'Sago', 'Cheese Cream Crown', 'Default']
sugarlevel = [0,25,50,75,100]
icelevel = ['Regular','Less','No','Hot'] 
size = ['Regular', 'Large']

fruit_tea= ["Guys Red Grapefruit","Watermelon Juice", "Guys Lemon", "Mango Lactobacollus Drink", "Lemon Vitamin C", "Honey Grapfruit Tea", "Grapefruit Yakult" ]
special_sand_ice = ["Little Universe","Fall in Love","Summer Suba Diving","Dream Chaser", "Pink Lady"]
cream_crown = ["Red Garden", "Green Tea", "Oolong", "Seasons", "Guys Cheese Mango", "Cranberry", "Coco Oreo", "Peach Monster", "Sago Berry"]
special = ["First Snow", "Night Life", "Misty Forest", "Green Fairy", "Night Elves"]
bubble_tea = ["Bubble Tea", "Green Milk Tea", "Coconut Milk Tea", "Red Bean Milk Tea","Pudding Milk Tea","Mango Coconut Dew", "Sago Coconut Milk"]

menu = []

#def random(a):
#    print(len(a))
def should_I_have_bubble_tea():
    #for i in range
    random_num = random.randint(1,101)
    if random_num>90:
        print("Yes")
    else:
        print("No")
    

def drinks():
    
    file = open("drinks_menu.txt", "r")
    menu = [] #empty list to input what in file
    x=0
    for line in file:
        #print(line)
        menu.append(line.strip())
        x+=1    
    file.close()
    #print(x)
    #print(menu)
    random_num = random.randint(0,len(menu)-1)
    if random_num > len(menu): print("Drinks:", menu[random_num])
    else: print("Drinks:", menu[random_num])
    

def topping_choice():
    ind = len(topping)
    random_num = random.randint(0,len(topping))
    #print(random_num)
    if random_num != ind: print('Extra Topping:',topping[random_num])
    elif random_num == ind : print('Topping:',topping[random_num-1])
    else: print('Extra Topping:',topping[random_num])
    
def sugar_level():
    ind = len(sugarlevel)
    random_num = random.randint(0,ind)
    #print(random_num)
    if random_num == ind:      
        print('Sugar Level:',sugarlevel[random_num -1],'%')
    else:
        print('Sugar Level:',sugarlevel[random_num],'%')

def ice_level():
    ind = len(icelevel)
    random_num = random.randint(0,len(icelevel))
    #print(random_num)
    if random_num == ind:
        
        print('Ice Level:',icelevel[random_num-1])
    else:
        print('Ice Level:',icelevel[random_num])
    
def drink_size():
    ind = len(size)
    random_num = random.randint(0,len(size))
    #print(random_num)
    if random_num == ind:
        print('Size:',size[random_num-1])
    #elif:print()
    else:
        print('Size:',size[random_num])


'''
print('Topping',len(topping))
print('Sugar',len(sugarlevel))
print('Ice',len(icelevel))
print('Size', len(size))'''

print(should_I_have_bubble_tea())
drinks()
drink_size()
sugar_level()
ice_level()
topping_choice()


#random(topping)
#random(size)
