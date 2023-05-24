import pygame
import random

# Inicialização do Pygame
pygame.init()

# Dimensões da janela do jogo
largura = 800
altura = 600

# Cores
azul = (0,0,255)
verde =  (0, 255, 0)

# Inicialização da janela do jogo
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo de Joquepo")

# Posições das opções
posicoes_opcoes = [(100, 400), (350, 400), (600, 400)]

# Tamanho desejado para as imagens
largura_opcao = 100
altura_opcao = 100

# Função para exibir as opções na tela
def exibir_opcoes():
    janela.blit(pedra_img, posicoes_opcoes[0])
    janela.blit(papel_img, posicoes_opcoes[1])
    janela.blit(tesoura_img, posicoes_opcoes[2])

pedra_img = pygame.image.load("image/pedra.png")
papel_img = pygame.image.load("image/papel.png")
tesoura_img = pygame.image.load("image/tesoura.png")

pedra_img = pygame.transform.scale(pedra_img, (largura_opcao, altura_opcao))
papel_img = pygame.transform.scale(papel_img, (largura_opcao, altura_opcao))
tesoura_img = pygame.transform.scale(tesoura_img, (largura_opcao, altura_opcao))

# Função para escolha aleatória da máquina
def escolha_maquina():
    opcoes = ["pedra", "papel", "tesoura"]
    return random.choice(opcoes)

# Função para determinar o vencedor
def determinar_vencedor(escolha_jogador, escolha_maquina):
    if escolha_jogador == escolha_maquina:
        return "Empate"
    elif (escolha_jogador == "pedra" and escolha_maquina == "tesoura") or \
         (escolha_jogador == "papel" and escolha_maquina == "pedra") or \
         (escolha_jogador == "tesoura" and escolha_maquina == "papel"):
        return "Você ganhou!"
    else:
        return "Você perdeu!"

fonte = pygame.font.Font(None,36)

# Função para exibir a notificação na tela
def exibir_notificacao(texto):
    texto_renderizado = fonte.render(texto, True, azul)
    posicao_texto = (largura // 2 - texto_renderizado.get_width() // 2, altura // 2 - texto_renderizado.get_height() // 2)
    janela.blit(texto_renderizado, posicao_texto)


def exibir_resultado(resultado):
    texto = fonte.render(resultado, True, azul)
    posicao_texto = (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2)
    janela.blit(texto, posicao_texto)

# Loop principal do jogo
jogo_ativo = True
escolha_jogador = None
while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

        # Verificar se o jogador clicou em uma opção
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            # Verificar se o jogador clicou na opção pedra
            if posicoes_opcoes[0][0] <= mouse_pos[0] <= posicoes_opcoes[0][0] + largura_opcao and \
               posicoes_opcoes[0][1] <= mouse_pos[1] <= posicoes_opcoes[0][1] + altura_opcao:
                escolha_jogador = "pedra"

            # Verificar se o jogador clicou na opção papel
            elif posicoes_opcoes[1][0] <= mouse_pos[0] <= posicoes_opcoes[1][0] + largura_opcao and \
                 posicoes_opcoes[1][1] <= mouse_pos[1] <= posicoes_opcoes[1][1] + altura_opcao:
                escolha_jogador = "papel"

            # Verificar se o jogador clicou na opção tesoura
            elif posicoes_opcoes[2][0] <= mouse_pos[0] <= posicoes_opcoes[2][0] + largura_opcao and \
                 posicoes_opcoes[2][1] <= mouse_pos[1] <= posicoes_opcoes[2][1] + altura_opcao:
                escolha_jogador = "tesoura"

            # Fazer a escolha da máquina e determinar o resultado
            if escolha_jogador is not None:
                opcao_maquina = escolha_maquina()
                resultado = determinar_vencedor(escolha_jogador, opcao_maquina)
                print("Escolha do jogador:", escolha_jogador)
                print("Escolha da máquina:", opcao_maquina)
                print("Resultado:", resultado)
                pygame.time.delay(2000)  # Pausa por 2 segundos (2000 milissegundos)
                escolha_jogador = None

    janela.fill((0,255,0))
    
    # Exibição das opções
    exibir_opcoes()


    if escolha_jogador is not None:
        opcao_maquina = escolha_maquina()
        resultado = determinar_vencedor(escolha_jogador, opcao_maquina)
        exibir_resultado(resultado)
        texto = fonte.render(resultado, True, azul)
        posicao_texto = (largura // 2 - texto.get_width() // 2, altura // 2 - texto.get_height() // 2)
        janela.blit(texto, posicao_texto)
        exibir_notificacao(texto)

        pygame.display.update()
        pygame.time.delay(2000)
        escolha_jogador = None

    # Atualização da tela
    pygame.display.update()

# Encerramento do Pygame
pygame.quit()
