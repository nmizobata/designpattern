import displaydevice as dd

class WeatherData:
    def __init__(self, temp:int, hum:int, psr:int):
        self.temperature = temp
        self.humidity = hum
        self.pressure = psr
        self.cond = dd.currentConditionsDisplay()
        self.stat = dd.statisticsDisplay()
        self.fore = dd.forecastDisplay()
        
    def getTemperature(self):
        import random
        self.temperature += random.randint(-1,1)
        return self.temperature
    
    def getHumidity(self):
        import random
        self.humidity += random.randint(-5,5)
        return self.humidity
    
    def getPressure(self):
        import random
        self.pressure = random.randint(-20,20)
        return self.pressure
    
    def measurementsChanged(self):
        temp = self.getTemperature()
        humidity = self.getHumidity()
        pressure = self.getPressure()
        self.cond.update(temp,humidity,pressure)
        self.stat.update(temp,humidity,pressure)
        self.fore.update(temp,humidity,pressure)
        
if __name__=="__main__":
    weather = WeatherData(25,75,760)
    for num in range(5):
        weather.measurementsChanged()
        
    
    
