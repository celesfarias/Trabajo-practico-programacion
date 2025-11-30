# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    # Terminó todo
    if i >= n - 1:
        return {"done": True}

    # ------------------ FASE BUSCAR ------------------
    if fase == "buscar":

        # Comparación visual
        a = min_idx
        b = j

        # Actualizar mínimo si corresponde
        if items[j] < items[min_idx]:
            min_idx = j

        j += 1

        # Si terminó el recorrido, pasamos a fase swap
        if j >= n:
            fase = "swap"

        return {
            "a": a,
            "b": b,
            "swap": False,
            "done": False
        }

    # ------------------ FASE SWAP ------------------
    if fase == "swap":

        a = i
        b = min_idx

        hubo_swap = (min_idx != i)

        if hubo_swap:
            items[i], items[min_idx] = items[min_idx], items[i]

        # Preparar siguiente pasada
        i += 1
        min_idx = i
        j = i + 1
        fase = "buscar"

        return {
            "a": a,
            "b": b,
            "swap": hubo_swap,
            "done": False
        }
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    
