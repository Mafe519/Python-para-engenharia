from flask import Flask, render_template_string, request, redirect, url_for, session, flash
import os
import datetime

app = Flask(__name__)
app.secret_key = 'chave_secreta_muito_segura'

# Reescrevendo as rotas para usar templates completos sem herança
@app.route('/')
def home():
    # Template HTML completo para a página inicial
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home - Meu Site Flask</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333;
                line-height: 1.6;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
            }
            header {
                background-color: #343a40;
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 2rem;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
            }
            .nav-links {
                display: flex;
                list-style: none;
            }
            .nav-links li {
                margin-left: 20px;
            }
            .nav-links a {
                text-decoration: none;
                color: white;
                font-weight: 500;
                transition: color 0.3s;
            }
            .nav-links a:hover {
                color: #17a2b8;
            }
            .hero {
                background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('https://source.unsplash.com/1600x900/?technology');
                background-size: cover;
                background-position: center;
                height: 60vh;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                text-align: center;
                color: white;
            }
            .hero h1 {
                font-size: 3rem;
                margin-bottom: 1rem;
            }
            .hero p {
                font-size: 1.5rem;
                margin-bottom: 2rem;
                max-width: 600px;
            }
            .btn {
                display: inline-block;
                background: #17a2b8;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                transition: background 0.3s;
            }
            .btn:hover {
                background: #138496;
            }
            .features {
                padding: 4rem 0;
                background: white;
            }
            .feature-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 2rem;
            }
            .feature-card {
                background: #f8f9fa;
                border-radius: 8px;
                padding: 2rem;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-icon {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                color: #17a2b8;
            }
            .about {
                padding: 4rem 0;
                background: #e9ecef;
            }
            .about-content {
                display: flex;
                align-items: center;
                gap: 3rem;
            }
            .about-text {
                flex: 1;
            }
            .about-image {
                flex: 1;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            }
            .about-image img {
                width: 100%;
                display: block;
            }
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
            }
            .section-title h2 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .section-title p {
                color: #6c757d;
                max-width: 600px;
                margin: 0 auto;
            }
            footer {
                background: #343a40;
                color: white;
                padding: 2rem 0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">Flask Site</div>
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/sobre">Sobre</a></li>
                    <li><a href="/servicos">Serviços</a></li>
                    <li><a href="/contato">Contato</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <section class="hero">
                <h1>Bem-vindo ao Flask Site</h1>
                <p>Desenvolvendo aplicações web simples e bonitas com o poder do Flask</p>
                <a href="/servicos" class="btn">Nossos Serviços</a>
            </section>
            
            <section class="features">
                <div class="container">
                    <div class="section-title">
                        <h2>Nossos Recursos</h2>
                        <p>Descubra como podemos ajudar a impulsionar seu projeto</p>
                    </div>
                    <div class="feature-grid">
                        <div class="feature-card">
                            <div class="feature-icon">&#128187;</div>
                            <h3>Desenvolvimento Web</h3>
                            <p>Criamos sites responsivos e aplicações web modernas usando as melhores tecnologias disponíveis.</p>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">&#128241;</div>
                            <h3>Design Responsivo</h3>
                            <p>Todos os nossos projetos são otimizados para funcionar perfeitamente em qualquer dispositivo.</p>
                        </div>
                        <div class="feature-card">
                            <div class="feature-icon">&#128202;</div>
                            <h3>Análise de Dados</h3>
                            <p>Transformamos seus dados em insights valiosos para ajudar nas decisões de negócios.</p>
                        </div>
                    </div>
                </div>
            </section>
            
            <section class="about">
                <div class="container">
                    <div class="about-content">
                        <div class="about-text">
                            <h2>Sobre Nós</h2>
                            <p>Somos uma equipe apaixonada por tecnologia e desenvolvimento web. Nossa missão é criar experiências digitais excepcionais que ajudem nossos clientes a alcançar seus objetivos.</p>
                            <p>Com anos de experiência em desenvolvimento web, estamos prontos para transformar suas ideias em realidade.</p>
                            <a href="/sobre" class="btn">Saiba Mais</a>
                        </div>
                        <div class="about-image">
                            <img src="https://source.unsplash.com/600x400/?team" alt="Nossa equipe">
                        </div>
                    </div>
                </div>
            </section>
        </main>
        
        <footer>
            <div class="container">
                <p>&copy; ''' + str(datetime.datetime.now().year) + ''' Flask Site. Todos os direitos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    return html

@app.route('/sobre')
def about():
    # Template HTML completo para a página sobre
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sobre - Meu Site Flask</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333;
                line-height: 1.6;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
            }
            header {
                background-color: #343a40;
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 2rem;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
            }
            .nav-links {
                display: flex;
                list-style: none;
            }
            .nav-links li {
                margin-left: 20px;
            }
            .nav-links a {
                text-decoration: none;
                color: white;
                font-weight: 500;
                transition: color 0.3s;
            }
            .nav-links a:hover {
                color: #17a2b8;
            }
            .btn {
                display: inline-block;
                background: #17a2b8;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                transition: background 0.3s;
            }
            .btn:hover {
                background: #138496;
            }
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
            }
            .section-title h2 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .section-title p {
                color: #6c757d;
                max-width: 600px;
                margin: 0 auto;
            }
            footer {
                background: #343a40;
                color: white;
                padding: 2rem 0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">Flask Site</div>
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/sobre">Sobre</a></li>
                    <li><a href="/servicos">Serviços</a></li>
                    <li><a href="/contato">Contato</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <div class="container" style="padding-top: 50px; padding-bottom: 50px;">
                <div class="section-title">
                    <h2>Sobre Nossa Empresa</h2>
                    <p>Conheça nossa história e nossa equipe</p>
                </div>
                
                <div style="max-width: 800px; margin: 0 auto;">
                    <h3>Nossa História</h3>
                    <p>Fundada em 2010, nossa empresa começou com uma pequena equipe de desenvolvedores apaixonados por criar soluções web inovadoras. Ao longo dos anos, crescemos e expandimos nossas competências para abranger uma ampla gama de serviços digitais.</p>
                    
                    <h3>Nossa Missão</h3>
                    <p>Temos como missão fornecer soluções tecnológicas que transformem a maneira como as empresas operam e se conectam com seus clientes. Acreditamos que a tecnologia deve ser acessível e impactante.</p>
                    
                    <h3>Nossos Valores</h3>
                    <ul>
                        <li><strong>Inovação:</strong> Buscamos constantemente novas ideias e abordagens.</li>
                        <li><strong>Qualidade:</strong> Comprometemo-nos com a excelência em tudo o que fazemos.</li>
                        <li><strong>Colaboração:</strong> Trabalhamos juntos para alcançar resultados extraordinários.</li>
                        <li><strong>Integridade:</strong> Agimos com honestidade e transparência em todas as interações.</li>
                    </ul>
                    
                    <h3>Nossa Equipe</h3>
                    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 20px; margin-top: 30px;">
                        <div style="text-align: center;">
                            <img src="https://source.unsplash.com/200x200/?person" alt="Membro da equipe" style="border-radius: 50%; margin-bottom: 10px;">
                            <h4>João Silva</h4>
                            <p>CEO & Fundador</p>
                        </div>
                        <div style="text-align: center;">
                            <img src="https://source.unsplash.com/200x200/?woman" alt="Membro da equipe" style="border-radius: 50%; margin-bottom: 10px;">
                            <h4>Maria Oliveira</h4>
                            <p>CTO</p>
                        </div>
                        <div style="text-align: center;">
                            <img src="https://source.unsplash.com/200x200/?man" alt="Membro da equipe" style="border-radius: 50%; margin-bottom: 10px;">
                            <h4>Carlos Santos</h4>
                            <p>Líder de Desenvolvimento</p>
                        </div>
                        <div style="text-align: center;">
                            <img src="https://source.unsplash.com/200x200/?person" alt="Membro da equipe" style="border-radius: 50%; margin-bottom: 10px;">
                            <h4>Ana Souza</h4>
                            <p>Designer UX/UI</p>
                        </div>
                    </div>
                </div>
            </div>
        </main>
        
        <footer>
            <div class="container">
                <p>&copy; ''' + str(datetime.datetime.now().year) + ''' Flask Site. Todos os direitos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    return html

@app.route('/servicos')
def services():
    # Template HTML completo para a página de serviços
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Serviços - Meu Site Flask</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333;
                line-height: 1.6;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
            }
            header {
                background-color: #343a40;
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 2rem;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
            }
            .nav-links {
                display: flex;
                list-style: none;
            }
            .nav-links li {
                margin-left: 20px;
            }
            .nav-links a {
                text-decoration: none;
                color: white;
                font-weight: 500;
                transition: color 0.3s;
            }
            .nav-links a:hover {
                color: #17a2b8;
            }
            .btn {
                display: inline-block;
                background: #17a2b8;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                transition: background 0.3s;
            }
            .btn:hover {
                background: #138496;
            }
            .feature-card {
                background: #f8f9fa;
                border-radius: 8px;
                padding: 2rem;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                transition: transform 0.3s;
            }
            .feature-card:hover {
                transform: translateY(-5px);
            }
            .feature-icon {
                font-size: 2.5rem;
                margin-bottom: 1rem;
                color: #17a2b8;
            }
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
            }
            .section-title h2 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .section-title p {
                color: #6c757d;
                max-width: 600px;
                margin: 0 auto;
            }
            footer {
                background: #343a40;
                color: white;
                padding: 2rem 0;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">Flask Site</div>
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/sobre">Sobre</a></li>
                    <li><a href="/servicos">Serviços</a></li>
                    <li><a href="/contato">Contato</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <div class="container" style="padding-top: 50px; padding-bottom: 50px;">
                <div class="section-title">
                    <h2>Nossos Serviços</h2>
                    <p>Soluções personalizadas para suas necessidades</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 30px; margin-top: 40px;">
                    <div class="feature-card">
                        <div class="feature-icon">&#128187;</div>
                        <h3>Desenvolvimento Web</h3>
                        <p>Criamos sites e aplicações web modernas, responsivas e otimizadas para SEO.</p>
                        <ul style="padding-left: 20px; margin-top: 15px;">
                            <li>Sites institucionais</li>
                            <li>E-commerce</li>
                            <li>Sistemas web personalizados</li>
                            <li>Progressive Web Apps</li>
                        </ul>
                        <p style="margin-top: 20px;"><strong>Preço:</strong> A partir de R$ 5.000</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">&#128241;</div>
                        <h3>Aplicativos Móveis</h3>
                        <p>Desenvolvemos aplicativos nativos e híbridos para iOS e Android.</p>
                        <ul style="padding-left: 20px; margin-top: 15px;">
                            <li>Aplicativos empresariais</li>
                            <li>Aplicativos de serviços</li>
                            <li>E-commerce mobile</li>
                            <li>Integração com APIs</li>
                        </ul>
                        <p style="margin-top: 20px;"><strong>Preço:</strong> A partir de R$ 8.000</p>
                    </div>
                    
                    <div class="feature-card">
                        <div class="feature-icon">&#128202;</div>
                        <h3>Análise de Dados</h3>
                        <p>Analisamos seus dados para fornecer insights valiosos para o seu negócio.</p>
                        <ul style="padding-left: 20px; margin-top: 15px;">
                            <li>Dashboards interativos</li>
                            <li>Relatórios personalizados</li>
                            <li>Business Intelligence</li>
                            <li>Modelagem preditiva</li>
                        </ul>
                        <p style="margin-top: 20px;"><strong>Preço:</strong> A partir de R$ 3.500</p>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 50px;">
                    <h3>Precisa de um serviço personalizado?</h3>
                    <p>Entre em contato conosco para discutirmos uma solução sob medida para o seu negócio.</p>
                    <a href="/contato" class="btn" style="margin-top: 20px;">Solicitar orçamento</a>
                </div>
            </div>
        </main>
        
        <footer>
            <div class="container">
                <p>&copy; ''' + str(datetime.datetime.now().year) + ''' Flask Site. Todos os direitos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    return html

@app.route('/contato')
def contact():
    # Template HTML completo para a página de contato
    html = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contato - Meu Site Flask</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333;
                line-height: 1.6;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                padding: 20px;
            }
            header {
                background-color: #343a40;
                color: white;
                padding: 1rem 0;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            nav {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 0 2rem;
            }
            .logo {
                font-size: 1.8rem;
                font-weight: 700;
            }
            .nav-links {
                display: flex;
                list-style: none;
            }
            .nav-links li {
                margin-left: 20px;
            }
            .nav-links a {
                text-decoration: none;
                color: white;
                font-weight: 500;
                transition: color 0.3s;
            }
            .nav-links a:hover {
                color: #17a2b8;
            }
            .btn {
                display: inline-block;
                background: #17a2b8;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                transition: background 0.3s;
                border: none;
                cursor: pointer;
            }
            .btn:hover {
                background: #138496;
            }
            .form-group {
                margin-bottom: 1.5rem;
            }
            .form-group label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
            }
            .form-control {
                width: 100%;
                padding: 0.75rem;
                border: 1px solid #ced4da;
                border-radius: 4px;
            }
            textarea.form-control {
                height: 150px;
                resize: vertical;
            }
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
            }
            .section-title h2 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            .section-title p {
                color: #6c757d;
                max-width: 600px;
                margin: 0 auto;
            }
            footer {
                background: #343a40;
                color: white;
                padding: 2rem 0;
                text-align: center;
            }
            .flash-messages {
                padding: 10px;
                margin: 10px 0;
                border-radius: 5px;
                background-color: #d4edda;
                color: #155724;
                border: 1px solid #c3e6cb;
            }
        </style>
    </head>
    <body>
        <header>
            <nav>
                <div class="logo">Flask Site</div>
                <ul class="nav-links">
                    <li><a href="/">Home</a></li>
                    <li><a href="/sobre">Sobre</a></li>
                    <li><a href="/servicos">Serviços</a></li>
                    <li><a href="/contato">Contato</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <!-- Mensagens flash para exibir confirmação de envio -->
            ''' + ('''
            <div class="container">
                <div class="flash-messages">
                    Sua mensagem foi enviada com sucesso! Entraremos em contato em breve.
                </div>
            </div>
            ''' if session.get('mensagem_enviada') else '') + '''
            
            <div class="container" style="padding-top: 50px; padding-bottom: 50px;">
                <div class="section-title">
                    <h2>Entre em Contato</h2>
                    <p>Estamos ansiosos para ouvir de você!</p>
                </div>
                
                <div style="display: flex; flex-wrap: wrap; gap: 30px; max-width: 1200px; margin: 0 auto;">
                    <div style="flex: 1; min-width: 300px;">
                        <h3>Informações de Contato</h3>
                        <p><strong>Endereço:</strong> Av. Paulista, 1000, São Paulo - SP</p>
                        <p><strong>Email:</strong> contato@flasksite.com</p>
                        <p><strong>Telefone:</strong> (11) 3333-4444</p>
                        
                        <h4 style="margin-top: 30px;">Horário de Funcionamento</h4>
                        <p>Segunda a Sexta: 9h às 18h</p>
                        <p>Sábados: 9h às 13h</p>
                    </div>
                    
                    <div style="flex: 2; min-width: 300px;">
                        <h3>Envie uma Mensagem</h3>
                        <form action="/enviar-contato" method="post">
                            <div class="form-group">
                                <label for="nome">Nome</label>
                                <input type="text" id="nome" name="nome" class="form-control" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="email">Email</label>
                                <input type="email" id="email" name="email" class="form-control" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="assunto">Assunto</label>
                                <input type="text" id="assunto" name="assunto" class="form-control" required>
                            </div>
                            
                            <div class="form-group">
                                <label for="mensagem">Mensagem</label>
                                <textarea id="mensagem" name="mensagem" class="form-control" required></textarea>
                            </div>
                            
                            <button type="submit" class="btn">Enviar Mensagem</button>
                        </form>
                    </div>
                </div>
            </div>
        </main>
        
        <footer>
            <div class="container">
                <p>&copy; ''' + str(datetime.datetime.now().year) + ''' Flask Site. Todos os direitos reservados.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    return html

@app.route('/enviar-contato', methods=['POST'])
def send_contact():
    # Simplificando para apenas marcar que a mensagem foi enviada
    session['mensagem_enviada'] = True
    return redirect('/contato')

# Manipulação de erros simplificada
@app.errorhandler(404)
def page_not_found(e):
    return '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página não encontrada</title>
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
                color: #333;
                text-align: center;
            }
            .container {
                padding: 100px 20px;
            }
            h1 {
                font-size: 8rem;
                margin: 0;
                color: #343a40;
            }
            h2 {
                margin-bottom: 20px;
            }
            .btn {
                display: inline-block;
                background: #17a2b8;
                color: white;
                padding: 12px 24px;
                text-decoration: none;
                border-radius: 5px;
                font-weight: 700;
                margin-top: 20px;
            }
            .btn:hover {
                background: #138496;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>404</h1>
            <h2>Página não encontrada</h2>
            <p>A página que você está procurando não existe ou foi movida.</p>
            <a href="/" class="btn">Voltar para Home</a>
        </div>
    </body>
    </html>
    ''', 404

if __name__ == '__main__':
    app.run(debug=True)
