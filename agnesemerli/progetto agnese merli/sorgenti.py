import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Sorgente:

    def __init__(self, df_settimanale, df_mensile, nome=''):
        self.nome = nome
        self.data_settimanale = df_settimanale
        self.data_mensile = df_mensile

        # Dati settimanali (puliti)
        self.x_settimanale, self.y_settimanale = self.pulisci(
            df_settimanale['Julian Date'], df_settimanale['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'])

        # Dati mensili (puliti)
        self.x_mensile, self.y_mensile = self.pulisci(
            df_mensile['Julian Date'], df_mensile['Photon Flux [0.1-100 GeV](photons cm-2 s-1)'])

    def pulisci(self, x, y):
       x = pd.to_numeric(x, errors='coerce').to_numpy(dtype=float) #capire come funziona
       y = pd.to_numeric(y, errors='coerce').to_numpy(dtype=float)

       mask = ~np.isnan(x) & ~np.isnan(y)

       mask = mask & (y > 0)

       return x[mask], y[mask]

    def grafico(self):
        
        plt.figure()
        plt.plot(self.x_settimanale, self.y_settimanale, '.', label='settimanale')
        plt.plot(self.x_mensile, self.y_mensile, 'o', label='mensile')
        plt.xlabel('Julian Date')
        plt.ylabel('Photon Flux')
        plt.title(f'{self.nome} - dati puliti')
        plt.legend()
        plt.show()
        
    def mescola(self, y):
        y = np.array(y, dtype=float) #settimanale o mensile
        n_sim = 1000
        np.random.seed(12143)

        casuali = np.random.random((n_sim, len(y)))
        indici = np.argsort(casuali, axis=1)

        return y[indici]
        
    def graf_sintetico(self, x, y):

        sint = self.mescola(y)

        plt.figure(figsize=(10, 5))

        plt.plot(
            x, y,
            'o',
            color='black',
            label='Reale'
        )

        # le prime 3 serie sintetiche solo per vedere come sono fatte 
        plt.plot(
            x,
            sint[:3].T,
            '.',
            alpha=0.5,
            label='Sintetici'
        )

        plt.xlabel('Julian Date')
        plt.ylabel('Photon Flux')
        plt.title(f'{self.nome} - Dati reali e sintetici')
        plt.legend()
        plt.grid(alpha=0.3)
        plt.show() #questo si apre dopo aver chiuso il grafico reale
        
        
        
        
        
        
        
        
        
        
        
        
