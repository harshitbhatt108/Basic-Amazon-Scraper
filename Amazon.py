from bs4 import BeautifulSoup
import requests
headers = {'User-Agent' : 'Mozilla/5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likw Gecko) chrome /58.0.3029.110 Safari/537.3'}
url = 'https://www.amazon.in/SoundBot-SB574-Bluetooth-Wireless-Speaker/dp/B07H2Z6T5C?ref_=Oct_DLandingS_PC_f5cd7136_6'

resp = requests.get(url, headers=headers)
s = BeautifulSoup(resp.content, features="lxml")
product_title = s.select("#productTitle")[0].get_text().strip()
print(product_title)
product_price = s.select("#priceblock_dealprice")[0].get_text().strip()
print(product_price)
product_stars = s.select("#acrPopover")[0].get_text().strip()
print(product_stars)
product_no_reviews = s.select("#acrCustomerReviewText")[0].get_text().strip()
print(product_no_reviews)
product_dmesg = s.select("#dynamicDeliveryMessage")[0].get_text().strip()
print(product_dmesg)
