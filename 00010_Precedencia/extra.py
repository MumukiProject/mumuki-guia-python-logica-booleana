def cuotas(tarjeta):
  switch(tarjeta):
    case "visa":
      return 6
    case "mastercard":
      return 2
    default:
      return 1



def paga_con_tarjeta(se_cobra_interes, tarjeta, efectivo_disponible):
  return not se_cobra_interes and cuotas(tarjeta) >= 3 or efectivo_disponible < 100

