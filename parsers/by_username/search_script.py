import requests
import bs4


def youtube(username):
    try:
        url = f'https://www.youtube.com/user/{username}'
        r = requests.get(url)
        if r.status_code == 200:
            return ['Youtube', '+']
        else:
            return ['youtube', '-']
    except:
        return ['youtube', 'error']


def wikipedia(username):
    try:
        url = f'https://meta.wikimedia.org/wiki/Special:CentralAuth?target={username}'
        r = requests.get(url)
        bb = bs4.BeautifulSoup(r.text, features='lxml')
        if not 'Global account information\nUsername' in bb.text:
            return ['Wikipedia', '-']
        return ['Wikipedia', '+']

    except:
        return ['Wikipedia', 'error']


def pinterest(username):
    try:
        url = 'https://www.pinterest.ru/' + username
        r = requests.get(url)
        if 'User not found' in r.text:
            return ['Pinterest', '-']
        else:
            return ['Pinterest', '+']
    except:
        return ['Pinterest', 'error']


def vimeo(username):
    try:
        url = 'https://vimeo.com/' + username
        r = requests.get(url)
        if 'Sorry, we couldn’t find that page' in r.text:
            return ['Vimeo', '-']
        else:
            return ['Vimeo', '+']
    except:
        return ['Vimeo', 'error']


def livejournal(username):
    try:
        url = f'https://{username}.livejournal.com/'
        r = requests.get(url)
        if 'is not currently registered.' in r.text:
            return ['Livejournal', '-']
        else:
            return ['Livejournal', '+']
    except:
        return ['Livejournal', 'error']


def steam(username):
    try:
        url = 'https://steamcommunity.com/id/' + username
        r = requests.get(url)
        if 'The specified profile could not be found.' in r.text:
            return ['Steam', '-']
        else:
            return ['Steam', '+']
    except:
        return ['Steam', 'error']


def dribbble(username):
    try:
        url = 'https://dribbble.com/' + username
        r = requests.get(url)
        if 'Whoops, that page is gone.' in r.text:
            return ['Dribbble', '-']
        else:
            return ['Dribbble', '+']
    except:
        return ['Dribbble', 'error']


def tiktok(username):
    try:
        url = f'https://www.tiktok.com/@{username}?lang=en'
        r = requests.get(url)
        if "Couldn't find this account</p>" in r.text:
            return ['TikTok', '-']
        else:
            return ['TikTok', '+']
    except:
        return ['TikTok', 'error']


def github(username):
    try:
        url = 'https://github.com/' + username
        r = requests.get(url)
        if 'Not Found' in r.text:
            return ['GitHub', '-']
        else:
            return ['GitHub', '+']
    except:
        return ['GitHub', 'error']


def ask_fm(username):
    try:
        url = 'https://ask.fm/' + username
        r = requests.get(url)
        if 'Well, apparently not anymore.' in r.text:
            return ['ASKfm', '-']
        else:
            return ['ASKfm', '+']
    except:
        return ['ASKfm', 'error']


def bitbucket(username):
    try:
        url = 'https://bitbucket.org/' + username
        r = requests.get(url)
        if 'That link has no power here' in r.text:
            return ['BitBucket', '-']
        else:
            return ['BitBucket', '+']
    except:
        return ['BitBucket', 'error']


def vk(username):
    try:
        url = 'https://vk.com/' + username
        r = requests.get(url)
        if '404 Not Found' in r.text:
            return ['VK', '-']
        else:
            return ['VK', '+']
    except:
        return ['VK', 'error']


def pastebin(username):
    try:
        url = 'https://pastebin.com/u/' + username
        r = requests.get(url)
        if 'Not Found (#404)' in r.text:
            return ['PasteBin', '-']
        else:
            return ['PasteBin', '+']
    except:
        return ['PasteBin', 'error']


def telegram(username):
    try:
        url = 'https://t.me/' + username
        r = requests.get(url)
        if f'You can contact @{username} right away.'.lower() not in r.text.lower():
            return ['Telegram', '-']
        else:
            return ['Telegram', '+']
    except:
        return ['Telegram', 'error']


def ok(username):
    try:
        url = 'https://ok.ru/' + username
        r = requests.get(url)
        if 'Этой страницы нет в OK' in r.text:
            return ['Odnoklassniki', '-']
        else:
            return ['Odnoklassniki', '+']
    except:
        return ['Odnoklassniki', 'error']


def echo_msc(username):
    try:
        url = 'https://echo.msk.ru/users/' + username
        r = requests.get(url)
        if 'Личная страница' in r.text:
            return ['Echo Moscow', '+']
        else:
            return ['Echo Moscow', '-']
    except:
        return ['Echo Moscow', 'error']


def wordpress(username):
    try:
        url = 'https://profiles.wordpress.org/' + username
        r = requests.get(url)
        if 'User not found' in r.text:
            return ['Wordpress', '-']
        else:
            return ['Wordpress', "+"]
    except:
        return ['Wordpress', 'error']


def blogspot(username):
    try:
        url = f'http://{username}.blogspot.com/'
        r = requests.get(url)
        if 'Блог не найден' in r.text:
            return ['Blogspot', '-']
        else:
            return ['Blogspot', '+']
    except:
        return ['Blogspot', 'error']


def check(data):
    return [data[0], [youtube(data[1]), wikipedia(data[1]), pinterest(data[1]), vimeo(data[1]), livejournal(data[1]),
            steam(data[1]), dribbble(data[1]), tiktok(data[1]), github(data[1]), ask_fm(data[1]),
            bitbucket(data[1]), vk(data[1]), pastebin(data[1]), telegram(data[1]), ok(data[1]),
            echo_msc(data[1]), wordpress(data[1]), blogspot(data[1])]]


print(check(['1', 'olegpash']))