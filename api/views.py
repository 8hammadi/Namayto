from core import *


class Service(threading.Thread):
    def __init__(self, incoming_message):
        threading.Thread.__init__(self)
        self.incoming_message = incoming_message
    def run(self):
        db = firebase.database()
        incoming_message = self.incoming_message
        z = ""
        id2 = incoming_message['entry'][0]["messaging"][0]["sender"]["id"]
        id_page = incoming_message['entry'][0]["messaging"][0]["recipient"]["id"]
        l = list(set(list(db.child("namaytu").get().val()) + [id2]))
        db.child("namaytu").set(l)
        try:
            z = incoming_message['entry'][0]["messaging"][0]["message"]["text"]
            z = str(z)
            if id2 in PAGES:return HttpResponse()
            elif z[0] == "<" and z[-1] == ">":
                l = db.child("namaytu").get().val()
                # l=[ "2905085029606882", "3875003225907875", "3085771881471066", "2995229067271184", "3484816754866592", "2986260201470292", "3018537741548883", "3017014978375028", "3291638520855003", "3101871916573648", "3089653867799934", "3893546020717120", "3411064752309963", "2866982593421699", "3008297079250901", "3142090509181569", "2361755073928132", "3176900485665508", "2963835893693953","3811676018873744", "2408603845909567", "3562429030450696", "3925758904163429", "2921433811297772", "3369815899695461", "4393651367319095", "3114524028634625", "3505369642810899", "3874360495967415", "2938995599513078", "3003649359702639", "4317661281592328", "3390452494331947", "2882526865136445", "3919414378130444", "2959796140736206", "3810491122358716", "2947941431925645", "3886472724760247", "2708204732619192", "4453552938003682", "3447868555228891", "3936885336352748", "3119026268158583", "3120364418002111", "2873410749441982", "3000213903367244", "2961411590608955", "3246107688746709", "3409079012453164", "3074419329317167", "3812762712130976", "2989403544476685", "3808630809209669", "3035269606519183", "3081259378579559", "3005846422828358", "2971238896277759", "2907984109318225", "2940221652758008", "2977545262333906", "3996696097037474", "3289037871109273", "2870013789714556", "2902162693171356", "3130883776950520", "3351080328259178", "3781893441880590", "2975687442499514", "3307868852571095", "2944823402305137", "3042995079123676", "3280116842021881", "3104226806334007", "2929431580487425", "2768603583268544", "3139795476078248", "4507953869230559", "3014777381935640", "2800406476751517", "2978742302219778", "2900844393334302", "2983240315047131", "3763243193749751", "2938179389568841", "3081806321885187", "2773918752719656", "2811191055677222", "2355069621262247", "3588759687805486", "2917229338384334", "3830749126996750", "3105292819535733", "2808757832568832", "3288329944531395", "3642371215779595", "3136697403104073", "4237899286250461", "2961949807222141", "2992393637509753", "3032980086790278", "2741815319261623", "100960198306277", "3644254895591665", "3291046200907208", "4067179213324691", "3016233785080403", "4132418156770191", "2972605692866009", "2783499178438626", "3252389064779615", "3235618589816414", "2991879000848718", "3799365553471872", "102979258096775", "2898901856893480", "3590107021004393", "3048960025140929", "2896762233693713", "3902754596461633", "2766493583479597", "2002375749886988", "3988690791171337", "2839588972830636", "2783656461757602", "3477358135626970", "108485137551605" ]
                test = z[1:-1]
                for i in l:
                    for j in PAGES:
                        send_to_fb(test, i,j)
            elif z == "hespress":
                url = "https://www.hespress.com"
                html = requests.get(url)
                parse = BeautifulSoup(html.text)
                for i in parse.findAll("div", class_="latest_news_box"):
                    send_to_fb(i.find("h3").getText(), id2, id_page)
                    send_to_fb(url + i.find("h3").find("a")["href"], id2,
                               id_page)
            elif "hespress.com" in z:
                driver.get(z)
                parse = BeautifulSoup(driver.page_source)
                r = parse.find(id="article_body").findAll("p")
                send_to_fb(str(" ".join([i.getText() for i in r][:3])),id2,id_page)
            elif z[0] == ":":
                for j in search(z[1:], tld="co.in", num=10, stop=10, pause=2):
                    send_to_fb(j, id2, id_page)
                send_to_fb("ارسل لنا الرابط الدي تريد", id2, id_page)
            elif z[0] == "@":
                results = YoutubeSearch(z[1:], max_results=10).to_json()
                if "videos" in results:
                    for i in json.loads(results)["videos"]:
                        send_to_fb(i["title"], id2, id_page)
                        send_to_fb("youtube.com" + i["link"], id2, id_page)
                    send_to_fb("اﺭﺳﻞ ﺭاﺑﻂ اﻟﻘﻴﺪﻳﻮ اﻟﺪﻱ ﺗﺮﻳﺪ", id2, id_page)
                    send_to_fb("ابدا ب > للحصول فقط على المقطع الصوتي", id2,
                               id_page)
            elif z[0] == "!":
                send_file(z[1:], id2, id_page)
            elif z[0] == ".":
                send_to_fb(trad(z[1:], "ar"), id2, id_page)
            elif z[0] == "*":
                send_to_fb(trad(z[1:], "fr"), id2, id_page)
            elif z[0] == "+":
                send_to_fb(trad(z[1:], "en"), id2, id_page)
            elif z[0] in "<>":
                audio(z[1:], id2, id_page)
            elif z[0]=="&":
                book(z[1:],id2,id_page)
            elif "youtu" in z:
                if "&list=" in z:
                    ydl = youtube_dl.YoutubeDL()
                    video = ydl.extract_info(z, download=0)
                    for i in video["entries"]:
                        time.sleep(10)
                        send_to_fb(i["title"], id2, id_page)
                        send_video_to_fb(i['formats'][-1]['url'], id2,
                                         i["title"], id_page)
                    return
                send_to_fb("اﻟﻤﺮﺟﻮ اﻧﺘﻈﺎﺭ ﺗﺤﻤﻴﻞ اﻟﻔﻴﺪﻳﻮ اﻟﺨﺎﺹ ﺑﻚ", id2,
                           id_page)
                y = yt(z)
                y["id"] = id2
                send_to_fb(y["title"], id2, id_page)
                send_video_to_fb(y["url"], id2, y["title"], id_page)
            elif z[0] == "?":
                send_to_fb(wikipedia.summary(z[1:]), id2, id_page)
            elif z[0] == "#":
                send_to_fb("اﻟﻤﺮﺟﻮ اﻧﺘﻈﺎﺭ ﺗﺤﻤﻴﻞ ﺗﻄﺒﻴﻘﻚ", id2, id_page)
                get_apk(z[1:], id2, id_page)
            elif "http" in z:
                ok(z, id2, id_page)
            elif z[0] == "/":
                download_google(z[1:], id2, id_page)
            elif z[0] == ",":
                download_baidu(z[1:], id2, id_page)
            elif z[0] == "=":
                #index
                if z == "=":
                    data = json.loads(open("motamadris/0.json").read())
                    for d in data:
                        send_to_fb(" =%s " % (d["id"]), id2, id_page)
                        send_to_fb("%s" % (d["title"]), id2, id_page)
                #choix
                try:
                    data = json.loads(
                        open("motamadris/%s.json" % (z[1:])).read())
                    for d in data:
                        send_to_fb(" =%s_%s " % (z[1:], d["id"]), id2, id_page)
                        send_to_fb(" %s" % (d["title"]), id2, id_page)
                except:
                    pass
                try:
                    A = z[1:].split("_")
                    d = A[-1]
                    A = "_".join(A[:-1])
                    data = json.loads(open("motamadris/P%s.json" % (A)).read())
                    send_to_fb(data[int(d) - 1]["title"], id2, id_page)
                    href = data[int(d) - 1]["href"]
                    if "pdf" in href:
                        send_file(href, id2, id_page)
                    elif "youtu" in href:
                        y = yt(href)
                        send_to_fb(y["title"], id2, id_page)
                        send_video_to_fb(y["url"], id2, y["title"], id_page)
                except:
                    pass
                try:
                    data = json.loads(
                        open("motamadris/P%s.json" % (z[1:])).read())
                    i = 0
                    for d in data:
                        i += 1
                        send_to_fb(" =%s_%s " % (z[1:], str(i)), id2, id_page)
                        send_to_fb(" %s" % (d["title"]), id2, id_page)
                except:
                    pass
            else:
                try:
                    send_to_fb(eval(z), id2, id_page)
                except Exception as e:
                    pass
                    send_to_fb("""
ﻣﺮﺣﺒﺎ ﺑﻜﻢ ﻓﻲ اﻟﻤﺠﻴﺐ اﻻﻟﻲ ﻧﻤﻴﺘﻮ  للمساعدة اتصل بالصفحة الرسمية للاسئلة web.facebook.com/108485137551605 """,
                               id2, id_page)
        except:
          pass
        try:
            attachments = incoming_message["entry"][0]["messaging"][0][
                "message"]["attachments"][0]
            id2 = incoming_message['entry'][0]["messaging"][0]["sender"]["id"]
            if id2 == id: return HttpResponse()
            payload = attachments["payload"]["url"]
            type = attachments["type"]
            if type == "audio":
                T = speech_to_text(payload)
                send_to_fb(T, id2, id_page)
                results = YoutubeSearch(T, max_results=10).to_json()
                for i in json.loads(results)["videos"]:
                    send_to_fb(i["title"], id2, id_page)
                    send_to_fb("youtube.com" + i["link"], id2, id_page)
                send_to_fb("اﺭﺳﻞ ﺭاﺑﻂ اﻟﻘﻴﺪﻳﻮ اﻟﺪﻱ ﺗﺮﻳﺪ", id2, id_page)
            if type == "image":
                to_text(payload, id2, id_page)
        except Exception as e:
            pass


