# # Write your code here
# def is_substring(substring, string):
#     for index in range(len(string)):
#         if string[index : index + len(substring)] == substring:
#             return True
#     return False

# # Below are some calls you can use to test it

# # This one should return False
# print(is_substring('bad', 'abracadabra'))

# # This one should return True
# print(is_substring('dab', 'abracadabra'))

##

# def count_substring(string, target):
#     index = 0
#     total = 0
#     while index < len(string):
#         if string[index : index + len(target)] == target:
#             total += 1
#         index += len(target)
#     return total

# print(count_substring('AAAA', 'AA'))

# def locate_first(string, target):
#     matches = []
#     index = 0
#     while index < len(string):
#         if string[index : index + len(target)] == target:
#             matches.append(index)
#             index += len(target)
#         else:
#             index += 1
#     return matches

# # Here are a couple function calls to test with.

# # This one should return 1
# print(locate_first('cookbook', 'ook'))

# # This one should return -1
# print(locate_first('all your bass are belong to us', 'base'))


# # Here is the example you can test it on:
# lines = ["Haiku frogs in snow",
#          "A limerick came from Nantucket",
#          "Tetrametric drum-beats thrumming, Hiawathianic rhythm."]

# # Write your function definition here:
# def breakify(str):
#     return "<br>".join(str)

# # Then call the function and print the results
# print(breakify(lines))


# def remove_substring(string, substring):
#     output = []
#     index = 0
#     while index < len(string):
#         if string[index:index+len(substring)] == substring:
#             index += len(substring)
#         else:
#             output.append(string[index])
#             index += 1
#     return "".join(output)

# print(remove_substring('SPAM!HelloSPAM! worldSPAM!!', 'SPAM!'))
# print(remove_substring("Whoever<br> wrote this<br> loves break<br> tags!", "<br>"))
# print(remove_substring('I am NOT learning to code.', 'NOT '))

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