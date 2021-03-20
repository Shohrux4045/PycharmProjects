with open('in.txt', 'r', encoding='UTF-8') as file:
    string = ''

    for text_in_file in file:
        string += text_in_file
    string = string.lower()
    string = string.replace(',', '')
    string = string.replace('.', '')
    string = string.replace('?', '')
    string = string.replace('\n', ' ')


    def word(string):
        start = 0
        i = 0
        word_list = []
        for x in range(0, len(string)):
            if " " == string[i:i + 1][0]:
                word_list.append(string[start:i])
                start = i + 1
            i += 1
        word_list.append(string[start:i])

        return word_list


    a = word(string)


    def get_dict(words):

        words_dict = dict()

        for word in words:
            if word in words_dict:
                words_dict[word] = words_dict[word] + 1
            else:
                words_dict[word] = 1
        return words_dict


    b = get_dict(a)

with open('in.txt', 'r', encoding='UTF-8') as in_file, open('out.txt', 'w', encoding='UTF-8') as out_file:
    for line in in_file:
        out_file.write(line)
    for key, val in b.items():
        out_file.write('\n{}-{}\n'.format(key, val))
