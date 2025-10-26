class main:
    def __init__(user,name,age)
        user.name = name 
        user.age = age
    
    def user_name(user):
        print(f"I am {user.name}")       
        print(f"and lived for {user.age} years")
    
println = main("jerricky",67 )
println.user_name()

#fun version or much more detailed

class main:
    def __init__(user,name,age):
        user.name = name
        user.age = age
    
    def user_name(user):
        print(f"greetings I am {user.name}")
        if user.age == 1:
            print("{user.name} is a year old")
        else:
            print(f"I have lived for over {user.age}")
    
    def IWantIce(user):
        print(f"{user.name} likes icecream")

println = main("grogru",1) 
println.user_name()
