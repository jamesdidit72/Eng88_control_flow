# loops
# for and while
# loops are used to ITERATE through data
# lists, dictionaries and sets

# first iteration
list_data = [1, 2, 3, 4, 5]
for number in list_data:
    if number == 1:
        print("1 was found")
    if number == 4:
        print("4 was found")
    if number == 5:
        print("5 was found")
else:
    print('better luck next time')


# second iteration

# student_1 = {
#     'name': 'James',
#     'key': 'value',
#     'stream': 'Cyber Security',  # string
#     'completed_lessons': 3,  # int
#     'completed_lesson_names': ["variables", "operators", "data_collections"]  # list
#
# }
# # for data in student_1:
# #     print(data)  # only prints the keys
# # for data in student_1.values():
# #     print(data)  # only prints the values
#
# for data in student_1.values():
#     if data == "Cyber Security":
#         break
#     print(data)