#Has four options, add to file, view the text file, sort the text file or exit program.

loopOn = True

while loopOn == True:

    choice = input("Insert / View / Sort / Exit\n")

    if choice == "Insert" or choice == "insert":
        x = 0
        while (x != '1'):
            x = input("Press any button to continue, 1 to end\n")
            if x == '1':
                continue
            with open('write.txt','a+') as file:
                number = input("Insert your number here:")
                file.write(number + "\n")

    if choice == "view" or choice == "View":
        with open('write.txt','r') as file:
            content = file.read()
            print(content.strip())

    if choice =="sort" or choice == "Sort":

        with open('write.txt','r') as file:
            new = []
            mylist = file.readlines()
            for line in mylist:
                stripped = line.strip()
                new.append(stripped)

            new.sort()
            print(new)

        with open ("write.txt","w") as file:
            for k in new:
                file.write(k + "\n")

    if choice == "Exit" or choice == "exit":
        loopOn = False
