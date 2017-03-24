# -*- coding: utf-8 -*-


import time
import Utils
import Models


def extendStringsToSameLen(s1, s2):
    if len(s1) > len(s2):
        s2.ljust(len(s1), "\0")
    elif len(s1) < len(s2):
        s1.ljust(len(s2), "\0")
    return s1, s2


def alignStrings(input, comparing, shiftValue):

    input, comparing = extendStringsToSameLen(input, comparing)

    if shiftValue < 0:
        input = input[:shiftValue]
        comparing = comparing[(-1*shiftValue):]

    elif shiftValue > 0:
        input = input[shiftValue:]
        comparing = comparing[:(-1*shiftValue)]

    return input, comparing


def scoreAlignment(scoreMatrix, inputString, comparingString, shiftValue):
    score = 0;

    inputString, comparingString = alignStrings(inputString, comparingString, shiftValue)

    for x, y in zip(inputString, comparingString):
        if x!="\0" and y!="\0":
            score += scoreMatrix.valueOf(x, y)
    return score


def globalPairwiseAlignmentAlgorithm(scoreMatrix, database, inputString):

    bestString = ""
    shiftValue = 0
    bestScore = 0

    bestAlignmentTime = 0
    alignmentTested = 0
    iterationsDone = 0

    iterator = database.iterator()

    algorithm_start_time = time.time()
    while iterator.hasNext():
        comparingString = iterator.next()
        found_better_alignment = False

        iterationsDone += 1
        alignment_start_time = time.time()

        max_absolute_shift_value = max(len(inputString), len(comparingString)) -1

        for currentShiftValue in range((-1) * max_absolute_shift_value, max_absolute_shift_value + 1):
            currentScore = scoreAlignment(scoreMatrix, inputString, comparingString, currentShiftValue)
            alignmentTested += 1
            if currentScore > bestScore:
                bestString = comparingString
                shiftValue = currentShiftValue
                bestScore = currentScore
                found_better_alignment = True

        alignment_end_time = time.time()

        if found_better_alignment:
            bestAlignmentTime = (alignment_end_time - alignment_start_time)

    algorithm_end_time = time.time()

    algorithm_time = algorithm_end_time - algorithm_start_time

    metrics = Models.AlgorithmMetrics(bestAlignmentTime, algorithm_time, alignmentTested, iterationsDone)
    results = Models.AlignmentAlgoResult(inputString, bestString, shiftValue, bestScore, metrics)

    return results


#############################################
#                 Program                   #
#############################################

output_filename = "output.txt"
string_filename = "datasets/input_string.txt"
matrix_filename = "datasets/score_matrix.txt"
database_basename = "datasets/databases/database_"
database_extension = ".txt"

size=input("Select database size: ")

database_filename = database_basename + size + database_extension

try:
    scoreMatrix = Utils.importScoreMatrix(matrix_filename)
    inputString = Utils.importString(string_filename)
except FileNotFoundError:
    print("Error: inputs not found")
    exit()

try:
    database = Utils.importDatabase(database_filename)
except FileNotFoundError:
    print("Error: database not found")
    exit()

print("\nReading data from " + database_filename)
print("\nFinding best alignment...")

results = globalPairwiseAlignmentAlgorithm(scoreMatrix, database, inputString)

print("\nTested " + str(results.metrics.iterations) + " sequences with " + str(results.metrics.alignmentsTested) + " alignments in total")

print("\nBest sequence found:")
print(results.bestString)
print("Shift value: " + str(results.shiftValue))
print("Score: " + str(results.score))

print("\nSequence alignment time: " + str(round(results.metrics.bestAlignmentTime, 3)) + " seconds")
print("Total algorithm time: " + str(round(results.metrics.totalTime, 3)) + " seconds")

Utils.printResults(output_filename, database_filename, matrix_filename, string_filename, results)