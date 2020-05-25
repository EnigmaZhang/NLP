"""
Wirter: Zhang Xiaotian
Description: This module is to process data into each line with a Chinese character.
Reference:
https://github.com/tensorflow/tensor2tensor
https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/test_data/example_usr_dir/my_submodule.py
"""

import sys

filename = sys.argv[1]
with open(filename, 'r', encoding='utf-8') as infile:
    with open(filename + '.clean', 'w', encoding='utf-8') as outfile:
        lines = infile.readlines()
        for line in lines:
            out = ""
            for i in line.strip():
                out += i + ' '
            out = out[:-1]
            out += '\n'
            outfile.write(out)
