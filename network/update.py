import requests
import time

url = 'https://gitee.com/saltsky/bright-software-services/raw/master/Service%20Launcher/version.info'
r = requests.get(url)
open ('network/info/version.info','wb').write(r.content)
