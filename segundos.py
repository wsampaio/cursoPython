

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

#segundos = 178615
#segundos = 178685


minutos = segundos // 60
segundos = segundos % 60

horas = minutos // 60;
minutos = minutos % horas

dias = horas // 24
horas = horas % dias



print()
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")



#resultado esperado
#print("2 dias, 1 horas, 36 minutos e 55 segundos.")




