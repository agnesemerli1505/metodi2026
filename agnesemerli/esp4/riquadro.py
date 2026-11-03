import pandas as pd
import matplotlib.pyplot as plt
url= "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"
tabella= pd.read_csv(url) 
#print(tabella.columns)
fig, ax = plt.subplots(figsize=(12,6))

ax.errorbar(tabella["TIME"], tabella["PDCSAP_FLUX"], yerr= tabella["PDCSAP_FLUX_ERR"], fmt='o' , markersize=2, capsize=2, elinewidth=1)
ax.set_ylim(1.012*10**6, 1.027*10**6)
ax.set_xlabel("Tempo")
ax.set_ylabel("Flusso (elettroni/s)")
ax.set_title("Flusso luminoso in funzione del tempo")

#plt.savefig("graficoflusso.pdf")

df2=tabella.loc[(tabella["TIME"] >= 952.40) & (tabella["TIME"] <= 952.67)] 

ins_ax = ax.inset_axes([0.65, 0.65, 0.35, 0.35])
ins_ax.errorbar(df2["TIME"], df2["PDCSAP_FLUX"], yerr=df2["PDCSAP_FLUX_ERR"], fmt='o', markersize=2, capsize=2, elinewidth=1)

"""
ins_ax.set_xlim(952.4, 952.67)
ins_ax.set_ylim(1.014, 1.024)
"""
plt.savefig("grafico_con_zoom.pdf")

plt.show()
