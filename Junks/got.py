def add_to_list(val, lst=[]):
    lst.append(val)
    return lst

print(add_to_list(1))
print(add_to_list(2))
print(add_to_list(3, []))
print(add_to_list(4))

//fixed version

def add_to_list(val, lst=None)://<==leason learned gumamit ng none kesa sa empty string mwahahaha
    if lst is None:
        lst = []//<===syaka ginamit mwahahahaha
    lst.append(val)
    return lst
