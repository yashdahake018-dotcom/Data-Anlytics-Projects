from bs4 import BeautifulSoup
import requests

url = 'https://docs.google.com/document/d/e/2PACX-1vSvm5gDlNVt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6Zxwn8rE6S4ghUsCj2VKR21oEP/pub'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr')

grid_data = {}
max_x, max_y = 0, 0
for row in rows[1:]:
  cols = row.find_all('td')
  if len(cols) == 3:
    try:
      x = int(cols[0].get_text().strip())
      char = cols[1].get_text().strip()
      y = int(cols[2].get_text().strip())
      grid_data[(x, y)] = char
      max_x = max(max_x, x)
      max_y = max(max_y, y)
    except ValueError:
      continue

for y in range(max_y, -1, -1):
  print(''.join([grid_data.get((x, y), ' ') for x in range(max_x + 1)]))

