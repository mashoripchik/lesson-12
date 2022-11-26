# Множества, неинденксируем тип данных, уникальные значения.
num_set = {7, 2, 3.5, 8.7, 5.9, 6, 9}
print(num_set)
string_set = {"Nicholas", "Michelle", "John", "Mercy"}
print(string_set)
num_set1 = set([1, 2, 3, 4, 5, 6])
print(num_set)
#пустое множество можно создать только при помощи метода set
x = set()
print(type(x))
for i in num_set:
    print(i)
#можно добавить элементы методом add
num_set.add(10)
print(num_set)
#удалить можно методом remove и discard(ошибку не выбивает если нет элемента)
#метод pop удаляет какой-то случайный элемент из множества
string_set.pop()
print(string_set)
#объединение множества можно сделать через метод union или как print(a| b| c), или x.union(y, z)
x = {1, 2, 3}
y = {4, 3, 6}
z = {7, 4, 9}
print(x | y | z)
print(x, y, z)
# пересечение множеств для двух будет через оператор & или через метод intersection()
x = {1, 2, 3}
y = {4, 3, 6}
print(x & y)
print(x.intersection(y))
# разница между множествами через -
A = {1, 2, 3}
B = {4, 3, 6}
print(A - B)
print(B - A)
#метод множеств copy
x = string_set.copy()
print(x)
# метод пересечения множеств isdisjoint
print(string_set.isdisjoint(x))
#метод frozenset неизменяемый тип данных
my_set = frozenset({1, 2, 3, 4})
print(type(my_set), my_set)