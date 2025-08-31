# 📚 Sistema de Gerenciamento de Biblioteca
Programação para Sistemas Web II – Trabalho Final
Professor: Carlos Anderson


Projeto apresentado ao Curso de Informática para Internet do Instituto Federal de Educaçãoo, Ciência e Tecnologia Baiano - Campus Guanambi, como requisito parcial para obtenção da nota parcial da disciplina de Programação para Sistemas Web, desenvolvido com o objetivo de gerenciar o controle de empréstimos de livros, bem como organizar suas características, como autor e categoria.

## 🔧 Funcionalidades

- Escurecer imagem
- Clarear imagem
- Negativar imagem
- Espelhar imagem verticalmente
- Aplicar filtro de Prewitt (detecção de bordas)
- Desfocar imagem (Gaussiano)
- Converter para tons de cinza
- Pixelizar imagem

## ⚙️ Como Executar Localmente

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/livia-trindade/psw-biblioteca.git
   ```

2. **Acesse a pasta do projeto**:
   ```bash
   cd psw-biblioteca
   ```

3. **Crie e ative um ambiente virtual (Opcional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realize as migrações do banco de dados**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superusuário**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor**:
   ```bash
   python manage.py runserver
   ```

8. **Acesse no localmente no seu navegador**:
   ```bash
   http://127.0.0.1:8000
   ```

## 💡 Instruções de Acesso

O sistema possui dois perfis de usuário:
 - Administrador da Biblioteca: acessa todas as views e pode gerenciar os livros, usuários e registrar empréstimos.
 - Usuário Comum: possui acesso restrito ao sistema, podendo apenas visualizar os livros, autores e categorias cadastradas e solicitar empréstimos.

Ao realizar o login com uma conta de administrador (superusuário), todas as funcionalidades da aplicação estarão disponíveis no menu lateral.
Por exemplo, ao acessar a página de livros, o administrador poderá:
 - Visualizar a lista completa de livros cadastrados;
 - Adicionar novos livros;
 - Atualizar as informações de livros existentes;
 - Excluir registros de livros, se necessário.


## 👥 Integrantes do Grupo

 - Lívia Trindade Vilasboas
 - Pedro Henrique Pereira Xavier
 - Luiz Henrique Viana Rocha
