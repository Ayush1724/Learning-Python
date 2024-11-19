class car:
    comp =""
    mod=""
    price=0
    def car_detail(self,a,b,c):
        self.comp=a
        self.mod=b
        self.price=c
    def show(self):
        print("CAR Company : ",self.comp)
        print("CAR Model : ",self.mod)
        print("CAR price : ",self.price)
        print("----------------------------------------------------")
        print()

mycar=car()
mycar.car_detail("maruti",800,200000)
mycar.show()

mycar1=car()
mycar1.car_detail("suzuki","Alto",400000)
mycar1.show()
        
mycar3=car()
mycar3.car_detail("TATA","NEXON",1000000)
mycar3.show()