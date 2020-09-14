def say_hello():
    return "Hello!"

#say_hello()

def confuse():
    print ("bears")
    return 42

#confuse()

def more_confused():
    2 + 2
#print(more_confused())

def start_K(string):
    if string[0] == "K":
        return True
    else:
        return False
#print(start_K("Abe"))


#this function checks to see if the word assigned to the long variable starts with the word assigned
    #to the long variable by running a for loop with an if statement that checks if each index position of "short"
        #is equal to the same as the corresponding index position of "long". If none of them are false, the function returns true.
            #hence, "return true is not nested in the if statement."
def starts_with(long, short):
    for position in range(len(short)):
        if short[position] != long[position]:
            return False
    return True        

#print(starts_with("banana", "bab"))

#This function uses a for loop to add all the characters in a list_of_strings and print the total.
def total_length(list_of_strings):
    total = 0
    for strings in list_of_strings:
        total = total + len(strings)
    return total
    
# Should return 6:
#print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
#print(total_length([]))

# Should return 8:
#print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
#print(total_length(["", '', "", '']))


#These two functions use the .random method to give us a random string or integer out of the list or range everytime the function is ran.
import random

def coin_flip():
    return random.choice(["heads", "tails"])

def die_roll():
    return random.randint(1, 6)


# This is a while loop. this function will run over and over until it is false. So as n is increase by 1 every iteration, the function will run until n is greater than 3. consult the while loops section of python_notes.html for more info.

def while_loops():
    n = 0
    while n < 3:
        print(n)
        n += 1

#print(while_loops())   


#This while loop runs until n is counted down from 10 to 1. When the while loop is no longer true, it prints "Blastoff!"
#We use the time module to make the program pause everytime it prints the value of 'n'.
def whileloop_blastoff():
    import time
    n = 10
    while n >= 1:
        print(n)
        time.sleep(1)
        n -= 1
        
    print("Blastoff!")

#print(whileloop_blastoff())


# This while loop prints the characters from the index of 's', starting with the first character until the entire word is printed.
def while_loop3():
    s = "Tenochtitlan"
    index = 0
    while index < len(s):
        index += 1
        print(s[:index])

#print(while_loop3())

#This loop does the opposite of the above function by setting the value of  index to the length of "s". while the index of "s" is greater than 0, it prints s[:index].

def while_loop4():
    s = "Tenochtitlan"
    index = len(s)
    while index > 0:
        print(s[:index])
        index -=1

#print(while_loop4())

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    
    if dolphin == True:
        shark_speed /= 2
    if shark_distance // shark_speed > pontoon_distance // you_speed:
        return "Alive!"
    else:
        return "Shark Bait!"


######The next two functions count how many target characters are in a string using two different methods: a for loop and a while loop.


#For this while loop, we need to create two variables: index = a character in the given string. Total = total number of targets in the given string.
#the while loop runs until the number of characters in the string is greater than the length of the string. 
#Then an "if" statement checks to see of the character being checked equals the target. If it is, the total increases by one.

def count_character_while(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index] == target:
            total += 1
        index += 1
    return total

#print(count_character_while("bonobos", "o"))  

#In this for loop, we also create two variables: "total" = sum of targets in given string. and "ch" which equals a character in the string.
# every time "ch" is equal to the target, the total increases by one.
def count_character_for(string, target):
    total = 0
    for ch in string:
        if ch == target:
            total += 1
    return total

#print(count_character_for("bonobos", "o"))

#This while loop returns the given sentence until it reaches a ".". it states: while the index of the given sentence is less than the length of the sentance,
# and the index of the sentence is not equal to "." return the sentence from the begining until the index contains a "." 
def until_dot(s):
    index = 0
    while index < len(s) and s[index] != ".":
        index += 1
    return s[:index]

#print(until_dot("This is a sentence. This is another."))

#This is the same function but written as a for loop.
def until_dot_for(s):
    for index in range(len(s)):
        if s[index] == ".":
            return s[:index]
     #notice this return statement not nested in the loop. this just means if a "." is not found in any index, print the whole "s".       
    return s[:index]        

#print(until_dot_for("This is a sentence. This is another."))


def find_512():
    for x in range(100):
        for y in range(100):
            if x * y == 512:
                return f"{x} * {y} == 512" 
    
