from util import getlines

day = 8

data = getlines(day)[0]

def to_layers(all_chars):
    ret = []
    for i in range(0, len(all_chars), 25 * 6):
        ret.append(all_chars[i:i+25*6])
    return ret

layers = to_layers(data)
def rank(layer):
    return len([c for c in layer if c == '0'])

def score(layer):
    return len([c for c in layer if c == '1']) * len([c for c in layer if c == '2'])

image = ['2'] * 150
for layer in layers:
    for i in range(150):
        if image[i] == '2':
            image[i] = layer[i]

i = 0
for c in image:
    print('*' if c == '1' else ' ', end="")
    i += 1
    if i == 25:
        print("")
        i = 0
    

layers = sorted(layers, key=rank)
print(score(layers[0]))