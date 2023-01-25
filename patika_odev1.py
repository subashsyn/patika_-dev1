def flatten(x):
    flat=[]
    for i in x:
        if type(i)==list:
            flat.extend(flatten(i))
        else:
            flat.append(i)
    return flat
l = [1,'a',['cat'],2,[[[3]],'dog'],4,5]
print("flatten example")
print(flatten(l))

print("----------------")

m= [[1, 2], [3, 4], [5, 6, 7]]
flatten_m = [e for l in m for e in l]
print("reverse of list")
print(flatten_m[::-1])
