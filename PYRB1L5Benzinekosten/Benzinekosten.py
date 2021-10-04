verzekering_per_maand = 23
benzine_kosten_per_liter = 1.54
liter_per_kilometer = 0.2 
km_per_maand = input("Hoeveel kilometer rij jij per maand? ")
km_per_maand = float(km_per_maand)

def maandelijkse_kosten(_km_per_maand):
    return (_km_per_maand * liter_per_kilometer * benzine_kosten_per_liter) + verzekering_per_maand

print("Jij betaald:", str(maandelijkse_kosten(km_per_maand)) + " Euro per maand!")

