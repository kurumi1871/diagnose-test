from wordcloud import WordCloud
from matplotlib import pyplot as plt

from urllib.request import urlopen
from bs4 import BeautifulSoup

site_url = "https://molcar-anime.com/"

#html = urllib.request.urlopen(site_url).read().decode('utf-8')

html = urlopen(site_url)
bsObj = BeautifulSoup(html, "html.parser")
text = ' '.join([tag.text for tag in bsObj('a')])

FONT_FILE = "C:\Windows\Fonts\MSGOTHIC.TTC"
word_cloud = WordCloud(font_path=FONT_FILE, background_color='white', colormap='plasma', width=1920, height=1080, collocations = False).generate(text)

plt.imshow(word_cloud)
plt.axis('off')
plt.show()