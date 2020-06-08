"""
Wirter: Zhang Xiaotian
Description: This module is to process data into each line with a Chinese character.
Reference:
https://github.com/tensorflow/tensor2tensor
https://github.com/tensorflow/tensor2tensor/blob/master/tensor2tensor/test_data/example_usr_dir/my_submodule.py
"""

with open("poems_edge_split.txt", mode="r", encoding="utf-8") as f:
    with open("tang.txt", mode="w", encoding="utf-8") as o:
        for line in f.readlines():
            line = ''.join([c for c in line if c != "[" and c != "]" and c != ' '])
            if len(line) >= 3 and line[-2] == "。" and line[-3] == "。":
                line = line[:-2] + '\n'
            o.write(line)

with open("tang.txt", mode="r", encoding="utf-8") as f:
    with open("tang_up.txt", mode="w", encoding="utf-8") as up:
        with open("tang_down.txt", mode="w", encoding="utf-8") as down:
            for line in f:
                line_str = line[:-1].split("。")
                for sentence in line_str:
                    up_down = sentence.split("，")
                    if len(up_down) == 2:
                        up_text = up_down[0] + '\n'
                        down_text = up_down[1] + '\n'
                        if (len(up_text) == len(down_text)):
                            up.write(up_text)
                            down.write(down_text)
                    

