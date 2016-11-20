def find_average():
    l=[]
    while True:
        numb = input("Please enter a number:")
        if numb != '':
            l.append (int(numb))
        else:
            break
    avg = sum(l)/len(l)
    print(avg)


