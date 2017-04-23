import time,queue,threading

def default_compare(a, b):
  if a < b:
    return -1
  elif a > b:
    return 1
  return 0

def sort(array, compare=default_compare):
  sorted = False
  queued_req = queue.Queue()
  while not sorted:
    sorted1 = threading.Thread(target=inner_sort,args=(array,1,compare,queued_req))
    sorted2 = threading.Thread(target=inner_sort,args=(array,0,compare,queued_req))
    sorted2.start()
    sorted1.start()
    sorted2.join()
    print sorted2.getName(),"Doing Even Part"
    sorted1.join()
    print sorted1.getName(),"Doing Odd Part"
    sorted = queued_req.get()
  return array

def inner_sort(array, start_i, compare,queue):
  sorted = True
  for i in range(start_i, len(array) - 1, 2):
    if compare(array[i], array[i + 1]) > 0:
      array[i], array[i + 1] = array[i + 1], array[i]
      sorted = False
  queue.put(sorted)
  #return sorted

def main():
 array = [3,6,1,5,9,7]
 sorted = sort(array)
 #for i in range(len(array)):
 # print array[i]
 for i in range(len(sorted)):
  print sorted[i]

if __name__ == "__main__":
 main()
