# import shelve
# FILENAME = "states6"
# with shelve.open(FILENAME) as file:
#     file['student1'] = {"FIO": "Aaaa", "Group": "13-19", "Performance": 60, "Grant": 120}
#     file['student2'] = {"FIO": "BBBB", "Group": "13-19", "Performance": 100, "Grant": 180}
#     file['student3'] = {"FIO": "XXXX", "Group": "13-19", "Performance": 50, "Grant": 120}
#     for key in file:
#             if file[key]["Performance"] >=60:
#
#                 print(file[key])
# with shelve.open(FILENAME) as states:
#      states.close()
# import shelve
# FILENAME = "states8"
# with shelve.open(FILENAME) as file:
#     file["Product1"] = {"name": "AAAA", "cost": 40, "quantity": 15}
#     file["Product2"] = {"name": "BBBB", "cost": 50, "quantity":  5}
#     file["Product3"] = {"name": "XXXX", "cost": 60, "quantity": 10}
#     j = 0
#     x = 0
#     for key in file:
#         j += file[key]["cost"]
#         x += file[key]["quantity"]
#         c=j/x
#     print(c)
#
#
# with shelve.open(FILENAME) as file:
#     file.close()




import shelve
FILENAME = "states"
with shelve.open(FILENAME) as file:
    file['student1'] = {"FIO": "Aaaa", "Group": "13-19", "Performance": 60, "Grant": 120}
    file['student2'] = {"FIO": "BBBB", "Group": "13-19", "Performance": 100, "Grant": 180}
    file['student3'] = {"FIO": "XXXX", "Group": "13-19", "Performance": 50, "Grant": 120}
    a=0
    for key in file:
            if file[key]["Performance"] <60:
                a=file[key]["Grant"]-24
                print(file[key])

print(f'Стипендия уменьшена на 20% - {a}')



# import shelve
# FILENAME = "states2"
# with shelve.open(FILENAME) as file:
#     file['student1'] = {"FIO": "Aaaa", "Group": "13-19", "Performance": 60, "Grant": 120}
#     file['student2'] = {"FIO": "BBBB", "Group": "13-19", "Performance": 100, "Grant": 180}
#     file['student3'] = {"FIO": "XXXX", "Group": "13-19", "Performance": 50, "Grant": 120}
#     a=0
#     for key in file:
#             if file[key]["Performance"] >70:
#                 a=file[key]["Grant"]+54
#                 print(file[key])
#
# print(f'Стипендия увелечина  на 30% - {a}')