from enums import EngineStatus
import constans


class Car:
    def __init__(self, status: EngineStatus, speed: int):
        # - 자동차는 처음에 대기상태 있어야 합니다. (시동이 꺼진 상태)
        self.__status = EngineStatus.Engine_Off
        self.__speed = 0

    # - 자동차는 운전자에 의해 시동이 걸리고, 이미 시동이 걸려있다면, 또 시동을 걸수는 없습니다.
    # - 자동차는 엔진시작/끝, 가속/감속을 할 수 있습니다.
    def set_engine_on_off(self, engine_status: EngineStatus) -> str:

        if engine_status == EngineStatus.Engine_On:
            if self.__status == EngineStatus.Engine_On:
                return f'이미 시동이 걸려있습니다. : {self.__status}'

            self.__status = EngineStatus.Engine_On
            return f'시동을 걸었습니다. : {self.__status}'

        # - 자동차가 달리는 동안에는 시동을 끌수 없습니다.
        if self.__speed > 0:
            return f"속도가 0일 경우에만 시동을 끌수있습니다. 현재속도 : {self.__speed}"

        if self.__status == EngineStatus.Engine_Off:
            return f'이미 시동이 꺼져있습니다. : {self.__status}'

        self.__status = EngineStatus.Engine_Off
        return f'시동을 껐습니다. : {self.__status}'

    def get_engine_status(self):
        return self.__status

    def get_speed(self):
        return self.__speed

    def set_accelateral(self, speed: int) -> str:
        # - 운전자가 시동을 끄면, 자동차는 더이상 움직일 수 없습니다. (시동이 꺼진 상태)
        if self.__status == EngineStatus.Engine_Off:
            return "시동이 꺼져있습니다."

        # - 최대속도는 200km/h 입니다.
        if speed > 0:
            if self.__speed >= constans.MAX_SPEED:
                return "현재 최고 속도 입니다"

            self.__speed += speed

            if self.__speed > constans.MAX_SPEED:
                self.__speed = constans.MAX_SPEED

        else:
            if self.__speed <= 0:
                return "현재 속도는 0 입니다"

            self.__speed += speed

            if self.__speed < 0:
                self.__speed = 0

        return f'현재 속도는 {self.__speed} 입니다'

    def __str__(self):
        return f'현재 상태 : {self.__status}, 속도 : {self.__speed}'