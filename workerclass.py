from lqproj import LinkedQueue
from llproj import LinkedList
class Worker:
    def __init__(self,id,name):
        self._name=name
        self._id=id
        self._works=LinkedQueue()
    def __str__(self):
        strg="Name:"+str(self._name)+"\nID  :"+str(self._id)
        return strg
    def addservice(self,service):
        self._works.enqueue(service)
    def removeservice(self):
        self._works.dequeue()
w1=Worker("W01","Ram")
w2=Worker("W02","Krish")
w3=Worker("W03","Shiv")
w4=Worker("W04","Balaji")
w5=Worker("W05","Vicky")
print(w1)
WorkersList=LinkedList()
WorkersList.insert(w1)
WorkersList.insert(w2)
WorkersList.insert(w3)
WorkersList.insert(w4)
WorkersList.insert(w5)
