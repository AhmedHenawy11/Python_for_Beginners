# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
names_lowercased = str(name1+name2).lower()

t_counter =names_lowercased.count("t")
r_counter =names_lowercased.count("r")
u_counter =names_lowercased.count("u")
e_counter =names_lowercased.count("e")
true_counter = t_counter + r_counter + u_counter + e_counter

l_counter =names_lowercased.count("l")
o_counter =names_lowercased.count("o")
v_counter =names_lowercased.count("v")
e_counter =names_lowercased.count("e")
love_counter = l_counter + o_counter + v_counter + e_counter
name_counter = int(str(true_counter) + str(love_counter))

if (name_counter < 10) or (name_counter > 90):
    print(f"Your score is {name_counter}, you go together like coke and mentos.")
elif (name_counter > 40) and (name_counter < 50):
    print(f"Your score is {name_counter}, you are alright together.")
else:
    print(f"Your score is {name_counter}.")
