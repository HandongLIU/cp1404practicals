# handong Liu


COLOUR_CODES = {"Bright Green": "#66ff00", "AntiqueWhite": "#faebd7",
                "Cadmium Green": "#006b3c", "Buff": "#f0dc82",
                "AntiqueWhite3": "#cdc0b0", "Celadon": "#ace1af",
                "Carnelian": "#b31b1b", "Orange Peel": "#ff9f00",
                "Coffee": "#6f4e37", "Orchid Pink": "#f2bdcd",
                "PaleGreen": "#98fb98", "Red1": "#ff0000", "SkyBlue": "#87ceeb",
                "SlateGray": "#708090", "Snow1": "#fffafa"}
colour_name = input("Enter a colour name: ")
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")