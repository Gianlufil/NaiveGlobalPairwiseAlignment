# -*- coding: utf-8 -*-

__author__ = 'gianlucafilippone'

import Models;

def importScoreMatrix(filename):

    #Import file
    input_file = open(filename, 'r')
    lines = input_file.read().splitlines()
    input_file.close()

    symbolsMap = {}

    #Select the first row and assign to each symbol an index to be used into the substitution matrix
    for index, symbol in enumerate(lines.pop(0)):
        symbolsMap[symbol] = index

    symbolNumber = len(symbolsMap)
    matrix = [ [ 0 for y in range(symbolNumber) ] for x in range(symbolNumber) ]

    for rowIndex, line in enumerate(lines):
        for colIndex, number in enumerate(line):
            matrix[rowIndex][colIndex] = number

    return Models.ScoreMatrix(matrix, symbolsMap)

def importDatabase(filename):

    # Import file
    input_file = open(filename, 'r')
    strings = input_file.read().splitlines()
    input_file.close()
    return Models.Database(strings)

def importString(filename):
    input_file = open(filename, 'r')
    string = input_file.read().splitlines().pop(0)
    input_file.close()
    return string