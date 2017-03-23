# -*- coding: utf-8 -*-

__author__ = 'gianlucafilippone'

import Models
import Utils

def scoreAlignment(scoreMatrix, inputString, comparingString):
    score = 0;
    for x, y in zip(inputString, comparingString):
        score += scoreMatrix.valueOf(x, y)
    return score


string_filename = "database/inputstring.txt"
matrix_filename = "database/score_matrix.txt"
database_filename= "database/strings.txt"

scoreMatrix = Models.ScoreMatrix.importScoreMatrix(matrix_filename)
database = Models.Database.initDatabase(database_filename)

inputString = Utils.importString(string_filename);

print(scoreAlignment(scoreMatrix, inputString, database.iterator().next()))