msg=input("ENTER MSG:-->")

spam_list=["made a lot of money","buy now","subscribe this","like this"]
if msg in spam_list:
    print("SPAM")
else:
    print("genuine")