import app
print("OPERATIONS")
print("1. Create a Key-Value pair with Time-to-Live.")
print("2. Create a Key-Value pair without Time-to-Live.")
print("3. Display the Value for a given Key.")
print("4. Delete a Key-Value pair.")
print("5. Save the datastore locally")
print("6. Exit")
while(True):
    ch=int(input(("Enter the Choice of your Operation :")))
    if(ch==1):
        key=input("Enter the Key = ")
        value=input("Enter the Value = ")
        Time_to_live=int(input("Enter the Time-to-Live = "))
        app.create(key,value,Time_to_live)
    if(ch==2):
        key=input("Enter the Key = ")
        value=input("Enter the Value = ")
        app.create(key,value)
    if(ch==3):
        key=input("Enter the Key = ")
        app.read(key)
    if(ch==4):
        key=input("Enter the Key = ")
        app.delete(key)
    if(ch==5):
        app.save()
    if(ch==6):
        print("Thank You!!")
        break

    
    
