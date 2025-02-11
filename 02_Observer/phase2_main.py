import phase2_weatherdata as wd
import phase2_displaydevice as dd

weatherdata = wd.WeatherData()
currentDisplay = dd.currentConditionsDisplay(weatherdata)
statisticsDisplay = dd.statisticsDisplay(weatherdata)
forecastDisplay = dd.forecastDisplay(weatherdata)

weatherdata.setMesurements(80,65,30)
weatherdata.setMesurements(70,50,80)
weatherdata.setMesurements(90,80,70)
