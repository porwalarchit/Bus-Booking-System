def TOH(n, source, dest, using):
    if n==1:
        print("Move Disk 1 from Rod", source, "to Rod", dest)
        return
    TOH(n-1, source, using, dest)
    print("Move Disk", n, "from Rod", source, "to Rod", dest)
    TOH(n-1, using, dest, source)

n=int(input("Enter Number of Disks:"))
A= input("Enter Source: ")
B= input("Enter Destination: ")
C= input("Enter Using: ")
TOH(n, 'A', 'B', 'C')
