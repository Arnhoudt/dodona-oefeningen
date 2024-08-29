cijfer = int(input())
minuten = int(input())

delta_minuten = int(input())

graden_cijfer = 360 / 12 * cijfer
graden_minuten = 360 / 60 * minuten
graden_delta_minuten = 360 / 60 * delta_minuten

verschil = (graden_cijfer - graden_minuten)%360

graden_delta_minuten_basis = graden_delta_minuten - verschil
print(int(graden_delta_minuten_basis//360+1))