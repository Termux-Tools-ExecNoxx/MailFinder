import os, re, sys, time, json, requests, random

r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

W = f"{w}\033[1;47m"
R = f"{w}\033[1;41m"
G = f"{w}\033[1;42m"
Y = f"{w}\033[1;43m"
B = f"{w}\033[1;44m"

space = "    "
des_space = "⁣  ⁣⁣  ⁣⁣ "
lines = space + "—"*60
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}


check = requests.get("http://flyzero.000webhostapp.com/project/mailfinder/Ip6.php").text
def cls():
    if sys.platform == 'win32':
          # clear in windows, java
          os.system('cls')
    else:
          # clear in linux, android, ubuntu
          os.system('clear')

def restart():
    cls()
    os.execl(sys.executable, sys.executable, *sys.argv)

def banner():
    print(f'''{b}
     __   __  _______  ___   ___      _______  ___   __    _  ______   _______  ______
    |  |_|  ||   _   ||   | |   |    |       ||   | |  |  | ||      | |       ||    _ |
    |       ||  |_|  ||   | |   |    |    ___||   | |   |_| ||  _    ||    ___||   | ||
    |       ||       ||   | |   |    |   |___ |   | |       || | |   ||   |___ |   |_||_
    |       ||       ||   | |   |___ |    ___||   | |  _    || |_|   ||    ___||    __  |
    | ||_|| ||   _   ||   | |       ||   |    |   | | | |   ||       ||   |___ |   |  | |
    |_|   |_||__| |__||___| |_______||___|    |___| |_|  |__||______| |_______||___|  |_|''')
    print(f'                  {w}.:.:;..{y} MailFinder v1.0 Developer: misha korzhik {w}..;:.:.')
    print(f'\n{des_space}{b}>> {w}To find the mail you need, write your last name and \n{des_space}{b}>> {w}first name in different ways. For example: vuiko, vuikoo, vu\n{des_space}{b}>> {w}It still takes a long time to find your e-mail.\n')

