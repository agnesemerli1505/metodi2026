from datetime import datetime , timedelta

birth= input('scrivi la tua data di nascita separando con - giorno mese e anno')
orario= input(' a che ora sei nato? ')

ora= datetime.now()
birth= datetime.strptime(birth, "%d-%m-%Y")
orario= datetime.strptime(orario, "%H:%M:%S")

print( 'data di nascita: ', birth)
print( 'anno: ' , birth.year)
print(' secondi: ', birth.second)

myage= ora.year - birth.year
print(' tu hai ', myage, ' anni')
myday= ora.day - birth.year
print( myday , ' giorni ')


