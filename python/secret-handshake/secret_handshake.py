def commands(binary_str):
    handshakes = []
    task = {0: 'wink', 1: 'double blink', 2: 'close your eyes',
            3: 'jump'}
    for index, value in enumerate(binary_str[::-1]):
        if value == '1':
            if index == 4:
                handshakes = handshakes[::-1]
            else:
                handshakes.append(task[index])
    return handshakes