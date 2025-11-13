# %% [markdown]
# # Sesión 5- Laboratorio 1: Calculadora de Precios
# Objetivo: Practicar la creación de funciones básicas
# 
# La función debe:
# 1. Calcular el precio final con IVA
# 2. Aplicar descuento si corresponde
# 3. Validar que los valores sean positivos

# %%
def calcular_precio_final(precio_base, cantidad, descuento=0):
    """
    Calcula el precio final de una compra incluyendo IVA y descuento
    Args:
        precio_base (float): Precio unitario del producto
        cantidad (int): Cantidad de unidades
        descuento (float): Porcentaje de descuento (0-1)
    Returns:
        float: Precio final después de IVA y descuento
    """
    # TODO: Implementar el cálculo siguiendo estos pasos:
    # 1. Validar que precio_base y cantidad sean positivos
    # 2. Validar que descuento esté entre 0 y 1
    # 3. En caso de que fallen las validaciones, regresar None
    # 4. Calcular subtotal (precio_base * cantidad)
    # 5. Aplicar descuento si existe
    # 6. Agregar IVA (19%)
    if precio_base >= 0 and cantidad >= 0 and 0 <= descuento <= 1:
        return (precio_base * cantidad) * (1 - descuento) * 1.19
    else:
        return None


# %%
def main():
    # Casos de prueba
    print("=== Calculadora de Precios ===")
    
    # Caso 1: Sin descuento
    precio1 = calcular_precio_final(100, 2)
    print(f"\nCaso 1 - Precio base: $100, Cantidad: 2")
    print(f"Precio final: ${precio1}")
    
    # Caso 2: Con descuento
    precio2 = calcular_precio_final(100, 2, 0.1)
    print(f"\nCaso 2 - Precio base: $100, Cantidad: 2, Descuento: 10%")
    print(f"Precio final: ${precio2}")

# %%
if __name__ == "__main__":
    main()

# %%



