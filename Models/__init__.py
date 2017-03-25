# -*- coding: utf-8 -*-


class ScoreMatrix:

    def __init__(self, matrix, symbols_map):
        self.matrix = matrix
        self.symbols_map = symbols_map

    def value_of_pair(self, on_row, on_col):
        row_index = self.symbols_map[on_row]
        col_index = self.symbols_map[on_col]
        return self.matrix[row_index][col_index]


class Database:

    def __init__(self, strings):
        self.strings = strings
        self.size = len(strings)

    def get_string(self, index):
        if index >= self.size:
            return False
        else:
            return self.strings[index]

    def iterator(self):
        return DatabaseIterator(self)


class DatabaseIterator:

    def __init__(self, database):
        self.database = database
        self.watching_index = 0

    def next(self):
        self.watching_index += 1
        return self.database.get_string(self.watching_index - 1)

    def has_next(self):
        return self.watching_index < self.database.size


class AlignmentAlgoResult:

    def __init__(self, input_string, best_string, shift_value, score, metrics):
        self.input_string = input_string
        self.best_string = best_string
        self.shift_value = shift_value
        self.score = score
        self.metrics = metrics


class AlgorithmMetrics:

    def __init__(self, best_alignment_time, total_time, alignments_tested, iterations):
        self.best_alignment_time = best_alignment_time
        self.total_time = total_time
        self.alignments_tested = alignments_tested
        self.iterations = iterations
