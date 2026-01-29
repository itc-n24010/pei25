commands = ['forward', 'back', 'Back', 'turn_left']

for cmd in commands:
    match cmd:
        case 'forward':
            print('前へ移動')
        case 'back':
            print('後ろへ移動')
        case 'turn_right':
            print('右へ回る')
        case 'turn_left':
            print('左へ回る')
        case x:
            print(x + 'は存在しないコマンド')
