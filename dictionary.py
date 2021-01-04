game = {
    'name': 'GTA V',
    'price': 300,
    'hour': 5,
    'online': True,
    'character': ['character 1', 'character 2', 'character 3']
}

if __name__ == "__main__":
    game['price'] = 315
    print(len(game))
    print(game)

    for c in game.get('character'):
        if c in 'character 2':
            print(c)
            break
