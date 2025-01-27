# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?

import csv
class NewYorkWeather():
    def __init__(self, csv_path="nyc_weather.csv"):
        self.info = self.get_weather(csv_path)
        self.temperatures = [float(i[1]) for i in self.info]
        self.info_dict = {e[0]: e[1] for e in self.info}


    def get_weather(self, csv_path) -> list:
        with open(csv_path, "r") as f:
            r = csv.reader(f, )
            info_list =[(i[0], i[1]) for i in r]
            info = info_list[1:]
        return info
    
    def __getitem__(self, key):
        return self.info_dict[key]


    def get_average_temperature(self, number_of_day):
        return sum(self.temperatures[:number_of_day]) / float(number_of_day)   
    
    def get_max_temperature(self, number_of_day):
        return max(self.temperatures[:number_of_day])
        

n = NewYorkWeather()
print(n.info)

print(n.get_average_temperature(7))
print(n.get_max_temperature(10))
print(n['Jan 9'])
print(n['Jan 4'])



