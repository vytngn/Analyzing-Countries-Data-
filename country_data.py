# Vy Nguyen - 202:01 – Midterm Assignment
from bs4 import BeautifulSoup
import requests

# Example URL for web scraping 
url = 'https://www.scrapethissite.com/pages/simple/'

# Send a get request and get a return of response object 
response = requests.get(url)
html_content = response.text

# Parse the content in html format and store it in variable soup
soup = BeautifulSoup(html_content, 'html.parser') 

#------------------------------------------------------------------------------------------------------------
# EXAMPLE 1: count the number of headings h1 , h2, h3, h4, and h5 in the html content
    # Method used: find_all()

# 1. Create a dictionary to hold the count of each headings (h1-h5)
heading_counts = {'h1':0,'h2':0, 'h3':0, 'h4':0, 'h5':0}

# 2. Find all heading tags using find_all
headings = soup.find_all(['h1','h2','h3','h4','h5'])

# 3. Iterate over each heading tag found
for heading in headings:
    tag_name = heading.name # get the name of the current heading tag 
    if tag_name in heading_counts: # if the tag matches the headings is in the dictionary 
        heading_counts[tag_name] +=1 #increament the corresponding value of the heading

# 4. Iterarate over dictionary with key=heading, value=count and print the counts
for heading, count in heading_counts.items():
    print(f"Number of {heading} tags:", count) 

print(f"\n{'-'*40}\n") #line break to end one example 

#--------------------------------------------------------------------------------------------------------------------
# EXAMPLE 2: find the country with the most population 
    # Method used: find() and find_next_sibling() 

# 1. Initialize variables to store the most populated country's name and population
max_population = 0
most_populated_country = ''

# 2. Find all tags with class country-name
country_names = soup.find_all(class_='country-name')

# 3. Iterate over each country name
for country in country_names:
    
    # 4. Get the next sibling div the current country that contain class = 'country-population' 
    population = int(country.find_next_sibling('div').find(class_='country-population').text)
    
    # 5. Compare population of current country with max_population
    if population > max_population: #if current country population > max 
        max_population = population # update max 
        most_populated_country = country.text.strip()  # Get the text of the country name without leading/trailing spaces

# Print the most populated country
print(f"The most populated country: is {most_populated_country} with the population of {max_population:,} people.")
print(f"\n{'-'*40}\n")#line break to end one example 

#--------------------------------------------------------------------------------------------------------
# EXAMPLE 3: find country name start with V and print its corresponding capital and population 
    # Method used: get_text()   

# 1.Find all divs with class 'country'
countries = soup.find_all('div', class_='country')

print(f"Information of countries start with letter V: ")

# 2.Iterate through each country and extract information 
for country in countries:
    # 3.Extract country name
    country_name = country.find(class_='country-name').get_text().strip() 
    # 4.Check if country name starts with 'V'
    if country_name.lower().startswith('v'):
        # 5. Extract capital
        capital = country.find(class_='country-capital').get_text().strip()
        # 6. Extract population
        population = int(country.find(class_="country-population").get_text().strip())
        
        # 7.Print the country name, capital and population
        print(f"- Country: {country_name}\n     Capital: {capital}\n     Population : {population:,}")

print(f"\n{'-'*40}\n") #line break to end one example 
        
