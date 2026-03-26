tarefas = [ ]

while True:
  print("\n--- Lista de Tarefas ---")
  print("1. Adicionar tarefa")
  print("2. Ver tarefas")
  print("3. Remover tarefa")
  print("4. Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
  tarefa = input("Digite a tarefa: ")
  tarefas.append(tarefa)
  print ("Tarefa adicionada!")

elif opcao == "2":
  if not tarefas:
    print("Nenhuma tarefa encontrada.")
  else:
    for i, tarefa in enumerate(tarefa, 1):
      print(f"{i}. {tarefa}")

elif opcao == "3":
  num = int(input("Número da tarefa para remover: "))
  if 0 < num <= len(tarefas):
    tarefas.pop(num - 1)
    print("Tarefa removida!")
  else:
    print(Número inválido.")

elif opcao == "4":
  print(Saindo...")
  break

else:
  print(Opção inválida.")
  
