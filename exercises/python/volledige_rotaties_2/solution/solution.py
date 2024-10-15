start_min = int(input())
delta = int(input())

afstand = 60 - start_min
delta_na_afstand = delta - afstand
print(delta_na_afstand % 60)