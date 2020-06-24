import pyowm
from pyowm.commons.enums import SubscriptionTypeEnum
owm = pyowm.OWM('0f8337ea1465c60cda11b37567fa4f53', )
city = input('Какой город вас интересует?: ')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather

w.wind()                  
               

print('В городе ' + city + ' сейчас температура: ' + str( w.temperature('celsius')) + "по Цельсию")
print('Влажность в указаном городе: ' + str(w.humidity)  )
