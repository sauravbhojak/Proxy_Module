import ast
import random
import requests
from urllib.parse import urlparse
import colorama
from colorama import Fore

search_request = ""


# todo------------------------------- Crawlera random -----------------------------------

def crawlera_random(search_url, headers, **kwargs):
    try:
        global passdata, current_proxy
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        while True:
            try:
                with open(
                        r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\crawlera.txt') as f:
                    data = f.read()
            except:
                with open(r'C:\proxy_module\proxies\crawlera.txt') as f:
                    data = f.read()
            res_dict = ast.literal_eval(data)
            a = random.choice(list(res_dict.values()))
            if type(a) == list:
                current_proxy = random.choice(a)
                print('\x1b[6;30;42m' + 'Your current crawlara proxy is : ' + '\x1b[0m', current_proxy)
            else:
                current_proxy = a
                print('\x1b[6;30;42m' + 'Your current crawlara proxy is : ' + '\x1b[0m', current_proxy)
            proxy_host = "proxy.crawlera.com"
            proxy_port = "8010"
            proxy_auth = f"{current_proxy}:"
            proxies = {
                "http": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                "https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
            }
            if passdata:
                search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies,
                                               verify=False)
                print('<----------------', search_request.status_code, '---------------->')
            else:
                search_request = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)
                print('<----------------', search_request.status_code, '---------------->')

            if (search_request.status_code != 200):
                continue
            else:
                if "/errors/validateCaptcha" not in search_request:
                    return search_request
                else:
                    continue
        return search_request
    except Exception as e:
        print(e)
        crawlera_random(search_url, headers, **kwargs)


# todo------------------------------- Crawlera country -----------------------------------

def crawlara_country(search_url, headers, country, **kwargs):
    try:
        global passdata, search_request

        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        c = ['all', 'us', 'hk', 'br', 'taiwan']
        while True:
            try:
                with open(
                        r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\crawlera.txt') as f:
                    data = f.read()
            except:
                with open(
                        r'C:\proxy_module\proxies\crawlera.txt') as f:
                    data = f.read()
            res_dict = ast.literal_eval(data)
            if country in c:
                current_proxy = res_dict.get(country)
                current_proxy = str(random.choice(current_proxy))
                print('\x1b[6;30;42m' + 'Your current crawlara proxy is : ' + '\x1b[0m', current_proxy)
                proxy_host = "proxy.crawlera.com"
                proxy_port = "8010"
                proxy_auth = f"{current_proxy}:"
                proxies = {
                    "http": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                    "https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
                }
                if passdata:
                    search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies,
                                                   verify=False)
                    print('<----------------', search_request.status_code, '---------------->')
                else:
                    search_request = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)
                    print('<----------------', search_request.status_code, '---------------->')

            elif country not in res_dict.keys():
                print(Fore.RED + 'Proxy for this country is not avaliable contact to TL')
                break
            else:
                current_proxy = res_dict.get(country)
                print('Your current crawlara proxy is : ', current_proxy)
                proxy_host = "proxy.crawlera.com"
                proxy_port = "8010"
                proxy_auth = f"{current_proxy}:"
                proxies = {
                    "http": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                    "https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)
                }
                search_request = ''
                if passdata:
                    search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies,
                                                   verify=False)
                    print('<----------------', search_request.status_code, '---------------->')
                else:
                    search_request = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)
                    print('<----------------', search_request.status_code, '---------------->')
                break
        return search_request
    except Exception as e:
        print(e)
        crawlara_country(search_url, headers, **kwargs)


# todo------------------------------- Luminati random -----------------------------------

