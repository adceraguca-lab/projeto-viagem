# projeto-viagem
APP Planejamento de viagem

## 📋 Descrição

Aplicativo de viagem que busca na internet dicas quando o usuário coloca o destino da viagem. O aplicativo permite que o usuário insira um destino e receba automaticamente dicas de viagem relevantes pesquisadas na web.

## 🚀 Funcionalidades

- Interface web intuitiva e responsiva
- Entrada de destino de viagem
- Busca automática de dicas de viagem na internet
- Exibição de resultados com títulos, descrições e links
- Dicas genéricas como fallback caso a busca falhe

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask (framework web)
- BeautifulSoup4 (parsing HTML)
- Requests (requisições HTTP)
- HTML/CSS/JavaScript

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/adceraguca-lab/projeto-viagem.git
cd projeto-viagem
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Como Usar

1. Execute o aplicativo:
```bash
# Para desenvolvimento (com debug):
FLASK_DEBUG=true python app.py

# Para produção:
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Digite o destino da sua viagem no campo de busca

4. Clique em "Buscar Dicas" para ver as recomendações

## 🔒 Segurança

O aplicativo implementa várias medidas de segurança:
- Sanitização de entrada de usuário para prevenir XSS
- Validação de URLs antes de exibir links
- Modo debug desabilitado por padrão em produção
- Timeout configurado para requisições externas
- Uso de textContent em vez de innerHTML para prevenir injeção de código

## 📸 Exemplo de Uso

1. Insira um destino (ex: "Paris", "Rio de Janeiro", "Tóquio")
2. O aplicativo irá buscar dicas de viagem na internet
3. Visualize as dicas com informações úteis sobre o destino

## 🔧 Configuração

O aplicativo roda por padrão na porta 5000 e em localhost (127.0.0.1).

Para habilitar modo debug durante desenvolvimento:
```bash
FLASK_DEBUG=true python app.py
```

Para produção, recomenda-se usar um servidor WSGI como Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📝 Licença

Este projeto está sob a licença especificada no arquivo LICENSE.
