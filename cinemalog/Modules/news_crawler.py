from bs4 import BeautifulSoup
from cinemalog.models import News
from requests import get
def crawler():
    url="https://www.zoomg.ir/feed"
    #get url
    response=get(url)

    # change url format to soup
    xml_soup=BeautifulSoup(response.text,'xml')
    source_news=xml_soup.link.string
    print('source url=',source_news)
    # get items from xml
    items=xml_soup.find_all('item')
    #write_to_file(testhtml,str(items))
    # get news from db
    all_news=News.objects.all()
    html=''
    save_before=False
    # get info from each item
    for container in items:
        if container.find('category') is not None:
            cats=container.find_all('category')
            for cat in cats:
                if cat.string == 'اخبار سینما و تلویزیون':
                    #check save before in db or not
                    for n in all_news:
                        if container.title.string == n.title:
                            save_before=True
                            html+=container.title.string+' before saved'+'\n'
                            break
                        else:   
                            save_before=False
                    #print(save_before)
                    if not save_before:        
                        news=News()
                        #append_to_file(result,container.title.string)
                        news.title=container.title.string    
                        soup=BeautifulSoup(container.description.string,'html.parser')
                        #append_to_file(result,soup.img['src'])
                        news.image=soup.img['src']
                        #append_to_file(result,soup.p.next)
                        news.desc=str(soup.p.next)
                        #append_to_file(result,container.pubDate.string)
                        news.published_at=container.pubDate.string
                        news.source=source_news
                        news.save()
                        html+=container.title.string+' added now'+'\n'
                        
    return html    

import time

def test():
    while True:
        crawler()
        print("Thread start")
        time.sleep(60*60)
