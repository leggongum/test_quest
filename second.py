'''
Вопрос №2

На языке Python или С++ написать минимум по 2 класса реализовывающих циклический буфер FIFO. 
Объяснить плюсы и минусы каждой реализации.

Оценивается:

1. Полнота и качество реализации
2. Оформление кода
3. Наличие сравнения и пояснения по быстродействию
'''

class CircularBuffer:
    def __init__(self, size: int):
        self.size = size
        self.head = self.tail = 0
        self.buffer = [0]*self.size
    

    def push(self, item):
        if self.is_full():
            self.pop()
            '''
            # Можно сделать буффер расширяемым в случае переполнения (в этом случае нужно удалить 23 строку и раскомментировать строки ниже)
            self.buffer = self.buffer[self.tail%self.size:] + self.buffer[:self.tail%self.size] + [0]*10
            self.head, self.tail = 0, self.size
            self.size += 10
            '''
        self.buffer[self.tail%self.size] = item
        self.tail += 1


    def pop(self) -> int:
        if self.is_empty():
            raise IndexError('Buffer is empty')
        item = self.buffer[self.head%self.size]
        self.head += 1
        return item


    def is_full(self) -> bool:
        return self.tail - self.head == self.size
    
    def is_empty(self) -> bool:
        return self.tail == self.head


### Вторая реализация: ###

from collections import deque

class CircularBuffer_v2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def push(self, item):
        self.buffer.append(item)

    def pop(self):
        if len(self.buffer) == 0:
            raise IndexError("Buffer is empty")
        return self.buffer.popleft()
    
"""
Реализация 1 (Используя список):

Плюсы:
1. Простая реализация с использованием базовых структур данных.
2. Возможность переделать так, чтобы буффер расширялся, когда пытаемся добавить элемент в переполненный буффер.

Реализация 2 (Используя deque):

Плюсы:
1. deque в библиотеке collections оптимизирован для быстрой вставки и удаления элементов; в тесте производительности работает быстрее первой реализации.
2. Поддерживает максимальную емкость (capacity), поэтому не требуется явно обрабатывать переполнение буфера.

Сравнение по быстродействию:
Обе реализации имеют время доступа к элементам O(1) для операций вставки и удаления. 
Но реализация с deque быстрее за счёт того, что часть логики циркулярного буфера написана на C
"""



'''Тест производительности:'''
from time import time

if __name__ == '__main__':

    start = time()
    q = CircularBuffer(150)
    [q.push(i) for i in range(10_000_000)]
    print(time() - start)


    start = time()
    q = CircularBuffer_v2(150)
    [q.push(i) for i in range(10_000_000)]
    print(time() - start)
