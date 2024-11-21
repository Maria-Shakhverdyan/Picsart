import threading
import time
import queue

log_queue = queue.Queue()

def log_reader(file_path: str):
    """Thread function to read new lines added to the log"""
    try:
        with open(file_path, 'r') as file:
            file.seek(0, 2)
            while True:
                try:
                    line = file.readline()
                    if line:
                        log_queue.put(line)
                    else:
                        time.sleep(0.5)
                except Exception as e:
                    print(f"Error in log_reader: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Unexpected error in log_reader: {e}")

def error_checker():
    """Thread function for checking strings for errors"""
    while True:
        try:
            line = log_queue.get(timeout=1)
            if "ERROR" in line:
                print("Error found:", line.strip())
            log_queue.task_done()
        except queue.Empty:
            pass
        except Exception as e:
            print(f"Error in error_checker: {e}")

def main():
    file_path = 'server_log.txt'
    read_thread = threading.Thread(target=log_reader, args=(file_path,))
    checker_thread = threading.Thread(target=error_checker)

    try:
        read_thread.start()
        checker_thread.start()

        read_thread.join()
        checker_thread.join()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting...")
    except Exception as e:
        print(f"Unexpected error in main: {e}")

if __name__ == "__main__":
    main()
