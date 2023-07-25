

class Animal():
    def __init__(self,respiratory,action,reproductive):
        self.respiratory = respiratory
        self.action = action
        self.reproductive = reproductive

class Dog(Animal):
    def __init__(self,respiratory,action,reproductive,sniffing,trainability):
        super().__init__(respiratory,action,reproductive)
        self.snifffing = sniffing
        self.trainability = trainability

class Bird(Animal):
    def __init__(self,respiratory,action,reproductive,fly_ability,feathers):
        super().__init__(respiratory,action,reproductive)
        self.fly_ability = fly_ability
        self.feathers = feathers

class Horse(Animal):
    def __init__(self,respiratory,action,reproductive,high_speed,durability):
        super().__init__(respiratory,action,reproductive)
        self.high_speed = high_speed
        self.durability = durability

