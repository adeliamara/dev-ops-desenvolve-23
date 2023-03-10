usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23,42,56}

usuarios_que_assistiram = usuarios_data_science | usuarios_machine_learning
repetidos = usuarios_machine_learning & usuarios_data_science


fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning

print(15 in fez_ds_mas_nao_fez_ml)


print(usuarios_que_assistiram)
print(repetidos)


print(usuarios_data_science ^ usuarios_machine_learning)


usuarios_que_assistiram.add(65)

print(usuarios_que_assistiram)
