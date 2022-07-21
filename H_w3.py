import statistics
"""
H.W 3
create by Alex Mircea
"""
#Privete  func for createData_set()
def createUser(name="UnName", age=0, sex="o", *others):
    """Create user info and return  to dataSet
    if have others run in loop & add  to user info"""
    user = {"name": name, "sex": sex, "age": age}
    if len(others) > 0:
        for dct in others:
            for k, v in dct.items():
                user[k] = v
    return user

def createData_set():
    """
    Create users with inputs from user
    If you have others details Not(id,name,sex,age) type name of data
    Click enter & Enter a value
    If Do not want type others type -1 to break
    input id for dataSet[key] &
    run on createUser() func ask input name,sex,age for user details
    after create user for dataSet ask if you wont create other user
    """
    dataSet = {}
    while (True):  # while for create new user in data_set
        breakPoint = 0
        others = {}
        while (int(breakPoint) != -1):  # while for others details
            data = input("If you wont other data. Enter name data (to Exit -1): ")
            if data == "-1":
                breakPoint = data
                if int(breakPoint) == -1:
                    break
            value = input("Enter value: ")
            others[data] = value

        id = input("Enter your id: ")
        if len(others) > 0:
            dataSet[id] = createUser(input("Enter a name: "), input("Enter a sex: "), input("Enter a age: "), others)
        else:
            dataSet[id] = createUser(input("Enter a name: "), input("Enter a sex: "), input("Enter a age: "))
        if input("You wont to create more user(Y,N)?").upper() == "N":
            return dataSet

def split_male_female(data):
    """
    The function split dictionary by sex Male or Female
    :param data: dictionary
    :return: res , male and female dictionaries with keys Male&Female
    """
    data_set_m = {}
    data_set_f = {}

    for key, value in data.items():
            for k, v in value.items():
                 if k == "sex" and v.lower().startswith("m"):
                     data_set_m[key] = value
                 if k == "sex" and v.lower().startswith("f"):
                     data_set_f[key] = value

    #print(data_set_m, "\n", data_set_f)#for test
    res = {"Male": data_set_m, "Female": data_set_f}
    return res


def find_median_average(data):
    """
     Calculate Average age and Median age for data
    :param data: dictionary
    :return: res, Average & median dictionaries with keys Average&median
    """
    avg = 0
    lst = []

    for key, value in data.items():
        for k , v in value.items():
            if k.lower() == "age":
                avg += v
                lst.append(v)

    lst.sort()
    avg /= len(data)
    median = statistics.median(lst)
    res = {"Average": round(avg, 3), "median" : median}
    return res

def print_values_above(data: dict,Pnum = 0):
    """
     print from dictionary all
     Prints all the values from dictionary whose age is above the number entered,
     if the user did not enter a number prints all the values
    :param data: dictionary, Pnum: positive num
    :return: res, Average & median dictionaries with keys Average&median
    """
    if Pnum > 0:
        for key, value in data.items():
            for k , v in value.items():
                if k.lower() == "age" and v > Pnum:
                    print(key, value)
    else:
        for key, value in data.items():
            print(key, value)


def main():
    # For check createData_set() func
    #data_set = createData_set()
    data_set = {1234234: {"name": "Tal", "sex": "male", "age": 22},
                2432442: {"name": "Shay", "sex": "female", "age": 33},
                3765765: {"name": "Tamir", "sex": "male", "age": 45},
                4765756: {"name": "Daniel", "sex": "female", "age": 36},
                5574747: {"name": "Alex", "sex": "male", "age": 67, "job:": "QA automation"},
                7757445: {"name": "2pac", "sex": "male", "age": 120,"Alive or dead": "Alive"},
                6213213: {"name": "Tali", "sex": "female", "age": 98}
                }
    # For check split_male_female() func
    print("Func split_male_female():")
    dictMaleFemale = split_male_female(data_set)
    for k,v in dictMaleFemale.items():
        print(k)
        for x,y in v.items():
            print(x,y)

    # For check find_median_average()
    print("\nFunc find_median_average():")
    dictMedianAvg = find_median_average(data_set)
    print(dictMedianAvg)

    # For check print_values_above()
    print("\nFunc print_values_above(data_set):")
    print_values_above(data_set)
    print("\nFunc print_values_above(data_set,num):")
    print_values_above(data_set, 44)




main()


