from multiprocessing import Process, Lock
import queue

def proc(num):
	print("Hello from %d." % num)
	print("Process %d running" % num)


if __name__ == '__main__':

	for i in range(10):
		p = Process(target=proc, args=(i,))
		p.start()


