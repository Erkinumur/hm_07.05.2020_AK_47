class Soldier:
    def __init__(self, name):
        self.name = name

    def fire(self, shots):
        for i in range(shots):
            print(f'{self.name} стреляет!!!\ntigi-tigitishh')

class Gun:
    def __init__(self, gun_name, max_bullet_in_mag):
        self.gun_name = gun_name
        self.bullets = max_bullet_in_mag
        self.max_bullet_in_mag = max_bullet_in_mag

    def fire(self, shots):
        for i in range(shots):
            if self.bullets:
                print(f'Выстрел из {self.gun_name}!\ntigi-tigitishh')        
                self.bullets -= 1
            else:
                print('Закончились патроны, нужна перезарядка!')
                break
    
    def reload(self):
        self.bullets = self.max_bullet_in_mag
        print(f'{self.gun_name} перезаряжен! Обойма полная!')

class Act_of_Shooting(Soldier, Gun):
    def __init__(self, name, gun_name, max_bullet_in_mag):
        Soldier.__init__(self, name)
        Gun.__init__(self, gun_name, max_bullet_in_mag)
    
    def fire(self, shots):
        while shots:
            if self.bullets:
                print(f'{self.name} делает выстрел из {self.gun_name}!\n tigi-tigitishh')
                shots -= 1
                self.bullets -= 1            
            else:
                print(f'{self.name} перезаряжает оружие!')
                self.reload()


example = Act_of_Shooting('Ryan', 'Deagle', 7)
example.fire(9)
                
            
