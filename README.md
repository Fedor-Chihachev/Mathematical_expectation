В данной программе представлено решение задачи из Яндекс контест (уровень medium)

Условие задачи:

Вася взял игральную кость и написал на гранях числа 
a1, a2, a3, a4, a5, a6
 
Для генерации случайного числа Вася решил воспользоваться следующим алгоритмом:

Выбрать число k
Подбросить кубик k раз и записать на листик последовательно выпавших чисел bj
Пройтись по списку с конца и вычеркнуть число 
bj , если оно равно bj-1 (b1  всегда останется в последовательности).
Определите математическое ожидание суммы оставшихся в последовательности чисел, если Вася сообщит вам числа ai и k.
​
Обратите внимание, что кубик у Васи честный и все выпадение любой из граней равновероятно. Кроме этого, подбрасывания кубика независимы.

Формат ввода
В первой строке записаны 6 целых чисел 
a1, a2, a3, a4, a5, a6 (1≤ai≤1000).
Во второй строке записано одно число k (1≤k≤1000).
Формат вывода
Выведите одно вещественное число — требуемое по условию задачи математическое ожидание.

Пример 1

Ввод

1 2 3 4 5 6

2

Вывод
6.4166666667
