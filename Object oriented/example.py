class House:
    num_rooms=5
    bathrooms=2
    def cost_evaluating(self,rate):
        cost= rate * self.num_rooms
        return cost
        pass
     # Functionality to calculate the costs from the area of the house

house1 = House()

print(house.num_rooms)
print(House.num_rooms)
house.num_rooms = 7