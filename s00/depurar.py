"""Diagnóstico D3 (semana 0): depuración.

Copia este archivo a tu repo (repos/cs-desde-cero/s00/depurar.py) y arréglalo allí.
Ejecuta:  python3 repos/cs-desde-cero/s00/depurar.py

La función tiene VARIOS bichos. No la reescribas desde cero: encuéntralos y arréglalos,
pensando en voz alta. Lo que nos interesa es CÓMO los buscas, no solo que los encuentres.
"""


def resumen_jugador(puntos):
    """Recibe las puntuaciones de un jugador en sus partidas (enteros, pueden ser negativos).

    Devuelve un diccionario con:
      - "partidas": cuántas partidas jugó
      - "maximo":   la puntuación más alta
      - "media":    la media exacta (float)
      - "mejora":   la racha más larga de partidas seguidas con puntuación estrictamente
                    creciente (una sola partida cuenta como racha de 1)
    Si la lista está vacía devuelve None.
    """
    if len(puntos) == 0:
        return None

    maximo = -10000
    total = 0
    for p in puntos:
        total += p
        if p > maximo:
            maximo = p

    racha = 1
    mejor = 1
    for i in range(1, len(puntos)):
        if puntos[i] > puntos[i - 1]:
            racha += 1
            mejor = max(mejor, racha)
        else:
            racha = 1

    return {
        "partidas": len(puntos),
        "maximo": maximo,
        "media": float(total / len(puntos)),
        "mejora": mejor,
    }


# ---------------------------------------------------------------- pruebas (no las toques)
if __name__ == "__main__":
    casos = [
        ([10, 20, 30], {"partidas": 3, "maximo": 30, "media": 20.0, "mejora": 3}),
        ([5, 4, 3], {"partidas": 3, "maximo": 5, "media": 4.0, "mejora": 1}),
        ([-5, -2, -9], {"partidas": 3, "maximo": -2, "media": -16 / 3, "mejora": 2}),
        ([7], {"partidas": 1, "maximo": 7, "media": 7.0, "mejora": 1}),
        ([1, 2, 1, 2, 3, 4], {"partidas": 6, "maximo": 4, "media": 13 / 6, "mejora": 4}),
        ([3, 4], {"partidas": 2, "maximo": 4, "media": 3.5, "mejora": 2}),
        ([], None),
    ]
    ok = 0
    for entrada, esperado in casos:
        obtenido = resumen_jugador(entrada)
        bien = obtenido == esperado
        ok += bien
        print("✅" if bien else "❌", entrada)
        if not bien:
            print("     esperado:", esperado)
            print("     obtenido:", obtenido)
    print(f"\nResultado: {ok}/{len(casos)}")
