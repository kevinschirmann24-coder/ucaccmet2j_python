import json 

Seattle = {}
list = []
january_precipitation_4 = 0
february_precipitation_4 = 0
march_precipitation_4 = 0
april_precipitation_4 = 0
may_precipitation_4 = 0
june_precipitation_4 = 0
july_precipitation_4 = 0
august_precipitation_4 = 0
september_precipitation_4 = 0
october_precipitation_4 = 0
november_precipitation_4 = 0
december_precipitation_4 = 0

with open('ucaccmet2j_python/precipitation.json') as file:
    data = json.load(file)
    #filter for a specific station
    for dict in data:
        for key in dict:
            if dict["station"] == "GHCND:US1WAKG0038":
                list.append(dict)
                #break is used or else for every dictionary analysed 4 total copies of it will be added to my list of dictionaries instead of just the one
                break

#calculate the precipitation of each individual month
for dict in list:
    for key in dict:
        if "2010-01" in dict["date"]: 
            january_precipitation_4 += dict["value"]
        #the code goes through each dictionary four times. Consequently, it sums each daily value 4 times. Therefore I need to divide by 4 to get the accurate monthly rainfall
        january_precipitation = int(january_precipitation_4) / 4
        if "2010-02" in dict["date"]: 
            february_precipitation_4 += dict["value"]
        february_precipitation = int(february_precipitation_4) / 4
        if "2010-03" in dict["date"]:
            march_precipitation_4 += dict["value"]
        march_precipitation = int(march_precipitation_4) / 4
        if "2010-04" in dict["date"]:
            april_precipitation_4 += dict["value"]
        april_precipitation = int(april_precipitation_4) / 4
        if "2010-05" in dict["date"]:
            may_precipitation_4 += dict["value"]
        may_precipitation = int(may_precipitation_4) / 4
        if "2010-06" in dict["date"]:
            june_precipitation_4 += dict["value"]
        june_precipitation = int(june_precipitation_4) / 4
        if "2010-07" in dict["date"]:
            july_precipitation_4 += dict["value"]
        july_precipitation = int(july_precipitation_4) / 4
        if "2010-08" in dict["date"]:
            august_precipitation_4 += dict["value"]
        august_precipitation = int(august_precipitation_4) / 4
        if "2010-09" in dict["date"]:
            september_precipitation_4 += dict["value"]
        september_precipitation = int(september_precipitation_4) / 4
        if "2010-10" in dict["date"]:
            october_precipitation_4 += dict["value"]
        october_precipitation = int(october_precipitation_4) / 4
        if "2010-11" in dict["date"]:
            november_precipitation_4 += dict["value"]
        november_precipitation = int(november_precipitation_4) / 4
        if "2010-12" in dict["date"]:
            december_precipitation_4 += dict["value"]
        december_precipitation = int(december_precipitation_4) / 4


#calculate the total precipitation of that year. CHECK FOR TIMES FOUR
total_precipitation_2010 = january_precipitation + february_precipitation + march_precipitation + april_precipitation + may_precipitation + june_precipitation + july_precipitation + september_precipitation + october_precipitation + november_precipitation + december_precipitation
print(total_precipitation_2010)