class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length
        
c = Figure("квадрат", 1)
a = Figure("тетраед", 12)
b = Figure("коло", "два ліктя")
