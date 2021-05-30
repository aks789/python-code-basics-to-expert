import requests
import bs4
import lxml


res=requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")


soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup.select('p')[0].getText())
print(soup.select('.toctext')[0].getText())

for item in soup.select('.toctext'):
    print(item.text)

res1 = requests.get('https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)')

soup1 = bs4.BeautifulSoup(res1.text,"lxml")

print(soup1.select('.thumbimage')[0]['src'])

res2 = requests.get('https:' + soup1.select('.thumbimage')[0]['src'])

f = open('my_comp_img.jpeg','wb')
f.write(res2.content)
f.close()

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
print(base_url.format('3'))

res = requests.get(base_url.format('1'))

soup = bs4.BeautifulSoup(res.text,"lxml")
products = soup.select('.product_pod')

example = products[0]

if 'star-rating Three' in str(example):
    print(True)
else:
    print(False)

print(example.select(".star-rating.Three"))

print(example.select('a')[1]['title'])

two_star_titles = []

for n in range(1,51):

    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(res.text,"lxml")

    books = soup.select(".product_pod")

    for book in books:
        if len(book.select('.start-rating.Two')) != 0:
            print('hello')
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)

res = requests.get('http://quotes.toscrape.com/')
soup = bs4.BeautifulSoup(res.text,'lxml')

print(soup.select('.author'))


print(soup)