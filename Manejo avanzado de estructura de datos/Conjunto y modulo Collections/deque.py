from collections import deque

# deque
# funciona como una cola de doble extremo

cola = deque([1, 2, 3, 4, 5])

cola.append(6)
cola.append(7)
cola.appendleft(0)

cola.pop()
cola.popleft()

print(cola)

print('-' * 40)

historial = deque(maxlen=3)
historial.extend([1, 2, 3])
historial.append(4)

print(historial)