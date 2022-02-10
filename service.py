import requests
from bs4 import BeautifulSoup 
from sql_parser import SQLighter
sql = SQLighter('parser')

url_action='https://www.ivi.ru/movies/boeviki'
url_drama = 'https://www.ivi.ru/movies/drama'
url_comedy = 'https://www.ivi.ru/movies/comedy'
url_triller = 'https://www.ivi.ru/movies/thriller'
url_melodrama = 'https://www.ivi.ru/movies/melodramy'
url_fantastika = 'https://www.ivi.ru/movies/fantastika'
url_fentezi = 'https://www.ivi.ru/movies/fentezi'
url_horror = 'https://www.ivi.ru/movies/horror'
url_war = 'https://www.ivi.ru/movies/voennye'
url_cartoon = 'https://www.ivi.ru/movies/detskiy'


sql.create_table()

def get_html(url): 
    response = requests.get(url)
    return response.text


def get_all_links(html): #находит определенные теги
    links=[]
    soup=BeautifulSoup(html,"html.parser")
    divs=soup.find("ul", class_="gallery__list gallery__list_slimPosterBlock gallery__list_type_poster gallery__gallery__list").find_all("li", class_="gallery__item gallery__item_virtual")
    for item in divs:
        movie_link=item.find("a").get('href')
        full_link="https://www.ivi.ru"+movie_link
        links.append(full_link)
    return links

def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find('section', class_='pageSection details__pageSection')
    name = divs.find('h1', class_='details__titleText details__titleText_primary').text
    year = divs.find('div', class_='parameters__info').find_all('a', class_='link parameters__link')[0].text
    city = divs.find('div', class_='parameters__info').find_all('a', class_='link parameters__link')[1].text
    # link_card = divs.find('div', class_='gallery__header').find('a').get('href') #Вот здесь сама сделаешь дома!
    
    print(name,year,city)
    sql.add_new_movies(name,year,city)

def parse():
    # for page in range(0,11):
    #     html = get_html(url_action)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)

    # for page in range(0,11):
    #     html = get_html(url_drama)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)
    # for page in range(0,11):
    #     html = get_html(url_comedy)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    # #         get_data(card_html)
    # for page in range(0,11):
    #     html = get_html(url_triller)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)
    # for page in range(0,11):
    #     html = get_html(url_melodrama)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)
    # for page in range(0,11):
    #     html = get_html(url_fantastika)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)
    for page in range(0,11):
        html = get_html(url_fentezi)
        movies = get_all_links(html)
        for card in movies:
            card_html = get_html(card)
            get_data(card_html)

    # html = get_html(url_horror)
    # movies = get_all_links(html)
    # for card in movies:
    #     card_html = get_html(card)
    #     get_data(card_html)

    # html = get_html(url_war)
    # movies = get_all_links(html)
    # for card in movies:
    #     card_html = get_html(card)
    #     get_data(card_html)

    # for page in range(0,18):
    #     html = get_html(url_cartoon)
    #     movies = get_all_links(html)
    #     for card in movies:
    #         card_html = get_html(card)
    #         get_data(card_html)

    
        

# parse()

      





