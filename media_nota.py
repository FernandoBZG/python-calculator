nota = 0
num_nota = 0
while True:
	try:
		nota += int(input("Digite sua nota: \n Ou se quiser o resultado digite: Resposta "))
		num_nota += 1
	except:
		print(f"Sua média é {nota/num_nota}")
		break