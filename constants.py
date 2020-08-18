SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1100

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

ORIGINAL_CAPTION = "Welcome to Allripe"

# Colors 
# 	           R    G    B
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FOREST_GREEN = (31, 162, 35)
BLUE = (0, 0, 255)
SKY_BLUE = (39, 145, 251)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
NEAR_BLACK = (19, 15, 48)
COMBLUE = (233, 232, 255)
GOLD = (255, 215, 0)
GREY = (195, 187, 187)
BROWN = (128, 64, 0)

# User constante

user_left = 'move left'
user_right = 'move right'
user_up = 'move up'
user_down = 'move down'
user_open = 'open object'
user_contact = 'activar chat'

coord_x = 550
coord_y = 350

Start_position = (coord_x, coord_y)
user_sprite = 'imagen user'
id_user = 'id user'

access = False
usuario = "Dirk"
usuario2 = "Alex"

UserDict = {
    'Dirk': ('Dirk', "Welcome", 'imagenes/Dirk.png'),
    'Alex': ('Alex', "Welcome", 'imagenes/Alex.png'),
    'Claire': ('Claire', "Welcome", 'imagenes/Claire.png'),
    'Sal': ('Sal', "Welcome", 'imagenes/Sal.png')
}

Toolshop_list = ["TSroom1", "TSroom2", "TSroom3", "TSroom4", "TSroom5",
                 "TSroom6", "TSroom7", "TSroom8", "TSroom9", "TSroom10"]

CarbonCap_list = ["CCroom1", "CCroom2", "CCroom3", "CCroom4", "CCroom5",
                  "CCroom6", "CCroom7", "CCroom8", "CCroom9", "CCroom10"]

FSC_list = ["FSCroom1", "FSCroom2", "FSCroom3", "FSCroom4", "FSCroom5",
            "FSCroom6", "FSCroom7", "FSCroom8", "FSCroom9", "FSCroom10"]

ED_list = ["EDroom1", "EDroom2", "EDroom3", "EDroom4", "EDroom5",
           "EDroom6", "EDroom7"]

FoodLab_list = ["FLroom1", "FLroom2", "FLroom3", "FLroom4", "FLroom5",
                "FLroom6", "FLroom7", "FLroom8", "FLroom9", "FLroom10"]

BIA_list = ["BIAroom1", "BIAroom2", "BIAroom3", "BIAroom4", "BIAroom5",
            "BIAroom6", "BIAroom7", "BIAroom8", "BIAroom9"]

Seccion_list = ['WelcomeSeccion', 'Toolshop', 'SeeingSpace',
                'CarbonCapture', 'EdibleDigital', 'FoodLab',
                'FoodSupplyChain', 'BIA', 'Exit']

Seccion_dict = {
    'WelcomeSeccion': ['imagenes/AXC.png', BROWN],
    'SeeingSpace': ['imagenes/AXC.png', GOLD],
    'Toolshop': ["imagenes/AXC Toolshop.png", PURPLE, Toolshop_list, 350, 200],
    'CarbonCapture': ["imagenes/AXC Toolshop.png", BLACK, CarbonCap_list],
    'EdibleDigital': ["imagenes/AXC Toolshop.png", YELLOW, ED_list],
    'FoodLab': ["imagenes/AXC Toolshop.png", RED, FoodLab_list],
    'FoodSupplyChain': ["imagenes/AXC Toolshop.png", ORANGE, FSC_list],
    'BIA': ["imagenes/AXC Toolshop.png", GREEN, BIA_list]
}

print(Seccion_dict['WelcomeSeccion'][0])

