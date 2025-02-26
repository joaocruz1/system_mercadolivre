Aqui está o README atualizado com as bibliotecas adicionadas e suas respectivas explicações sobre o funcionamento no sistema:

---

# Sistema de Gerenciamento de E-commerce 🚀

Bem-vindo ao **Sistema de Gerenciamento de E-commerce para o Mercado Livre**! 🎉  

Este projeto foi desenvolvido para auxiliar gestores de e-commerce no gerenciamento de produtos, usuários e operações de vendas, oferecendo uma solução completa e automatizada. Com uma interface interativa e intuitiva, você poderá controlar o fluxo de produtos, gerenciar usuários e supervisionar todas as operações de forma eficiente.  

---

## Objetivo do Sistema  

O sistema tem como finalidade principal:  
- **Gerenciar usuários** de uma loja, permitindo controle de acesso e permissões. 👥  
- **Adicionar, editar e remover produtos** diretamente no sistema, sem a necessidade de planilhas. 🛠️  
- **Supervisionar o fluxo de produtos**, garantindo que todas as operações sejam rastreadas e auditadas. 📊  
- **Integrar com a API do Mercado Livre** para publicação e atualização de produtos. 📤  
- **Gerar logs detalhados** com o status de cada operação (sucesso ou erro). 📜  

---

## Funcionalidades Principais  

### 1. **Login e Autenticação** 🔐  
- Tela de login interativa para autenticação de usuários.  
- Controle de acesso baseado em perfis (administrador, gestor, operador).  
- Logout seguro com limpeza de sessão.  

### 2. **Gerenciamento de Usuários** 👥  
- Cadastro de novos usuários com diferentes níveis de permissão.  
- Edição e remoção de usuários existentes.  
- Visualização de todos os usuários cadastrados na loja.  

### 3. **Gerenciamento de Produtos** 🛍️  
- **Adição de produtos**: Inserção direta de produtos no sistema, com campos como nome, descrição, categoria, preço, quantidade e URL da imagem.  
- **Edição de produtos**: Atualização de informações dos produtos cadastrados.  
- **Remoção de produtos**: Exclusão de produtos do sistema.  
- **Visualização de produtos**: Listagem de todos os produtos com filtros por categoria, status, etc.  

### 4. **Supervisão do Fluxo de Produtos** 📊  
- Acompanhamento em tempo real do status de cada produto (publicado, pendente, erro).  
- Histórico de operações realizadas por cada usuário.  
- Geração de relatórios detalhados para auditoria.  

### 5. **Integração com o Mercado Livre** 📤  
- Publicação de produtos diretamente na plataforma do Mercado Livre utilizando a API oficial.  
- Atualização de produtos já publicados.  
- Sincronização de status entre o sistema e a plataforma.  

### 6. **Geração de Logs e Relatórios** 📜  
- Logs detalhados com o status de cada operação (sucesso ou erro).  
- Relatórios personalizados para análise de desempenho e tomada de decisão.  

### 7. **Interface Web Intuitiva** 💻  
- Navegação simples e eficiente entre as funcionalidades.  
- Design responsivo para acesso em diferentes dispositivos.  

---

## Tecnologias Utilizadas 🔧  

### Bibliotecas Principais  

- **Python** 🐍: Linguagem principal do sistema.  
- **Flask** 🌐: Framework web para criação da interface e rotas.  
- **SQLAlchemy** 🗃️: ORM para gerenciamento do banco de dados.  
- **pandas** 📊: Para manipulação de dados e geração de relatórios.  
- **requests** 📡: Para integração com a API do Mercado Livre.  
- **python-dotenv** 🔑: Para gerenciamento de variáveis de ambiente.  
- **Bootstrap** 🎨: Para o design da interface web.  

### Outras Bibliotecas e suas Funções  

