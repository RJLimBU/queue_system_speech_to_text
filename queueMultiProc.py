from multiprocessing import Process, Lock, Queue, Lock
import queue


def proc(q):
	num = q.get()
	print("Hello from item %d." % num)
	print("item %d running" % num)
	

if __name__ == '__main__':
	
	q = Queue()


	# p = Process(target=proc, args=(q,))
	# p.start()
	for i in range(10):
		p = Process(target=proc, args=(q,))
		p.start()

	for item in range(10):
		q.put(item)

	#print("before join")
	print(p.name)
	
	p.join()
