class Name:
    def __init__(self, name) -> None:
        if name not in ["Богдан", "Oleg"]:
            raise ValueError("Дозволені імена: Богдан, Oleg")
        self.name = name

a = Name("Ладик")