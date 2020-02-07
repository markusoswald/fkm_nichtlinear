import math as m

## FKM-Richtlinie Nichtlinear
## Rechnerischer Festigkeitsnachweis unter expliziter Erfassung nichtlinearen Werkstoffverformungsverhaltens

## Statischer Nachweis

# Festlegung der elastisch-plastischen Ergebnisse aus der FEM-Rechnung
sigma_xx = 280.0
sigma_yy = 90.0
sigma_zz = 50.0
tau_xy = 100.0
tau_yz = 80.0
tau_zx = 40.0

# Von Mises Vergleichsspannung
sigma_V = 1.0/m.sqrt(2) * m.sqrt((sigma_xx-sigma_yy)**2 + (sigma_yy-sigma_zz)**2 + (sigma_zz-sigma_xx)**2 + 6 * (tau_xy**2 + tau_yz**2 + tau_zx**2))
# Hydrostatische Spannung
sigma_H = 1.0/3.0 * (sigma_xx + sigma_yy + sigma_zz)
# Spannungsmehrachsigkeitsgrad
h = sigma_H/sigma_V

# Versagensgrenzkurve