#print(find_512()



##This one gave me problems.......
#The purpose of this function is to check to see if a string contains a substring by looping through the strings index and comparing it to the substring.
#this is the "while loop" edition.

def is_substring_w(substring, string):
    index = 0
    while index < len(string):
        if string[index : index + len(substring)] == substring: #confusing index shit breakdown: everytime the loop is ran, index is increased by 1.
            return True #First iteration looks like this. "string[0 : 0 + len(substring)]" #Second iteration: "string[1 : 1 + len(substring)]"
        index += 1
    return False
 
 # This one should return False
#print(is_substring_w('bad', 'abracadabra'))

   # This one should return True
#print(is_substring_w('dab', 'abracadabra'))
    

#This is the same function except it uses a for loop:
def is_substring_f(substring, string):
    for index in range(len(string)): #for the given string, range(len(string))= from 0 - 11.
        if string[index : index + len(substring)] == substring:
            return True
    #notice how "else:" is not nested inside the if statement. This makes the function return False if the loop runs out of iterations without being True.
    else:
        return False
        

# This one should return False
#print(is_substring_f('bad', 'abracadabra'))

   # This one should return True
#print(is_substring_f('dab', 'abracadabra'))

#This function does the same as the above 2 functions, but it shows the total occurences of a given target in a given string.
def count_substring(string, target):
    index = 0
    total = 0 #we must create another variable to store the loops check results
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1 #every time the loop comes back true, it adds 1 to the total.
            index += len(target) # notice how index increases by the len(target). This is so the code doesnt count overlapping targets. ex: "aa" in "aaaa" could = 3 if index only increased by 1.
        else: # if string index != target, index only increases by 1.
            index += 1
    return total

# Here's a call you can test it with. This should print 4:
#print(count_substring('love, love, love, all you need is love', 'love'))

#print(count_substring('AAAA', 'AA'))

#This function returns the index location of the target instead of the total instances of the target in a string.
#If there is no target contained in the string, "-1" is returned. this will be explained later apparently.
def locate_first(string, target):
    
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            return index
        else:
            index += 1
    return -1

# Here are a couple function calls to test with.

# This one should return 1
#print(locate_first('cookbook', 'ook'))

# This one should return -1
#print(locate_first('all your bass are belong to us', 'base'))

######In this function we want to find all instances of a target.
#To do this we must create a variable containing an empty list. this will store the locations of any targets found in a given string/
def locate_all(string, target):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            matches.append(index)#Whenever the target is equal to the index location, it is added to the matches list.
            index += len(target)
        else:
            index += 1
    return matches

# Here are a couple function calls to test with.

# This one should return 1
#print(locate_all('cookbook', 'ook'))

# This one should return -1
#print(locate_all('all your bass are belong to us', 'base'))

######PLOT TWIST#########

#most of the above functions are already methods within python.




#this function uses the join method to insert an html break tag in between every string in the given list.

lines = ["Haiku frogs in snow",
         "A limerick came from Nantucket",
         "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]
def breakify(strings):
    return "<br>".join(strings)

#print(breakify(lines))



###This next function builds off the previous function except instead of adding something, we are finding instances of a substring and taking them out.
#Because you cant modify words in a string, we have to put the results into a new string.
def remove_substring(string, substring):
    index = 0
    output = []
    while index < len(string):
        if string[index : index + len(substring)] == substring:
            index += len(substring)
        else:
            output.append(string[index])
            index += 1 #Notice we still have to increase index by one if the loop doesnt find any instances of the substring.
    return "".join(output)

# Here are some strings you can test your function:
#print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
#print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
#print(remove_substring('I am NOT learning to code.', 'NOT '))

####This is the same function, but with a couple lines added to replace a substring with a given replacement.
def replace_substring(string, substring, replacement):
    output = []
    index = 0
    
    while index < len(string):
        if string[index:index+len(substring)] == substring:
            output.append(replacement)
            index += len(substring)
            
        else:
            output.append(string[index])
            index += 1
    return "".join(output)

# Here are some examples you can test it with:
print(replace_substring('Hot SPAM!drop soup, and curry with SPAM!plant.', 'SPAM!', 'egg'))
print(replace_substring("The word 'definately' is definately often misspelled.", 'definately', 'definitely'))
