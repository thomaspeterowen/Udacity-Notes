# def word_triangle(string):
    # length = len(string)
    # for n in range(length):
        # print(string[:length - n])
# word_triangle("abracadabra")
# def adverbly(string):
    # return string + 'ly'
# print(adverbly("quick"))
# string = input("Hi, what's your name?\n")
# string2 = input("Ah what an unusual name...\nCan I call you " + adverbly(string) + "?")
# n1 = input("\nGive one number please")
# n2 = input("\nGive another number please")
# n3 = input("\nGive one more number please")
# sum = int(n1) + int(n2) + int(n3)
# print(f"The sum is equal to {sum}!")

# Add your function definition here
# def starts_with(long, short):
    # return long[0:len(short)] == short

# A call like this should return True:
# print(starts_with("apple", "app"))

# And one like this should return False:
# print(starts_with("manatee", "mango"))

# def good_length(pw):
    # return len(pw) >= 8 and len(pw) <=64

# This should print False, because it's under eight characters.
# print(good_length("2short"))

# This should print True, since it's between eight and 64 characters long:
# print(good_length("nice password, yo"))

# This should print False, since it's over 64 characters long:
# print(good_length("This is really much too long for a password. I mean, it's really secure, but I don't want to type this much every time I log in, okay?"))

# Add your code here.
def total_length(inp):
    length = 0
    for item in inp:
        length = length + len(item)
    return length

# Should return 6:
# print(total_length(['foo', 'bar']))

# Should return 0 (it's an empty list):
# print(total_length([]))

# Should return 8:
print(total_length(['balloons']))

# Should return 0 (it has four empty strings):
print(total_length(["", '', "", '']))