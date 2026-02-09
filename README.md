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
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Digite o destino da sua viagem no campo de busca

4. Clique em "Buscar Dicas" para ver as recomendações

## 📸 Exemplo de Uso

1. Insira um destino (ex: "Paris", "Rio de Janeiro", "Tóquio")
2. O aplicativo irá buscar dicas de viagem na internet
3. Visualize as dicas com informações úteis sobre o destino

## 🔧 Configuração

O aplicativo roda por padrão na porta 5000. Para alterar, edite o arquivo `app.py`:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Altere a porta aqui
```

## 📝 Licença

Este projeto está sob a licença especificada no arquivo LICENSE.
