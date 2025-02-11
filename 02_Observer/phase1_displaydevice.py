from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def update(self):
        pass
    
class currentConditionsDisplay(Device):
    def update(self, temp, humidity, pressure):
        print("気温:摂氏{}°, 湿度:{}%, 気圧:{}hpa".format(temp,humidity,pressure))
        
class statisticsDisplay(Device):
    def __init__(self):
        self.prev_temperature = 0
        self.prev_humidity = 0
        self.prev_pressure = 0
        
    def update(self, temp, humidity, pressure):
        
        if self.prev_temperature != 0:
            print("温度変化:{}".format(temp-self.prev_temperature))
            print("湿度変化:{}".format(humidity-self.prev_humidity))
            print("気圧変化:{}".format(pressure - self.prev_pressure))
                  
        self.prev_temperature = temp
        self.prev_humidity = humidity
        self.prev_pressure = pressure

class forecastDisplay(Device):
    def update(self, temp, humidity, pressure):
        import random
        num = random.randint(1,3)
        if num == 1:
            print("明日は晴れます")
        elif num == 2:
            print("天気が崩れつつあります")
        elif num == 3:
            print("天気が回復しつつあります")

if __name__=="__main__":
    cond = currentConditionsDisplay()
    stat = statisticsDisplay()
    forecast = forecastDisplay()
    temperature = 25
    humidity = 70
    pressure = 900
    
    for num in range(5):
        import random
        temperature += random.randint(-3,3)
        humidity += random.randint(-5,5)
        pressure += random.randint(-20,20)
        print('-----{}'.format(num+1))
        cond.update(temperature,humidity,pressure)
        stat.update(temperature,humidity,pressure)
        forecast.update(temperature,humidity,pressure)
    
        