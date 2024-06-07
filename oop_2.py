





class Convert_T:

    def __init__(self, T) -> None:
        self.T= T 

    def F_C(self):
        F= self.T
        C = (F-32)*(5/9)
        return C


    def C_F(self):
        C= self.T
        F= (C*(9/5)+32)
        return F
# conver second to minute    
class Converttime1:
    def __init__(self, T) -> None:
        self.T= T 

        
    def S_M(self):
        S= self.T
        M= S*60
        return M
    

    def M_S(self):
        M= self.T
        S= M/60
        return S
    

    def S_H(self):
        S= self.T
        H= S*360
        return H
    
    def H_S(self):
        H= self.T
        S= H/360


# convert day to month and year
class ConvertTime2:

    def __init__(self,T) -> None:
        self.T= T

    def D_M(self):
        D= self.T
        M = int(D/30)
        d=  D%30
        return ("{} month and {} day".format(M, d))

    def M_D(Self):
        M= Self.T
        D= M*30
        return D

    def D_Y(self):
        D= self.T
        Y= int(D/365)
        d= D%30
        return ("{} year and {} day".format(Y, d))

    def Y_D(self):
        Y= self.T
        D= Y*365
        return D






# convert pascal to .....
class canvert_pressure:
    def __init__(self, P) -> None:
        self.P= P

    def Pas_Bar(self):
        Pas= self.P
        Bar= (10^-5)* Pas
        return Bar

    def Pas_At(self):
        Pas= self.P
        At= ((1.0197)*(10^-5))* Pas
        return At
    
    def Pas_Atm(self):
        Pas= self.P
        Atm= ((9.8692)*(10^-6))*Pas
        return Atm
    
    def Pas_Torr(self):
        Pas= self.P
        Torr= ((7.5006)*(10^-3))*Pas
        return Torr

    def Pas_Psi(self):
        Pas= self.P
        Psi= ((145.04)*(10^-6)) * Pas

        return Psi   

        




        


