import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()

    # NASA MARRS NEWS
    # URL of page to be scraped
    url = "https://mars.nasa.gov/news/"
    # Retrieve page with Browser
    browser.visit(url)

    # HTML object
    html = browser.html 

    # Create BeautifulSoup object; parse with 'html.parser'
    soup = BeautifulSoup(html, 'html.parser')

    # Extract latest News title text
    news_title_s = soup.find_all('div', class_="content_title")[1].find("a").text

    # Extract latest News paragraph text
    news_p_s = soup.find('div', class_="article_teaser_body").text

    # Quit browser
    browser.quit()

    #MARS FACTS

    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # URL of page to be scraped
    facts_url = "https://space-facts.com/mars/"

    # Use the read_html function in Pandas to automatically scrape any tabular data from a page
    facts_tables = pd.read_html(facts_url)

    # Slice off any of those dataframes that we want using normal indexing
    facts_df = facts_tables[0]

    # Rename the columns and set Description column as index
    facts_df = facts_df.rename (columns ={0:"Description", 1:"Mars"})
    facts_df.set_index("Description", inplace=True) 

    # Convert the data to a HTML table string
    html_table = facts_df.to_html()

    # Strip unwanted newlines to clean up the table
    html_table = html_table.replace('\n', '')

    #MARS HEMISPHERE

    # URL of page to be scraped
    hem_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Retrieve page with the requests module
    response = requests.get(hem_url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')

    # Examine the results, then determine element that contains sought info
    # titles are returned as an iterable list
    results = soup.find_all('div', class_='description')

    titles = []

    # Loop through returned results
    for result in results:
        title = result.find('h3').text
        titles.append(title)
    
    # Examine the results, then determine element that contains sought info
    # image urls are returned as an iterable list
    img_results = soup.find_all('div', class_='item')

    image_urls = []

    # Loop through returned results
    for result in img_results:
        href = result.find('a')['href']
        link = 'https://astrogeology.usgs.gov' + href
    
        # Retrieve page with the requests module
        response2 = requests.get(link)
        # Create BeautifulSoup object; parse with 'lxml'
        soup2 = BeautifulSoup(response2.text, 'lxml')
        href2 = soup2.find('img', class_='wide-image')['src']
        img_url = 'https://astrogeology.usgs.gov' + href2
        image_urls.append(img_url)

    #Append the dictionary with the image url string and the hemisphere title to a list. 
    #This list will contain one dictionary for each hemisphere.
    hemisphere_image_urls = [
        {"title": titles[0], "img_url": image_urls[0]},
        {"title": titles[1], "img_url": image_urls[1]},
        {"title": titles[2], "img_url": image_urls[2]},
        {"title": titles[3], "img_url": image_urls[3]},
    ]

    all_info = {
        "latest_news_title": news_title_s,
        "latest_news_paragraph": news_p_s,
        "mars_fact": html_table,
        "mars_hemisphere": hemisphere_image_urls
    }

    return all_info