var = 26
po = (var*var + 1)
lst = []
def indivs():
    for i in range(1, po):
        for j in range(i,po):
            sameRow = j in range(i,var*(i//var+1)+1)
            colBehind = i%var == 0 or (i%var >= j%var and j%var != 0)
            if sameRow or colBehind:
                continue
            k = (i,j)
            w = (k[1] % var if k[1] % var != 0 else var) - k[0] % var + 1
            h = ((k[1] - k[0]) // var) + 1
            e = (w-1) * (h-1) * var
        data = [w, h, e]
        data.sort()
        lst.append(data)
    lst.sort()
    for i in lst:
        for j in lst:
            if (i[1], i[2]) in ((w,h), (h,w)):
                lst.remove(i)
    for i in lst:
        print(i[0], "x",  i[1], ";", i[2], "|", "True")
def totals():
    for i in range(1,po):
        for j in range(i,po):
            sameRow = j in range(i,var*(i//var+1)+1)
            colBehind = i%var == 0 or (i%var >= j%var and j%var != 0)
            if sameRow or colBehind:
                continue
            k = (i,j)
            w = (k[1] % var if k[1] % var != 0 else var) - k[0] % var + 1
            h = ((k[1] - k[0]) // var) + 1
            e = (w-1) * (h-1) * var
            print("Co-ords:", i, ",", j, "|", "Diff:", e, "|", "Size:", w,"x",h)
