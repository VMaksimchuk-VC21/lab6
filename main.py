class TransportCompany:
    def __init__(self, name):
        """Инициализация атрибутов класса"""
        self.__name = name
        self.__vehicles = []

    @property
    def name(self):
        """Уровень доступности атрибута"""
        return self.__name

    @property
    def vehicles(self):
        """Уровень доступности атрибута"""
        return self.__vehicles

    def __str__(self):
        """Вывод информации об объекте"""
        return f"Фирма: {self.name}"

    def add_vehicle(self, vehicle):
        """Добавляет новый транспорт в список."""
        self.__vehicles.append(vehicle)


class Vehicle:
    def __init__(self, model, company):
        """Инициализация атрибутов класса"""
        self.__model = model
        self.__company = company
        self.__drivers = []

    @property
    def model(self):
        """Уровень доступности атрибута"""
        return self.__model

    @property
    def company(self):
        """Уровень доступности атрибута"""
        return self.__company

    @property
    def drivers(self):
        """Уровень доступности атрибута"""
        return self.__drivers

    def __str__(self):
        """Вывод информации об объекте"""
        return f"Транспорт: {self.model} ({self.company.name})"

    def add_driver(self, driver):
        """Добавляет нового водителя в список."""
        self.__drivers.append(driver)


class Driver:
    def __init__(self, name):
        """Инициализация атрибутов класса"""
        self.__name = name

    @property
    def name(self):
        """Уровень доступности атрибута"""
        return self.__name

    def __str__(self):
        """Вывод информации об объекте"""
        return f"Водитель: {self.name}"


def create_company():
    """Создает компанию, запрашивая у пользователя название."""
    name = input("Введите название фирмы: ")
    return TransportCompany(name)


def create_vehicle(company):
    """Создает транспорт, запрашивая у пользователя его модель."""
    model = input("Введите модель транспорта: ")
    return Vehicle(model, company)


def create_driver():
    """Создает водителя, запрашивая у пользователя его имя."""
    name = input("Введите имя водителя: ")
    return Driver(name)


def print_driver(driver):
    """Выводим имя водителя"""
    print(driver)


def menu():
    """Отображает меню и предоставляет пользователю опции для взаимодействия с программой."""
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
            company = create_company()
            print("Фирма создана")
        elif point == "2":
            if company:
                vehicle = create_vehicle(company)
                company.add_vehicle(vehicle)
                print("Транспорт создан")
            else:
                print("Сначала создайте фирму")
        elif point == "3":
            if vehicle:
                driver = create_driver()
                vehicle.add_driver(driver)
                print("Водитель создан")
            else:
                print("Сначала создайте транспорт")
        elif point == "4":
            if company:
                print(company)
            else:
                print("Сначала создайте фирму")
        elif point == "5":
            if vehicle:
                print(vehicle)
            else:
                print("Сначала создайте транспорт")
        elif point == "6":
            if driver:
                print_driver(driver)
            else:
                print("Сначала создайте водителя")
        elif point == "7":
            print("Выход из программы")
            break
        else:
            print("Выберите верный пункт меню")


if __name__ == "__main__":
    menu()