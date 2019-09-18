def game(player):   #function definition
    j=0
    lst = [0, 0, 0, 0, 0, 0, 0, 0, 0]   #defining a list
    while j<9:
        x,y=input("Enter the position and number").split()  #reading multiple inputs
        if int(x)==(1 or 3 or 5 or 7 or 9): #updating the value of list whenver the players enter a number
            lst[int(x)-1]=int(y)
        else:
            lst[int(x) - 1] = int(y)
        i=0
        while i<9:
            if (i%3==0):
                print()
            print(lst[i],end=" ")
            i+=1
        print()
        if player in "Player 1's chance":   #defining the chances of the players
            player="Player 2's chance"
            print(player)
        else:
            player="Player 1's chance"
            print(player)
        j += 1
    c_sum = [0, 0]  #finding the sum of columnn elements
    i = 0
    k = 0
    while i < 3:
        while k < 9:
            c_sum[i] = c_sum[i] + lst[k]
            k += 3
    print("column elemnts sum is:") #printing the sum of column elements
    i = 0
    while i < 3:
        print(c_sum[i])
    d_sum = [0, 0]  #finding the diagonal elements sum
    i = 0
    k = 0
    while i < 2:
        while k < 9:
            d_sum[i] = d_sum[i] + lst[k]
            k += 4
        i += 1
        print("Diagonal elemnts sum is:")   #printing of diagonal elements sum
        i = 0
    while i < 2:
        print(d_sum[i])
    r_sum = [0, 0, 0]   #finding row elemnts sum
    i = 0
    k = 0
    while i < 3:
        while k < 3:
            r_sum[i] = r_sum[i] + lst[k]
            k += 1
        i += 1
        print("Row elemnts sum is:")    #printing row elements sum
        i = 0
    while i < 3:
        print(r_sum[i])


print("Welcome to the game")
choice=input("Enter your choice of odd or even")    #asking the player to chose 
if choice=="odd":
    print("You are player 1")
else:
    print("You are player 2")
player="Player 1's chance"
print(player)
game(player)    #function calling

