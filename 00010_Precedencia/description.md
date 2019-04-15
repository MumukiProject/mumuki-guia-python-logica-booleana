Cuando una expresión matemática tiene varios operadores, sabemos que las multiplicaciones y divisiones se efectuarán antes que las sumas y las restas:

```python
5 * 3 + 8 / 4 - 3 = 14
```

Al igual que en matemática, cuando usamos operadores lógicos las expresiones se evalúan en un orden determinado llamado _precedencia_.

¿Cuál es ese orden? ¡Hagamos la prueba!

Teniendo definida la función:

```python
def paga_con_tarjeta(se_cobra_interes, tarjeta, efectivo_disponible):
  return not se_cobra_interes and cuotas(tarjeta) >= 3 or efectivo_disponible < 100
```

> Probala en la consola con los valores:

>* `ム paga_con_tarjeta(True, "visa", 320)`
>* `ム paga_con_tarjeta(False, "visa", 80)`
>* `ム paga_con_tarjeta(True, "mastercard", 215)`
>* `ム paga_con_tarjeta(True, "mastercard", 32)`
