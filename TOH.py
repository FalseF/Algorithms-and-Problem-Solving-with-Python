def TOH(disk, start, aux, end):
    if disk==1:
        print("Move disk 1 from {} to {}.".format(start, end))
        return
    TOH(disk-1,start,end,aux)
    print("Move disk {} from {} to {}.".format(disk,start,end))
    TOH(disk-1,aux,start,end)
disk = int(input())
start = input()
aux= input()
end = input()
TOH(disk, start,aux,end)