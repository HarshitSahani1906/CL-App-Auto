import random
# number = random.randint(1000,9999)
# digits=[int(x) for x in str(number)]
# print(digits)
# print(number)


def randomNumber(lower_limit, upper_limit,  output):
    number = random.randint(lower_limit, upper_limit)
    # print(number)
    if output == "Number":
        return number
    elif output == "List":
        digits=[int(x) for x in str(number)]
        print(digits)
        return digits



# digit=randomNumber()
# for x in range(0, 4):
#
#     print("Xpath_digit" + str(x) +"--->"+ str(digit[x] ))
#     print("We're on time %d" % (x))

