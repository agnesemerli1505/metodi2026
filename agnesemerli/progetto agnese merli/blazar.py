
import matplotlib.pyplot as plt
import pandas as pd
from sorgenti import Sorgente

# J1229.0+0202
df1_sett = pd.read_csv('4FGL_J1229.0+0202_weekly_17_11_2026.csv') 
df1_mens = pd.read_csv('4FGL_J1229.0+0202_monthly_17_11_2026.csv')

# J1555.7+1111
df2_sett = pd.read_csv('4FGL_J1555.7+1111_weekly_17_11_2026.csv')
df2_mens = pd.read_csv('4FGL_J1555.7+1111_monthly_17_11_2026.csv')

# 4FGL_J2202.7+4216
df3_sett = pd.read_csv('4FGL_J2202.7+4216_weekly_17_11_2026.csv')
df3_mens = pd.read_csv('4FGL_J2202.7+4216_monthly_17_11_2026.csv')

# 4FGL_J2253.9+1609
df4_sett = pd.read_csv('4FGL_J2253.9+1609_weekly_17_11_2026.csv')
df4_mens = pd.read_csv('4FGL_J2253.9+1609_monthly_17_11_2026.csv')

# sorgenti
s1 = Sorgente(df1_sett, df1_mens, 'J1229.0+0202')
s2 = Sorgente(df2_sett, df2_mens, 'J1555.7+1111')
s3 = Sorgente(df3_sett, df3_mens, 'J2202.7+4216')
s4 = Sorgente(df4_sett, df4_mens, 'J2253.9+1609')

# sorgente a piacere: grafico e serie sintetiche
s3.grafico()

s3.graf_sintetico(
    s3.x_settimanale,
    s3.y_settimanale
)
