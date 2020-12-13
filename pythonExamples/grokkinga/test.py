# from kostya import City

VDV_INFO = {
    "favorite_car": "kruzak",
    "favorite_color": "BLACK",
    "population": 123456,
    "size": 1000,
    "houses": 100,
    "corona_cases_deatth": 0,
    "corona_cases_sick": 0,
}


class City:
    def __init__(self, name=None, hole=True, info=None):
        self.name = name
        self.hole = hole
        self.info = info

    def give_all_money_to_moscow(self):
        print("Just take my money")

    def someone_died(self):
        self.info["population"] -= 1

    def __str__(self):
        return f"Пошел нахуй из {self.name}a!"

    def printInfo(self):
        for k,v in self.info.items():
            print( f"{self.name} {k} {v}")


VDV_INFO['favorite_car']
# moscow = City()

vladik = City(name="vladik", hole=True, info=VDV_INFO)

print(vladik)
vladik.printInfo()

VDV_INFO.get('size2', "Not found")
vladik.hasattr('hole')

hasattr(vladik, 'info')

my_data = vladik.info
for k,v in my_data.items():
    if isinstance(v, int):
        print(f"{k} - {v}")

with open("s.txt", "r") as f:
    l = f.read()


f = open("s.txt", "r")
f.read()
f.close()


def rsum(x):
    if x <= 0:
        return 0
    else:
        return x + rsum(x - 1)

print(rsum(7))

