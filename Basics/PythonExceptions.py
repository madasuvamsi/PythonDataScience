
try:
    fn = int(input("Enter First Number:"))
    sn = int(input("Enter Second Number:"))

    result=fn/sn
    print("Result is ",result)

except Exception as e:
    print("Error occured in Program execution")
    print("The Exception is ",e)
    print(type(e))
    with open("E:\\PythonDataScience\\Logs\\log.txt","a") as f:
        f.write("\n")
        f.write("PythonExceptions.py File  "+str(e))


finally:
    print("Program Exec completed")