#Conversor de segundos

segundos = int(input("Por favor, entre com o numero de segundos que deseja converter: "))

#segundos = 178615
#segundos = 178685
minutos = 0
horas = 0
dias = 0


minutos = segundos // 60
segundos = segundos % 60

horas = minutos // 60;
if horas > 0:
    minutos = minutos % horas

dias = horas // 24
if dias > 0:
    horas = horas % dias


print()
print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")

