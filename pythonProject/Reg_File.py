with open('registrations_.txt', 'r', encoding='utf-8') as file:
    users_list = []
    for line in file:
        users = line.split()
        users_list.append(users)

# print(users_list)
good_users_list_filter_full_elements = []
good_users_list_filter_name = []
good_users_list_filter_finally = []
bad_users_list = []
item = 0

for item in users_list:
    if len(item) == 3:
        good_users_list_filter_full_elements.append(item)
    else:
        bad_users_list.append(item)

for item1 in good_users_list_filter_full_elements:
    if item1[0].isalpha() and item1[2].isdigit():
        good_users_list_filter_name.append(item1)
    else:
        bad_users_list.append(item1)

for item2 in good_users_list_filter_finally:
    if "@" in item2[1] and "." in item2[1]:
        good_users_list_filter_finally.append(item2)
    else:
        bad_users_list.append(item2)


# print(bad_users_list)
with open('registration_good.log.txt', 'w', encoding='utf-8') as f:
    joined = '\n'.join(' '.join(map(str, row)) for row in good_users_list_filter_finally)
    f.writelines(joined)
with open('registration_bad.log.txt', 'w', encoding='utf-8') as gg:
    joined = '\n'.join(' '.join(map(str, row)) for row in bad_users_list)
    gg.writelines(joined)