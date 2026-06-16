print('Mini Game: A Floresta Misteriosa \n ' + 'Regras e avisos: Você é um aventureiro que precisa encontrar o tesouro escondido na Floresta Misteriosa. Em cada situação, escolha A ou B. Se escolher a opção correta, continua a aventura. Se errar, recebe GAME OVER. \n ' + 'inicio \n' + 'Você chega à entrada da floresta e vê dois caminhos.')

ftq = input('A) Seguir pela trilha iluminada. aperte (a) para confirmar sua resposta \n' + 'B) Entrar na caverna escura. aperte(b) para confirmar sua resposta \n')

print('Fase 2 \n ' + 'Você encontra um rio bloqueando a passagem.')

ftq2 = input('A) Tentar atravessar nadando. para confirmar sua resposta \n' + 'B) Usar a ponte de madeira. para confirmar sua resposta \n')

print('Fase 3 \n ' + 'Um velho guardião faz uma pergunta: "O que vale mais: a coragem ou a ganância?"')

ftq3 = input('A) Coragem. aperte (a) para confirmar sua resposta \n' + 'B) Ganância. aperte (b) para confirmar sua resposta \n')

print('Fase final \n ' + 'Você chega diante de dois baús.')

ftq4 = input('A) Abrir o baú dourado. (a) para confirmar sua resposta \n' + 'B) Abrir o baú de pedra com um símbolo antigo. (a) para confirmar sua resposta \n')

if ftq == 'a':
    print('Resposta correta!')
else:
    print('Resposta incorreta!')
if ftq2 == 'b':
    print('Resposta correta!')
else:
    print('Resposta incorreta!')
if ftq3 == 'a':
    print('Resposta correta!')
else:
    print('Resposta incorreta!')
if ftq4 == 'b':
    print('Resposta correta!')
else:
    print('Resposta incorreta!')