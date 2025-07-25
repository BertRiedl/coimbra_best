import time

from src.record_tools import Device
import keyboard

# Change these variables to suit your hypothesis
TIME_TRIAL = 30
NUMBER_OF_QUESTIONS = 20


def main():

    # Bitalino configuration
    bitalino_address = "00:21:08:35:15:17" # “/dev/tty.BITalino-XX-XX”
    bitalino_sampling_rate = 1000
    bitalino_channels = [0, 1, 2]

    session_id = input("Session ID: ")
    device = Device(bitalino_address, bitalino_sampling_rate, bitalino_channels, session_id)

    # Starting session acquisition
    print("Start session acquisition\n")
    device.start()
    time.sleep(TIME_TRIAL)

    question = 1
    while question <= NUMBER_OF_QUESTIONS:
        device.state = "q"
        print(f"Question {question}!")
        print("Waiting response...")

        key = keyboard.read_key()   # Block
        print(f"Answer : {key}\n")  # Select a key to identify a truth or lie block
        device.state = key
        time.sleep(20)
        time.sleep(TIME_TRIAL)
        question += 1

    device.state = "q"
    device.stop()

    print("Ending session")


if __name__ == '__main__':
    main()
