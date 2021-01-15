# Web Scraping Challenge

Data and instructions provided by UC Berkeley Extension Data Analytics Bootcamp.

# Introduction 

The goal of this assignment is to use my newfound knowledge and skills on web scraping and using MongoDB as well as learned materials on flask, html and bootstrap to create a web application. 

The web application scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page.

# Technologies/Libraries

- HTML

- Inline CSS
 
- Bootstrap 4.5

- Python Pandas

- Jupyter Notebook

- flask and Flask, render_template, redirect

- flask_pymongo and PyMongo

- splinter and Browser

- BeautifulSoup

- requests

- webdriver_manager.chrome and ChromeDriverManager

-  Conda Environment used: PythonData

# Detailed Instructions/Assignment Background

### Step 1 - Scraping

- Complete your initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

- Create a Jupyter Notebook file called mission_to_mars.ipynb and use this to complete all of your scraping and analysis tasks. The following outlines what you need to scrape.

##### NASA Mars News

- Scrape the NASA Mars News Site (https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text. Assign the text to variables that you can reference later.

##### Mars Facts

- Visit the Mars Facts webpage here (https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

- Use Pandas to convert the data to a HTML table string.

##### Mars Hemispheres

- Visit the USGS Astrogeology site here (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

- You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

- Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

- Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.

### Step 2 - MongoDB and Flask Application

    - Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

    - Start by converting your Jupyter notebook into a Python script called scrape_mars.py with a function called scrape that will execute all of your scraping code from above and return one Python dictionary containing all of the scraped data.

    - Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

    - Store the return value in Mongo as a Python dictionary.

    - Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

    - Create a template HTML file called index.html that will take the mars data dictionary and display all of the data in the appropriate HTML elements. Use the following as a guide for what the final product should look like, but feel free to create your own design.

# Files

- Missions_to_Mars folder contains:

    1. mission_to_mars.ipynb for scraping
    2. scrape.mars_py has the function for scraping
    3. app.py is the application
    4. templates folder contains the index.html

# Process and Credits

My first assignment doing web scraping and MongoDB. I used class materials and outside resources for reference.

Here are the outside resources that I used for this assignment (as well as attempts):

- https://splinter.readthedocs.io/en/latest/elements-in-the-page.html
- https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html
- https://stackoverflow.com/questions/48909593/how-can-i-display-bootstrap-card-horizontally-in-jinja-2-for-each-loop
