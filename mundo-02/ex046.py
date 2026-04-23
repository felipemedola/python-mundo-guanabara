import time

print('Preparar lançamento de foguete...')

for c in range(10, -1, -1):
    print(c)
    time.sleep(1)

print('BUM! Lançamento realizado!')