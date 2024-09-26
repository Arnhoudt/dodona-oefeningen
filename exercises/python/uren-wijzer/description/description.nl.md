Bepaal hoe vaak de minutenwijzer een specifiek uurpunt passeert.
Je krijgt drie invoerwaarden:
- **minuten**: De startpositie van de minutenwijzer.
- **uur**: Het uur dat als "passeerpunt" wordt gebruikt.
- **delta_minuten**: Het aantal minuten dat de minutenwijzer zal afleggen.

Als de minutenwijzer start op dezelfde positie als het uurpunt, wordt dit geteld als één keer passeren.

## Voorbeeld

```console?lang=python=>>>
input:
11
5
45
Output:
0
```

```console?lang=python=>>>
input:
1
0
180
Output:
3
```