import pandas as pd
import classe_prova
url= "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"
tabella= pd.read_csv(url)

prova= classe_prova.dati(tabella)
print(prova)
