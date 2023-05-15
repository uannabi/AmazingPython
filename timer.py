
import time

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print("Time remaining: {} seconds".format(remaining_time))
        time.sleep(1)
    
    print("Timer completed!")

# Example usage: Timer for 10 seconds
timer(10)


'''
In the example above, we define a function called timer that takes the number of seconds as an argument. Inside the function, we calculate the end_time by adding the desired number of seconds to the current time using time.time().

Next, we enter a loop that continues until the current time (time.time()) exceeds the end_time. In each iteration of the loop, we calculate the remaining time by subtracting the current time from the end_time, and then we print the remaining time.

The time.sleep(1) statement pauses the execution of the program for 1 second, so the loop iterates once per second.

Once the loop completes, we print a message to indicate that the timer has completed.

In the example usage, we call the timer function with an argument of 10, which sets the timer for 10 seconds. You can adjust the duration of the timer by passing a different value as an argument to the timer function.
'''
