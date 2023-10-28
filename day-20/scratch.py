class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    @staticmethod
    def swim() -> None:
        print("moving in water.")

    def breathe(self) -> None:
        super().breathe()
        print("doing this underwater.")


nemo = Fish()

nemo.swim()
nemo.breathe()
