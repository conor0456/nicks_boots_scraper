import requests
from bs4 import BeautifulSoup
from decouple import config
LENGTHS = config('LENGTHS').split(",")
WIDTHS = config('WIDTHS').upper().split(",")

URL = "https://nicksboots.com/in-stock-boots/ready-to-ship/?product_list_limit=all"

def get_in_stock_products():
	matches = []
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, "html.parser")
	elements = soup.find_all("span", class_="product-item-link")
	for element in elements:
	    span_text = element.text
	    match = is_a_match(span_text)
	    if match:
	    	matches.append(span_text.strip())
	return matches
	
def is_a_match(string):
	width_match = False
	length_match = False
	model_match = True
	for length in LENGTHS:
		length_match = length_match or string.find(str(length)) >= 0
	for width in WIDTHS:
		width_match = width_match or string.find(str(width)) >= 0
	return width_match and length_match and model_match