import requests
from bs4 import BeautifulSoup


def decode_gdoc(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table in the google document
    table = soup.find('table')
    #Ignore header
    rows = table.find_all('tr')[1:]
    char_map = {}

    #Max grid length and width
    max_x = 0
    max_y = 0

#Iterate for rows and extract x,unicode char,and y
    for row in rows:
        cells = row.find_all('td')
        if len(cells)==3:
            x = int(cells[0].text.strip())
            char = cells[1].text.strip()
            y = int(cells[2].text.strip())
            char_map[(x,y)]= char
            max_x = max(max_x, x)
            max_y = max(max_y, y)

#Print grid
    for y in reversed(range(max_y + 1)):
        row_str = ""
        for x in range(max_x + 1):
            row_str += char_map.get((x, y), " ")
        print(row_str)  


#URL to decode
url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
decode_gdoc(url)