import random as r
c_numb = r.randint(1, 10)
print(c_numb)
count = 1
my_numb = int(input("Try to find the the number between 1 and 10: "))
while c_numb != my_numb:
    if c_numb > my_numb:
        print("Your number is less")
    else:
        print("Your number is greater")
    my_numb = int(input("Try to give another value: "))
    count += 1
print(f"You found the correct number in {count} tries. \n\n\nNow you think a number between 1 and 10. "
    "\nIf guessed number is less enter (-), if greater enter (+), if true enter (T)")

c_guess = r.randint(1, 10)
print(f"I guessed {c_guess}")
my_hint = input("Give your hint: ")
comp_count = 1
while True:
    if my_hint == '+':
        c_guess = r.randint(c_guess, 10)
    elif my_hint == '-':
        c_guess = r.randint(1, c_guess)
    elif my_hint == 't':
        break
    comp_count += 1

print(f"Computer found the correct number in {comp_count} tries")
if comp_count < count:
    print(f"Computer won with {comp_count} tries. You tried {count} times")
elif comp_count > count:
    print(f"You won with {count} tries. Computer tried {comp_count} times")
else:
    print("The result is draw")