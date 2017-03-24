# -*- coding: utf-8 -*-

import Models

def importScoreMatrix(filename):

    input_file = open(filename, 'r')
    lines = input_file.read().splitlines()
    input_file.close()

    symbolsMap = {}

    for index, symbol in enumerate(lines.pop(0)):
        symbolsMap[symbol] = index

    symbolNumber = len(symbolsMap)
    matrix = [ [ 0 for y in range(symbolNumber) ] for x in range(symbolNumber) ]

    for rowIndex, line in enumerate(lines):
        for colIndex, number in enumerate(line):
            matrix[rowIndex][colIndex] = int(number)

    return Models.ScoreMatrix(matrix, symbolsMap)


def importDatabase(filename):
    input_file = open(filename, 'r')
    strings = input_file.read().splitlines()
    input_file.close()
    return Models.Database(strings)


def importString(filename):
    input_file = open(filename, 'r')
    string = input_file.read().splitlines().pop(0)
    input_file.close()
    return string
