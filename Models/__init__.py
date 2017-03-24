# -*- coding: utf-8 -*-

class ScoreMatrix:

    def __init__(self, matrix, symbolsMap):
        self.matrix = matrix
        self.symbolsMap = symbolsMap

    def valueOf(self, onRow, onCol):
        rowIndex = self.symbolsMap[onRow]
        colIndex = self.symbolsMap[onCol]
        return self.matrix[rowIndex][colIndex]


class Database:

    def __init__(self, strings):
        self.strings = strings
        self.size = len(strings)

    def askString(self, index):
        if index>=self.size:
            return False
        else:
            return self.strings[index]

    def iterator(self):
        return DatabaseIterator(self)


class DatabaseIterator:

    def __init__(self, database):
        self.database = database
        self.watchingIndex = 0;

    def next(self):
        self.watchingIndex += 1
        return self.database.askString(self.watchingIndex-1)

    def hasNext(self):
        return self.watchingIndex < self.database.size


class AlignmentAlgoResult:

    def __init__(self, inputString, bestString, shiftValue, score, metrics):
        self.inputString = inputString
        self.bestString = bestString
        self.shiftValue = shiftValue
        self.score = score
        self.metrics = metrics


class AlgorithmMetrics:

    def __init__(self, bestAlignmentTime, totalTime, alignmentsTested, improvements, iterations):
        self.bestAlignmentTime = bestAlignmentTime
        self.totalTime = totalTime
        self.alignmentsTested = alignmentsTested
        self.improvements = improvements
        self.iterations = iterations