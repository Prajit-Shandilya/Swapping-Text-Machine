def swappingText():
    file1Name=input("Enter 1st file path:")
    file2Name=input("Enter the 2nd file path:")

    with open(file1Name,'r') as f1:
        data1=f1.read() 

    with open(file2Name,'r') as f2:
        data2=f2.read()

    with open (file1Name,'w') as f1:
        f1.write(data2)

    with open (file2Name,'w') as f2:
        f2.write(data1) 

swappingText()           

