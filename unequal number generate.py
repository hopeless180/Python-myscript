
if __name__ == "__main__":
    p_num = 2044211451
    num = p_num
    count = 0
    str1 = ""
    while(count<10):
        count += 1
        if num % (10**count) == 9:
            i = num - num % (10**count)*(10**(count-1))
        else: 
            i = num + 10**(count-1)
        str1 = str1 + str(i)+","
    print(str1)

