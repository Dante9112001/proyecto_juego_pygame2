import time
contador = 3
while True:
    time.sleep(2)
    print(contador)
    contador -= 1
    if contador == 0:
        break