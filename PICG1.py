#Primeira Lista PIGC

#Imports necessarios
import matplotlib.pyplot as plt
import matplotlib.image as npimg
import numpy as np

#_____________Funcao imread (segunda questao)
def imread (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print img #Verificando conversao da imagem

#    plt.imshow(img) #Convertendo ndarray para pyplot
#    plt.show()  #imprimindo imagem como imagem

#_____________Funcao nchannels (terceira questao)
def nchannels (imagem): #inserindo imagem por parametro
    img = npimg.imread(imagem) #Convertendo a imagem para ndarray
    print len(img[1])




def size (imagem):
    img = npimg.imread(imagem)
    le = img.shape

    print le

#testando funcoes
imread ('gostosa.jpg') #primeira questao letra a
imread ('gostosa.tif') #primeira questao letra b
imread ('50x50.gif') #primeira questao letra c
#nchannels('gostosa.tif')
#nchannels('gostosa.jpg')
#size('gostosa.jpg')
