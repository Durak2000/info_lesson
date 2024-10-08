![image](https://i.ytimg.com/vi/dQw4w9WgXcQ/maxresdefault.jpg)
# Вопросы
1. Чтобы сложить два положительных целых числа, записанные в 8-разрядных ячейках, нужно следовать правилам двоичной арифметики. В 8-разрядной системе представляются числа в формате беззнаковых целых чисел.

Пример сложения двух положительных целых чисел

Допустим, нам нужно сложить два числа: 25 и 70.

**Преобразуем числа в двоичный формат.**
- 25 в двоичном формате: 00011001
- 70 в двоичном формате: 01000110

2. Дополнительный код двоичного числа получается добавлением 1 к младшему значащему разряду его дополнения до 1
3. Переполнение в операции сложения может возникать в зависимости от знаков слагаемых и разрядности представления чисел
4. Арифметико-логическое устройство 
5. Разработка специального устройства для вычитания целых чисел не требуется, потому что вычитание можно эффективно реализовать с использованием существующих операций и архитектуры для сложения
6. -
7.  Сравнение кодов чисел со знаком и без знака требует различных подходов по нескольким причинам, связанным с тем, как числа представлены в каждом случае
8. Поразрядные операции — это операции, которые выполняются непосредственно над отдельными битами (разрядами) чисел. Такие операции часто используются в программировании для работы с двоичными числами, управления битами, а также для оптимизации производительности
9. Арифметические операции и поразрядные операции относятся к различным категориям операций, каждая из которых служит своим целям и имеет свои особенности
10. маска — это битовая последовательность, используемая для управления доступом к отдельным битам данных или для фильтрации информации. Маски применяются в различных сценариях, таких как работа с битами, сетевое взаимодействие и манипуляции с данными.
11. Чтобы сбросить определённый бит (то есть записать в него 0) с использованием битовой маски, необходимо применить операцию **поразрядного И** (AND) с маской, в которой целевой бит установлен в 0, а остальные биты — в 1.
12. Чтобы сбросить 2 младших бита 16-разрядного числа, нужно создать маску, в которой 2 младших бита будут равны 0, а остальные 14 битов — равны 1.  
13. Чтобы установить определённый бит (то есть записать в него 1) с использованием битовой маски, необходимо создать маску, в которой целевой бит будет равен 1, а все остальные биты — равны 0
14. Чтобы установить 2 старших бита 16-разрядного числа, нужно создать маску, в которой 2 старших бита равны 1, а все остальные 14 битов равны 0 
15. Чтобы определить, делится ли число на 4 или на 8, можно использовать логические операции, связанные с побитовой арифметикой. Делимость на 4 и 8 зависит от младших битов числа в двоичном представлении
16. Установка или сброс битов двоичного кода (изменение определённых битов) находит применение в различных практических задачах и областях
17. Операция "исключающее ИЛИ" (XOR, от англ. "exclusive OR") имеет несколько важных и полезных свойств и применений в компьютерных науках и программировании 
18. Шифрование с использованием операции "исключающее ИЛИ" (XOR) — это простой и эффективный способ защиты данных. Ниже представлен алгоритм шифрования, который использует XOR для обработки данных: вместо статической маски будет применяться динамическая маска, изменяющаяся на каждом этапе шифрования. Это позволит сделать шифрование менее предсказуемым
19. Для определения, совпадают ли биты S' (результат сложения) и S (предыдущее значение) в контексте переполнения при сложении, можно использовать операцию "исключающее ИЛИ" 
20. Операция «НЕ» (также известная как логическое отрицание или инверсия) играет ключевую роль в представлении отрицательных чисел в двоичной системе, особенно в методе, известном как **дополнение до двух**.
21. Инверсия всех битов в двоичном числе (или побитовая инверсия) может быть выполнена без использования логической операции «НЕ» с помощью других подходов. Один из самых простых способов — использовать операцию «исключающее ИЛИ» (XOR) с маской, состоящей из всех единиц
22. Сдвиг — это операция, при которой двоичное число сдвигается влево или вправо на заданное количество битов. В результате этой операции все биты числа смещаются на указанное количество позиций, и могут быть добавлены нули или взяты другие значения для заполнения пустых мест в зависимости от типа сдвига
23. Обработка самого старшего и самого младшего битов при различных типах сдвига зависит от направления сдвига и типа сдвига, который используется. Рассмотрим подробно, как обрабатываются эти биты при каждом из типов сдвига.
24.  Логический сдвиг вправо (LSR) удаляет самый младший бит и добавляет 0 в самый старший бит. Это приводит к тому, что при переходе через старший бит происходит потеря информации о знаке. 
25. Логический сдвиг и арифметический сдвиг имеют различия в трактовке старшего бита, что чрезвычайно важно при работе с знаковыми числами, представленными в двоичной системе
26. Арифметический сдвиг влево, в отличие от арифметического сдвига вправо, в общем случае не имеет отдельного определения, так как его поведение аналогично логическому сдвигу влево
27. Арифметический сдвиг вправо (ASR) используется для деления знаковых целых чисел на 2 с учетом знака. Обычно знак сохраняется, поэтому старший бит (знак) копируется в свободный старший разряд при выполнении сдвига.
28. -
# Задачи
1. 00011111 + 00010011 = 00110010

2) 11100001 + 00010011 = 11110100

3) -

4) 1011111 ; 11011111

5) 1100 * 111 = 1010100

6) 11110100 * 111 = 10101100

7) Коля просто догодался пременить переместительный закон для умножения

8) 119 и 136 , 119 и -120

9) код заглавиой = код строчной abdF16

10) код cтрочной = код загалавной or2016

11) Решение коли приводит к неправильным ответам , когда сумма цифр больше 15

12) 4 , 8 , 16 - все они деляться на число 4

13) X and 1=0 , X and 7=0 , X and F = 0

14) a: = a xor b ; b:= b xor a ; a:= a xor b

15) R: = x Shr 16 ; 6: = ( X Sbr 8 ) 8 F16 ; B: = x

16) правильны оба

17) y : = ( X Shi4 ) Shr4 ; z:= ( X Shr4 ) Shi4

18) при использовании 16 - битных данных : EDCO16 , EDF16

19) при использовании 16 - битных данных : 0123(16) 4123(16) 0123(16) OFED(16) CFED(16) FFED(16)

20) EE(16) ; 77(16) = 119 = ( 256 - 18 ) 12 , F7(16) = -9

21) FF(16) , FF(16) , FF(16) ,

22) Z = 1100(2) = 12

    Z = Z ShI 1 = 11000(2)

    X = Z = 11000(2)

    X = X ShI 2 = 1100000(2)



    X = X + Z = 1111000(2) = 120
