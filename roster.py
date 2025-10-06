import pandas as pd
from bs4 import BeautifulSoup as Soup
from get_site import get_site
import io

def scrape_roster(roster_id : int) -> pd.DataFrame:
    url: str = f"https://stats.ncaa.org/teams/{roster_id}/roster"
    site_text: io.StringIO = get_site(url)
    roster: pd.DataFrame = pd.read_html(site_text)[0]
    soup = Soup(site_text, 'html.parser')
    rows: list[Soup] = soup.find(class_="dataTable small_font no_padding").find_all('tr')
    tags: list[int] = []
    for row in rows[1:]:
        tags.append(int(row.find('a')['href'].split('/')[-1]))
    roster['Player_id'] = 0
    for i, player_id in enumerate(roster['Player_id']):
        roster.at[i, 'Player_id'] = tags[i]
    roster = roster.rename(columns={'GP': 'Games_Played', 'GS': 'Games_Started', 'High School' : 'High_School', '#' : 'Number'})
    pd.to_numeric(roster['Games_Played'], errors='coerce').astype("Int64")
    pd.to_numeric(roster['Games_Started'], errors='coerce').astype("Int64")
    pd.to_numeric(roster['Number'], errors='coerce').astype("Int64")
    return roster



if __name__ == '__main__':
    scrape_roster(590565).to_csv("test.csv")