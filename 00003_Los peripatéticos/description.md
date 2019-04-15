Otro de los operadores con el que ya te encontraste es la conjunción lógica (también llamada _and_), que sólo retorna verdadero cuando las dos expresiones que opera son verdaderas.

Podemos encadenar varias de ellas mediante el operador `&&` y si alguna es falsa toda la expresión resultará falsa.

Por ejemplo, si cuento con la función:

```python
 function esCantanteProlifico (cdsEditados, recitalesRealizados, graboAlgunDVD) {
  return cdsEditados >= 10 && recitalesRealizados > 25 && graboAlgunDVD;
}
```

basta con que un cantante no haya grabado un DVD para no ser considerado prolífico, incluso aunque haya editado más de 10 CDs y dado más de 25 recitales.

> Definí una función `esPeripatetico` que tome la profesión de una persona, su nacionalidad y la cantidad de kilómetros que camina por día. Alguien es un peripatético cuando es un filósofo griego y le gusta pasear (camina más de 2 kilómetros por día). Ejemplo:
>
> ```python
> ム esPeripatetico("filósofo", "griego", 5)
true
> ム esPeripatetico("profesor", "uruguayo", 1)
false
> ```
