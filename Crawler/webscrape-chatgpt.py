import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

url = "https://www.youtube.com/@krishnaik06/videos"

# Send an HTTP request to the URL and get the HTML content
html_content = requests.get(url).text

# print(html_content.encode('utf-8'))

html_content.find_element(
    By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span').click()

html_content.implicitly_wait(6)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(html_content, "html.parser")
print(len(soup.find_all("a")))

# Find all the video links in the page
video_links = []
# for link in soup.find_all("a"):
#     print(link)
#     href = link.get("href")
#     if href.startswith("/watch"):
#         video_links.append("https://www.youtube.com" + href)

# Print the video links
for link in video_links:
    print(link)
