#Loop Control Statements = change a loops execution from its normal sequence
#
# break = used to erminate the loop entirely
#continue = skips to the next iteration of the loop
#pass = does noting, acts as a placeholder

#using the break rule in order to get out of the while loop
while True:
    name = input("Enter your name: ")
    if name != "":
        break

phone_number = "123-456-7890"

#using the continue rule in order to skip the "-" in the phone number
for i in phone_number:
    if i == "-":
        continue
    print(i, end = "")

#using the pass in order to do nothing if i hits 13
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)