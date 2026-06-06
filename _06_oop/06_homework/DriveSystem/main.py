from driver import Driver
from car import Car
from menu_ui import MenuUI
from enums import EngineStatus


def main():
    car = Car(EngineStatus.Engine_Off,0 )
    driver = Driver(car)

    menu = MenuUI(driver, car)
    menu.run()

if __name__ == "__main__":
    main()