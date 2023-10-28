name_1 = input (" Как тебя зовут?: ")
if name_1 == str ("Петя"):
	print ("Привет Петя, как дела?")
elif name_1 == str ("Боря"):
	print ("Боря привет, мне нужен Петя")
elif name_1 == str("Лёля"):
	print ("Золотко скажи Пете, чтобы он почистил зубы")
else: 
  	print ("Позовите Петю")
while name_1 != str ("Петя"):
		name_1 = input (" Как тебя зовут?: ")
		

name_2 = input ("Петя ты умеешь читать?")
if name_2 != str ("да"):
	name_3 = input ("Петя надо учится читать!!!:")
	if name_3 == str ("хорошо"):
		print ("Так держать!")
elif name_2 == str ('да'):
	print ("Молодец!")

name_4 = int (input ("Сколько будет 8+14?: "))
while name_4 != int(22):
	print ("Неправильно")
	name_4 = int(input ("Сколько будет 8+14?: "))
else:
	name_4 == int(22)
	print ("Молодец Петя!")
	
	
print()

        

	
