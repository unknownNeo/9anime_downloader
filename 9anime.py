import requests
from os import system
import server
from glob import glob
from sys import platform

def priv():
    lists = glob('*.txt')
    lists.remove('tmp.txt')
    if len(lists) == 0:
        print('No anime List found')
        return 0    
        
    for i in range(0,len(lists)):
        print(str(i + 1) + ' || ' + lists[i].replace('.txt',''))
    while True:
        num = int(input('Select the anime : '))
        if num > len(lists) + 1 or num < 0:
            print("[!] Enter Only Number Avilable in List...")
        else:
            file = lists[num - 1]
            break
    f = open(file,'r', encoding = 'utf-8').readlines()
    total = len(f)
    for i in range(0,len(f)):
        print("Ep no. " + str(total - (1 + i) + 1) + " : " + f[i])
    print('Total Episodes are : ' + str(total))
   
    num = input('Enter the episode number : ') 
    con = '-' + str(num)
    ep = int(con)
    link = f[ep]
    print(f[ep],end = '')
    print('getting server list...')
    servers = server.server(link)
    getting_link(servers,link)
    
def getting_link(servers,link):
    count = 1
    for i in servers:
        print(str(count) + ' | ' + i)
        count += 1
    count = count - 1
    while True:
        
        try:
            s = input("select server : ")
            int(s)
            
            if int(s) > count or int(s) < 1:
                print('Invaled server number....(using default server)')
            s = 1
            r_type = server.link(link,servers[int(s) - 1])
            if r_type == 0:
                break
        except ValueError:
            print("Enter only Number....")

def episode(url,anime):
    search = 'href="/watch/' + url.split('/')[-1]
    r = requests.get(url)
    file = 'tmp.txt'
    w = open(file,'w',encoding = 'utf-8')
    w.write(r.text)
    print('reading page')
    f = open(file,'r',encoding = 'utf-8').readlines()
    for i in f:
        if "episodes" in i:
            l = i

    link = l.split(' ')
    links = []
    for i in link:
        if search in i:
            links.append(i)
    
    total = int(len(links)/2)
    w = open(anime + '.txt','w', encoding = 'utf-8')
    for i in range(0,len(links),2):
        w.write(links[i].replace('href="','https://9anime.vip').replace('"','') + '\n')
    w.close()
    f = open(anime + '.txt','r', encoding = 'utf-8').readlines()
    for i in range(0,len(f)):
        print("Ep no. " + str(total - (1 + i) + 1) + " : " + f[i])
    print('Total Episodes are : ' + str(total))
    
#////////////////////////////////////////episode number/////////////////////////////////////////////////////

def from_link():  
    url = str(input('Enter the Url of anime : '))
    if '?' in url:
        url = url.split('?')[0]
    anime = url.split('/')[-1]
    
    print(anime)

    
    episode(url,anime)

    f = open(anime + '.txt','r', encoding = 'utf-8').readlines()
    if len(f) == 0:
        print("Please check The link...")
        if platform == 'win32':
            system('del ' + anime + '.txt')
        elif platform == 'linux':
            system('rm ' + anime + '.txt')
    else:    
        num = input('Enter the episode number : ') 
        con = '-' + str(num)
        ep = int(con)
        link = f[ep]
        print(f[ep],end = '')
        print('getting server list...')
        servers = server.server(link)
        getting_link(servers,link)
        
print(' 1 || Check the Priv. Anime list\n 2 || Use URL')
s = int(input(': '))
if s > 2 or s < 1:
    print('Select From above Option Only...')
else:
    if s == 1:
        priv()
    else:
        from_link()