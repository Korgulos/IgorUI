
class Color:
    def __init__(self, color_id, color_name, color_color):
        self.color_id = color_id
        self.color_name = color_name
        self.color_color = color_color


colors = []
read = Color(1, "Crvena", "background-color:rgb(255,0,0)")
colors.append(read)
blue = Color(2, "Plava", "background-color:rgb(0,0,255)")
colors.append(blue)
yellow = Color(3, "Žuta", "background-color:rgb(255,255,0)")
colors.append(yellow)
purple = Color(4, "Ljubičasta", "background-color:rgb(128,0,255)")
colors.append(purple)
green = Color(5, "Zelena", "background-color:rgb(0,255,0)")
colors.append(green)
orange = Color(6, "Narandžasta", "background-color:rgb(255,128,0)")
colors.append(orange)
white = Color(7, "Bela", "background-color:rgb(255,255,255)")
colors.append(white)
black = Color(8, "Crna", "background-color:rgb(0,0,0)")
colors.append(black)
