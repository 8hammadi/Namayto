from core import *


class Service(threading.Thread):
    def __init__(self, incoming_message):
        threading.Thread.__init__(self)
        self.incoming_message = incoming_message

    def run(self):
        incoming_message = self.incoming_message
        z = ""
        id2 = incoming_message['entry'][0]["messaging"][0]["sender"]["id"]
        id_page = incoming_message['entry'][0]["messaging"][0]["recipient"][
            "id"]
        l = list(set(list(db.child("namaytu").get().val()) + [id2]))
        db.child("namaytu").set(l)
        if "message" in incoming_message['entry'][0]["messaging"][0]:
            z = incoming_message['entry'][0]["messaging"][0]["message"]["text"]
            z = str(z)
            if id2 in PAGES:
                return HttpResponse()
            if z[0] == "<" and z[-1] == ">":
                l = db.child("namaytu").get().val()
                test = z[1:-1]
                for i in l:
                    send_to_fb(test, i)
            elif z == "hespress":
                url = "https://www.hespress.com"
                html = requests.get(url)
                parse = BeautifulSoup(html.text)
                for i in parse.findAll("div", class_="latest_news_box"):
                    send_to_fb(i.find("h3").getText(), id2, id_page)
                    send_to_fb(url + i.find("h3").find("a")["href"], id2,
                               id_page)
            elif "www.hespress.com" in z:
                html3 = requests.get(z)
                parse3 = BeautifulSoup(html3.text)
                r = parse3.find(id="article_body").findAll("p")
                send_to_fb(" ".join([i.getText() for i in r]),id2,id_page)
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
                        # send_to_fb("%d ﺳﺎﻋﺔ %d ﺩﻗﻴﻘﺔ%d ﺗﺎﻧﻴﺔ"%cool(i["id"]),id2)
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
                #download
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
                # choix pdf
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
        # except:
        #   pass
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
