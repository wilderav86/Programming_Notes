import random #imports random module
import words #imports the noun, verb, and template lists

def silly_strings(nouns, verbs, templates): #names the function and chooses what parameters are needed.
    template = random.choice(templates) #Tells the function to choose a random template.
    output = [] # A variable created to store the results of the loop.
    position = 0 # A variable created so the loop has a position to advance.
    while position < len(template): # A loop that will run as long as the position in the template is within the length of the template.
        if template[position:position+8] == "{{noun}}": #checks if every 8 positions of the template are equal to "{{noun}}"
            output.append(random.choice(nouns)) # If the check is true, a random noun is added to the output.
            position += 8 #if the check is true, the position advances 8 spaces.
        elif template[position:position+8] == "{{verb}}": # This check does the same, but with "{{verb}}"
            output.append(random.choice(verbs))
            position += 8
        else:
            output.append(template[position]) # If no instances of "{{verb}}" or "{{noun}}" are found in an 8 space section, whatever character in that position is added to output.
            position += 1 # If no instances are found, the position advances by 1.
    output = "".join(output) #after the entire loop is finished, all the positions given to output are joined.
    return output

if __name__ == '__main__':
    print(silly_strings(words.nouns, words.verbs,
        words.templates))