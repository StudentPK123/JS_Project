#list of cities with railway stations
CITY_LIST = [
    "Kraków",
    "Katowice",
    "Wrocław",
    "Białogard",
    "Ciechanów",
    "Białystok",
    "Giżycko",
    "Gniezno",
    "Poznań",
    "Kalisz",
    "Kielce",
    "Kołobrzeg"
]

#list of train connections between the various cities
RAILWAY_CONNECTIONS = [
    ("Kraków","Gniezno"),
    ("Kraków","Wrocław"),
    ("Gniezno","Wrocław"),
    ("Wrocław","Kalisz"),
    ("Kalisz","Kołobrzeg"),
    ("Kołobrzeg","Poznań"),
    ("Gniezno","Kołobrzeg"),
    ("Kołobrzeg","Kraków"),
    ("Kielce","Poznań"),
    ("Poznań","Giżycko"),
    ("Giżycko","Białystok"),
    ("Białystok","Kalisz"),
    ("Kalisz","Poznań")
]