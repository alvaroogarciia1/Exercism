band_colors:list = ['black', 'brown', 'red', 'orange',
               'yellow', 'green', 'blue', 'violet',
               'grey', 'white']

def value(colors:list):
    return band_colors.index(colors[0])*10 + band_colors.index(colors[1])
