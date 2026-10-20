from datetime import datetime , timedelta

birth= input('scrivi la tua data di nascita separando con - giorno mese e anno e orario di nascita separato con :')

ora= datetime.now()
birth= datetime.strptime(birth, "%d-%m-%Y %H:%M:%S")


print( 'data di nascita: ', birth)
print( 'anno: ' , birth.year)
print(' secondi: ', birth.second)

myage= ora.year - birth.year
print(' tu hai ', myage, ' anni')
datediff = ora - birth
print('giorni', datediff.days)
print('secondi', datediff.days*86400)


