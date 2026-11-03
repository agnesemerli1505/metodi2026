import pandas as pd
import matplotlib.pyplot as plt
url= "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"
tabella= pd.read_csv(url) #data frame del file
print(tabella.columns)
#plt.plot(tabella["TIME"], tabella["PDCSAP_FLUX"], 'o' ) usa le clonne indicate come x e y rispettivamente

plt.errorbar(tabella["TIME"], tabella["PDCSAP_FLUX"], yerr= tabella["PDCSAP_FLUX_ERR"], fmt='o' , markersize=2, capsize=2, elinewidth=1)
plt.xlabel("tempo")							#markersize rende i punti più piccoli, capsize aggiunge i trattini alle estremita
plt.ylabel("flusso (elettroni/s)")	#elinewidth è lo spessore delle sbarre
plt.title("Flusso luminoso in funzione del tempo")

plt.savefig("graficoflusso.pdf")
plt.show()

df2=tabella.loc[(tabella["TIME"] >= 952.40) & (tabella["TIME"] <= 952.67)] 

plt.errorbar(df2["TIME"], df2["PDCSAP_FLUX"], yerr=df2["PDCSAP_FLUX_ERR"], fmt='o', markersize=2, capsize=2, elinewidth=1)

plt.xlabel("tempo") 

plt.ylabel("flusso (elettroni/s)")
plt.title("Zoom del flusso luminoso nel punto di minimo tra 952.40 e 952.67 secondi ")
plt.savefig("zoom_flusso.pdf")

plt.show()
