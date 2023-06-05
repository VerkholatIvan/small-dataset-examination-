

# ---------------------------------------------------------------
# CREATING DICTIONARIES     （︶^︶）
# ---------------------------------------------------------------


# The main array to store dictionaries
arr = [{ "name": "James", "class": "FC01", "exam score": 75, "coursework score": 45 },
     { "name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85 },
     { "name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75 },
     { "name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55 },
     { "name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80 },
     { "name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75 }]


# ---------------------------------------------------------------
# DEF MAIN FUNCTIONS    \(￣︶￣*\))
# ---------------------------------------------------------------


# DEF FUNCTION AS AN "ARRAY.APPEND()"
def plus(array, item):
    return array + [item]


# DEF FILTERING FUNCTION 
def filter(key, value):
    f = []
    for i in range(len(arr)): ## Looking through every object list 
        for x in arr[i].keys(): ## Looking through the key names of dictionaries
            if x == key: 
                if arr[i][x] == value:
                    f = plus(f, arr[i])
    return f


# DEF AGGREGATE FUNCTION
def aggregate(x):
    g = []
    for i in range(len(arr)): ## Looking through every object list 
        g = plus(g, (arr[i][x])) 
    return sum(g)/len(g)


# DEF SORTING FUNCTION 
def sorting(x):
    arr_new = arr
    flag = True ## boolean object for stoping while loop
    while flag: ## until no changes, the while loop w'ont stop
        flag = False
        for idx in range(len(arr_new) - 1):
            if arr_new[idx+1][x] > arr_new[idx][x]: ## if next index is bigger >> switch positions
                arr_new[idx], arr_new[idx+1] = arr_new[idx+1], arr_new[idx]
                flag = True ## if something changed, then while loop continues
    return arr_new


# ---------------------------------------------------------------
# CREATING THE WHILE LOOP       ＼（〇_ｏ）／
# ---------------------------------------------------------------


# Interaction hints output
print("\n\nTo interact with database, you need to write down one the given command:\n")
print("\033[1mFILTER\033[0m filter keys by their names")
print("\033[1mAGGREGATE\033[0m find an average of the given database")
print("\033[1mSORTED\033[0m sort information by given key")
print("\033[1mEXIT\033[0m to stop a programm\n")

# A variable to stop the while loop
check = True 

while check:
    user = input(">> ")
    
    ## Filter function
    if user == "filter" or user == "Filter" or user == "FILTER" or user == '1':
        keyfilter = input("Choose keys to filter\n>> ") 
        print("By which", keyfilter, "you want to filter")
        valuefilter = input(">> ") 
        if valuefilter.isnumeric():
            valuefilter = int(valuefilter)

        ### filter output
        output_filter = filter(keyfilter, valuefilter)
        if len(output_filter) == 0:
            print('Error    There are no such values\n')
        else: print(*output_filter, sep='\n')
        print('\n')

    
# ------

    ## Aggregate function
    if user == 'aggregate' or user == 'Aggregate' or user == 'AGGREGATE' or user == '2':
        keygate = input('Enter key to aggregate\n>> ')
        

        ### No error found
        try:
            output_aggregate = aggregate(keygate)  

        ### aggregate output
            print(output_aggregate, '\nRounded -->', round(output_aggregate))
            print('\n')

        ### Error has been found
        except:
            print("Error    no integer was found\nTry again\n")

# ------   

    ## Sorting function
    if user == "sorted" or user == "Sorted" or user == "SORTED" or user == "3":
        keysort = input("Enter which key need to be sorted\n>> ")
        
        ### No error found
        try:
            output_sorting = (sorting(keysort))

            #### sorting output
            print(*output_sorting, sep='\n')
            print('\n')

        ### Error has been found
        except:
            print("Error    there is no such a key\nTry again\n")

# ------  

    ## Exit function
    if user == "exit" or user == "Exit" or user == "EXIT" or user == '4':
        check = False    