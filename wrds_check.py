# Create dictionary and collect correct words
wrds_dict = []

for _ in range(int(input())):
    word = input().lower()
    if word not in wrds_dict:
        wrds_dict.append(word)

# Create list and collect all the words, which not in dictionary
incorr_wrds = []
for _ in range(int(input())):
    txt_wrds = [txt_wrd.lower() for txt_wrd in input().split()]
    for txt_wrd in txt_wrds:
        if txt_wrd not in wrds_dict:
            incorr_wrds.append(txt_wrd)

for word in incorr_wrds:
    print(word)
