
def detente_isentropique(M0,gamma,angle_expension):
    
    coef = {
        "lambda" : sqrt((gamma-1)/(gamma+1)),
        "beta" : sqrt(pow(M0,2)-1),
        "A" : 1.3604,
        "B" : 0.0962,
        "C" : -0.5127,
        "D" : -0.6722,
        "E" : -0.3278,
        "mu_generatrice" : np.pi/2*(sqrt(6)-1)
    }
    mu_0 = abs(1/coef["lambda"]*np.arctan(coef["lambda"]*coef["beta"])-np.arctan(coef["beta"]))
    mu_1 = mu_0 + np.deg2rad(angle_expension)
    y = pow(mu_1/coef["mu_generatrice"],2/3)
    M1 = abs((1+coef["A"]*y + coef["B"]*pow(y,2) +coef["C"]*pow(y,3))/(1+coef["D"]*y+coef["E"]*pow(y,2)))
    
    P1_P0 = pow(((1+((gamma-1)/2)*pow(M0,2)))/((1+((gamma-1)/2)*pow(M1,2))), (gamma/(gamma-1)))
    Cp = ((P1_P0)-1)/(1/2*gamma*pow(M0,2))
    
    data = [P1_P0,Cp,M1]
    
    return data