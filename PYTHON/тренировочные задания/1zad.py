class RGB:
    #конструктор
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.bloe = b
    def ratio(self):
        print(round(self.red/255, 2))
        print(round(self.green/255, 2))
        print(round(self.bloe/255, 2))
        

r = int(input())
g =  int(input())
b = int(input())
print = RGB(r, g, b)
print.ratio
