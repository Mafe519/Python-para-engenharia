import pygame

# ============= INICIALIZAÇÃO DO PYGAME =============
# Inicializa todos os módulos do Pygame
pygame.init()

# Define as dimensões da janela (largura x altura em pixels)
LARGURA, ALTURA = 600, 400
tela = pygame.display.set_mode((LARGURA, ALTURA))

# Define o título da janela
pygame.display.set_caption("Movimento da Bola - Exemplo Didático")

# ============= DEFINIÇÃO DE CORES =============
# Cores são representadas em RGB (Vermelho, Verde, Azul)
# Valores entre 0 e 255 para cada componente
BRANCO = (255, 255, 255)  # RGB para branco
VERMELHO = (255, 0, 0)    # RGB para vermelho
AZUL = (0, 0, 255)        # RGB para azul

# ============= CONFIGURAÇÃO DA BOLA =============
# Posição inicial da bola (centro da tela)
x, y = LARGURA // 2, ALTURA // 2
# Velocidade de movimento da bola (pixels por frame)
velocidade = 5
# Tamanho da bola (raio em pixels)
raio = 20

# ============= LOOP PRINCIPAL DO JOGO =============
clock = pygame.time.Clock()  # Objeto para controlar FPS
rodando = True
while rodando:
    # Controla a velocidade do jogo (30 FPS)
    clock.tick(30)
    
    # ===== CAPTURA DE EVENTOS =====
    # Processa todos os eventos na fila de eventos
    for evento in pygame.event.get():
        # Verifica se o usuário fechou a janela
        if evento.type == pygame.QUIT:
            rodando = False
    
    # ===== CONTROLE DE MOVIMENTO =====
    # Captura teclas pressionadas
    teclas = pygame.key.get_pressed()
    
    # Move a bola de acordo com as setas do teclado
    if teclas[pygame.K_LEFT]:
        x -= velocidade  # Move para esquerda
    if teclas[pygame.K_RIGHT]:
        x += velocidade  # Move para direita
    if teclas[pygame.K_UP]:
        y -= velocidade  # Move para cima
    if teclas[pygame.K_DOWN]:
        y += velocidade  # Move para baixo
    
    # ===== TRATAMENTO DE LIMITES DA TELA =====
    # Impede que a bola saia da tela
    if x - raio < 0:
        x = raio  # Limite esquerdo
    if x + raio > LARGURA:
        x = LARGURA - raio  # Limite direito
    if y - raio < 0:
        y = raio  # Limite superior
    if y + raio > ALTURA:
        y = ALTURA - raio  # Limite inferior
    
    # ===== RENDERIZAÇÃO =====
    # Limpa a tela preenchendo-a com a cor branca
    tela.fill(BRANCO)
    
    # Desenha a bola na posição atual
    pygame.draw.circle(tela, VERMELHO, (x, y), raio)
    
    # Atualiza a tela com tudo o que foi desenhado
    pygame.display.update()

# Encerra o Pygame quando o loop terminar
pygame.quit()
