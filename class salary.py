class abc:
    salary=0
    ta=0
    da = 0
    hra=0
    pf=0
    ttl=0
    ttl1=0
    tax=0
    def abc(self):
        self.salary=int(input("Enter the basic salary :- "))
        self.ta=0.20*self.salary
        self.da=0.35*self.salary
        self.hra=0.25*self.salary
        self.pf=0.125*self.salary
        self.esic=0.075*self.salary 
        self.ttl=self.salary+self.ta+self.da+ self.hra-self.pf-self.esic
        print("Basic salary :- ",self.salary)
        print("TA :- ",self.ta)
        print("DA :- ",self.da)
        print("HRA :- ",self.hra)
        print("PF :- ",self.pf)
        print("ESIC :- ",self.esic)
        print("Salary befor tax :- ",self.ttl)
        if(self.ttl<=100000):
         print("No Tax")
         print("Salary is :- ",self.ttl)
        elif self.ttl<=120000:
           self.ttl2=self.ttl-0.10*self.ttl
           print("Salary after tax:- ",self.ttl2)
        else:
           self.ttl2=self.ttl-0.20*self.ttl 
           print("Salary after tax :",self.ttl2)
obj=abc()
obj.abc()

