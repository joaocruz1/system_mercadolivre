Sistema de Importação e Publicação de Produtos no Mercado Livre 🚀

📝 Descrição do Projeto

Este sistema tem como objetivo automatizar o processo de importação de produtos de uma planilha Excel e publicação desses produtos na plataforma Mercado Livre. Ele foi desenvolvido para facilitar o trabalho de gestores de e-commerce, reduzindo erros manuais e otimizando o tempo.

✨ Funcionalidades Principais

🔐 Realizar Login: Autentica o usuário no sistema para acessar a API do Mercado Livre.

📂 Importar Planilha de Produtos: Lê os dados de uma planilha Excel contendo informações como nome, descrição, preço, categoria, quantidade e URL da imagem.

✅ Validação dos Dados: Verifica se os dados da planilha estão completos e seguem o formato exigido pela API do Mercado Livre.

📤 Publicação de Produtos: Envia os produtos para a plataforma Mercado Livre utilizando sua API oficial.

📜 Geração de Logs: Salva um log com o status de publicação de cada produto (sucesso ou erro).

📊 Atualização da Planilha: Adiciona uma coluna com o status de cada produto após o processamento.

🔄 Fluxo de Operação

Conforme descrito no fluxograma:

O sistema solicita o login do usuário.

Caso o login falhe, o processo é encerrado.

O usuário insere a planilha de produtos.

Se nenhuma planilha for inserida, o sistema exibe uma mensagem de erro e solicita a entrada novamente.

Os dados da planilha são lidos e validados.

Dados incompletos ou inválidos geram um erro, e o usuário deve corrigir a planilha.

Uma vez validados, os dados são extraídos e enviados para a API do Mercado Livre.

Produtos publicados com sucesso são registrados.

Produtos com erro de publicação geram logs detalhados.

O sistema atualiza a planilha com o status final de cada produto e encerra o processo.

📋 Requisitos do Sistema

Linguagem: Python 🐍

Bibliotecas Necessárias:

pandas para manipulação de planilhas.

openpyxl para leitura e escrita de arquivos Excel.

requests para integração com a API do Mercado Livre.

python-dotenv para gerenciar credenciais.

⚙️ Configuração Inicial

Clone o repositório do sistema.

Instale as dependências utilizando o seguinte comando:

pip install pandas openpyxl requests python-dotenv

Crie um arquivo .env na raiz do projeto e adicione o token de acesso à API do Mercado Livre:

MERCADO_LIVRE_ACCESS_TOKEN=seu_token_aqui

Prepare a planilha com os campos obrigatórios:

Nome 🛍️

Descrição ✍️

Categoria 🗂️

Preço 💰

Quantidade 📦

URL da imagem 🌐

🚀 Como Utilizar

Execute o script principal do sistema:

python main.py

Insira as credenciais de login quando solicitado.

Forneça o caminho para a planilha de produtos.

Aguarde o processamento e verifique os logs gerados.

Consulte a planilha atualizada para visualizar o status final de cada produto.

🔮 Melhorias Futuras

Implementar suporte para tokens dinâmicos (refresh token).

Adicionar interface gráfica para facilitar o uso.

Suporte para outras plataformas de e-commerce.

🤝 Contribuições

Contribuições são bem-vindas! Envie um pull request ou entre em contato com os mantenedores do projeto.
