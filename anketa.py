print ("Как твое имя?")
name = input()
print ("Рад видеть тебя,",  name, '!',  sep =' ')
age = int(input ("Сколько тебе лет, " + name + "?"))
print ("А я думал тебе", age + 1, end = " ")
x = age + 1
if x >= 11 and x <=19:
	print("лет")
else:
	if x % 10 >= 2 and x % 10 <=4:
		print ("года")
print ("!")
print (name , " с кем ты сегодня гулял?")
name_1 = (input ())
if name_1 == str("Оля") or str("Лера"):
	print ("Это твоя сестра?")
elif name_1 == ("Боря"):
	print ("Это твой брат?")
else:
	print ("Я не знаю, кто это")
answed = input ()
print ("А ты убрался в комнате перед приходом гостей? Ведь чистота залог здоровья!")
answed_1 = input ()
if answed_1 == str ("да"):
	print ("Молодец")
else:
	print ("Плохо," + name + "комнату надо содержать в чистоте")
print ("Давай поиграем в калькулятор, ты будешь вводить 2 числа, а я буду их складывать")
digit_1 = int(input("Введи первое число: "))
digit_2 = int(input("Введи второе число: "))
summ = digit_1 + digit_2
summ_1 = str (summ)
print ("Ответ: " + summ_1)