from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def fetch_anime():
    try:
        response = requests.get("https://api.jikan.moe/v4/top/anime")
        response.raise_for_status()
        return response.json()['data']
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/anime')
def get_anime():
    anime_data = fetch_anime()
    
    # english title
    for anime in anime_data:
        anime['title'] = anime.get('title_english') or anime.get('title')
        
    return jsonify(anime_data)

if __name__ == '__main__':
    app.run(debug=True)
