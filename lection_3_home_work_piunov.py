SLOG1 = 'dupka'    #сложение
SLOG2 = 'zalupka'
print(SLOG1 + SLOG2)

print(SLOG2 * 7)    #дублирование
print(SLOG1 * 5)

len('PITONSLOGNYI')    #длинна строки
print(len('PITONSLOGNYI'))
print(len('zalupka'))

BUKVA = 'dupkazalupka'    #доступ по номеру или индексу
print(BUKVA[2])
print(BUKVA[7])
print(BUKVA[11])

KUSOCHEKSTROKI = 'dupkazalupka'    #извлечение среза (извлечь кусочек строки)
print(KUSOCHEKSTROKI[7:11])
print(KUSOCHEKSTROKI[0:4])

CHISLO1 = 13    #число обычное цельночисловое
CHISLO2 = 14.90    #число с плавающей точкой
CHISLO3 = '14.90'    #строка
print(type(CHISLO1))
print(type(CHISLO2))
print(type(CHISLO3))

SUMMA = 13 + 14.90
print(SUMMA)

SPISOK = ['gopka', 'nogka', 'ruchka', '1234', '3.67']
SLOVNIK = {'dupka': 'zopka', 'babochka': 'metelik', 'velik': 'lisaped'}
KORTEG = tuple('Hello im VOVAN super python developer')
print(type(SPISOK))
print(type(SLOVNIK))
print(type(KORTEG))

NOMERA_DUPOK = [13, 67, 43, 105, 99]    #функция мин и макс в списке
print(min(NOMERA_DUPOK))
print(max(NOMERA_DUPOK))

STROKA1 = 'PITONSLOGNYI'    #функция мин и макс в строках с длинной строки
STROKA2 = 'dupka'
STROKA3 = 'zalupka'
print(min(STROKA1, STROKA2, STROKA3, key=len))
print(max(STROKA1, STROKA2, STROKA3, key=len))

STROKA4 = 'zaluPka'    #не понял почему выдает z, я ж написал большую букву Р(возможно не уловил смысл функции)
print(max(STROKA4))

BUKVI = 'zalup' in 'dupkazalupka'    #оператор принадлежности in и not in
print(BUKVI)

SPISOK_CIFR = 87 in [1, 2, 3, 4, 5]
print(SPISOK_CIFR)

POHAVAT = 'morogenka' not in {'pirogenka', 'shaurma', 'pureshka'}
print(POHAVAT)

OPITUVANNYA = input('how many time in the day you mastrubate?')    #if elif else
mastrubation = int('OPITUVANNYA')
if mastrubation >= 15:
    print('oslepnesh balda')
elif 10 <= mastrubation < 15:
    print('ne uvlekaysya izvrashuga')
else:
    print('krasavchik')    #что я делаю не так? как проверить запустить эту прогу