def luminati_random(search_url, headers, **kwargs):
    try:
        global passdata, search_request, end
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        while True:
            try:
                with open(
                        r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\luminati.txt') as f:
                    data = f.read()
            except:
                with open(r'C:\proxy_module\proxies\luminati.txt') as f:
                    data = f.read()
            res_dict = ast.literal_eval(data)
            key = res_dict.keys()
            random_psw = str(random.choice(list(key)))
            country = random_psw
            start = 1
            if country == 'au':
                end = 50
            elif country == 'br':
                end = 10
            elif country == 'ca':
                end = 10
            elif country == 'fr':
                end = 60
            elif country == 'gr':
                end = 40
            elif country == 'in':
                end = 40
            elif country == 'it':
                end = 9
            elif country == 'jp':
                end = 25
            elif country == 'nl':
                end = 25
            elif country == 'rs':
                end = 10
            elif country == 'sp':
                end = 10
            elif country == 'sn':
                end = 50
            elif country == 'sn2':
                end = 50
            elif country == 'tw':
                end = 30
            elif country == 'tr':
                end = 10
            elif country == 'id':
                end = 10
            elif country == 'us':
                end = 30
            elif country == 'us2':
                end = 30
            elif country == 'uk':
                end = 30
            elif country == 'uk2':
                end = 30

            CP = (res_dict[random_psw]['psw'])
            CP = CP.split(':')
            country = CP[0]
            psw = CP[1]

            # x = f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(1, 30)}:{psw}@zproxy.lum-superproxy.io:22225"
            current_proxy = {
                "https": f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(start, end)}:{psw}@zproxy.lum-superproxy.io:22225",
                "http": f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(start, end)}:{psw}@zproxy.lum-superproxy.io:22225"}
            print('\x1b[6;30;42m' + 'Your current Luminati proxy is : ' + '\x1b[0m', current_proxy)

            if passdata:
                search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=current_proxy,
                                               verify=False)
                print('<----------------', search_request.status_code, '---------------->')

            else:
                search_request = requests.get(url=search_url, headers=headers, proxies=current_proxy, verify=False)
                print('<----------------', search_request.status_code, '---------------->')

            if (search_request.status_code != 200):
                continue
            else:
                if "/errors/validateCaptcha" not in search_request:
                    return search_request
                else:
                    continue
        return search_request
    except Exception as e:
        print(e)
        luminati_random(search_url, headers, **kwargs)


# todo------------------------------- Luminati country -----------------------------------

def luminati_country(search_url, headers, country, **kwargs):
    try:
        global passdata, search_request, end
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        while True:
            try:
                with open(
                        r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\luminati.txt') as f:
                    data = f.read()
            except:
                with open(r'C:\proxy_module\proxies\luminati.txt') as f:
                    data = f.read()
            res_dict = ast.literal_eval(data)
            k = list(res_dict.keys())
            if country in k:
                start = 1
                if country == 'au':
                    end = 50
                elif country == 'br':
                    end = 10
                elif country == 'ca':
                    end = 10
                elif country == 'fr':
                    end = 60
                elif country == 'gr':
                    end = 40
                elif country == 'in':
                    end = 40
                elif country == 'it':
                    end = 9
                elif country == 'jp':
                    end = 25
                elif country == 'nl':
                    end = 25
                elif country == 'rs':
                    end = 10
                elif country == 'sp':
                    end = 10
                elif country == 'sn':
                    end = 50
                elif country == 'sn2':
                    end = 10
                elif country == 'tw':
                    end = 30
                elif country == 'tr':
                    end = 10
                elif country == 'id':
                    end = 10
                elif country == 'us':
                    end = 30
                elif country == 'us2':
                    end = 30
                elif country == 'uk':
                    end = 30
                elif country == 'uk2':
                    end = 30

                key = res_dict.get(country)
                values = list(key.values())
                CP = values[0]
                CP = CP.split(':')
                country = CP[0]
                psw = CP[1]
                # f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(1, 30)}:{psw}@zproxy.lum-superproxy.io:22225
                current_proxy = {
                    "https": f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(start, end)}:{psw}@zproxy.lum-superproxy.io:22225",
                    "http": f"lum-customer-c_11e7173f-zone-zone_{country}{random.randint(start, end)}:{psw}@zproxy.lum-superproxy.io:22225"}
                print('\x1b[6;30;42m' + 'Your current Luminati proxy is : ' + '\x1b[0m', current_proxy)
            else:
                print(Fore.RED + 'Proxy for this country is not avaliable contact to TL')
                break
            search_request = ''
            if passdata:
                search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=current_proxy,
                                               verify=False)
                print('<----------------', search_request.status_code, '---------------->')
            else:
                search_request = requests.get(url=search_url, headers=headers, proxies=current_proxy, verify=False)
                print('<----------------', search_request.status_code, '---------------->')
            break
        return search_request
    except Exception as e:
        print(e)
        luminati_country(search_url, headers, **kwargs)


# todo------------------------------- Strome Proxy -----------------------------------

