import threading
def calc_square(number):
    print('Square:' , number * number)
    result = number * number
    print(result)
def calc_quad(number):
    print('Quad:' , number * number * number * number)
if __name__ == "__main__":
    number = 7
    result=None
thread1 = threading.Thread(target=calc_square, args=(number,))
thread2 = threading.Thread(target=calc_quad, args=(number,))
# Will execute both in parallel
thread1.start()
thread2.start()
# Joins threads back to the parent process, which is this
# program
print(result)

thread1.join()
thread2.join()
# This program reduces the time of execution by running tasks in              parallel
