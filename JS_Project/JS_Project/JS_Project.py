import trainStation

a = trainStation.TrainStation(2, "test2")
b = trainStation.write_place_to_txt(a)
if not b:
    print("FALSE")
else:
    print("TRUE")
b = trainStation.read_place_from_txt()

for c in b:
    print(c.get_id(), c.get_name() )
print(a.get_id(), a.get_name() )