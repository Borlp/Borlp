import random #importing random
import time #importing time
from random import randint #importing randint for percents
import os #importing os for clear command
clear = lambda: os.system('cls') #clear command (only for windows)
def main(): #main function
    name1 = input("Input first name : ") #first person name
    name2 = input("Input second name : ") #second person name
    time.sleep(0.51) #just waiting a little bit
    print(f"Calculating love status between {name1} and {name2}...") #printing first and second name
    time.sleep(1) #just waiting a little bit
    percent = random.randint(0, 100) #random 0 to 100% chance
    input(f"The love power between {name1} and {name2} is : {percent}%") #printing first and second name and percent
    input() #input
    clear() #clearing the console
    main() #return
main()#start main() when you open a file.

