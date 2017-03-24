# -*- coding: utf-8 -*-

import Models
from datetime import datetime

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

def printResults(output_filename, database_filename, matrix_filename, string_filename, results):
    output_file = open(output_filename, 'w')

    output_file.write("*****GLOBAL PAIRWISE ALIGNMENT RESULTS*****")
    output_file.write("\n(Output date: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ")\n")

    output_file.write("\nDatabase file: " + database_filename)
    output_file.write("\nScore matrix file: " + matrix_filename)
    output_file.write("\nString input file: " + string_filename)
    output_file.write("\n")

    output_file.write("\nTested " + str(results.metrics.iterations) + " sequences with " + str(
        results.metrics.alignmentsTested) + " alignments in total")
    output_file.write("\n")

    output_file.write("\nInput String:\n")
    output_file.write(results.inputString)

    output_file.write("\n\nBest sequence found:\n")
    output_file.write(results.bestString)
    output_file.write("\n")
    output_file.write("\nShift value: " + str(results.shiftValue))
    output_file.write("\nScore: " + str(results.score))
    output_file.write("\n")

    output_file.write("\nAlignment:\n")
    if results.shiftValue < 0:
        for i in range(-1*(results.shiftValue)):
            output_file.write(" ")
    output_file.write(results.inputString)
    output_file.write("\n")
    if results.shiftValue > 0:
        for i in range(results.shiftValue):
            output_file.write(" ")
    output_file.write(results.bestString)

    output_file.write("\n\nSequence alignment time: " + str(round(results.metrics.bestAlignmentTime, 3)) + " seconds")
    output_file.write("\nTotal algorithm time: " + str(round(results.metrics.totalTime, 3)) + " seconds")