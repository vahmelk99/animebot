import requests
from bs4 import BeautifulSoup
import uuid 
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
def getVideo(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    try: video = soup.select('source[res="1080"]')[0]
    except:
        try: video = soup.select('source[res="720"]')[0]
        except:
            try: video = soup.select('source[res="480"]')[0]
            except:
                try: video = soup.select('source[res="360"]')[0]
                except:
                    try: video = soup.select('source')[0]
                    except: return None
    return video['src']
def download_video_series(video_links):  
    file_name = video_links.split('/')[-1]  
    r = requests.get(video_links, stream = True, headers=headers)  
    file_name = uuid.uuid4().hex[:6].upper()+'.mp4'
    with open(file_name, 'wb') as f:  
        for chunk in r.iter_content(chunk_size = 1024*1024):  
            if chunk:  
                f.write(chunk)  
    return file_name