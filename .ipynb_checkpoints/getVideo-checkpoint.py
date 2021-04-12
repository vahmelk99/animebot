def getVideo(URL):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        video = soup.select('source[res="1080"]')[0]
    except:
        try:
            video = soup.select('source[res="720"]')[0]
        except:
            try:
                video = soup.select('source[res="480"]')[0]
            except:
                try:
                    video = soup.select('source[res="480"]')[0]
                except:
                    try:
                        video = soup.select('source')[0]
                    except:
                        return None
    return video['src']

def download_video_series(video_links):  
  
    for link in video_links:  
  
        '''iterate through all links in video_links  
        and download them one by one'''
          
        # obtain filename by splitting url and getting  
        # last string  
        file_name = link.split('/')[-1]  
  
        #print( "Downloading file:%s"%file_name)  
          
        # create response object  
        r = requests.get(link, stream = True, headers=headers)  
          
        # download started  
        with open(file_name, 'wb') as f:  
            for chunk in r.iter_content(chunk_size = 1024*1024):  
                if chunk:  
                    f.write(chunk)  
          
        #print( "%s downloaded!\n"%file_name ) 
  
    #print ("All videos downloaded!") 
    return