- **blinker==1.9.0**: Fornece suporte a sinais (signals) no Flask, permitindo a execução de ações específicas em eventos do sistema.  
- **cachelib==0.13.0**: Utilizado para caching de dados, melhorando o desempenho do sistema.  
- **cachetools==5.5.1**: Oferece ferramentas para implementação de caches em memória.  
- **certifi==2025.1.31**: Fornece certificados SSL para garantir conexões seguras.  
- **charset-normalizer==3.4.1**: Auxilia na normalização de caracteres para evitar problemas de codificação.  
- **click==8.1.8**: Biblioteca para criação de interfaces de linha de comando (CLI).  
- **colorama==0.4.6**: Adiciona cores ao terminal para melhorar a legibilidade de logs.  
- **Flask-Login==0.6.3**: Gerencia autenticação e sessões de usuários no Flask.  
- **Flask-Session==0.8.0**: Armazena sessões de usuários no servidor.  
- **future==1.0.0**: Garante compatibilidade com versões futuras do Python.  
- **google-auth==2.38.0**: Autenticação com APIs do Google.  
- **google-auth-oauthlib==1.2.1**: Suporte a OAuth para autenticação com APIs do Google.  
- **gspread==6.1.4**: Integração com planilhas do Google Sheets.  
- **httplib2==0.22.0**: Biblioteca HTTP para requisições.  
- **idna==3.10**: Suporte a internacionalização de domínios (IDNA).  
- **itsdangerous==2.2.0**: Geração de tokens seguros para autenticação.  
- **Jinja2==3.1.5**: Motor de templates para renderização de páginas HTML.  
- **MarkupSafe==3.0.2**: Segurança para templates HTML.  
- **msgspec==0.19.0**: Serialização e desserialização de dados.  
- **oauth2client==4.1.3**: Cliente OAuth2 para autenticação.  
- **oauthlib==3.2.2**: Implementação do protocolo OAuth.  
- **peewee==3.17.8**: ORM leve para gerenciamento de banco de dados.  
- **pefile==2021.9.3**: Análise de arquivos PE (Windows).  
- **pewee==0.1.0.dev9**: Extensões para o ORM Peewee.  
- **pyasn1==0.6.1**: Implementação de ASN.1 para criptografia.  
- **pyasn1_modules==0.4.1**: Módulos ASN.1 para protocolos como SSL.  
- **pyparsing==3.2.1**: Biblioteca para análise de texto.  
- **requests-oauthlib==2.0.0**: Suporte a OAuth para a biblioteca `requests`.  
- **rsa==4.9**: Implementação de criptografia RSA.  
- **six==1.17.0**: Compatibilidade entre Python 2 e 3.  
- **termcolor==2.3.0**: Adiciona cores ao terminal.  
- **urllib3==2.3.0**: Cliente HTTP para requisições seguras.  
- **Werkzeug==3.1.3**: Biblioteca utilitária para o Flask.  
- **yaspin==3.1.0**: Exibe spinners animados no terminal durante operações.  

---

## Configuração Inicial ⚙️  

### 1. **Clone o Repositório**  
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```

### 2. **Instale as Dependências**  
   ```bash
   pip install -r requirements.txt
   ```

### 3. **Configure as Variáveis de Ambiente**  
   Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:  
   ```plaintext
   MERCADO_LIVRE_ACCESS_TOKEN=seu_token_aqui
   DATABASE_URL=sqlite:///database.db
   SECRET_KEY=sua_chave_secreta_aqui
   ```

### 4. **Inicialize o Banco de Dados**  
   Execute o script para criar o banco de dados e as tabelas necessárias:  
   ```bash
   python init_db.py
   ```

### 5. **Execute o Sistema**  
   Inicie o servidor Flask:  
   ```bash
   python main.py
   ```

---

## Como Utilizar 🚀  

### 1. **Acesso ao Sistema**  
- Acesse a interface web através do navegador.  
- Faça login com suas credenciais.  

### 2. **Gerenciamento de Usuários**  
- Na seção de usuários, adicione, edite ou remova usuários conforme necessário.  

### 3. **Gerenciamento de Produtos**  
- Adicione novos produtos, edite informações existentes ou remova produtos do sistema.  
- Visualize todos os produtos cadastrados com filtros e opções de busca.  

### 4. **Publicação no Mercado Livre**  
- Selecione os produtos que deseja publicar e envie para o Mercado Livre.  
- Acompanhe o status de publicação em tempo real.  

### 5. **Supervisão e Relatórios**  
- Acesse a seção de supervisão para acompanhar o fluxo de produtos.  
- Gere relatórios detalhados para análise e auditoria.  

---

## Melhorias Futuras 🔮  

- **Suporte para tokens dinâmicos (Refresh Token)**: Para maior segurança e praticidade na integração com a API do Mercado Livre.  
- **Integração com outras plataformas de e-commerce**: Expansão do sistema para outras plataformas como Amazon, Shopee, etc.  
- **Notificações em tempo real**: Alertas para operações concluídas ou erros durante a publicação.  
- **Dashboard analítico**: Gráficos e métricas para análise de desempenho das vendas.  

---

## Contribuições 🤝  

Sua contribuição é muito bem-vinda! Se você deseja ajudar a melhorar este projeto:  

1. Faça um **fork** do repositório.  
2. Crie uma **branch** com a sua feature ou correção.  
3. Envie um **Pull Request** com as alterações sugeridas.  

Se precisar de ajuda, entre em contato com os mantenedores do projeto.  

---

**Aproveite a experiência e boas vendas! 🛒🚀**  

--- 

Agora o README está completo com todas as bibliotecas explicadas e suas funções no sistema! 🚀