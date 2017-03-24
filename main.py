# -*- coding: utf-8 -*-

__author__ = 'gianlucafilippone'

import time

import Models
import Utils

strings_filename = "database/inputstring.txt"
matrix_filename = "database/score_matrix.txt"
database_filename = "database/strings_big.txt"

def scoreAlignment(scoreMatrix, inputString, comparingString):
    score = 0;
    for x, y in zip(inputString, comparingString):
        score += scoreMatrix.valueOf(x, y)
    return score

def getStringShifts(string):
    shifts = []
    for i in range(len(string)):
        shifts.append(string[i:]+string[:i])
    return shifts

start_program_time = time.time()

scoreMatrix = Models.ScoreMatrix.importScoreMatrix(matrix_filename)
database = Models.Database.initDatabase(database_filename)
inputString = Utils.importString(strings_filename)

end_acquiring_database_time = time.time()
acquiring_database_time = end_acquiring_database_time - start_program_time

print ("Acquiring database time: " + str(acquiring_database_time))

bestString = ""
bestAlignment = ""
bestScore = 0
bestIndex = 0

bestAlignmentTime = 0
alignmentTested = 0
improvementFound = 0
iterationsDone = 0

iterator = database.iterator()

algorithm_start_time = time.time()

while iterator.hasNext():
    currentComparingString = iterator.next()
    found_better_alignment = False

    iterationsDone += 1
    alignment_start_time = time.time()

    for currentComparingShift in getStringShifts(currentComparingString):
        currentScore = scoreAlignment(scoreMatrix, inputString, currentComparingShift)
        alignmentTested += 1
        if currentScore > bestScore:
            bestString = currentComparingString
            bestAlignment = currentComparingShift
            bestScore = currentScore
            bestIndex = alignmentTested
            improvementFound += 1

    alignment_end_time = time.time()

    if found_better_alignment:
        bestAlignmentTime = (alignment_end_time - alignment_start_time)

algorithm_end_time = time.time()

algorithm_time = algorithm_end_time - alignment_start_time

print("Best alignment found:")
print(bestString)
print("Score: " + str(bestScore))

print("\nTested " + str(iterationsDone) + " sequences with " + str(alignmentTested) + " alignments in total")
print("Solution improved " + str(improvementFound) + " times")
print("Best solution found after " + str(bestIndex) + " iterations")

print("\nBest sequence alignment time: " + str(bestAlignmentTime))
print("Total time: " + str(algorithm_time))