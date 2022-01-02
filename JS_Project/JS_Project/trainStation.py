import json

class TrainStation(object):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name 

filename = 'Data\connection_matrix.txt'

def read_place_from_txt():
    list_place = []
    with open(filename) as file:
        for line in file:
            read_tab = line.split(":")
            list_place.append(TrainStation(int(read_tab[0]), read_tab[1].rstrip()))
    return list_place

def write_place_to_txt(self):
    read_place = read_place_from_txt()
    for place in read_place:
        if self.get_name() == place.get_name():
            return False
    text_to_write = str(self.id) + ":" + self.name + "\n"
    with open(filename, 'a') as f:
        f.writelines(text_to_write)
        return True
