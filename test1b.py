class Archer:
    # class properties
    def __init__(self, name, health, num_arrows):
        self.name = name
        self.health = health
        self.num_arrows = num_arrows

    # class methods, i.e. class functions which can be used as object.method()
    def get_shot(self):
        if self.health > 0:
            self.health -= 1
        else:
            raise Exception(f"{self.name} is dead")
        return print(self.health)

    def shoot(self, target):
        if self.num_arrows > 0:
            self.num_arrows -= 1
            print(f"{self.name} shoots {target}")
        else:
            raise Exception(f"{self.name} can't shoot")

    # don't touch below this line

    def get_status(self):
        return self.name, self.health, self.num_arrows

    def print_status(self):
        print(f"{self.name} has {self.health} health and {self.num_arrows} arrows")
