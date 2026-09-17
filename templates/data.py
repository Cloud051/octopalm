import requests
from dataclasses import dataclass

@dataclass
class Anime:
    title: str | int
    type1: str
    source: str
    episodes: int
    status: str
    airing: bool
    aired: str | int
    duration: str | int
    rating: str | int
    score: int
    scored_by: int
    rank: int
    popularity: int
    members: int
    favorites: int
    synopsis: str | int
    season: str
    year: int
    img: str
    
    def __str__(self):
        return f"""
    Title: {self.title}
    Type: {self.type1}
    Source: {self.source}
    Episodes: {self.episodes}
    Status: {self.status}
    Airing: {self.airing}
    Aired: {self.aired}
    Duration: {self.duration}
    Rating: {self.rating}
    Score: {self.score}
    Scored By: {self.scored_by}
    Rank: {self.rank}
    Popularity: {self.popularity}
    Members: {self.members}
    Favorites: {self.favorites}
    Synopsis: {self.synopsis}
    Season: {self.season}
    Year: {self.year}
    img: {self.img}
    """
    
    def to_dict(self):
        return {
            'title': self.title,
            'type': self.type1,
            'source': self.source,
            'episodes': self.episodes,
            'status': self.status,
            'airing': self.airing,
            'aired': self.aired,
            'duration': self.duration,
            'rating': self.rating,
            'score': self.score,
            'scored_by': self.scored_by,
            'rank': self.rank,
            'popularity': self.popularity,
            'members': self.members,
            'favorites': self.favorites,
            'synopsis': self.synopsis,
            'season': self.season,
            'year': self.year,
            'img': self.img
        }

def fetch_anime(endpoint_url: str = "https://api.jikan.moe/v4/top/anime"):
    try:
        response = requests.get(endpoint_url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['data']
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching anime: {e}")
        return []

def create_anime_objects(data_anime):
    anime_objects = []
    for anime in data_anime:
        anime_obj = Anime(
            title=anime['title_english'],
            type1=anime['type'],
            source=anime['source'],
            episodes=anime['episodes'],
            status=anime['status'],
            airing=anime['airing'],
            aired=anime['aired']['string'],
            duration=anime['duration'],
            rating=anime['rating'],
            score=anime['score'],
            scored_by=anime['scored_by'],
            rank=anime['rank'],
            popularity=anime['popularity'],
            members=anime['members'],
            favorites=anime['favorites'],
            synopsis=anime['synopsis'],
            season=anime['season'],
            year=anime['year'],
            img=anime['images']['jpg']['image_url']
        )
        anime_objects.append(anime_obj)
    return anime_objects

def save_anime_to_file(anime_objects):
    with open("anime.txt", "w") as file:
        for anime in anime_objects:
            file.write(f"{anime.title},{anime.type1},{anime.source},{anime.episodes},{anime.status},{anime.airing},{anime.aired},{anime.duration},{anime.rating},{anime.score},{anime.scored_by},{anime.rank},{anime.popularity},{anime.members},{anime.favorites},{anime.synopsis},{anime.season},{anime.year},{anime.img}\n")

def display_anime(anime_object):
    for anime in anime_object:
        print(anime)
        print("---")

anime_data = fetch_anime()
anime_objects = create_anime_objects(anime_data)
display_anime(anime_objects)
save_anime_to_file(anime_objects)