def mailfinder():
    name = str(input(f"{space}{b}[{w}?{b}]{w} While victim name:{b} ").lower())
    familia = str(input(f"{space}{b}[{w}?{b}]{w} While victim familia:{b} ").lower())
    data = [
    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "yandex.com",
    "yandex.ru",
    "yandex.ua",
    "live.com",
    ]
    print('')
    if not data: restart()
    if not name: restart()
    if not familia: restart()
    fullname = name + familia
    na1 = '@'
    fa1 = '@'
    #names
    if 'iy' in name: na1 = name.replace('iy', 'ij')
    elif 'ch' in name: na1 = name.replace('ch', 'c')
    elif 'sha' in name: na1 = name.replace('sha', 'sa')
    elif 'viy' in name: na1 = name.replace('viy', 'vi')
    #familia
    if 'ch' in familia: fa1 = familia.replace('ch', 'c')
    elif 'sh' in familia: fa1 = familia.replace('sh', 'z')
    elif 'tvie' in familia: fa1 = familia.replace('tvie', 'tviy')
    elif 'ushun' in familia: fa1 = familia.replace('ushun', 'yshyn')
    elif 'kov' in familia: fa1 = familia.replace('kov', 'kiv')
    elif 'zhi' in familia: fa1 = familia.replace('zhi', 'zi')
    elif 'sahl' in familia: fa1 = familia.replace('sahl', 'sakhl')

    ik_n = name + 'ik'
    mar_n = name + 'marmelad'
    ok0 = "0"+familia+"."
    print(w+lines)
    listuser = [
        ok0.replace(" ","")+na1+"777",
        ok0.replace(" ","")+na1+"62",
        ok0.replace(" ","")+na1+"122",
        ok0.replace(" ","")+na1+"528",
        ok0.replace(" ","")+na1+"538",
        ok0.replace(" ","")+na1+"122000",
        ok0.replace(" ","")+na1+"160511",
        ok0.replace(" ","")+na1,
        ik_n.replace(" ","")+familia+"62",
        ik_n.replace(" ","")+familia+"72",
        ik_n.replace(" ","")+familia+"82",
        ik_n.replace(" ","")+familia+"98",
        ik_n.replace(" ","")+familia+"97",
        ik_n.replace(" ","")+familia+"89",
        ik_n.replace(" ","")+familia+"72",
        ik_n.replace(" ","")+familia+"61",
        ik_n.replace(" ","")+familia+"53",
        ik_n.replace(" ","")+familia+"52",
        ik_n.replace(" ","")+familia+"199",
        ik_n.replace(" ","")+familia+"198",
        familia.replace(" ","")+na1+"0000",
        familia.replace(" ","")+na1+"00000",
        familia.replace(" ","")+na1+"0001",
        familia.replace(" ","")+na1+"00001",
        familia.replace(" ","")+na1+"100000",
        familia.replace(" ","")+na1+"150611",
        familia.replace(" ","")+na1+"122000",
        familia.replace(" ","")+na1+"323",
        familia.replace(" ","")+na1+"528",
        familia.replace(" ","")+na1+"538",
        familia.replace(" ","")+na1+"666",
        familia.replace(" ","")+na1+"707",
        familia.replace(" ","")+na1+"701",
        familia.replace(" ","")+na1+"344",
        familia.replace(" ","")+na1+"811",
        familia.replace(" ","")+na1+"400",
        familia.replace(" ","")+na1+"100",
        familia.replace(" ","")+na1+"666",
        familia.replace(" ","")+na1+"945",
        familia.replace(" ","")+"."+name,
        familia.replace(" ","")+"."+na1,
        fa1.replace(" ","")+name,
        fa1.replace(" ","")+na1,
        fa1.replace(" ","")+"."+name,
        fa1.replace(" ","")+"."+na1,
        familia.replace(" ","")+"."+name,
        name.replace(" ","")+fa1,
        name.replace(" ","")+"."+familia,
        familia.replace(" ","")+"."+ik_n,
        familia.replace(" ","")+"."+mar_n,
        familia.replace(" ","")+"."+na1,
        familia.replace(" ","")+"."+mar_n+"707",
        familia.replace(" ","")+"."+mar_n+"777",
        familia.replace(" ","")+"."+mar_n+"906",
        familia.replace(" ","")+"."+mar_n+"969",
        familia.replace(" ","")+"."+mar_n+"700",
        familia.replace(" ","")+"."+mar_n+"600",
        familia.replace(" ","")+"."+mar_n+"323",
        familia.replace(" ","")+"."+mar_n+"313",
        familia.replace(" ","")+"."+mar_n+"500",
        familia.replace(" ","")+"."+mar_n+"400",
        familia.replace(" ","")+"."+mar_n+"99",
        familia.replace(" ","")+"."+mar_n+"89",
        familia.replace(" ","")+"."+mar_n+"61",
        familia.replace(" ","")+"."+mar_n+"62",
        familia.replace(" ","")+"."+mar_n+"71",
        familia.replace(" ","")+"."+mar_n+"81",
        familia.replace(" ","")+"."+mar_n+"95",
        familia.replace(" ","")+"."+mar_n+"85",
        familia.replace(" ","")+"."+mar_n+"60",
        familia.replace(" ","")+"."+mar_n+"50",
        familia.replace(" ","")+"."+mar_n+"55",
        familia.replace(" ","")+"."+mar_n+"1",
        familia.replace(" ","")+"."+mar_n+"7",
        familia.replace(" ","")+"."+mar_n+"6",
        familia.replace(" ","")+"."+mar_n+"10",
        familia.replace(" ","")+"."+mar_n+"9",
        familia.replace(" ","")+"."+mar_n+"8",
        familia.replace(" ","")+"."+mar_n+"3",
        familia.replace(" ","")+"."+mar_n+"2",
        familia.replace(" ","")+"."+mar_n+"881",
        familia.replace(" ","")+"."+mar_n+"999",
        familia.replace(" ","")+"."+mar_n+"222",
        familia.replace(" ","")+"."+mar_n+"393",
        familia.replace(" ","")+"."+mar_n+"383",
        fullname.replace(" ","")+"777",
        fullname.replace(" ","")+"150611",
        fullname.replace(" ","")+"717",
        fullname.replace(" ","")+"707",
        fullname.replace(" ","")+"760",
        fullname.replace(" ","")+"999",
        fullname.replace(" ","")+"666",
        fullname.replace(" ","")+"809",
        fullname.replace(" ","")+"807",
        fullname.replace(" ","")+"888",
        fullname.replace(" ","")+"848",
        fullname.replace(" ","")+"844",
        fullname.replace(" ","")+"909",
        fullname.replace(" ","")+"900",
        fullname.replace(" ","")+"950",
        fullname.replace(" ","")+"955",
        fullname.replace(" ","")+"960",
        fullname.replace(" ","")+"970",
        fullname.replace(" ","")+"670",
        fullname.replace(" ","")+"610",
        fullname.replace(" ","")+"606",
        fullname.replace(" ","")+"650",
        fullname.replace(" ","")+"681",
        fullname.replace(" ","")+"662",
        fullname.replace(" ","")+"555",
        fullname.replace(" ","")+"505",
        fullname.replace(" ","")+"550",
        fullname.replace(" ","")+"525",
        fullname.replace(" ","")+"537",
        fullname.replace(" ","")+"531",
        fullname.replace(" ","")+"411",
        fullname.replace(" ","")+"477",
        fullname.replace(" ","")+"444",
        fullname.replace(" ","")+"499",
        fullname.replace(" ","")+"323",
        fullname.replace(" ","")+"333",
        fullname.replace(" ","")+"321",
        fullname.replace(" ","")+"388",
        fullname.replace(" ","")+"370",
        fullname.replace(" ","")+"300",
        fullname.replace(" ","")+"299",
        fullname.replace(" ","")+"288",
        fullname.replace(" ","")+"270",
        fullname.replace(" ","")+"277",
        fullname.replace(" ","")+"266",
        fullname.replace(" ","")+"240",
        fullname.replace(" ","")+"244",
        fullname.replace(" ","")+"255",
        fullname.replace(" ","")+"232",
        fullname.replace(" ","")+"222",
        fullname.replace(" ","")+"211",
        fullname.replace(" ","")+"200",
        fullname.replace(" ","")+"199",
        fullname.replace(" ","")+"189",
        fullname.replace(" ","")+"188",
        fullname.replace(" ","")+"166",
        fullname.replace(" ","")+"165",
        fullname.replace(" ","")+"169",
        fullname.replace(" ","")+"196",
        fullname.replace(" ","")+"150",
        fullname.replace(" ","")+"142",
        fullname.replace(" ","")+"133",
        fullname.replace(" ","")+"120",
        fullname.replace(" ","")+"111",
        fullname.replace(" ","")+"100",
        fullname.replace(" ","")+"707",
        fullname.replace(" ","")+"000",
        fullname.replace(" ","")+"00",
        fullname.replace(" ","")+"62",
        fullname.replace(" ","")+"71",
        fullname.replace(" ","")+"54",
        fullname.replace(" ","")+"23",
        fullname.replace(" ","")+"22",
        fullname.replace(" ","")+"99",
        fullname.replace(" ","")+"89",
        fullname.replace(" ","")+"69",
        fullname.replace(" ","")+"96",
        fullname.replace(" ","")+"60",
        fullname.replace(" ","")+"59",
        fullname.replace(" ","")+"11",
        fullname.replace(" ","")+"10",
        fullname.replace(" ","")+"9",
        fullname.replace(" ","")+"7",
        fullname.replace(" ","")+"6",
        fullname.replace(" ","")+"4",
        fullname.replace(" ","")+"3",
        fullname.replace(" ","")+"2",
        fullname.replace(" ","")+"1",
        fullname.replace(" ","")+"0",
        fullname.replace(" ",""),
        familia.replace(" ","")+na1+"323",
        familia.replace(" ","")+na1+"528",
        familia.replace(" ","")+na1+"538",
        familia.replace(" ","")+na1+"666",
        familia.replace(" ","")+na1+"707",
        familia.replace(" ","")+na1+"701",
        familia.replace(" ","")+na1+"344",
        familia.replace(" ","")+na1+"811",
        familia.replace(" ","")+na1+"400",
        familia.replace(" ","")+na1+"100",
        familia.replace(" ","")+na1+"666",
        familia.replace(" ","")+na1+"945",
        familia.replace(" ","")+na1+"888",
        familia.replace(" ","")+na1+"111",
        familia.replace(" ","")+na1+"222",
        familia.replace(" ","")+na1+"333",
        familia.replace(" ","")+na1+"444",
        familia.replace(" ","")+na1+"555",
        familia.replace(" ","")+na1+"888",
        familia.replace(" ","")+na1+"777",
        familia.replace(" ","")+na1+"999",
        familia.replace(" ","")+na1+"000",
        familia.replace(" ","")+na1+"001",
        familia.replace(" ","")+na1+"002",
        familia.replace(" ","")+na1+"003",
        familia.replace(" ","")+na1+"877",
        familia.replace(" ","")+na1+"312",
        familia.replace(" ","")+na1+"841",
        familia.replace(" ","")+na1+"808",
        familia.replace(" ","")+na1+"607",
        familia.replace(" ","")+na1+"62",
        familia.replace(" ","")+na1+"61",
        familia.replace(" ","")+na1+"81",
        familia.replace(" ","")+na1+"79",
        familia.replace(" ","")+na1+"41",
        familia.replace(" ","")+na1+"42",
        familia.replace(" ","")+na1+"44",
        familia.replace(" ","")+na1+"56",
        familia.replace(" ","")+na1+"55",
        familia.replace(" ","")+na1+"57",
        familia.replace(" ","")+na1+"69",
        familia.replace(" ","")+na1+"12",
        familia.replace(" ","")+na1+"11",
        familia.replace(" ","")+na1+"10",
        familia.replace(" ","")+na1+"32",
        familia.replace(" ","")+na1+"36",
        familia.replace(" ","")+na1+"76",
        familia.replace(" ","")+na1+"40",
        familia.replace(" ","")+na1+"9",
        familia.replace(" ","")+na1+"8",
        familia.replace(" ","")+na1+"7",
        familia.replace(" ","")+na1+"6",
        familia.replace(" ","")+na1+"5",
        familia.replace(" ","")+na1+"4",
        familia.replace(" ","")+na1+"3",
        familia.replace(" ","")+na1+"2",
        familia.replace(" ","")+na1+"1",
        familia.replace(" ","")+na1+"0",
        name.replace(" ","")+fa1,
        na1.replace(" ","")+fa1,
        #fa1 na1
        fa1.replace(" ","")+na1+"0000",
        fa1.replace(" ","")+na1+"00000",
        fa1.replace(" ","")+na1+"0001",
        fa1.replace(" ","")+na1+"00001",
        fa1.replace(" ","")+na1+"100000",
        fa1.replace(" ","")+na1+"150611",
        fa1.replace(" ","")+na1+"122000",
        fa1.replace(" ","")+na1+"323",
        fa1.replace(" ","")+na1+"528",
        fa1.replace(" ","")+na1+"538",
        fa1.replace(" ","")+na1+"666",
        fa1.replace(" ","")+na1+"707",
        fa1.replace(" ","")+na1+"701",
        fa1.replace(" ","")+na1+"344",
        fa1.replace(" ","")+na1+"811",
        fa1.replace(" ","")+na1+"400",
        fa1.replace(" ","")+na1+"100",
        fa1.replace(" ","")+na1+"666",
        fa1.replace(" ","")+na1+"945",
        fa1.replace(" ","")+na1+"888",
        fa1.replace(" ","")+na1+"111",
        fa1.replace(" ","")+na1+"222",
        fa1.replace(" ","")+na1+"333",
        fa1.replace(" ","")+na1+"444",
        fa1.replace(" ","")+na1+"555",
        fa1.replace(" ","")+na1+"888",
        fa1.replace(" ","")+na1+"777",
        fa1.replace(" ","")+na1+"999",
        fa1.replace(" ","")+na1+"000",
        fa1.replace(" ","")+na1+"001",
        fa1.replace(" ","")+na1+"002",
        fa1.replace(" ","")+na1+"003",
        fa1.replace(" ","")+na1+"877",
        fa1.replace(" ","")+na1+"312",
        fa1.replace(" ","")+na1+"841",
        fa1.replace(" ","")+na1+"808",
        fa1.replace(" ","")+na1+"607",
        fa1.replace(" ","")+na1+"62",
        fa1.replace(" ","")+na1+"61",
        fa1.replace(" ","")+na1+"81",
        fa1.replace(" ","")+na1+"79",
        fa1.replace(" ","")+na1+"41",
        fa1.replace(" ","")+na1+"42",
        fa1.replace(" ","")+na1+"44",
        fa1.replace(" ","")+na1+"56",
        fa1.replace(" ","")+na1+"55",
        fa1.replace(" ","")+na1+"57",
        fa1.replace(" ","")+na1+"69",
        fa1.replace(" ","")+na1+"12",
        fa1.replace(" ","")+na1+"11",
        fa1.replace(" ","")+na1+"10",
        fa1.replace(" ","")+na1+"32",
        fa1.replace(" ","")+na1+"36",
        fa1.replace(" ","")+na1+"76",
        fa1.replace(" ","")+na1+"40",
        fa1.replace(" ","")+na1+"9",
        fa1.replace(" ","")+na1+"8",
        fa1.replace(" ","")+na1+"7",
        fa1.replace(" ","")+na1+"6",
        fa1.replace(" ","")+na1+"5",
        fa1.replace(" ","")+na1+"4",
        fa1.replace(" ","")+na1+"3",
        fa1.replace(" ","")+na1+"2",
        fa1.replace(" ","")+na1+"1",
        fa1.replace(" ","")+na1+"0",
        fa1.replace(" ","")+na1,
        #na1 fa1
        na1.replace(" ","")+fa1+"0000",
        na1.replace(" ","")+fa1+"00000",
        na1.replace(" ","")+fa1+"0001",
        na1.replace(" ","")+fa1+"00001",
        na1.replace(" ","")+fa1+"100000",
        na1.replace(" ","")+fa1+"150611",
        na1.replace(" ","")+fa1+"122000",
        na1.replace(" ","")+fa1+"323",
        na1.replace(" ","")+fa1+"528",
        na1.replace(" ","")+fa1+"538",
        na1.replace(" ","")+fa1+"666",
        na1.replace(" ","")+fa1+"707",
        na1.replace(" ","")+fa1+"701",
        na1.replace(" ","")+fa1+"344",
        na1.replace(" ","")+fa1+"811",
        na1.replace(" ","")+fa1+"400",
        na1.replace(" ","")+fa1+"100",
        na1.replace(" ","")+fa1+"666",
        na1.replace(" ","")+fa1+"945",
        na1.replace(" ","")+fa1+"888",
        na1.replace(" ","")+fa1+"111",
        na1.replace(" ","")+fa1+"222",
        na1.replace(" ","")+fa1+"333",
        na1.replace(" ","")+fa1+"444",
        na1.replace(" ","")+fa1+"555",
        na1.replace(" ","")+fa1+"888",
        na1.replace(" ","")+fa1+"777",
        na1.replace(" ","")+fa1+"999",
        na1.replace(" ","")+fa1+"000",
        na1.replace(" ","")+fa1+"001",
        na1.replace(" ","")+fa1+"002",
        na1.replace(" ","")+fa1+"003",
        na1.replace(" ","")+fa1+"877",
        na1.replace(" ","")+fa1+"312",
        na1.replace(" ","")+fa1+"841",
        na1.replace(" ","")+fa1+"808",
        na1.replace(" ","")+fa1+"607",
        na1.replace(" ","")+fa1+"62",
        na1.replace(" ","")+fa1+"61",
        na1.replace(" ","")+fa1+"81",
        na1.replace(" ","")+fa1+"79",
        na1.replace(" ","")+fa1+"41",
        na1.replace(" ","")+fa1+"42",
        na1.replace(" ","")+fa1+"44",
        na1.replace(" ","")+fa1+"56",
        na1.replace(" ","")+fa1+"55",
        na1.replace(" ","")+fa1+"57",
        na1.replace(" ","")+fa1+"69",
        na1.replace(" ","")+fa1+"12",
        na1.replace(" ","")+fa1+"11",
        na1.replace(" ","")+fa1+"10",
        na1.replace(" ","")+fa1+"32",
        na1.replace(" ","")+fa1+"36",
        na1.replace(" ","")+fa1+"76",
        na1.replace(" ","")+fa1+"40",
        na1.replace(" ","")+fa1+"9",
        na1.replace(" ","")+fa1+"8",
        na1.replace(" ","")+fa1+"7",
        na1.replace(" ","")+fa1+"6",
        na1.replace(" ","")+fa1+"5",
        na1.replace(" ","")+fa1+"4",
        na1.replace(" ","")+fa1+"3",
        na1.replace(" ","")+fa1+"2",
        na1.replace(" ","")+fa1+"1",
        na1.replace(" ","")+fa1+"0",
        #name fa1
        name.replace(" ","")+fa1,
        name.replace(" ","")+fa1+"323",
        name.replace(" ","")+fa1+"528",
        name.replace(" ","")+fa1+"538",
        name.replace(" ","")+fa1+"666",
        name.replace(" ","")+fa1+"707",
        name.replace(" ","")+fa1+"701",
        name.replace(" ","")+fa1+"344",
        name.replace(" ","")+fa1+"811",
        name.replace(" ","")+fa1+"400",
        name.replace(" ","")+fa1+"100",
        name.replace(" ","")+fa1+"666",
        name.replace(" ","")+fa1+"945",
        name.replace(" ","")+fa1+"888",
        name.replace(" ","")+fa1+"111",
        name.replace(" ","")+fa1+"222",
        name.replace(" ","")+fa1+"333",
        name.replace(" ","")+fa1+"444",
        name.replace(" ","")+fa1+"555",
        name.replace(" ","")+fa1+"888",
        name.replace(" ","")+fa1+"777",
        name.replace(" ","")+fa1+"999",
        name.replace(" ","")+fa1+"000",
        name.replace(" ","")+fa1+"001",
        name.replace(" ","")+fa1+"002",
        name.replace(" ","")+fa1+"003",
        name.replace(" ","")+fa1+"877",
        name.replace(" ","")+fa1+"312",
        name.replace(" ","")+fa1+"841",
        name.replace(" ","")+fa1+"808",
        name.replace(" ","")+fa1+"607",
        name.replace(" ","")+fa1+"62",
        name.replace(" ","")+fa1+"61",
        name.replace(" ","")+fa1+"81",
        name.replace(" ","")+fa1+"79",
        name.replace(" ","")+fa1+"41",
        name.replace(" ","")+fa1+"42",
        name.replace(" ","")+fa1+"44",
        name.replace(" ","")+fa1+"56",
        name.replace(" ","")+fa1+"55",
        name.replace(" ","")+fa1+"57",
        name.replace(" ","")+fa1+"69",
        name.replace(" ","")+fa1+"12",
        name.replace(" ","")+fa1+"11",
        name.replace(" ","")+fa1+"10",
        name.replace(" ","")+fa1+"32",
        name.replace(" ","")+fa1+"36",
        name.replace(" ","")+fa1+"76",
        name.replace(" ","")+fa1+"40",
        name.replace(" ","")+fa1+"9",
        name.replace(" ","")+fa1+"8",
        name.replace(" ","")+fa1+"7",
        name.replace(" ","")+fa1+"6",
        name.replace(" ","")+fa1+"5",
        name.replace(" ","")+fa1+"4",
        name.replace(" ","")+fa1+"3",
        name.replace(" ","")+fa1+"2",
        name.replace(" ","")+fa1+"1",
        ik_n.replace(" ","")+familia,
        ik_n.replace(" ","")+familia+"62",
        ik_n.replace(" ","")+familia+"528",
        ik_n.replace(" ","")+familia+"707",
        ik_n.replace(" ","")+familia+"81",
        ik_n.replace(" ","")+familia+"312",
        ik_n.replace(" ","")+familia+"323",
        ik_n.replace(" ","")+familia+"150611",
        ik_n.replace(" ","")+familia+"001",
        ik_n.replace(" ","")+familia+"1",
        ik_n.replace(" ","")+familia+"2",
        ik_n.replace(" ","")+familia+"3",
        ik_n.replace(" ","")+familia+"4",
        ik_n.replace(" ","")+familia+"7",
        ik_n.replace(" ","")+familia+"54",
        ik_n.replace(" ","")+familia+"55",
        ik_n.replace(" ","")+familia+"528",
        ik_n.replace(" ","")+familia+"538",
        ik_n.replace(" ","")+familia+"81",
        ik_n.replace(" ","")+familia+"96",
        ik_n.replace(" ","")+familia+"000",
        ik_n.replace(" ","")+familia+"44",
        ik_n.replace(" ","")+familia+"43",
        ik_n.replace(" ","")+familia+"2000",
        ik_n.replace(" ","")+familia+"2001",
        ik_n.replace(" ","")+familia+"2002",
        ik_n.replace(" ","")+familia+"2003",
        ik_n.replace(" ","")+familia+"2004",
        ik_n.replace(" ","")+familia+"2005",
        ik_n.replace(" ","")+familia+"2006",
        ik_n.replace(" ","")+familia+"2007",
        ik_n.replace(" ","")+familia+"2008",
        ik_n.replace(" ","")+familia+"2009",
        ]
    f = open("result.txt","w")
    ok = []
    try:
        for user in listuser:
            for domain in data:
                email = user + "@" + domain
                api_num = '1 000 000'
                apis = ['18b15db3-4c02-473e-bb2d-39805a993abf', '83218c83-69c0-4238-ba69-2c18699998f4', '2501fcca-29e5-4fff-b48e-7cf70d6ead1e', '18476942-d0db-4a3e-9574-639c6f48f851', '014888c0-095a-4a7e-8367-6e12c857ffa0', 'cddbbcdd-0fd1-46e6-9cb8-476f8fc1e07b', '47c2769a-6dd2-4bc0-ac81-7b8c191238a9', 'c9170bef-30a2-4d76-bf1d-e16532446893', '9c6405cd-7213-4d31-a7fd-b6218c97d4f7', '93302033-0fc2-45d1-9be3-aad7aa2e9fe6', '560b7d47-91bf-4362-b548-85d23f831322', '1512da7c-95b7-4ce6-9b56-70db932964cc', '1110e3b2-00d8-4633-8813-48b837971e13', 'dce9497b-ecfd-4ecc-b159-ed3cf5519ab6', 'c9d6bbea-6b41-4bcb-b1a6-421b95d40c92', '935cef62-fcd3-4958-a6bd-e44e76b6610e', 'f3e53f50-16a5-4b6c-8a86-33e57263ac7f', '49da25eb-cafb-4dbd-9a4d-f837d89aa6b7', '78fa66d9-3aeb-4775-8742-1a197bbfe4d1', 'b91d73e7-b039-43ab-b8f7-fb763b12f341', '15816a58-c827-41de-9faa-13fd9a677724', 'c58b57b4-5aa7-420d-ac46-f063af1488f7', '4a1cba4c-c6fc-4d7e-b514-c76da9178f59', '14cea250-83fe-48ba-b2ad-8e57cb23a80e', '7b94ca89-2659-450b-b830-6423e64dd7f8', '68e4af7d-b1d5-474f-a8dd-0a69b78114b9', '93f1baa4-8ea2-4b4b-905d-56e0286ede67', 'be1a5f7e-06d0-49ee-95db-de8d59b25186', '150de096-a9a0-450c-a20d-4a212d74f696', '07452089-66bc-4e70-ab80-90f83c6f300f', 'fb36f45a-5627-499f-a399-9de47fbee171', 'fb36f45a-5627-499f-a399-9de47fbee171', 'b35ca57f-cfa9-4e49-80a3-90cddd04d71d', '9d767511-ad68-49ff-b252-bf42a671c2e8', '960c5ccf-18b3-4417-bca0-6ace2f042fcf', '5aa9818d-44c9-46ed-b749-76f3a654e52e', '8048a6dd-7bde-4e9b-bac0-cd6f1ba39ef8', '064e2356-9189-41bd-bb1c-239c714e08dc', '95c8e2e0-9085-4048-8092-4392e4209bb1', '98893b7f-b76f-484e-8f54-8b0c26bd7c6e', 'f4037fd5-637b-4a55-bbea-6ade15517c04', 'de131a1e-64b1-4ff3-b560-5a9a783a8136', '87c0d451-89e7-4056-8a84-862c09ad4456', 'f6ece0f0-2151-4282-bd13-5e7070991491', '6fc96263-8b04-4208-a9df-8b25912b4c42', 'dd43ac2d-e93a-466b-ab82-a1e71c922e02', '3ffe1c4e-287e-4440-9df9-5d36d78a8dce', '879127a3-fe82-44a1-bc48-486293d49186', '9e8e5203-07a4-42cd-bf4d-310b10f70976', '54ef3d7a-d15a-4dec-a724-976083d0744e']
                api = random.choice(apis)
                response = requests.get(
                    "https://isitarealemail.com/api/email/validate",
                    params = {'email': email},
                    headers = {'Authorization': "Bearer " + api })
                status = response.json()['status']
                if status == "valid":
                    ok.append(email)
                    f.write(email+"\n")
                    print(f"{space}{B} DONE {w} Status: {g}valid{w} Email: {email}")
                else:
                    pass
    except KeyboardInterrupt:
        print("\r"),;sys.stdout.flush()
        pass
    f.close()
    print(w+lines)
    print(f"{space}{b}>{w} {str(len(ok))} retrieved as: {y}result.txt{w}")

cls()
banner()
mailfinder()