coord_room = {
    'roomtype1': [(424, 70), (674, 70), (851, 246), (851, 496), (674, 673), (424, 673), (248, 496), (248, 246)],
    'roomtype2': [550, 400],
    'roomtype3': [(150, 150), (950, 150), (950, 650), (150, 650)],
    'roomtype4': [(150, 150), (950, 150), (950, 650), (150, 650)],
    'roomtype5': [(150, 150), (950, 150), (950, 650), (150, 650)],
    'roomtype6': [(150, 150), (950, 150), (950, 650), (150, 650)],
    'roomtype7': [(150, 150), (950, 150), (950, 650), (150, 650)],
    'roomtype8': [(150, 150), (950, 150), (950, 650), (150, 650)]
}
coord_start = {
    # start position [door in x, door in y, door out x, door out y,]
    'roomtype1': [550, 350, 550, 350],
    'roomtype2': [525, 600],
    'roomtype3': [180, 350, 850, 350],
    'roomtype4': [180, 350, 850, 350],
    'roomtype5': [180, 350, 850, 350],
    'roomtype6': [180, 350, 850, 350],
    'roomtype7': [180, 350, 850, 350],
    'roomtype8': [180, 350, 850, 350]
}
Room_dict = {
    'WelcomeArea': ('Welcome Area', 'roomtype1'),

    'SeeingRoom': ('Seeing Room', 'roomtype2'),

    "TSroom1": ("Toolshop", 'roomtype3'),
    "TSroom2": ("Toolshop-Ideas", 'roomtype3'),
    "TSroom3": ("Toolshop-Concept sketches", 'roomtype3'),
    "TSroom4": ("Toolshop-CAD", 'roomtype3'),
    "TSroom5": ("Toolshop-Tools", 'roomtype3'),
    "TSroom6": ("Toolshop-Element propertype", 'roomtype3'),
    "TSroom7": ("Toolshop-Integrated propertype", 'roomtype3'),
    "TSroom8": ("Toolshop-ITM", 'roomtype3'),
    "TSroom9": ("Toolshop-TEST", 'roomtype3'),
    "TSroom10": ("Toolshop-Appoval", 'roomtype3'),

    "BIAroom1": ("BIA ", 'roomtype8'),
    "BIAroom2": ("BIA-Site Analysis", 'roomtype8'),
    "BIAroom3": ("BIA-Multiple Idea Rooms", 'roomtype8'),
    "BIAroom4": ("BIA-Concept Sketches", 'roomtype8'),
    "BIAroom5": ("BIA-CAD", 'roomtype8'),
    "BIAroom6": ("BIA-Physical prototypes", 'roomtype8'),
    "BIAroom7": ("BIA-3 in Plans", 'roomtype8'),
    "BIAroom8": ("BIA-Multiple Test Rooms", 'roomtype8'),
    "BIAroom9": ("BIA-Approval Room", 'roomtype8'),

    "CCroom1": ("Carbon Capture", 'roomtype4'),
    "CCroom2": ("Carbon Capture-Ideas", 'roomtype4'),
    "CCroom3": ("Carbon Capture-Concept", 'roomtype4'),
    "CCroom4": ("Carbon Capture-Data Flows", 'roomtype4'),
    "CCroom5": ("Carbon Capture-Models", 'roomtype4'),
    "CCroom6": ("Carbon Capture-Equations", 'roomtype4'),
    "CCroom7": ("Carbon Capture-Algorithms", 'roomtype4'),
    "CCroom8": ("Carbon Capture-Calculator", 'roomtype4'),
    "CCroom9": ("Carbon Capture-Tests", 'roomtype4'),
    "CCroom10": ("Carbon Capture-Approval", 'roomtype4'),

    "EDroom1": ("Edible Digital", 'roomtype7'),
    "EDroom2": ("Edible Digital- Ideas", 'roomtype7'),
    "EDroom3": ("Edible Digital- Concept sketches", 'roomtype7'),
    "EDroom4": ("Edible Digital- Digital models", 'roomtype7'),
    "EDroom5": ("Edible Digital- In situ", 'roomtype7'),
    "EDroom6": ("Edible Digital-TEST", 'roomtype7'),
    "EDroom7": ("Edible Digital-Appoval", 'roomtype7'),

    "FLroom1": ("FoodLab", 'roomtype6'),
    "FLroom2": ("FoodLab-Ideas", 'roomtype6'),
    "FLroom3": ("FoodLab-Concept sketches", 'roomtype6'),
    "FLroom4": ("FoodLab-Data Flows", 'roomtype6'),
    "FLroom5": ("FoodLab-Tools", 'roomtype6'),
    "FLroom6": ("FoodLab-Element propertype", 'roomtype6'),
    "FLroom7": ("FoodLab-Integrated propertype", 'roomtype6'),
    "FLroom8": ("FoodLab-ITM", 'roomtype6'),
    "FLroom9": ("FoodLab-TEST", 'roomtype6'),
    "FLroom10": ("FoodLab-Appoval", 'roomtype6'),

    "FSCroom1": ("Food Supply Chain", 'roomtype5'),
    "FSCroom2": ("Food Supply Chain-Ideas", 'roomtype5'),
    "FSCroom3": ("Food Supply Chain-Concept sketches", 'roomtype5'),
    "FSCroom4": ("Food Supply Chain-Data Flows", 'roomtype5'),
    "FSCroom5": ("Food Supply Chain-Tools", 'roomtype5'),
    "FSCLroom6": ("Food Supply Chain-Element propertype", 'roomtype5'),
    "FSCroom7": ("Food Supply Chain-Integrated propertype", 'roomtype5'),
    "FSCroom8": ("Food Supply Chain-ITM", 'roomtype5'),
    "FSCroom9": ("Food Supply Chain-TEST", 'roomtype5'),
    "FSCroom10": ("Food Supply Chain-Appoval", 'roomtype5')
}

