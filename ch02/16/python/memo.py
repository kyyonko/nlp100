# -*- coding: utf-8 -*-

in_file_name = "../../hightemp.txt"
out_file_name_template = "splitted_%d.log"

max_lines = 1000000

split_index = 2
line_index = 1
out_file = open(out_file_name_template % (split_index,), "w")
in_file = open(in_file_name)
line = in_file.readline()
while line:
    if line_index > max_lines:
        print("Starting file: %d" % split_index)
        out_file.close()
        split_index = split_index + 1
        line_index = 1
        out_file = open(out_file_name_template % (split_index,), "w")
    out_file.write(line)
    line_index = line_index + 1
    line = in_file.readline()

out_file.close()
in_file.close()
