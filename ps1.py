data = input("Enter binary data that has to be transmitted")
count = 0
for i in range(0, len(data)):
    if data[i] in '01':
        if data[i] in '1':
            count += 1
    else:
        print("Please enter a valid binary data")
        break
