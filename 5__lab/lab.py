class Rocket:
    def __init__(self, name:str, mass) -> None:
        assert isinstance(name, str), "Назва ракети має бути типу стрічка"
        assert name.isascii(), "Назва повинна містити символи з таблиці ASASCII"
        assert mass > 0, "Маса має бути більшою за 0"
        self.name = name
        self.mass = mass

        @property
        def info(self):
            return f"Ракета {self.name} важить {self.mass} кг"
        @property
        def info_en(self):
            return self.mass * 2.20462
        def convert_mass(self):
            return

