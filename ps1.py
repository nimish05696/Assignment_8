# getting input data
data = input("Enter binary data that has to be transmitted")
count = 0
for i in range(0, len(data)):   # starting of loop till the end of data
    if data[i] in '01':
        if data[i] in '1':
            count += 1
    else:
        print("Please enter a valid binary data")   # checking of boundary condition
        break
if (count % 2 == 0):    #checking for even parity bit
    print("Parity bit data:{0}".format(data + "1"))
    data2 = data.replace("010", "0100") #searching for 010 and replacing with 0100
    print("Transmitting data:{0}".format(data2 + "10101"))  #final transmitted data
else:
    print("Parity bit data:{0}".format(data + "0"))
    data2=data.replace("010","0100")
    print("Transmitting data:{0}".format(data2+"00101"))
