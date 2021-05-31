my_Task1file=open("Numbers.txt", "w")
my_Task1file.write(str("3"))
my_Task1file.write("\n")
my_Task1file.write(str("45"))
my_Task1file.write("\n")
my_Task1file.write(str("83"))
my_Task1file.write("\n")
my_Task1file.write(str("21"))
my_Task1file.write("\n")
my_Task1file.close

my_Task1file=open("Numbers.txt", "a")
my_Task1file.write("\n")
my_Task1file.write(str("This program has been successfully completed."))
my_Task1file.close

my_Task1file=open("Numbers.txt", "r")
my_Task1file.close
