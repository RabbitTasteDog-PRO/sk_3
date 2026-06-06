from enums import EngineStatus
import car


class Driver:
    def __init__(self, car: car.Car):
        self.__car = car

    # 운전자는 시동걸기/끄기,
    def engine_on_off(self, engine_status: EngineStatus):
        if self.__car is None:
            return "자동차가 등록되지 않았습니다."

        return self.__car.set_engine_on_off(engine_status)

    # 엔진 상태 가져오기
    def get_engine_status(self):
        if self.__car is None:
            return EngineStatus.Engine_Off

        return self.__car.get_engine_status()

    # 악셀 또는 브레이크를 밟을 수 있습니다.
    # 운전자가 악셀을 밟으면, 자동차는 10km/h씩 가속할 수 있습니다.
    # 운전자가 브레이크를 밟으면, 자동차는 10km/h씩 감속할 수 있습니다.
    def accelerationUpDown(self, speed: int):
        if self.__car is None:
            return "자동차가 등록되지 않았습니다."

        return self.__car.set_accelateral(speed)

    # 운전자가 시동을 끄면, 자동차는 더이상 움직일 수 없습니다. (시동이 꺼진 상태)

    def __str__(self):
        return "운전자"