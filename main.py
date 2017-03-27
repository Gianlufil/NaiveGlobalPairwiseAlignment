# -*- coding: utf-8 -*-

import time

import Utils
import Models


def extend_strings_to_same_len(s1, s2):
    if len(s1) > len(s2):
        s2.ljust(len(s1), "\0")
    elif len(s1) < len(s2):
        s1.ljust(len(s2), "\0")
    return s1, s2


def align_strings(input_string, comparing_string, shift_value):

    input_string, comparing_string = extend_strings_to_same_len(input_string, comparing_string)

    if shift_value < 0:
        input_string = input_string[:shift_value]
        comparing_string = comparing_string[(-1 * shift_value):]

    elif shift_value > 0:
        input_string = input_string[shift_value:]
        comparing_string = comparing_string[:(-1 * shift_value)]

    return input_string, comparing_string


def score_alignment(substitution_matrix, input_string, comparing_string, shift_value):
    score = 0

    input_string, comparing_string = align_strings(input_string, comparing_string, shift_value)

    for x, y in zip(input_string, comparing_string):
        if x != "\0" and y != "\0":
            score += substitution_matrix.value_of_pair(x, y)
    return score


def global_pairwise_alignment_algorithm(substitution_matrix, database, input_string):

    algorithm_start_time = time.time()

    best_string = ""
    shift_value = 0
    best_score = 0

    best_alignment_time = 0
    alignment_tested = 0
    iterations_done = 0

    iterator = database.iterator()

    while iterator.has_next():
        comparing_string = iterator.next()
        found_better_alignment = False
        iterations_done += 1

        alignment_start_time = time.time()

        max_absolute_shift_value = max(len(input_string), len(comparing_string)) - 1

        for currentShiftValue in range((-1) * max_absolute_shift_value, max_absolute_shift_value + 1):
            current_score = score_alignment(substitution_matrix, input_string, comparing_string, currentShiftValue)
            alignment_tested += 1
            if current_score > best_score:
                best_string = comparing_string
                shift_value = currentShiftValue
                best_score = current_score
                found_better_alignment = True

        alignment_end_time = time.time()

        if found_better_alignment:
            best_alignment_time = (alignment_end_time - alignment_start_time)

    algorithm_end_time = time.time()

    algorithm_time = algorithm_end_time - algorithm_start_time

    metrics = Models.AlgorithmMetrics(best_alignment_time, algorithm_time, alignment_tested, iterations_done)
    results = Models.AlignmentAlgoResult(input_string, best_string, shift_value, best_score, metrics)

    return results


def is_database_valid(database, substitution_matrix):
    iterator = database.iterator()
    while iterator.has_next():
        for char in iterator.next():
            if char not in substitution_matrix.symbols_map:
                return False
    return True


def is_input_string_valid(input_string, substitution_matrix):
    for char in input_string:
        if char not in substitution_matrix.symbols_map:
            return False
    return True

#############################################
#                 Program                   #
#############################################

output_filename = "output.txt"
string_filename = "datasets/input_string.txt"
matrix_filename = "datasets/substitution_matrix.txt"
database_basename = "datasets/databases/database_"
database_extension = ".txt"

size=input("Select database size: ")

database_filename = database_basename + size + database_extension

try:
    substitution_matrix = Utils.import_substitution_matrix(matrix_filename)
    input_string = Utils.import_input_string(string_filename)
except FileNotFoundError:
    print("Error: inputs not found")
    exit()

try:
    database = Utils.import_database(database_filename)
except FileNotFoundError:
    print("Error: database not found")
    exit()

print("\nReading data from " + database_filename)

if not is_database_valid(database, substitution_matrix):
    print("Error: the datasets are not compatible with the substitution matrix")
    exit()

if not is_input_string_valid(input_string, substitution_matrix):
    print("Error: the input string is not compatible with the substitution matrix")
    exit()

print("\nFinding best alignment...")

results = global_pairwise_alignment_algorithm(substitution_matrix, database, input_string)

print("\nTested " + str(results.metrics.iterations) + " sequences with "
      + str(results.metrics.alignments_tested) + " alignments in total")

print("\nBest sequence found:")
print(results.best_string)
print("Shift value: " + str(results.shift_value))
print("Score: " + str(results.score))

print("\nSequence alignment time: " + str(round(results.metrics.best_alignment_time, 3)) + " seconds")
print("Total algorithm time: " + str(round(results.metrics.total_time, 3)) + " seconds")

Utils.print_results(output_filename, database_filename, matrix_filename, string_filename, results)
