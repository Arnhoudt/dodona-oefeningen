plan_uren = int(input())
plan_minuten = int(input())

dagen = int(input())
uren = int(input())
minuten = int(input())

plan_tot_minuten = plan_minuten + plan_uren * 60
tot_minuten = ((dagen * 24) + uren) * 60 + minuten

delta_plan_dagen = tot_minuten // plan_tot_minuten
delta_plan_uren = (tot_minuten - delta_plan_dagen * plan_tot_minuten) //60
delta_plan_minuten = tot_minuten - delta_plan_dagen * plan_tot_minuten - delta_plan_uren * 60

print("Als er op Aarde ",dagen," dagen, ", uren," uren en ", minuten, " minuten voorbij zijn gegaan, zullen er op deze planeet ", delta_plan_dagen," dagen, ",delta_plan_uren," uren en ",delta_plan_minuten, " minuten verstreken zijn.")