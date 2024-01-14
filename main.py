class TransportCompany:
    def __init__(self, name):
        self.__name = name
        self.__vehicles = []

    @property
    def name(self):
        return self.__name

    @property
    def vehicles(self):
        return self.__vehicles

    def __str__(self):
        return f"Фирма: {self.name}"

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)


class Vehicle:
    def __init__(self, model, company):
        self.__model = model
        self.__company = company
        self.__drivers = []

    @property
    def model(self):
        return self.__model

    @property
    def company(self):
        return self.__company

    @property
    def drivers(self):
        return self.__drivers

    def __str__(self):
        return f"Транспорт: {self.model} ({self.company.name})"

    def add_driver(self, driver):
        self.__drivers.append(driver)


class Driver:
    def __init__(self):
       return


    def __str__(self):
        return


def create_company():
    return


def create_vehicle():
    return


def create_driver():
    return


def menu():
    company = None
    vehicle = None
    driver = None

    while True:
        print("\nМеню:")
        print("1. Создать фирму")
        print("2. Создать транспорт")
        print("3. Создать водителя")
        print("4. Вывести информацию о фирме")
        print("5. Вывести информацию о транспорт")
        print("6. Вывести информацию о водителе")
        print("7. Выход из программы")

        point = input("Выберите пункт меню: ")

        if point == "1":
            pass
        elif point == "2":
            pass
        elif point == "3":
            pass
        elif point == "4":
            pass
        elif point == "5":
            pass
        elif point == "6":
            pass
        elif point == "7":
            pass
        else:
            pass


if __name__ == "__main__":
    menu()
