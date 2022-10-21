# NUMBER 1

# A commonly used method to provide a rough estimate of the right length of snowboard for a rider is 
# to calculate 88 percent of their height (the actual ideal length really depends on a large number of 
# other factors). Write a program that will help people estimate the length of snowboard they should buy. 
# Obtain the users height in feet and inches (assume these values will be entered as integers) and display 
# the length of snowboard in centimeters to the user. There are 2.54 centimeters in an inch.

# The following demonstrates the proper behavior of the program: Enter your height.
# Feet: 5
# Inches: 4
# Suggested board length: 143.0528 cm

feet,inches = eval(input(print("Enter your height in feet and inches:")))

height_in_cm = float(feet)*12*2.54 + float(inches)*2.54
board_length = float(height_in_cm)*88/100

print("suggested board length = ", board_length)


# NUMBER 2

# Newtons Second Law of motion is expressed in the formula F = m _ a where F is force, m is mass, and a is acceleration. 
# Assume that the user knows the mass of an object and the force on that object but wants to obtain the object’s acceleration 
# a. Write a program that prompts the user to enter the mass in kilograms (kg) and the force in Newtons (N). The user should 
# enter both values on the same line separated by a comma. Calculate the acceleration using the above formula and display the 
# result to the user.

# The following demonstrates the proper behavior of the program: Enter the mass in kg and the force in N: 55.4, 6.094
# The acceleration is 0.11000000000000001

mass,force = eval(input(print("Enter the mass in kg and the force in N:")))
print("mass = ",mass,"kg Force = ",force,"N")

acceleration = force/mass

print("The acceleration is ",acceleration)


# NUMBER 3

# In the word game Mad Libs, people are asked to provide a part of speech, such as a noun, verb, adverb, or adjective. 
# The supplied words are used to fill in the blanks of a preexisting template or replace the same parts of speech in a 
# preexisting sentence. Although we don’t yet have the tools to implement a full Mad Libs game, we can implement code that 
# demonstrates how the game works for a single sentence. Consider this sentence:
# A Shinigami lugged my purple socks out of the drawer as if he were a vegetarian fishing a caterpillar
# out of his salad.

# Write a program that will do the following:
# 1. Print the following template:
# A Shinigami [verb] my [adjective] [noun] out of the [noun] as if he were a vegetarian fishing a [noun] out of his salad.
# 2. Prompt the user for a verb, an adjective, and three nouns.
# 3. Print the template with the terms in brackets replaced with the words the user provided.
# Use string concatenation (i.e., the combining of strings with the plus sign) as appropriate.

# The following demonstrates the proper behavior of this code
# A Shinigami [verb] my [adjective] [noun] out of the [noun] as if he were a vegetarian fishing a [noun] out of his salad.
# Enter a verb: bounced
# Enter an adjective: invisible
# Enter a noun: parka
# Enter a noun: watermelon
# Enter a noun: lion
# A Shinigami bounced my invisible parka out of the watermelon as if he were a vegetarian fishing a lion out of his salad.

verb,adjective,noun1,noun2,noun3 = input(print("Enter a verb, an adjective, and three nouns"))
print("A Shinigami " + (verb) + "my " + (adjective) + (noun3) + "out of the " + (noun2) + "as if he were a vegetarian fishing a " + (noun3) + "out of his salad.")