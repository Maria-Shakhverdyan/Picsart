import multiprocessing
import csv
import os

def process_file(file_path, result_queue):
    """
    Processes a CSV file to calculate the total number of transactions 
    and the total transaction amount.

    Args:
        file_path (str): Path to the CSV file.
        result_queue (multiprocessing.Queue): Queue to store results (file name, total transactions, total amount).

    Exceptions:
        Handles potential errors such as file reading issues or invalid data formats.
    """
    try:
        total_transactions = 0
        total_amount = 0.0

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    total_transactions += 1
                    total_amount += float(row['Amount'])
                except KeyError:
                    print(f"Error: Missing 'Amount' column in {file_path}")
                except ValueError:
                    print(f"Error: Invalid 'Amount' value in {file_path}")
        
        result_queue.put((os.path.basename(file_path), total_transactions, total_amount))
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
    except Exception as e:
        print(f"Unexpected error while processing file {file_path}: {e}")

def main():
    """
    Main function that finds all CSV files in the current directory,
    processes them using multiprocessing, and generates a summary report.

    Exceptions:
        Handles errors such as directory reading issues or unexpected exceptions during processing.
    """
    try:
        directory = './'
        files = [f for f in os.listdir(directory) if f.endswith('.csv')]

        if not files:
            print("No CSV files found in the directory.")
            return

        result_queue = multiprocessing.Queue()
        processes = []

        for file_name in files:
            file_path = os.path.join(directory, file_name)
            process = multiprocessing.Process(target=process_file, args=(file_path, result_queue))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()

        total_transactions = 0
        total_amount = 0.0
        print("Final Report:")
        while not result_queue.empty():
            try:
                file_name, file_transactions, file_amount = result_queue.get()
                print(f"File: {file_name} -> Transactions: {file_transactions}, Total Amount: {file_amount:.2f}")
                total_transactions += file_transactions
                total_amount += file_amount
            except Exception as e:
                print(f"Error while retrieving data from the queue: {e}")

        print(f"\nTotal Transactions: {total_transactions}")
        print(f"Total Transaction Amount: {total_amount:.2f}")
    except Exception as e:
        print(f"Unexpected error in main function: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"Unexpected error in the program: {e}")