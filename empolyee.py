class Employee:

    def _init_(self):
        print("employee created")

    def _del_(self):
        print("destructor called")

def create_obj():
    print("making object.........")
    obj = Employee()
    print("function end.......")
    return obj

print("calling create_obj() function......")
obj = create_obj()
print("programe end.....")