Doors_WelcomeArea = {
    'Door_Seeing_Space': [(276 + 248, 70), (326 + 248, 70)],
    'Door_Food_SC': [(248, 276 + 70), (248, 326 + 70)],
    'Door_Carbon_Capture': [(603 + 248, 276 + 70), (603 + 248, 326 + 70)],
    'Door_Edible_Digital': [(497 + 248, 532 + 70), (532 + 248, 497 + 70)],
    'Door_FoodLab': [(106 + 248, 532 + 70), (70 + 248, 497 + 70)],
    'Door_Toolshop': [(106 + 248, 70 + 70), (70 + 248, 106 + 70)],
    'Door_Building_Int': [(497 + 248, 70 + 70), (532 + 248, 106 + 70)]
}

# Coord_stripe
up_states = {
    0: (0, 512, 64, 64), 1: (64, 512, 64, 64), 2: (128, 512, 64, 64), 3: (192, 512, 64, 64), 4: (256, 512, 64, 64),
    5: (320, 512, 64, 64), 6: (384, 512, 64, 64), 7: (448, 512, 64, 64), 8: (512, 512, 64, 64)
}
left_states = {
    0: (0, 576, 64, 64), 1: (64, 576, 64, 64), 2: (128, 576, 64, 64), 3: (192, 576, 64, 64), 4: (256, 576, 64, 64),
    5: (320, 576, 64, 64), 6: (384, 576, 64, 64), 7: (448, 576, 64, 64), 8: (512, 576, 64, 64)
}
down_states = {
    0: (0, 640, 64, 64), 1: (64, 640, 64, 64), 2: (128, 640, 64, 64), 3: (192, 640, 64, 64), 4: (256, 640, 64, 64),
    5: (320, 640, 64, 64), 6: (384, 640, 64, 64), 7: (448, 640, 64, 64), 8: (512, 640, 64, 64)
}
right_states = {
    0: (0, 704, 64, 64), 1: (64, 704, 64, 64), 2: (128, 704, 64, 64), 3: (192, 704, 64, 64), 4: (256, 704, 64, 64),
    5: (320, 704, 64, 64), 6: (384, 704, 64, 64), 7: (448, 704, 64, 64), 8: (512, 704, 64, 64)
}
AXC_dict = {
    'AXC': 'Allripe extended campus',
    'NPC': 'Development Pipeline',
    'Development Pipeline': "the process for each of Allripe's six areas",
    'HatBots': "AI system of 6 types, based on 6 thinking hats",
    'NPC': "Non-Player Character, automatic sprites/avatars that operate in AXC",

}