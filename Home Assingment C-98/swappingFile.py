
def swappingText():
    file1Name=input("Enter 1st file path:")
    file2Name=input("Enter the 2nd file path:")

    file1=open(file1Name,"r")
    file2=open(file2Name,'r')
    data1=file1.read()
    data2=file2.read()
    file1=open(file1Name,'w')
    file1.write(data2)
    file2=open(file2Name,'w')
    file2.write(data1)

swappingText()


