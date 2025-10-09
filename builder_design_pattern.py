# builder design pattern

class Computer:
    def __init__(self,cpu,ram,storage):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage

    def __str__(self):
        return f"{self.cpu}\n{self.ram}\n{self.storage}"

class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self,cpu):
        self.cpu = cpu
        return self

    def set_ram(self, ram):
        self.ram = ram
        return self

    def set_storage(self, storage):
        self.storage = storage
        return self


    def build(self):
        return Computer(self.cpu, self.ram, self.storage)

b = ComputerBuilder()
build_variable =b.set_cpu('Intel Core I7').set_ram('8GB').set_storage("512TB SSD").build()
print(build_variable)