@csrf_exempt
def api(request):
    if request.method == 'POST':
        form = request.POST
        if "@" in form:
            # print(form)
            send_to_fb("SnubbyLand @id " + form["@"])
            return HttpResponse()
    return HttpResponse("ok")


def url2yield(url, chunksize=1024):
    s = requests.Session()
    # Note: here i enabled the streaming
    response = s.get(url, stream=True)

    chunk = True
    while chunk:
        chunk = response.raw.read(chunksize)
        if not chunk:
            break
        yield chunk


# Then creation your view using StreamingHttpResponse
def get_image(request):
    img_url = "https://kinsta.com/fr/wp-content/uploads/sites/4/2019/08/jpg-vs-jpeg.jpg"
    return StreamingHttpResponse(url2yield(img_url), content_type="image/jpeg")


def privacy_policy_api(request):
    return render(
        request, "privacy_policy.html", {
            "id_app": "536485193704830",
            "url_image": "https://ensias.pythonanywhere.com/media/image.png"
        })


def privacy_policy_ia(request):
    return render(request, "privacy_policy.html", {
        "id_app": "634877914028588"
    })


class YoMamaBotView(generic.View):
    def get(self, request, *args, **kwargs):
        if "hub.verify_token" not in self.request.GET:
            return HttpResponse("ok")
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        thread1 = Service(incoming_message)
        thread1.start()
        return HttpResponse()


class Github(generic.View):
    def get(self, request, *args, **kwargs):
        if "hub.verify_token" not in self.request.GET:
            return HttpResponse("ok")
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        return HttpResponse()
