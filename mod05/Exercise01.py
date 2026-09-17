i = 1
while i <= 1000:
    print(f"{i}\n" * (i % 3 == 0) , end = "")
    i+=1