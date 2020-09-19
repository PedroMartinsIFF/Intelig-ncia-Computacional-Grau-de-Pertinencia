# ------------------- inputs -------------------------

Temperatura = float(input("Entre com a temperatura: \n"))
Luz = int(input("Entre com a % de luz: \n"))

# ------------- Calculando Grau de Pertinencia ----------------

# --------------------- Temperatura (Frio) --------------------

if Temperatura <= 10:
    PertinenciaFrio = 1
else:
    if 10 < Temperatura < 25:
        PertinenciaFrio = ((-0.07 * Temperatura) + 1.7)
    else:
        if Temperatura >= 25:
            PertinenciaFrio = 0
print("----------------------------------------------")
print("Pertinencia Frio:")
print(PertinenciaFrio)
# --------------------- Temperatura (Morno) --------------------
if (Temperatura <= 13) or (Temperatura > 30):
    PertinenciaMorno = 0
else:
    if Temperatura < 20:
        PertinenciaMorno = ((0.14 * Temperatura) - 1.9)
    else:
        if 20 <= Temperatura <= 27:
            PertinenciaMorno = 1
        else:
            if 27 < Temperatura <= 30:
                PertinenciaMorno = ((-0.3 * Temperatura) + 9.1)
print("----------------------------------------------")
print("Pertinencia Morno:")
print(PertinenciaMorno)
# ------------------ Temperatura (Quente) ----------------------
if Temperatura <= 20:
    PertinenciaQuente = 0
else:
    if 20 < Temperatura < 35:
        PertinenciaQuente = ((0.07 * Temperatura) - 1.4)
    else:
        if Temperatura >= 35:
            PertinenciaQuente = 1

print("----------------------------------------------")
print("Pertinencia Quente:")
print(PertinenciaQuente)
# ------------------ Tempo (Nublado) ---------------------------
if Luz <= 30:
    PertinenciaNublado = 1
else:
    if 30 < Luz < 70:
        PertinenciaNublado = ((-0.025 * Luz) + 1.75)
    else:
        if Luz >= 70:
            PertinenciaNublado = 0

print("----------------------------------------------")
print("Pertinencia Nublado:")
print(PertinenciaNublado)
# ------------------ Tempo (Parcial) ----------------------------
if (Luz <= 30) or (Luz >= 70):
    PertinenciaParcial = 0
else:
    if Luz == 50:
        PertinenciaParcial = 1
    else:
        if 30 < Luz < 50:
            PertinenciaParcial = ((0.05 * Luz) - 1.5)
        else:
            if 50 < Luz < 70:
                PertinenciaParcial = ((-0.05 * Luz) + 1.5)

print("----------------------------------------------")
print("Pertinencia Parcial:")
print(PertinenciaParcial)
# ------------------ Tempo (Sol) -------------------------------
if Luz <= 30:
    PertinenciaSol = 0
else:
    if 30 < Luz < 70:
        PertinenciaSol = ((0.025 * Luz) - 0.75)
    else:
        if Luz >= 70:
            PertinenciaSol = 1

print("----------------------------------------------")
print("Pertinencia Sol:")
print(PertinenciaSol)

# -------------------- Calculo das Regras ---------------------

if PertinenciaFrio > PertinenciaNublado:
    R1 = PertinenciaFrio
else:
    R1 = PertinenciaNublado

if PertinenciaQuente < PertinenciaSol:
    R2 = PertinenciaQuente
else:
    R2 = PertinenciaSol

if PertinenciaMorno < PertinenciaParcial:
    R3 = PertinenciaMorno
else:
    R3 = PertinenciaParcial

if PertinenciaFrio < PertinenciaNublado:
    R4 = PertinenciaFrio
else:
    R4 = PertinenciaNublado

if PertinenciaMorno < PertinenciaSol:
    R5 = PertinenciaMorno
else:
    R5 = PertinenciaSol

R6 = PertinenciaQuente
print("----------------------------------------------")
print("Regra 1")
print(R1)
print("----------------------------------------------")
print("Regra 2")
print(R2)
print("----------------------------------------------")
print("Regra 3")
print(R3)
print("----------------------------------------------")
print("Regra 4")
print(R4)
print("----------------------------------------------")
print("Regra 5")
print(R5)
print("----------------------------------------------")
print("Regra 6")
print(R6)

SomaRegras = R1 + R2 + R3 + R4 + R5 + R6

# -------------------- Calculo final ------------

if R1 == 0:
    Resultado1 = 0
else:
    Resultado1 = (R1 - 1.5) / (-0.03)

if R2 == 0:
    Resultado2 = 0
else:
    Resultado2 = (R2 + 2) / (0.04)

if R3 == 0:
    Resultado3 = 0
    Resultado3Ex = 0
else:
    if R3 == 1:
        Resultado3 = 50
        Resultado3Ex = 0
    else:
        if 0 < R3 < 1:
            Resultado3 = (R3 + 1) / (0.04)
            Resultado3Ex = (R3 - 1) / (-0.04)

if R4 == 0:
    Resultado4 = 0
    Resultado4Ex = 0
else:
    if R4 == 1:
        Resultado4 = 1
        Resultado4Ex = 0
    else:
        if 0 < R4 < 1:
            Resultado4 = (R4 + 1) / (0.04)
            Resultado4Ex = (R4 - 1) / (-0.04)

if R5 == 0:
    Resultado5 = 0
else:
    Resultado5 = (R5 + 2) / (0.04)

if R6 == 0:
    Resultado6 = 0
else:
    Resultado6 = (R6 + 2) / (0.04)

ResultadoFinal = ((Resultado1 * R1) + (Resultado2 * R2) + (Resultado3 * R3) + (Resultado3Ex * R3) + (Resultado4 * R4) + (Resultado4Ex * R4) + (Resultado5 * R5) + (Resultado6 * R6)) / SomaRegras

print("----------------------------------------------")
print("Resultado Final")
print(ResultadoFinal)

input()






