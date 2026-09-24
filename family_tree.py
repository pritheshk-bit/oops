class familymenber:
    def _init__(self, eye_color, height_cn):
        self. eye_color =  eye_color
        self.height_cn = height_cn

    def show_traits(self):
        print("eye color: ", self. eye_color )
        print("heigh (cn): ", self.height_cn )

class kid(familymenber):

    def __init__(self,name,age, eye_color, height_cn):
        self. age =  age
        self. name =  name
        super()._init__( eye_color, height_cn)

    def show_traits(self):
            print("age: ", self.age)
            print("name: ", self.name)
            super().show_traits()

    def favorite_hooddy(self, hobby):
         print(self.name ,"loves", hobby)

child = kid("maya" ,10 ,"brown" , 140)

child.show_traits()
child.favorite_hooddy("painting")

print("ls kid a subclass of familymenber?",issubclass(kid , familymenber))