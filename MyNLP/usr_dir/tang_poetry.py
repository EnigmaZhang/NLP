

with open("全唐诗.txt", mode="r", encoding="utf-8") as f:
    with open("tang.txt", mode="w", encoding="utf-8") as o:
        for line in f.readlines():
            if len(line.strip()) != 0 and line.strip()[0] != "卷":
                o.write(line)

token = []
with open("tang.txt", mode="r", encoding="utf-8") as f:
    with open("tang.txt.up", mode="w", encoding="utf-8") as up:
        with open("tang.txt.down", mode="w", encoding="utf-8") as down:
            for line in f.readlines():
                sentences = line.split("。")
                up_down = []
                for sentence in sentences:
                    up_down.extend(sentence.split("，"))
                for i in up_down:
                    if len(i.strip()) != 0 and "--" not in i and '（' not in i and '）' not in i:
                        token.append(i)
                while len(token) >= 2:
                    up.write(token[0] + '\n')
                    down.write(token[1] + '\n')
                    token = token[2:]
print(token)

