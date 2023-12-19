grocery_list = {} #made a dict to store data in.
while True:   #started a loop here
    try: 
        item = input().lower()  #got the input with everything in lower case.
        if item in grocery_list: #find a similar item already present in dict 
            grocery_list[item] += 1 #if we find anything similar just add 1 more to it than printing it agaim.
        else:
            grocery_list[item] = 1 # if didnt found the item in dict just keep it 1.
    except EOFError:  #closing the loop with ctrl + d
        for key in sorted(grocery_list.keys()): #sorting the keys data in the dict.
          print(grocery_list[key], key.upper()) #printing the amount of data and the data of dit with everything upper.
        break #breaking the loop to end the whole code.
