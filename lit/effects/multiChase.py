import random
name = "Multi-Chase"

start_string = name + " started!"

description = "The string is sequentially covered by random colors with multiple at the same time"

def create_heads(lights, args):
    num_heads = int(args['number'])
    colors = [random.random() for _ in range(0, num_heads)]
    head_locations = [i*(-lights.num_leds//num_heads) for i in range(0, num_heads)]
    return [head_locations, colors]

schema = {
    'speed': {
        'value': {
            'type': 'number',
            'min': 0,
            'max': 100,
            'default': 50
        },
        'user_input': True,
        'required': False
    },
    'number': {
        'value': {
            'type': 'number', #TODO integer type (or step)
            'min': 1,
            'max': 15,
            'default': 3
        },
        'user_input': True,
        'required': False,
        'index': 0
    },
    'heads': {
        'value': {
            'type': 'tuple list',
            'default_gen': create_heads
        },
        'user_input': False
    }
}

def update(lights, step, state):
    heads = state['heads']
    for i in range(len(heads[0])):
        if heads[0][i] >= 0:
            lights.set_pixel_hsv(heads[0][i], heads[1][i], 1, 1)
        heads[0][i] += 1
        if heads[0][i] >= lights.num_leds:
            heads[0][i] = 0
            heads[1][i] = random.random()