def storm_proxy(search_url, headers, **kwargs):
    try:
        global passdata

        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        userid = 'storm4saurav1'
        password = 'storm4saurav1'
        host = '5.79.73.131'
        port = '13150'

        Storm_proxies = {
            "https": f"http://{userid}:{password}@{host}:{port}/",
            "http": f"http://{userid}:{password}@{host}:{port}/",
        }
        print('\x1b[6;30;42m' + 'Your current strome proxy is : ' + '\x1b[0m', Storm_proxies)
        if passdata:
            search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=Storm_proxies,
                                           verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        else:
            search_request = requests.get(url=search_url, headers=headers, proxies=Storm_proxies, verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        return search_request
    except Exception as e:
        print(e)
        storm_proxy(search_url, headers, **kwargs)


# todo------------------------------- Residential -----------------------------------

def residential(search_url, headers, **kwargs):
    try:
        global passdata

        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        proxy_auth_new = str("sauravgmailcom:p5ScH2eKVeK4")
        proxy_host_new = "152.44.97.155"
        proxy_port_new = "9000"
        proxies_new = {"http": "https://{}@{}:{}/".format(proxy_auth_new, proxy_host_new, proxy_port_new),
                       "https": "http://{}@{}:{}/".format(proxy_auth_new, proxy_host_new, proxy_port_new)}

        print('\x1b[6;30;42m' + 'Your current residential proxy is : ' + '\x1b[0m', proxies_new)
        if passdata:
            search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies_new,
                                           verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        else:
            search_request = requests.get(url=search_url, headers=headers, proxies=proxies_new, verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        return search_request
    except Exception as e:
        print(e)
        residential(search_url, headers, **kwargs)


# todo------------------------------- Instatnse_proxy -----------------------------------

def instance_proxy(search_url, headers, **kwargs):
    try:
        global passdata

        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        proxyips = [
            '173.232.7.185:8800',
            '192.161.162.125:8800',
            '104.140.73.82:8800',
            '23.19.97.67:8800',
            '104.140.215.42:8800',
            '50.2.25.51:8800',
            '173.232.7.27:8800',
            '50.2.25.231:8800',
            '173.232.7.87:8800',
            '192.126.161.215:8800',
            '50.2.15.119:8800',
            '104.140.215.112:8800',
            '104.140.73.235:8800',
            '192.161.162.126:8800',
            '173.234.232.146:8800',
            '104.140.73.251:8800',
            '104.140.73.175:8800',
            '192.161.162.55:8800',
            '192.126.161.47:8800',
            '173.232.7.211:8800',
            '50.2.15.30:8800',
            '50.2.15.35:8800',
            '104.140.215.51:8800',
            '104.140.73.32:8800',
            '23.19.97.71:8800',
            '173.234.232.173:8800',
            '50.2.25.205:8800',
            '23.19.97.104:8800',
            '104.140.215.216:8800',
            '23.19.97.216:8800',
            '173.234.232.103:8800',
            '104.140.215.126:8800',
            '104.140.73.158:8800',
            '192.126.161.53:8800',
            '23.19.97.72:8800',
            '173.234.232.214:8800',
            '50.2.15.246:8800',
            '104.140.215.149:8800',
            '192.161.162.2:8800',
            '104.140.183.8:8800',
            '50.2.15.194:8800',
            '104.140.183.48:8800',
            '50.2.25.75:8800',
            '104.140.215.36:8800',
            '192.161.162.121:8800',
            '104.140.73.234:8800',
            '104.140.183.141:8800',
            '173.232.7.130:8800',
            '173.234.232.44:8800',
            '50.2.25.234:8800',
            '104.140.215.89:8800',
            '23.19.97.151:8800',
            '192.126.161.227:8800',
            '104.140.183.224:8800',
            '50.2.15.109:8800',
            '104.140.183.10:8800',
            '104.140.215.70:8800',
            '192.161.162.44:8800',
            '50.2.25.238:8800',
            '173.234.232.233:8800',
            '173.232.7.62:8800',
            '192.161.162.21:8800',
            '192.161.162.215:8800',
            '192.126.161.56:8800',
            '104.140.183.195:8800',
            '50.2.25.135:8800',
            '192.126.161.115:8800',
            '104.140.183.231:8800',
            '173.232.7.175:8800',
            '104.140.215.122:8800',
            '50.2.15.74:8800',
            '173.232.7.85:8800',
            '23.19.97.239:8800',
            '50.2.25.198:8800',
            '192.126.161.122:8800',
            '192.126.161.153:8800',
            '192.161.162.6:8800',
            '50.2.15.76:8800',
            '23.19.97.38:8800',
            '173.234.232.27:8800',
            '23.19.97.205:8800',
            '50.2.25.58:8800',
            '50.2.25.40:8800',
            '173.232.7.126:8800',
            '104.140.183.59:8800',
            '173.232.7.53:8800',
            '173.234.232.194:8800',
            '104.140.183.246:8800',
            '104.140.73.198:8800',
            '173.234.232.239:8800',
            '50.2.15.22:8800',
            '50.2.15.96:8800',
            '104.140.73.75:8800',
            '192.126.161.173:8800',
            '173.234.232.192:8800',
            '192.161.162.155:8800',
            '104.140.73.147:8800',
            '104.140.183.239:8800',
            '192.126.161.132:8800',
            '23.19.97.165:8800',
        ]

        proxies = {
            "http": f"http://{(random.choice(proxyips))}",
        }

        print('\x1b[6;30;42m' + 'Your current instatnse proxy is : ' + '\x1b[0m', proxies)
        if passdata:
            search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies,
                                           verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        else:
            search_request = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        return search_request
    except Exception as e:
        print(e)
        instance_proxy(search_url, headers, **kwargs)


# todo------------------------------- Proxymesh -----------------------------------

def proxymesh(search_url, headers, **kwargs):
    try:
        global passdata

        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        host_ls = ['world.proxymesh.com', 'open.proxymesh.com']
        proxy_auth = str("ss:saurav$2018")
        proxy_host = str(random.choice(host_ls))
        proxy_port = "31280"
        proxies = {"http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                   }

        print('\x1b[6;30;42m' + 'Your current Proxymesh proxy is : ' + '\x1b[0m', proxies)
        if passdata:
            search_request = requests.post(url=search_url, headers=headers, data=passdata, proxies=proxies,
                                           verify=False)
            print('<----------------', search_request.status_code, '---------------->')
        else:
            search_request = requests.get(url=search_url, headers=headers, proxies=proxies, verify=False)

            print('<----------------', search_request.status_code, '---------------->')
        return search_request
    except Exception as e:
        print(e)
        proxymesh(search_url, headers, **kwargs)


# todo------------------------------- Scraper_API_Country -----------------------------------

def scraper_api_country(search_url, headers, country, **kwargs):
    try:
        global passdata, fileContent, search_request
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""
        try:
            with open(
                    r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\scraper_api.txt') as f:
                data = f.read()
        except:
            with open(r'C:\proxy_module\proxies\scraper_api.txt') as f:
                data = f.read()
        res_dict = ast.literal_eval(data)
        scraper_api_key = random.choice(list(res_dict.values()))

        print('\x1b[6;30;42m' + 'Your current Scraper_API is : ' + '\x1b[0m', scraper_api_key, 'country is : ', country)

        link = "https://docs.google.com/spreadsheets/d/1ktYk6UtMyw_QA23cjfN_XSRZadN2ziLh0QbXGQtp4EU/edit#gid=0"
        domain = urlparse(link).netloc
        segments = link.rpartition('/')
        link = segments[0] + "/export?format=csv"
        file = requests.get(link)

        if file.status_code == 200:
            fileContent = file.content.decode('utf-8')
            url = search_url
            a = url.split('//')[1]
            domain = a.split('/')[0]

        if domain in fileContent:
            payload = {'api_key': scraper_api_key, 'country_code': f'{country}', 'keep_headers': True}
            if passdata:
                search_request = requests.post(url=search_url, params=payload, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')
            else:
                search_request = requests.get(url=search_url, params=payload, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')
        else:
            print(Fore.RED + '<------You are not allow to use this proxy for this domain----->')
    except Exception as e:
        print(e)
        scraper_api_country(search_url, headers, **kwargs)


# todo------------------------------- Scraper_API -----------------------------------

def scraper_api(search_url, headers, **kwargs):
    try:
        global passdata, fileContent, search_request
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""

        try:
            with open(
                    r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\scraper_api.txt') as f:
                data = f.read()
        except:
            with open(r'C:\proxy_module\proxies\scraper_api.txt') as f:
                data = f.read()
        res_dict = ast.literal_eval(data)
        scraper_api_key = random.choice(list(res_dict.values()))

        print('\x1b[6;30;42m' + 'Your current Scraper_API is : ' + '\x1b[0m', scraper_api_key)
        link = "https://docs.google.com/spreadsheets/d/1ktYk6UtMyw_QA23cjfN_XSRZadN2ziLh0QbXGQtp4EU/edit#gid=0"
        domain = urlparse(link).netloc
        segments = link.rpartition('/')
        link = segments[0] + "/export?format=csv"
        file = requests.get(link)

        if file.status_code == 200:
            fileContent = file.content.decode('utf-8')
            url = search_url
            a = url.split('//')[1]
            domain = a.split('/')[0]

        if domain in fileContent:
            payload = {'api_key': scraper_api_key, 'keep_headers': True}
            if passdata:

                search_request = requests.post(url=search_url, params=payload, data=passdata, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')
            else:
                search_request = requests.get(url=search_url, params=payload, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')

            if (search_request.status_code != 200):
                scraper_api(search_url, headers, **kwargs)
            else:
                if "/errors/validateCaptcha" not in search_request:
                    return search_request
                else:
                    scraper_api(search_url, headers, **kwargs)
        else:
            print(Fore.RED + '<------You are not allow to use this proxy for this domain----->')

        return search_request
    except Exception as e:
        print(e)
        scraper_api(search_url, headers, **kwargs)


# todo------------------------------- Scraper_API_render -----------------------------------

def scraper_api_render(search_url, headers, **kwargs):
    try:
        global passdata, fileContent, search_request
        if kwargs:
            for arg in kwargs.values():
                passdata = arg
        else:
            passdata = ""

        try:
            with open(
                    r'\\192.168.1.127\e\Saurav_Bhojak\Working\other_projects\R&D\random_proxy_module\scraper_api.txt') as f:
                data = f.read()
        except:
            with open(r'C:\proxy_module\proxies\scraper_api.txt') as f:
                data = f.read()
        res_dict = ast.literal_eval(data)
        scraper_api_key = random.choice(list(res_dict.values()))

        print('\x1b[6;30;42m' + 'Your current Scraper_API is : ' + '\x1b[0m', scraper_api_key)
        link = "https://docs.google.com/spreadsheets/d/1ktYk6UtMyw_QA23cjfN_XSRZadN2ziLh0QbXGQtp4EU/edit#gid=0"
        domain = urlparse(link).netloc
        segments = link.rpartition('/')
        link = segments[0] + "/export?format=csv"
        file = requests.get(link)

        if file.status_code == 200:
            fileContent = file.content.decode('utf-8')
            url = search_url
            a = url.split('//')[1]
            domain = a.split('/')[0]

        if domain in fileContent:
            payload = {'api_key': scraper_api_key, 'keep_headers': True, 'render': True}
            if passdata:
                search_request = requests.post(url=search_url, params=payload, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')
            else:
                search_request = requests.get(url=search_url, params=payload, headers=headers)
                print('<----------------', search_request.status_code, '---------------->')

        else:
            print(Fore.RED + '<------You are not allow to use this proxy for this domain----->')

    except Exception as e:
        print(e)
        scraper_api_render(search_url, headers, **kwargs)


# todo------------------------------- All_proxies -----------------------------------

def allproxies(search_url, headers, country=None, **kwargs):
    global response
    try:
        all = ['scraper_api_country',
               'scraper_api',
               'crawlera_random',
               'scraper_api_render',
               'proxymesh',
               'instance_proxy',
               'residential',
               'storm_proxy',
               'luminati_country',
               'luminati_random',
               'crawlara_country',
               ]
        random_proxy = random.choice(all)
        print(random_proxy)

        if random_proxy in 'scraper_api_country':
            scraper_api_country(search_url, headers, country, **kwargs)
        elif random_proxy in 'scraper_api':
            scraper_api(search_url, headers, **kwargs)
        elif random_proxy in 'crawlera_random':
            crawlera_random(search_url, headers, **kwargs)
        elif random_proxy in 'scraper_api_render':
            scraper_api_render(search_url, headers, **kwargs)
        elif random_proxy in 'proxymesh':
            proxymesh(search_url, headers, **kwargs)
        elif random_proxy in 'instance_proxy':
            instance_proxy(search_url, headers, **kwargs)
        elif random_proxy in 'residential':
            residential(search_url, headers, **kwargs)
        elif random_proxy in 'storm_proxy':
            storm_proxy(search_url, headers, **kwargs)
        elif random_proxy in 'luminati_country':
            luminati_country(search_url, headers, country, **kwargs)
        elif random_proxy in 'luminati_random':
            luminati_random(search_url, headers, **kwargs)
        elif random_proxy in 'crawlara_country':
            crawlara_country(search_url, headers, country, **kwargs)
        else:
            allproxies(search_url, headers, country=None, **kwargs)

    except Exception as e:
        print(e)
