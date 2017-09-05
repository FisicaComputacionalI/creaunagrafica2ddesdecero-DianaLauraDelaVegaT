import numpy as np 
import pylab as pl
# Numero de semestres
x =(1,2,3,4,5,6,7,8)
# Promedio por semestre
y =(7.5,8,7.75,8.5,7.6,8.25,7.25,7.8)
pl.plot(x,y)
pl.xlabel("Semestre", color='blue')
pl.ylabel("Pomedio", color='red')
 
pl.title('PromedioxSemestre', fontsize=24, color='black',)
pl.savefig('graficaTareaP.png')
pl.show
