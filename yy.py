import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_table_content(i_page):
    url = f'https://www.talaadthai.com={i_page}'
    source = requests.get(url)

    soup = BeautifulSoup(source.content, 'lxml', from_encoding='utf-8')
    div = soup.find('div', id='content')
    table = div.find('table', class_='tdlg')
    rows = table.find_all('tr')

    ls = []  # list to store text of all elements in all the rows.
    for i, row in enumerate(rows):
        # Each element is enclosed by either <th> or <td> tag.
        if i == 0:
            elements = row.find_all('th')
        else:
            elements = row.find_all('td')

        # list to store text of all the elements in this row:
        ls_elements_in_row = []
        for element in elements:
            text = element.text
            ls_elements_in_row += [text]

        ls += [ls_elements_in_row]

    df = pd.DataFrame(ls[1::])
    df.columns = ls[0]

    return df


if __name__ == '__main__':
    app.run_server(debug=True)
