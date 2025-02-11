
class cookie:
    def __init__(self,color):
        self.color = color
    
    def get_color(self):
        return self.color

    def set_color(self,color):
        self.color = color

cookie_1 = cookie("green")
cookie_2 =  cookie("blue")

print('cookie one is',cookie_1.get_color())
print('cookie two is',cookie_2.get_color())




