import math as m

## FKM-Richtlinie Nichtlinear
## Rechnerischer Festigkeitsnachweis unter expliziter Erfassung nichtlinearen Werkstoffverformungsverhaltens

#--------------------------------------------------
## Statischer Nachweis
#--------------------------------------------------

# Festlegung der elastisch-plastischen Ergebnisse aus der FEM-Rechnung (Beispiel Lagerbock, S. 20)
sigma_xx = 63.9
sigma_yy = 12.9
sigma_zz = 4.2
tau_xy = -0.9
tau_yz = 0.2
tau_zx = 0.9

# Von Mises Vergleichsspannung
sigma_V = 1.0/m.sqrt(2) * m.sqrt((sigma_xx-sigma_yy)**2 + (sigma_yy-sigma_zz)**2 + (sigma_zz-sigma_xx)**2 + 6 * (tau_xy**2 + tau_yz**2 + tau_zx**2))
# Hydrostatische Spannung
sigma_H = 1.0/3.0 * (sigma_xx + sigma_yy + sigma_zz)
# Spannungsmehrachsigkeitsgrad
h = sigma_H/sigma_V

#--------------------------------------------------
# Versagensgrenzkurve (Beispiel Lagerbock, S.20)
A_g = 16.1/100.0
A = 21.8/100.0
Z = 25.4/100.0
if A >= 6:
    epsilon_0 = 4
else:
    epsilon_0 = 0.3 * A
epsilon_ref_1 = m.log(1.0 / (1.0 - Z))
h_ref_2 = 1.0/6.0 * (1.0 + m.exp(1.44 * (Z - A_g / (1 + A_g))))
epsilon_ref_2 = 1.0/2.0 * Z
beta = - 1.0 / h_ref_2 * m.log((epsilon_ref_2 - epsilon_0)/(epsilon_ref_1 - epsilon_0))
print(epsilon_0)
print(epsilon_ref_1)
print(epsilon_ref_2)
print(h_ref_2)
print(beta)



#--------------------------------------------------
# Werkstoffkennwerte (Beispiel Lagerbock, S. 20)
R_p_N = 278.0
R_m_N = 399.0
E = 155.0

a = 5
