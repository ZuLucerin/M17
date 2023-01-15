# M17
Module_17
Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.

В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.

Далее программа работает по следующему алгоритму:

Преобразование введённой последовательности в список

Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

 

Подсказка

Помните, что у вас есть числа, которые могут не соответствовать заданному условию. В этом случае необходимо вывести соответствующее сообщение

Ответ компилятора:
C:\Users\Анастасия\AppData\Local\Programs\Python\Python38\python.exe C:\Users\Анастасия\PycharmProjects\TESTSF\venv\17.9_Zueva.py 
Введите последовательность чисел через пробел: 135 82 45 2112 
Введите число: 555
Список до сортировки:  [135, 82, 45, 2112, 555]
Список после сортировки: [45, 82, 135, 555, 2112]

Process finished with exit code 0
