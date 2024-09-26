uren = int(input())
minuten = int(input())
delta_minuten = int(input())

minuten = (minuten + delta_minuten) % 60
uren = (uren + (minuten + delta_minuten) // 60) % 24

print("{}u{}".format(uren, minuten))


