import pygame

# Inicializa
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Movimento da Bola")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

# Bola
x, y = 300, 200
velocidade = 5
raio = 20

# Loop principal
rodando = True
while rodando:
    pygame.time.delay(30)  # Reduz velocidade do loop
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Desenho
    tela.fill(BRANCO)
    pygame.draw.circle(tela, VERMELHO, (x, y), raio)
    pygame.display.update()

pygame.quit()
