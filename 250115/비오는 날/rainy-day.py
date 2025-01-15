n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Write your code here!
class Weather:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

lst_weather = [Weather(date[i], day[i], weather[i]) for i in range(n)]
lst_weather.sort(key=lambda x: x.date)
for w in lst_weather:
    if w.weather == 'Rain':
        print(w.date, w.day, w.weather)
        break
