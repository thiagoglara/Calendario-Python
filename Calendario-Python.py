import calendar

# Obtenha o ano e o mês
ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))

# Imprima o calendário
cal = calendar.month(ano, mes)
print(cal)

#outra forma de mostrar o calendário completo	
#print ("O calendário do ano 2023 é:")
#print (calendar.calendar(2023))
