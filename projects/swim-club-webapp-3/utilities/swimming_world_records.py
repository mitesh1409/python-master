import gazpacho
import json

# Scraping the page at this URL to retrieve swimming world records data.
URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
# No. of table records that we need.
TABLE_RECORDS = (0, 1, 3, 4)
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")
PATH_TO_JSON_DATA = "swimming_world_records.json"

html = gazpacho.get(URL)
soup = gazpacho.Soup(html)
tables = soup.find('table')

world_records = {}
for table_record, course in zip(TABLE_RECORDS, COURSES):
    world_records[course] = {}
    for row in tables[table_record].find("tr", mode="all")[1:]:
        columns = row.find("td", mode="all")
        event = columns[0].text
        if "relay" not in event:
            time = columns[1].text
            name = columns[3].text
            country = columns[4].text
            date = columns[5].text
            world_records[course][event] = {
                "time": time,
                "name": name,
                "country": country,
                "date": date
            }

with open(PATH_TO_JSON_DATA, "w") as wr_file:
    json.dump(world_records, wr_file)

print(f"Swimming world records data are saved into {PATH_TO_JSON_DATA} file.")
