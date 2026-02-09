from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def buscar_dicas_viagem(destino):
    """
    Busca dicas de viagem na internet para o destino especificado.
    """
    dicas = []
    
    try:
        # Usando DuckDuckGo HTML para buscar dicas de viagem
        query = f"{destino} dicas de viagem turismo"
        url = f"https://html.duckduckgo.com/html/?q={requests.utils.quote(query)}"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extrair resultados de busca
            resultados = soup.find_all('div', class_='result')
            
            for resultado in resultados[:5]:  # Pegar os primeiros 5 resultados
                titulo_elem = resultado.find('a', class_='result__a')
                snippet_elem = resultado.find('a', class_='result__snippet')
                
                if titulo_elem and snippet_elem:
                    titulo = titulo_elem.get_text(strip=True)
                    snippet = snippet_elem.get_text(strip=True)
                    link = titulo_elem.get('href', '')
                    
                    dicas.append({
                        'titulo': titulo,
                        'descricao': snippet,
                        'link': link
                    })
        
        # Se não encontrou resultados, adicionar dicas genéricas
        if not dicas:
            dicas = [
                {
                    'titulo': f'Explore {destino}',
                    'descricao': f'Pesquise sobre os principais pontos turísticos de {destino}.',
                    'link': '#'
                },
                {
                    'titulo': 'Documentação',
                    'descricao': 'Verifique se você precisa de visto ou documentos especiais.',
                    'link': '#'
                },
                {
                    'titulo': 'Clima',
                    'descricao': f'Consulte a previsão do tempo para {destino} antes de viajar.',
                    'link': '#'
                },
                {
                    'titulo': 'Moeda Local',
                    'descricao': 'Informe-se sobre a moeda local e taxas de câmbio.',
                    'link': '#'
                },
                {
                    'titulo': 'Cultura e Costumes',
                    'descricao': f'Aprenda sobre a cultura e costumes locais de {destino}.',
                    'link': '#'
                }
            ]
    
    except Exception as e:
        print(f"Erro ao buscar dicas: {e}")
        # Retornar dicas genéricas em caso de erro
        dicas = [
            {
                'titulo': f'Planeje sua viagem para {destino}',
                'descricao': 'Pesquise sobre hospedagem, transporte e atrações turísticas.',
                'link': '#'
            },
            {
                'titulo': 'Documentação necessária',
                'descricao': 'Verifique passaporte, vistos e vacinas necessárias.',
                'link': '#'
            },
            {
                'titulo': 'Melhor época para visitar',
                'descricao': f'Pesquise qual a melhor época do ano para visitar {destino}.',
                'link': '#'
            }
        ]
    
    return dicas


@app.route('/')
def index():
    """Página inicial com formulário para entrada do destino."""
    return render_template('index.html')


@app.route('/buscar', methods=['POST'])
def buscar():
    """Endpoint para buscar dicas de viagem."""
    destino = request.form.get('destino', '').strip()
    
    if not destino:
        return jsonify({'erro': 'Por favor, informe um destino'}), 400
    
    dicas = buscar_dicas_viagem(destino)
    
    return jsonify({
        'destino': destino,
        'dicas': dicas
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
