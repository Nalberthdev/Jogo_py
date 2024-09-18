import pyautogui
from random import randint
from time import sleep

quer_jogar_denovo = 's'  

while quer_jogar_denovo == 's':
    cpu = randint(1, 100)
    print(cpu)  
    cont = 1
    
    while True:
        tentativa = pyautogui.prompt('Digite o seu palpite de 1 até 100: ')  # Usando prompt do pyautogui
        try:
            tentativa = int(tentativa)
            if 1 <= tentativa <= 100:  
                break
            else:
                pyautogui.alert('Por favor, digite um número entre 1 e 100.')
        except ValueError:
            pyautogui.alert('Entrada inválida! Por favor, digite apenas números.')

    while tentativa != cpu:
        if tentativa > cpu:
            pyautogui.alert('É MENOR !!!!!!!!!!!!!!!')
            sleep(0.1)
        elif tentativa < cpu:
            pyautogui.alert('É MAIOR !!!!!!!!!!!!!!!')
            sleep(0.1)

        while True:
            tentativa = pyautogui.prompt('Digite novamente: ')
            try:
                tentativa = int(tentativa)
                if 1 <= tentativa <= 100:
                    break
                else:
                    pyautogui.alert('Por favor, digite um número entre 1 e 100.')
            except ValueError:
                pyautogui.alert('Entrada inválida! Por favor, digite apenas números.')

        cont += 1
        print('Você está na tentativa de número: ', cont)

    pyautogui.alert(f'Parabéns! Você acertou! O número era {cpu}.\nVocê precisou de {cont} tentativas.')

    quer_jogar_denovo = pyautogui.confirm('Quer jogar novamente?', buttons=['Sim', 'Não']).lower()

    while quer_jogar_denovo != 'sim' and quer_jogar_denovo != 'não':
        pyautogui.alert('Use apenas Sim ou Não.')
        quer_jogar_denovo = pyautogui.confirm('Quer jogar novamente?', buttons=['Sim', 'Não']).lower()

print("Obrigado por jogar!")
