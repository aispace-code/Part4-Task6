# Household type, total area and furniture name listThe new house has no furniture at all.
# Furniture has a name and area, of whichBed: 4 square metersWardrobe: 2 square metersTable:
# 1.5 square meters
# Add the above three pieces of furniture to the house
# When printing a house, output is required: household type, total area, remaining area,
# furniture name list.

class House:
    land = 69

    def __init__(self, furniture):
        self.furn_list = furniture
        self.table = furniture_list[0]
        self.bed = furniture_list[1]
        self.wardrobe = furniture_list[2]
        self.total_land = 100
        self.type = ''

    def calc_area(self, table, bed, wardrobe):
        self.total_land = table + bed + wardrobe

    def final_output(self):
        self.type = 'Family'
        self.remaining_area = self.land - self.total_land
        return ''.join((str(self.remaining_area), ' ', ' '.join(self.furn_list), ' ', self.type))


furniture_list = ['Table', 'Bed', 'Wardrobe']
house = House(furniture_list)
house.calc_area(2, 5, 8)
print(house.final_output())
