# Write a program to implement matrix multiplication. Also #implement multi-threaded matrix multiplication with either one #thread per row or one thread per cell. Analyze and compare their #performance. (Mini Project)
import threading
import time
import random

# Function to perform matrix multiplication
def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not suitable for multiplication.")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Function to perform matrix multiplication with one thread per row
def multiply_row(A, B, result, start_row, end_row):
    for i in range(start_row, end_row):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

# Function for multi-threaded matrix multiplication with one thread per row
def multi_threaded_matrix_multiply(A, B, num_threads):
    if len(A[0]) != len(B):
        raise ValueError("Matrix dimensions are not suitable for multiplication.")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    threads = []
    rows_per_thread = len(A) // num_threads

    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = (i + 1) * rows_per_thread if i < num_threads - 1 else len(A)
        thread = threading.Thread(target=multiply_row, args=(A, B, result, start_row, end_row))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

# Measure the time it takes to perform matrix multiplication
def measure_time(matrix_size, num_threads):
    A = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]
    B = [[random.randint(1, 10) for _ in range(matrix_size)] for _ in range(matrix_size)]

    start_time = time.time()
    result_single = matrix_multiply(A, B)
    end_time = time.time()
    single_threaded_time = end_time - start_time

    start_time = time.time()
    result_multi = multi_threaded_matrix_multiply(A, B, num_threads)
    end_time = time.time()
    multi_threaded_time = end_time - start_time

    print(f"Matrix Size: {matrix_size} x {matrix_size}")
    print(f"Number of Threads: {num_threads}")
    print(f"Single-threaded Time: {single_threaded_time:.6f} seconds")
    print(f"Multi-threaded Time: {multi_threaded_time:.6f} seconds")
    print("Matrices are equal:", result_single == result_multi)
    print()

if __name__ == "__main__":
    matrix_size = 100  # Adjust the matrix size
    num_threads = 4   # Adjust the number of threads

    measure_time(matrix_size, num_threads)
