¿Nunca te pasó haber querido hacer algún trámite en el banco y llegar sólo para darte cuenta de que estaba cerrado? A Dory :tropical_fish: sí, por lo que vamos a desarrollar una función que ayude a la gente despistada como ella.

Sabemos que el banco está abierto los días de semana que no son [feriados](https://es.wikipedia.org/wiki/D%C3%ADa_festivo) y siempre y cuando estemos dentro del horario bancario. Además, ya contamos con las siguientes funciones:

* `dentro_de_horario_bancario`: recibe un horario :clock10: (una hora en punto que puede ir desde las 0 hasta las 23) y nos dice si está dentro de la franja de atención del banco. 
* `es_fin_de_semana`: recibe un día y nos dice si es `"sábado"` o `"domingo"`.

> Definí la función `es_dia_de_semana`. Luego completá `esta_abierto` que recibe un booleano (el cual indica si es feriado), un día y un horario, y nos dice si el banco está abierto:
> 
> ``` python
> ム esta_abierto(False, "sábado", 10)
> False # Porque es fin de semana
> ム esta_abierto(True, "lunes", 10)
> False # Porque es feriado
> ム esta_abierto(False, "martes", 20)
> False # Porque no está dentro del horario bancario
> ム esta_abierto(False, "jueves", 11)
> True # Porque no es feriado, 
>       # es un día  de semana 
>       # y está dentro del horario bancario
> ```