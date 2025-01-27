# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?

import csv
class PoemCount():
    def __init__(self, path="poem.txt"):
        self.info = self.get_count(path)

    def get_count(self, path):
        contents = {}
        with open(path, 'r', encoding="utf-8") as f:
            for line in f:
                for w in line.split(' '):
                    w = w.replace('\n', "").replace(",", "").replace('.',"")
                    if w not in contents:
                        contents[w] = 1
                    else:
                        contents[w] += 1
        return contents


p = PoemCount()
print(p.info)



