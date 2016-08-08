import re

print("".join(enc_chrs[0] * int(enc_chrs[1:]) for enc_chrs in re.findall(r"\w\d+", input())))
