#try block: tests a code for errors
#expect block: code to run if error happens
#else block: code to run if no error happens
#finally block: code to run regardless of try/except block
flower = int(input("how many flowers does the farmer have?"))
try:
    print(flower*300)
except:
    print("There is a problem")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")