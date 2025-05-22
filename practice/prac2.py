import multiprocessing

def calculate_square(number):
    print(f"Square of {number}: {number * number}")

numbers = [1, 2, 3, 4,23,25,13,877]
processes = []
if __name__=="__main__":
    for num in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(num,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()  # Wait for all processes to finish