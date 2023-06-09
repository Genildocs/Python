# Instruções
# Neste exercício, desenvolveremos um sistema de controle simples para um reator nuclear.
# 1 Verificar a criticidade do reator.
import math


def is_criticality_balanced(temperature, neutrons_emitted):

    if temperature < 800:
        if neutrons_emitted > 500:
            if temperature * neutrons_emitted < 500000:
                return True
    else:
        return False
print(is_criticality_balanced(750,600))

# 2. Determine a faixa de saída de energia

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current;
    porcent_eficience = math.trunc((generated_power / theoretical_max_power) * 100)

    if porcent_eficience > 80:
        return 'Estado de eficiencia: green'
    elif porcent_eficience >= 60:
        return 'Estado de eficiencia: orange'
    elif porcent_eficience >= 30:
        return 'Estado de eficiencia: red'
    else:
        return 'Estado de eficiencia: black {ALERTA}'


print(reactor_efficiency(25,50,15000))
