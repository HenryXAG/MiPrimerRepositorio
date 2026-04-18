## entrada del monto de compra
monto = float(input("Ingrese el monto total de su compra: "))


if monto > 100:
    descuento = monto * 0.20
    total = monto - descuento
    print("Descuento aplicado (20%):", descuento)
    print("Total a pagar:", total)
elif monto >= 50 and monto <= 100:
    descuento = monto * 0.10
    total = monto - descuento
    print("Descuento aplicado (10%):", descuento)
    print("Total a pagar:", total)
else:
    print("Sin descuento aplicado (Monto menor a 50)")
    print("Total a pagar:", monto)

## usé float() por si el monto tiene decimales
## y el and asegura que el monto esté en el rango VIP de 50 a 100.
