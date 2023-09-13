import re
filename = "期望th_3_d_4.txt"
fr = open(filename)
lines = fr.readlines()
fw = open('期望th_3_d_4_new.txt', 'w')

lines_list = []
line_list = []
new_line_list = []
line_for_write = []
for line in lines:
    print(line)
    line_list = re.split(';', line)
    new_line_list.append(line_list[0][4:])
    for word in line_list[1:]:
        new_line_list.append(word[5:9])
        new_line_list.append(word[-4:])
    # new_line_list = list(filter(lambda x: x[0] != 't' and x[0] != 'd', line_list))
    # new_line_list = [x.strip(';') for x in new_line_list]
    print(new_line_list)
    for i in range(len(new_line_list) - 1):
        if i % 2 == 0:
            line_for_write = []
        line_for_write.append(new_line_list[i])
        line_for_write.append(new_line_list[i + 1])
        if i % 2 == 0:
            line_for_write[-1] += '\n'
            fw.writelines(','.join(line_for_write))
fr.close()
fw.close()


