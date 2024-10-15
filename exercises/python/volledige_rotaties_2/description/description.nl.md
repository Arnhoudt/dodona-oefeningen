Ontwikkel een programma dat berekent hoe vaak de minutenwijzer van een klok een volledige rotatie maakt, van de 12-uur-positie (0 minuten) terug naar dezelfde positie. Houd er rekening mee dat de minutenwijzer niet start op de 12-uur-positie. Je moet dus het aantal resterende minuten tot de top van de klok aftrekken van de verstreken tijd (delta minuten).

Invoer:
- \( m \): startpositie van de minutenwijzer (in minuten). Getal van 1 tot en met 60 (om het eenvoudiger te maken)
- \( d \): het aantal minuten dat verstrijkt na de start.

## Voorbeeld

```console?lang=python=>>>
input:
60
120
Output:
2
```

```console?lang=python=>>>
input:
5
115
Output:
1
```

```console?lang=python=>>>
input:
55
125
Output:
2
```