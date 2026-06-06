import driver
import car
import constans
from enums import EngineStatus


class MenuUI:
    def __init__(self, dri: driver.Driver, c: car.Car):
        self.__dri = dri
        self.__c = c

    def show_menu(self):
        print("-" * 30)
        print("운전 콘솔 프로그램")
        print("-" * 30)
        print("1. 시동 걸기")
        print("2. 시동 끄기")
        print("3. 악셀 밟기")
        print("4. 브레이크 밟기")
        print("5. 자동차 상태 확인")
        print("0. 종료")
        print("-" * 30)

    def run(self):
        while True:
            self.show_menu()
            menu = input("메뉴를 선택하세요 : ")
            if menu == "1":
                print(self.__dri.engine_on_off(EngineStatus.Engine_On))
            elif menu == "2":
                print(self.__dri.engine_on_off(EngineStatus.Engine_Off))

            elif menu == "3":
                print(self.__dri.accelerationUpDown(constans.ACELATER_SPEED))

            elif menu == "4":
                print(self.__dri.accelerationUpDown(-constans.ACELATER_SPEED))

            elif menu == "5":
                print(self.__c)

            elif menu == "0":
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")
