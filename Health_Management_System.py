"""
    Manages Diet and Exercises for clients
        3 clients:  Harry, Rohan and Hammad
"""

def getdate():
    import datetime
    return datetime.datetime.now()
def retrieve():
    """
        It will retrieve the data of client for exercise and diet
    """
    try:
        with open(clientlog[clientnumber][logdata]) as f:
            for i in f:
                print(i, end="")
    except Exception as e:
        print("there are no data as such")
def log():
    if clientnumber in [1, 2, 3]:
        while True:
            try:
                with open(clientlog[clientnumber][logdata], "a") as f:
                    try:
                        inp = input("Enter " + clientname[clientnumber] + "'s" + " " + log_for[logdata] + "\n")
                        f.write("[{}]\t".format(getdate()))
                        f.write(inp + "\n")
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
                print("creating file {}".format(clientlog[clientnumber][logdata]))
                with open(clientlog[clientnumber][logdata], "w") as f:
                    pass
    else:
        print("client is not registered")

while True:
    try:
        log_retrieve = int(input("Press 1 to log or 2 for retrieve "))
        clientnumber = int(input("Enter the client number: press 1 for Harry, 2 for Rohan, 3 for Hammad \n"))
        logdata = int(input("Press 1 for exercise or press 2 for diet:\n"))
        clientname = {1: "Harry", 2: "Rohan", 3: "Hammad"}
        log_for = {1: "Exercise", 2: "Diet"}
        clientlog = {1: {1: clientname[1]+"_Exercise.txt",
                         2: clientname[1]+"_Diet.txt"},
                     2: {1: clientname[2]+"_Exercise.txt",
                         2: clientname[2]+"_Diet.txt"},
                     3: {1: clientname[3]+"_Exercise.txt",
                         2: clientname[3]+"_Diet.txt"}
                     }
        if log_retrieve == 1:
            log()
            break
        else:
            retrieve()
            break

    except Exception:
        print("Please enter number")
        in2 = int(input("Press 1 to continue or 0 to exist"))
        if in2 == 0:
            break
        else:
            pass