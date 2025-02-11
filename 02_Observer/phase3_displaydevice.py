from abc import ABC, abstractmethod
import phase3_weatherdata as wd

class Observer:
    def update(self, temp, humidity, puressure):
        pass
    
class DisplaElement:
    def display(self):
        pass

class currentConditionsDisplay(Observer, DisplaElement):
    def __init__(self, weatherdata:wd.WeatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.weatherdata = weatherdata
        self.weatherdata.resisterObserver(self)
        
        
    # def update(self, temp, humidity, pressure):
    #     self.temperature = temp
    #     self.humidity = humidity
    #     self.display()

    def update(self):
        self.temperature = self.weatherdata.getTemperature()
        self.humidity = self.weatherdata.getHumidity()
        self.display()
    
    def display(self):
        print("現在の気象状況: 温度 {}°  湿度 {}% ".format(self.temperature, self.humidity))
        
class statisticsDisplay(Observer, DisplaElement):
    def __init__(self, weatherdata: wd.WeatherData):
        self.prev_temperature = 0
        self.prev_humidity = 0
        self.prev_pressure = 0
        self.weatherdata = weatherdata
        self.weatherdata.resisterObserver(self)
        
    # def update(self, temp, humidity, pressure):
    #     if self.prev_temperature !=0:
    #         self.display(temp-self.prev_temperature, humidity-self.prev_humidity, pressure-self.prev_pressure)                 
    #     self.prev_temperature = temp
    #     self.prev_humidity = humidity
    #     self.prev_pressure = pressure

    def update(self):
        current_temperature = self.weatherdata.getTemperature()
        current_humidity = self.weatherdata.getHumidity()
        current_pressure = self.weatherdata.getPressure()
        if self.prev_temperature !=0:
            self.display(current_temperature-self.prev_temperature, 
                         current_humidity-self.prev_humidity, 
                         current_pressure-self.prev_pressure)
        self.prev_temperature = current_temperature
        self.prev_humidity = current_humidity
        self.prev_pressure = current_pressure
    
    def display(self, diff_temp, diff_humidity, diff_pressure):
        print("温度変化:{}".format(diff_temp))
        print("湿度変化:{}".format(diff_humidity))
        print("気圧変化:{}".format(diff_pressure))

class forecastDisplay(Observer, DisplaElement):
    def __init__(self, weatherdata: wd.WeatherData):
        self.weatherdata = weatherdata
        self.weatherdata.resisterObserver(self)
        
    def update(self):
        temp = self.weatherdata.getTemperature()
        humidity = self.weatherdata.getHumidity()
        pressure = self.weatherdata.getPressure()
        mode = (temp+humidity+pressure) % 3
        self.display(mode)
    
    def display(self,mode):
        if mode == 1:
            print("明日は晴れます")
        elif mode == 2:
            print("天気が崩れつつあります")
        elif mode == 0:
            print("天気が回復しつつあります")

if __name__=="__main__":
    import phase3_weatherdata as wd
    weather = wd.WeatherData()
    cond = currentConditionsDisplay(weather)
    stat = statisticsDisplay(weather)
    forecast = forecastDisplay(weather)
    temperature = 25
    humidity = 70
    pressure = 900
    
    for num in range(5):
        import random
        temperature += random.randint(-3,3)
        humidity += random.randint(-5,5)
        pressure += random.randint(-20,20)
        print('-----{}'.format(num+1))
        weather.setMesurements(temperature, humidity, pressure)
        