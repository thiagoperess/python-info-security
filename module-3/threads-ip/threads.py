from threading import Thread
from time import sleep

def car(velocity, pilot):
    path_car = 0
    while path_car <= 100:
        print(f'O piloto {pilot} já percorreu {path_car}Km')
        path_car += velocity
        sleep(0.5)


thread_car_one = Thread(target=car, args=[1, 'Python']) 
thread_car_two = Thread(target=car, args=[2, 'Thiago']) 

thread_car_one.start()
thread_car_two.start()

