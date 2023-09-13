filename = "实际th_3_d_4.txt"
fr = open(filename)
lines = fr.readlines()
fw = open('实际th_3_d_4_new.txt', 'w')

lines_list = []
line_list = []
for line in lines:
    line_list = line.split()
    new_line_list = list(filter(lambda x: x[0] != 't' and x[0] != 'd', line_list))
    new_line_list = [x.strip(';') for x in new_line_list]
    # print(new_line_list)
    new_line_list[-1] += '\n'
    fw.writelines(','.join(new_line_list))
fr.close()
fw.close()


