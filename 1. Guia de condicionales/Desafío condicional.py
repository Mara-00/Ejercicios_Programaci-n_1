#Tarifa base:
#Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
#El costo por metro cúbico (m³) de agua es de $200/m³.

CARGO_FIJO = 7000
COSTO_METRO = 200
IVA = 0.21
bonificacion = 0
recargo = 0

tipo_cliente = input("Ingrese el tipo de cliente: Residencial, Comercial o Industrial")
cantidad_metros = float(input("Ingrese cantidad de metros consumidos: "))

subtotal_consumo = (cantidad_metros * COSTO_METRO) + CARGO_FIJO

#Cliente Residencial:
#Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
#Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
#Casos especiales:
#Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
#En todos los casos, se aplica el IVA del 21% sobre el total.

if tipo_cliente == "Residencial":
    if cantidad_metros < 30 :
        print("Bonificación 10%")
        bonificacion = 0.1
    elif cantidad_metros > 80:
        print("Recargo 15%")
        recargo = 0.15
    if subtotal_consumo < 35000:
        bonificacion += 0.05
#Cliente Comercial:
#Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
#Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
#Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
elif tipo_cliente == "Comercial":
    if cantidad_metros > 150:
        print("Bonificación 8%")
        bonificacion = 0.08
    elif cantidad_metros >300:
        print("Bonificación 12%")
        bonificacion = 0.12
    elif cantidad_metros < 50:
        print("Recargo 5%")
        recargo = 0.05
#Cliente Industrial:
#Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
#consumo.
#Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
#Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
else:
    if cantidad_metros > 1000:
        print("Bonificación 30%")
        bonificacion = 0.3
    elif cantidad_metros >500:
        print("Bonificación 20%")
        bonificacion = 0.2
    elif cantidad_metros < 200:
        print("Recargo 10%")
        recargo = 0.1



#Calcular:
#Subtotal de consumo.
#Bonificaciones, si corresponde
#Recargos, si corresponde
#Subtotal, con recargos y bonificaciones.
#IVA aplicado (21%), si corresponde.
#Total final a pagar.
#Mostrar en pantalla el desglose de los cálculos.

total_bonificacion = subtotal_consumo * bonificacion
total_recargo = subtotal_consumo * recargo
subtotal_porcentaje_aplicado = subtotal_consumo - total_bonificacion + total_recargo

importe_iva = subtotal_porcentaje_aplicado * IVA

total_pagar = subtotal_porcentaje_aplicado + importe_iva

print(f"El subtotal es: {subtotal_consumo}")
print(f"El recargo total es: {total_recargo}")
print(f"El bonificación total es: {total_bonificacion}")
print(f"El subtotal con recargo y  bonificación es: {subtotal_porcentaje_aplicado}")
print(f"El IVA es: {importe_iva}")
print(f"El total a pagar es: {total_pagar}")