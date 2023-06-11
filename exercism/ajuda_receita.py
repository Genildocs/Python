# nstruções
# você escreverá algum código para ajudá-lo a preparar uma linda lasanha de seu livro de receitas favorito.
#
# Você tem cinco tarefas, todas relacionadas a cozinhar sua receita.
#

# 1. Defina o tempo de cozimento esperado em minutos

TEMPO_DE_ASSAR_ESPERADO = 40

# 2. Calcule o tempo restante de cozimento em minutos
def bake_time_remaining(minutes):

    if minutes <= 40:
        return TEMPO_DE_ASSAR_ESPERADO - minutes

print(bake_time_remaining(10))

# 3. Calcule o tempo de preparo em minutos

def preparation_time_in_minutes(number_of_layers):
    return number_of_layers * 2;

print(preparation_time_in_minutes(5))

# 4. Calcule o tempo total de cozimento (preparação + cozimento) em minutos

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
   to_minutes_cozinhando = elapsed_bake_time + preparation_time_in_minutes(number_of_layers)
   return to_minutes_cozinhando

print(elapsed_time_in_minutes(3,20))