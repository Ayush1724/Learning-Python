class car:
    comp=""
    mod=""
    avg=0
    price=0
    dis=0
    fuel=0
    def car_detail(self,a,b,c,d,e):
        self.comp=a
        self.mod=b
        self.price=c
        self.dis=d
        self.fuel=e
        self.avg=d/e
    def show(self):
        print("CAR Company :- ",self.comp)
        print("CAR Model :- ",self.mod)
        print("CAR price :- ",self.price)
        print("CAR Distance :- ",self.dis)
        print("CAR Fuel :- ",self.fuel)
        print("CAR Average :- ",self.avg)
        print("------------------------------")

mycar=car()
mycar.car_detail("Suzuki","ALTO",400000,500,25)  
mycar.show()      

mycar=car()
mycar.car_detail("TATA","NEXON",1000000,500,18)  
mycar.show()

mycar=car()
mycar.car_detail("Mahindra","XUV300",1200000,500,22)  
mycar.show()