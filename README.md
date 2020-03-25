# Mapa

## Descrição

Mapa com a localização de subreddits locais linkados em postagens do subreddit [r/EmPortugues](https://www.reddit.com/r/EmPortugues/).

O mapa editado sobre [OpenStreetMap](https://www.openstreetmap.org/#map=4/-15.13/-53.19) gera um arquivo HTML usando [GeoPy](https://geopy.readthedocs.io/en/stable/) com [Nominatim](https://nominatim.openstreetmap.org/) como serviço de geolocalização para encontrar coordenadas de uma lista de lugares a fim de colocar marcadores com links para os respectivos subreddits com a ajuda de [Folium](https://python-visualization.github.io/folium/).

O processo de edição do mapa se dá a partir da autenticação de um agente `Nominatim()` para encontrar `addressdetails` de cada endereço por meio de `geocode()` verificando a `latitude` e a `longitude` de cada um listado em TXT com a finalidade de indicar os respectivos nomes dos subreddits presentes em outra lista paralela para marcar cada um deles com um `Icon()` e adicionar um `Popup()` com um link para determinado subreddit antes de salvar a tarefa com `save()`.

As informações apresentadas no mapa são: a geolocalização de cada local e o link de cada subreddit listado.

## Sumário

* [Instalação](#Instalação)
* [Instruções](#Instruções)
* [Dependências](#Dependências)
* [Colaboração](#Colaboração)
* [Mapa](#Mapa)
* [Referências](#Referências)

## Instalação

1. Clone o repositório;
2. execute um interpretador de comandos;
3. navegue até a pasta;
4. e rode `py map.py`.

## Instruções

Para alterar o agente de usuário, em [map.py](https://github.com/subreddit-emportugues/mapa/blob/master/map.py), edite:
```
geonames_account=''
```

Para alterar os detalhes de saída, em [map.py](https://github.com/subreddit-emportugues/mapa/blob/master/map.py), edite:
```
place_location = g.geocode(place, addressdetails=True, timeout=1000)
```

Para alterar os detalhes do endereço, em [map.py](https://github.com/subreddit-emportugues/mapa/blob/master/map.py), edite:
```
location = [place_location.latitude, place_location.longitude],
```

Para alterar as cores dos ícones dos marcadores, em [map.py](https://github.com/subreddit-emportugues/mapa/blob/master/map.py), edite:
```
icon = folium.Icon(color="orange"),
```

Para alterar os textos das janelas pop-up, em [map.py](https://github.com/subreddit-emportugues/mapa/blob/master/map.py), edite:
```
popup = folium.Popup('<a href="https://www.reddit.com/' + subreddit_line + '" target="_blank" style="font-weight:bold;">' + subreddit_line + '</a>')
```

## Dependências

> GeoPy/Nominatim
```
from geopy import Nominatim
```
```
from geopy.exc import GeocoderServiceError
```
```
from geopy.exc import GeocoderTimedOut
```

> Folium
```
import folium
```
```
from folium.features import CustomIcon
```

> linecache
```
import linecache
```

> time
```
import time
```

## Colaboração

Você pode colaborar com o desenvolvimento deste projeto! 

[Confira os kanbans deste projeto](https://github.com/orgs/subreddit-emportugues/projects/9), [entre em contato com a equipe de moderação](https://reddit.com/message/compose?to=/r/EmPortugues) e [participe da equipe de desenvolvimento](https://github.com/orgs/subreddit-emportugues/teams/desenvolvedores) para saber a respeito do progresso deste repositório caso queira colaborar antes de [reportar um novo problema](https://github.com/subreddit-emportugues/auto-moderador/issues) ou [solicitar o recebimento de uma modificação](https://github.com/subreddit-emportugues/auto-moderador/pulls).

## Mapa

### https://emportugues.org/data/map.html

## Referências

* Mapa: https://emportugues.org/data/map.html
* Comunidade: https://www.reddit.com/r/EmPortugues
* Organização: https://github.com/subreddit-emportugues
* Repositório: https://github.com/subreddit-emportugues/mapa
* Projeto: https://github.com/orgs/subreddit-emportugues/projects/9
* Equipe: https://github.com/orgs/subreddit-emportugues/teams/desenvolvedores
* Licença: https://github.com/subreddit-emportugues/mapa/blob/master/LICENSE
