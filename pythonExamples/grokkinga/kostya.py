colors = {
    "white": "WHITE CHRISTMAS", 
    "black": "BIG BLACK DICK",
    "yellow": "PINE-APLE AFTER PUKE"
}

VDV_INFO = {
            "favorite_car": "kruzak",
            "favorite_color": "BLACK",
            "population": 123456,
            "size": 1000,
            "houses": 100,
            "corona_cases_deatth": 0,
            "corona_cases_sick": 0
        }

class City():
    def __init__(self, name=None, hole=True, info=None):
        self.name = name
        self.hole = hole
        self.info = {
            "favorite_car": "kruzak",
            "favorite_color": "BLACK",
            "population": 0,
            "size": 0,
            "houses": 0,
            "corona_cases_deatth": 0,
            "corona_cases_sick": 0
        }

    def give_all_money_to_moscow(self):
        print("Just take my money")

    def someone_died(self):
        self.info["population"] -= 1

    def __str__(self):
        return f"Пошел нахуй из {self.name}"
