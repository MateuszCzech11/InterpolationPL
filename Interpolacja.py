import matplotlib.pyplot as plt
import numpy as np
class Interpolacja:
    def __init__(self,X:list,Y:list):
        """
        Argumenty X,Y przekazywane do konstruktora to array liczb, których kolejne indeksy (i) w arrayu odpowiadają
        parze współrzędnych (Xi,Yi) gdzie Yi= f(Xi)
        np. X=[1,2,3] Y=[3,2,1] => f(X[0])=Y[0] lub inaczej f(1)=3
        oznacza to, że array X i array Y muszą być tej samej długości, w przeciwnym wypadku wystąpi błąd
        """
        if(len(X)!=len(Y)):
            raise Exception("Obie listy muszą być tej samej długości!")
        self.X = X
        self.Y = Y



    def InterpolacjaLagrangea(self,xp:float) -> float:
        """
        Funkcja tworzy wielomian Lagrange'a i następnie oblicza wartość tego wielomianu L(xp) dla podanej wartości xp (x podane)
        """
        wynik=0.0
        for i in range(len(self.X)):
            węzeł = 1
            for j in range(len(self.X)):
                if i!=j:
                    węzeł*=(xp- self.X[j]) / (self.X[i]-self.X[j])
            wynik += self.Y[i] *węzeł
        return wynik
                    



    def WykresLagrangea(self, zakres:list = None):
        """
        Funkcja wyświetla wykres dla wielomianu interpolacyjnego Lagrange'a dla podanego zakresu
        (zmienna zakres to array liczbowy dwuelementowy, pierwsza liczba to początek zakresu liczb, a druga to koniec)
        Zakresu nie trzeba podawać, wtedy za końcowe punkty wykresu zostaną użyte krańcowe wartości z arraya X
        """
        if zakres:
            wartości_x=np.linspace(zakres[0],zakres[1],1000)
        else:
            wartości_x =np.linspace(min(self.X),max(self.X),1000)

        wartości_funkcji = self.InterpolacjaLagrangea(wartości_x)
        plt.plot(wartości_x,wartości_funkcji,label = "Wielomian Lagrange'a na podst. podanych węzłów")
        plt.title("Interpolacja Lagrange'a")
        plt.scatter(self.X,self.Y, color = "red",label="Podane węzły") #Wyświetla na wykresie węzły interpolacji (punkty) podane w konstruktorze
        plt.axvline(x=0, c="black",linewidth=0.5) #Pozioma linia oznaczająca oś Oy
        plt.axhline(y=0, c="black",linewidth=0.5) #Pionowa linia oznaczająca oś Ox
        plt.legend()
        plt.xlabel("Oś X")
        plt.ylabel("Oś Y")
        plt.show()





    def InterpolacjaNewtona(self,xp:float) -> float:
        """
        Funkcja wykonuje interpolację Newtona na postawie znanych wartości X[i] i odpowiadających im Y[i],
        a następnie oblicza wartość tego wielomianu N(xp) dla podanej wartości xp (x podane)

        dlX - zmienna pomocnicza określająca ilość węzłów (inaczej długość arraya X)
        Yc - kopia wartości funkcji z podanych węzłów - konieczna w celu obliczania N(xp) bez zmiany wartości początkowych listy Y
        """
        dlX = len(self.X)
        Yc = self.Y.copy()
        for j in range(1, dlX):
            for i in range(dlX-1, j-1, -1):
                Yc[i] = (Yc[i] - Yc[i-1]) / (self.X[i] - self.X[i-j])
        wynik = Yc[-1]
        for i in range(dlX-2, -1, -1):
            wynik = Yc[i] + (xp - self.X[i]) * wynik
        return wynik




    def WykresNewtona(self, zakres:list = None):
            """
            Funkcja wyświetla wykres dla wielomianu interpolacyjnego Newtona dla podanego zakresu
            (zmienna zakres to array liczbowy dwuelementowy, pierwsza liczba to początek zakresu liczb, a druga to koniec)
            Zakresu nie trzeba podawać, wtedy za końcowe punkty wykresu zostaną użyte krańcowe wartości z arraya X
            """
            if zakres:
                wartości_x=np.linspace(zakres[0],zakres[1],1000)
            else:
                wartości_x =np.linspace(min(self.X),max(self.X),1000)

            wartości_funkcji = self.InterpolacjaNewtona(wartości_x)
            plt.plot(wartości_x,wartości_funkcji,label = "Wielomian Newtona na podst. podanych węzłów", color = "y")
            plt.title("Interpolacja Newtona")
            plt.scatter(self.X,self.Y, color = "red",label="Podane węzły") #Wyświetla na wykresie węzły podane w konstruktorze
            plt.axvline(x=0, color="black",linewidth=0.5) #Pozioma linia oznaczająca oś Oy
            plt.axhline(y=0, color="black",linewidth=0.5) #Pionowa linia oznaczająca oś Ox
            plt.legend()
            plt.xlabel("Oś X")
            plt.ylabel("Oś Y")
            plt.show()

#Autor: Mateusz Czech UEK 2023
