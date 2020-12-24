import requests

def server(url):
    r = requests.get(url)
    w = open('tmp.txt','w',encoding = 'utf-8')
    w.write(r.text)
    w.close()
    search = '&amp;s='
    f = open('tmp.txt','r',encoding = 'utf-8').readlines()
    for line in f:
        if search in line:
            find = line;
            break
            
    find = find.split('>')
    server = []
    for index in find:
        if search in index:
            server.append(index)
     
    servers = []
    for i in server:
        #print(i.split('=')[-1].split('"')[0])
        servers.append(i.split('=')[-1].split('"')[0])
    
    return servers
    
def link(link,server):
    file = 'tmp.txt'
    link = link + "&s=" + server
    url = "https://9anime.vip:443/ajax/anime/load_episodes_v2?s=" + server
    referer = link.split('&')[0].replace('\n','')
    ep = referer.split('=')[-1]
    #baar oserbeprint(ep)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", 
        "Accept": "application/json, text/javascript, */*; q=0.01", 
        "Accept-Language": "en-US,en;q=0.5", 
        "Accept-Encoding": "gzip, deflate", 
        "Prefer": "safe", 
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", 
        "X-Requested-With": "XMLHttpRequest", 
        "Origin": "https://9anime.vip", 
        "Referer": referer, 
        "Connection": "close"
        }
    data = {"episode_id": ep}
    r = requests.post(url, headers=headers, data=data)
    #system('rm tmp.txt')
    w = open('tmp.txt','w')
    w.write(r.text)
    w.close()
    f = open('tmp.txt','r').readlines()
    links = f[0].split('"')
    for i in links:
        if 'stream365.live/embed' in i:
            link = i
            break


#//////////////////////////////sending request for mp4 link/////////////////////////////////////
    print('getting link for Video')
    url = link[:-1].replace('stream365.live','stream365.live:443')
    #print("url : " + url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", 
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
        "Accept-Language": "en-US,en;q=0.5", 
        "Accept-Encoding": "gzip, deflate", 
        "Prefer": "safe", 
        "Referer": referer, 
        "Connection": "close", 
        "Upgrade-Insecure-Requests": "1"
        }
    r = requests.get(url, headers=headers)
    w = open(file,'w')
    w.write(r.text)
    w.close()
    #print('data : ')
    #print(r.text)
    f = open(file,'r').readlines()
    if len(f) == 0:
        print("Try diffrent server......")
        return 1
    else:
        search = 'sources:[{"file":'
        for i in f:
            if search in i:
                l = i
                print('found')
                break

        li = l.replace('\t','').replace('\n','').replace('}]','').split('"')
        link = li[3]
        v_link = link.replace('\\','')
        print("video link : " + v_link)
        return 0
