def func1():
    try:
        result=int(input("Please provide number: "))
    except:
        print ("Wrong input")
    finally:
        print ("end")

func1()

def func2():
    while True:
        try:
            n=int(input("Enter a number"))
        except:
            print ("Wrong input! Enter again \n")
            continue
        else:
            break
    print("Your number squared is : ")
    print(n**2)

func2()