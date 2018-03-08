# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
# Read in a page
html = scraperwiki.scrape("https://www.wagamama.com/restaurants?q=west%20midlands")
#
# Find something on the page using css selectors
root = lxml.html.fromstring(html)
restaurants = root.cssselect("div.content")

for restaurant in restaurants:
    record = {}
    record['Name'] = restaurant("h2").text
    record['Address'] = restaurant("div.address").text
    record['Postcode'] = restaurant("div.postcode").text
    record['Company'] = "Wagamama"

    print record, '------------'

    scraperwiki.sqlite.save(['Name'], record)

# Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
