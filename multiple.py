def func():

    for x in range(1, 101):

        if x % 15 == 0:
            print("ThreeFive")

        elif x % 3 == 0:
            print("Three")

        elif x % 5 == 0:
            print("Five")

        else:
            print(x)

if __name__ == "__main__":
    func()