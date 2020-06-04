import threading
import time 
import requests

# Numero de llamadas
numCall = 20

# url de llamada
url = "https://www.your-apirest-to-call.com/"

class apiThread (threading.Thread):
    def __init__(self, name, url):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        t_1 = time.time()
        response = requests.get(url)
        t_2 = time.time()
        print ("%s, status_code = %s, time = %s" % (self.name, response.status_code, (t_2-t_1)))

print ("Iniciando test de estres de api")
print ("Configuradas %s llamadas a la api de forma asíncrona" % (numCall))

threads = []
for x in range(numCall):
    threads.append(apiThread("Llamada %s" % ((x+1)), url))
    threads[-1].start()

# wait for all threads to finish                                            
for t in threads:                                                           
    t.join()  

print ("Exiting Main Thread")