
HEADER="""
GIMP Palette
Name: wodore_colors
#
"""

# source
colors= {
    "primary": {
      100: "#8fd6b7",
      200: "#6DC59F",
      300: "#4DB286",
      400: "#408C6B",
      500: "#346751",
      600: "#2A5B46",
      700: "#224E3B",
      800: "#1A4231",
      900: "#133426",
    },
    "secondary": {
      100: "#B2D7E1",
      200: "#AAD7DE",
      300: "#A7DADD",
      400: "#A3DBD9",
      500: "#9DD9D2",
      600: "#68C5C1",
      700: "#3F9DA2",
      800: "#29626B",
      900: "#153037",
    },
    "accent": {
      100: "#E8C563",
      200: "#E3C04F",
      300: "#DEBD3A",
      400: "#D8BB27",
      500: "#BFAB25",
      600: "#AD951F",
      700: "#998019",
      800: "#846A15",
      900: "#6F5610",
    },
    "positive": {
      100: "#8CE9C7",
      200: "#6EE3B0",
      300: "#50DD96",
      400: "#32D77A",
      500: "#25BF5E",
      600: "#21AB5D",
      700: "#1D9559",
      800: "#198053",
      900: "#156B4B",
    },
    "negative": {
      100: "#F2ACAB",
      200: "#EB817F",
      300: "#E55A57",
      400: "#DF3330",
      500: "#BF211E",
      600: "#AC1D1B",
      700: "#961A17",
      800: "#801614",
      900: "#6E1311",
    },
    "info": {
      100: "#ABCFF2",
      200: "#84B8EB",
      300: "#5EA1E3",
      400: "#398ADA",
      500: "#2673BF",
      600: "#1E61A4",
      700: "#174F87",
      800: "#113D69",
      900: "#0B2B4B",
    },
    "warning": {
      100: "#FF8593",
      200: "#FF707C",
      300: "#FF6169",
      400: "#FF4D4F",
      500: "#FF3C38",
      600: "#FF0F13",
      700: "#E6000B",
      800: "#B8000F",
      900: "#8F0011",
    },
    "dark": {
      200: "#315E47",
      300: "#264A38",
      400: "#1C3629",
      500: "#112119",
      600: "#101E17",
      700: "#0E1B14",
    },
    "dark-page": {
      500: "#0a140f"
    },
    "black": {
      100: "#575757",
      200: "#4A4A4A",
      300: "#3B3B3B",
      400: "#2B2B2B",
      500: "#1C1C1C",
      600: "#0F0F0F",
      700: "#000000",
    },
    "white": {
      500: "#FFFFFF",
      600: "#FCFCFC",
      700: "#FAFAFA",
      800: "#F7F7F7",
    }
}


def hex_to_rgb(hex):
    hex = hex.replace('#','')
    rgb = []
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)

print(HEADER.strip())
# main colors
for name, shades in colors.items():
    color = shades.get(500)
    rgb_color = ' '.join([f"{i:>3}" for i in hex_to_rgb(color)])
    print(f"{rgb_color:<12} {name}")
for name, shades in colors.items():
    print(f"# {name}:")
    for shade, color in shades.items():
        rgb_color = ' '.join([f"{i:<3}" for i in hex_to_rgb(color)])
        print(f"{rgb_color:<12} {name}-{shade}")
