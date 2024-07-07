import time
import threading
# Global variables for the stopwatch
start_time = 0
elapsed_time = 0
is_running = False
def start_stopwatch():
    global start_time, is_running
    start_time = time.time() - elapsed_time
    is_running = True
    print("Stopwatch started.")

def pause_stopwatch():
    global elapsed_time, is_running
    if is_running:
        elapsed_time = time.time() - start_time
        is_running = False
        print("Stopwatch paused.")

def reset_stopwatch():
    global elapsed_time, is_running
    elapsed_time = 0
    is_running = False
    print("Stopwatch reset.")

def display_stopwatch():
    global elapsed_time, is_running

    while True:
        if is_running:
            elapsed_time = time.time() - start_time

        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time % 1) * 1000)

        print(f"\rTime: {minutes:02}:{seconds:02}:{milliseconds:03}", end="")
        time.sleep(0.1)  # Update display every 0.1 seconds
if __name__ == "__main__":
    # Create and start the display thread
    display_thread = threading.Thread(target=display_stopwatch)
    display_thread.start()

    # Main loop for user interaction
    while True:
        print("\nStopwatch Menu:")
        print("1. Start")
        print("2. Pause")
        print("3. Reset")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            start_stopwatch()
        elif choice == '2':
            pause_stopwatch()
        elif choice == '3':
            reset_stopwatch()
        elif choice == '4':
            print("Exiting Stopwatch App.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

    # Wait for the display thread to finish before exiting
    display_thread.join()
