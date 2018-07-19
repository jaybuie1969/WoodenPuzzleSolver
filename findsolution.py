import numpy as np
import pylab
import json

gamePieces = []
with open('pieces.json') as jsonData:
    gamePieces = json.load(jsonData)

def recurseToSolution(available, alreadyTaken, gamePieces, permutation):
    if (type(available) != list):
        available = []

    if (type(alreadyTaken) != list):
        alreadyTaken = []

    if (len(available) > 0):
        for i in range(0, len(available)):
            tempList = available.copy()
            alreadyTaken.append(tempList.pop(i))

            permutation = recurseToSolution(tempList, alreadyTaken, gamePieces, permutation)

            alreadyTaken.pop()
    else:
        permutation = testPieces(alreadyTaken, gamePieces, permutation)

        alreadyTaken = []

    return permutation

def testPieces(pieceOrder, pieces, permutation_start):
    permutation = permutation_start

    bitLength = 2 * len(pieceOrder)
    for byteArray in (((np.array(list(range(0, 2 ** bitLength)))[:,None] & (1 << np.arange(bitLength)))) > 0).astype(int):
        configurations = []

        i = 0
        while (i < len(byteArray)):
            pieceOrderIndex = int(i / 2)

            configurations.append(
                {
                    'i': pieceOrderIndex,
                    'index': pieceOrder[pieceOrderIndex],
                    'side': 'front' if (byteArray[i] == 0) else 'back',
                    'orientation': 0 if (byteArray[i + 1] == 0) else 1,
                }
            )

            i = i + 2

        permutation = permutation + 1

        bottomPieceSides = [{'side':pieces[configurations[i]['index']][configurations[i]['side']], 'orientation':configurations[i]['orientation']} for i in range(0, 3)]
        bottom = np.ones((3, 3), dtype=int)
        for i in range(0, 3):
            bottom[i, 0] = bottomPieceSides[i]['side'][0] if (bottomPieceSides[i]['orientation'] == 0) else bottomPieceSides[i]['side'][2]
            bottom[i, 1] = bottomPieceSides[i]['side'][1]
            bottom[i, 2] = bottomPieceSides[i]['side'][2] if (bottomPieceSides[i]['orientation'] == 0) else bottomPieceSides[i]['side'][0]

        topPieceSides = [{'side':pieces[configurations[i]['index']][configurations[i]['side']], 'orientation':configurations[i]['orientation']} for i in range(3, 6)]
        top = np.ones((3, 3), dtype=int)
        for i in range(0, 3):
            top[0, i] = topPieceSides[i]['side'][0] if (topPieceSides[i]['orientation'] == 0) else topPieceSides[i]['side'][2]
            top[1, i] = topPieceSides[i]['side'][1]
            top[2, i] = topPieceSides[i]['side'][2] if (topPieceSides[i]['orientation'] == 0) else topPieceSides[i]['side'][0]

        print(permutation)
        if (((bottom + top) <= 0).all()):
            print('Match Found!')
            print('')

            descriptions = {
                -1: 'hole',
                0: 'flat',
                1: 'knob'
            }

            print('Bottom:')
            for i in range(0, 3):
                print('--------------------')
                print('| ' + descriptions[bottom[i, 0]] + '  ' +  descriptions[bottom[i, 1]] + '  ' + descriptions[bottom[i, 2]] + ' |')
                print('--------------------')

            print('')

            topPieces = []
            for i in range(3, 6):
                temp = pieces[configurations[i]['index']]['front' if (configurations[i]['side'] == 'back') else 'back']
                topPieces.append([(temp[0] if (configurations[i]['orientation'] == 0) else temp[2]), temp[1], (temp[2] if (configurations[i]['orientation'] == 0) else temp[0])])

            print('Top:')
            print('|------|------|-------|')
            print('| ' + descriptions[topPieces[0][0]] + ' | ' + descriptions[topPieces[1][0]] + ' | ' + descriptions[topPieces[2][0]] + ' |')
            print('| ' + descriptions[topPieces[0][1]] + ' | ' + descriptions[topPieces[1][1]] + ' | ' + descriptions[topPieces[2][1]] + ' |')
            print('| ' + descriptions[topPieces[0][2]] + ' | ' + descriptions[topPieces[1][2]] + ' | ' + descriptions[topPieces[2][2]] + ' |')
            print('|------|------|-------|')

            exit()

    return permutation

recurseToSolution(list(range(0, len(gamePieces))), [], gamePieces, 0);
