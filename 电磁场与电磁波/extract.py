import os
import re

src_file = r"D:\PROJECTS\MoMoJeeObsidian\MoMoJeeOsidian\电磁场与电磁波\教材和PPT\MinerU_markdown_第六版教材-第3章_2041905903615332352.md"

with open(src_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

s34, s35, s36 = [], [], []
current = None

for i, line in enumerate(lines):
    if i >= 2163 and i < 2331:
        s34.append(line)
    elif i >= 2331 and i < 3127: # 3.5 starts to 3.6
        s35.append(line)
    elif i >= 3127: # 3.6 starts
        s36.append(line)

with open("34_temp.md", "w", encoding="utf-8") as f:
    f.writelines(s34)
with open("35_temp.md", "w", encoding="utf-8") as f:
    f.writelines(s35)
with open("36_temp.md", "w", encoding="utf-8") as f:
    f.writelines(s36)

print("Temp files created.")
