from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def resisterObserver(self):
        pass
    
    @abstractmethod
    def removeObserver(self):
        pass
    
    @abstractmethod
    def notifyObservers(self):
        pass

class WeatherData(Subject):
    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    def resisterObserver(self, observer):
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        self.observers.remove(observer)
        
    def notifyObservers(self):
        self.temperature = self.getTemperature()
        self.humidity = self.getHumidity()
        self.pressure = self.getPressure()
        for observer in self.observers:
            observer.update()
    
    def getTemperature(self):
        # import random
        # self.temperature += random.randint(-1,1)
        return self.temperature
    
    def getHumidity(self):
        # import random
        # self.humidity += random.randint(-5,5)
        return self.humidity
    
    def getPressure(self):
        # import random
        # self.pressure += random.randint(-20,20)
        return self.pressure
    
    def measurementsChanged(self):
        self.notifyObservers()
        
    def setMesurements(self, temp, humidity, pressure):
        # テスト用の関数
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurementsChanged()

    
        
if __name__=="__main__":
    import phase3_displaydevice as dd
    
    weather = WeatherData()
    dd.currentConditionsDisplay(weather)
    dd.statisticsDisplay(weather)
    weather.setMesurements(25,55,75)
    weather.setMesurements(27,55,56)
    
    
