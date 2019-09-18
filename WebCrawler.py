import requests
from bs4 import BeautifulSoup

def getSingleItemData(itemURL = "https://www.amazon.in/"):
    sourceCode = requests.get(itemURL)
    plainText = sourceCode.text
    soup = BeautifulSoup(plainText, features='html.parser')
    for itemName in soup.findAll('span', {'id': 'productTitle'}):
        print(str(itemName.string))
