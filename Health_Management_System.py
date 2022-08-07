"""
    Manages Diet and Exercises for clients
        3 clients:  Harry, Rohan and Hammad
"""

def getdate():
    import datetime
    return datetime.datetime.now()

clientnumber = int(input("Enter the client number: press 1 for Harry, 2 for Rohan, 3 for Hammad \n"))
log = int(input("Press 1 to log exercise or press 2 to log diet:\n"))
clientname = {1: "Harry", 2: "Rohan", 3: "Hammad"}
log_for = {1: "Exercise", 2: "Diet"}

clientlog = {1: {1: "Harry_Exercise.txt",
                 2: "Harry_Diet.txt"},
             2: {1: "Rohan_Exercise.txt",
                 2: "Rohan_Diet.txt"},
             3: {1: "Hammad_Exercise.txt",
                 2: "Hammad_Diet.txt"}
             }

if clientnumber in [1, 2, 3]:
    while True:
        try:
            with open(clientlog[clientnumber][log], "a") as f:
                try:
                    inp = input("Enter "+clientname[clientnumber]+"'s"+" "+ log_for[log]+ "\n")
                    f.write("[{}]\t".format(getdate()))
                    f.write(inp+"\n")
                    inp1 = int(input("Press 1 to add more Exercise / Diet or Press 0 to exit\n"))
                    if inp1 == 0:
                        break
                    elif inp1 == 1:
                        pass
                    else:
                        print("choose from given option")
                except Exception as e:
                    print("Please put number\n")
                    inp1 = int(input("Press 1 to add more Exercise / Diet or Press 0 to exit\n"))
                    pass
        except Exception as e:
            print(e)
            print("creating file {}".format(clientlog[clientnumber][log]))
            with open(clientlog[clientnumber][log], "w") as f:
                pass
else:
    print("client is not registered")
