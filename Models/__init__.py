# -*- coding: utf-8 -*-
from turtledemo.penrose import dart

__author__ = 'gianlucafilippone'

import Utils;

class ScoreMatrix:

    def __init__(self, matrix, symbolsMap):
        self.matrix = matrix
        self.symbolsMap = symbolsMap

    def valueOf(self, onRow, onCol):
        rowIndex = self.symbolsMap[onRow]
        colIndex = self.symbolsMap[onCol]
        return self.matrix[rowIndex][colIndex]

    def importScoreMatrix(filename):
        return Utils.importScoreMatrix(filename)


class Database:

    def __init__(self, strings):
        self.strings = strings
        self.size = len(strings)

    def askString(self, index):
        if index>=self.size:
            return False
        else:
            return self.strings[index]

    def initDatabase(filename):
        return Utils.importDatabase(filename)

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
