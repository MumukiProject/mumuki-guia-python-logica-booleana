Cuando una expresión matemática tiene varios operadores, sabemos que las multiplicaciones y divisiones se efectuarán antes que las sumas y las restas:

```python
5 * 3 + 8 / 4 - 3 = 14
```

Al igual que en matemática, cuando usamos operadores lógicos las expresiones se evalúan en un orden determinado llamado _precedencia_.

¿Cuál es ese orden? ¡Hagamos la prueba!

Teniendo definida la función:

```python
function pagaConTarjeta(seCobraInteres, tarjeta, efectivoDisponible) {
  return !seCobraInteres && cuotas(tarjeta) >= 3 || efectivoDisponible < 100;
}
```

> Probala en la consola con los valores:

>* `ム pagaConTarjeta(true, "visa", 320)`
>* `ム pagaConTarjeta(false, "visa", 80)`
>* `ム pagaConTarjeta(true, "mastercard", 215)`
>* `ム pagaConTarjeta(true, "mastercard", 32)`
