import sys

lines = open(sys.argv[1]).read().split('\n')

seeds = lines[0].split(':')[1].split()

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

"""
range
2

seed numbers
98 99

soil numbers
50 51
"""
def iterate_over(i,working_set):
    for l in lines[i+2:]:
        if (len(l) <= 2) or (':' in l):
            return
        a = l.split()
        for ind,b in enumerate(a): a[ind] = int(b)
        try:
            for index in range(a[0],a[0]+(a[2])):
                working_set.append([index,0])
            for index,num in enumerate(range(a[1],a[1]+(a[2]))):
                working_set[index][1] = num
            return working_set
        except Exception as e:
            print(e)
            pass

for i,line in enumerate(lines[1:]):
    if ':' in line:
        working_set = globals()[line.split()[0].replace('-','_')]
        working_set = iterate_over(i,line,working_set)
        print(working_set)

print(seed_to_soil)
print(soil_to_fertilizer)
print(fertilizer_to_water)
print(water_to_light)
print(temperature_to_humidity)
print(humidity_to_location)

print(seeds)
