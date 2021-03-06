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
        if id2 in PAGES:return HttpResponse()
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
            if type == "image":
                to_text(payload, id2, id_page)
        except Exception as e:
            pass
        
        z = incoming_message['entry'][0]["messaging"][0]["message"]["text"]
        z = str(z)
        if z[0] in "()><":
            results = YoutubeSearch(z[1:], max_results=10).to_json()
            if "videos" in results:
                for i in json.loads(results)["videos"]:
                    audio("youtube.com" + i["link"], id2, id_page)
        elif z=="id":
            send_to_fb("F"+id2,id2,id_page)
        elif z[0].lower()=="e":
            i=int(z[1:])%(leng)
            send_to_fb(ERDATA["English words/sentences"][i],id2,id_page)
        elif "###" in z:
            url,title=z.split("###")
            url=url.replace("#",".")
            print("[%s]"%(url))
            url_to_fb(url, title, id2,id_page)
        elif z[0].lower()=="f":
            i=int(z[1:])%(leng)
            send_to_fb(ERDATA["French words/sentences"][i],id2,id_page)
        elif z[0]=="X":
            send_to_fb("ok",id2,id_page)
            send_to_fb("لقد تم ارسال الدعوة المرجو قبولها في فيس بوك للمطورين",z[1:],id_page)
        elif z.lower()=="ana":
            send_to_fb(random.choice(ana),id2,id_page)
        elif z[0]=="$":
            z=z[1:]
            if ">>" in z:
                a,b=z.split(">>")
                db.child("%s/%s/%s"%(id_page,id2,a)).set(b)
                send_to_fb("ok",id2,id_page)
                if a=="AccessToken":
                    send_to_fb("AccessTokenOk",id2,id_page)
                if a=="PageID":
                    send_to_fb("PageIDOK",id2,id_page)
            else:
                send_to_fb(db.child("%s/%s/%s"%(id_page,id2,z)).get().val(),id2,id_page)
        elif z[0] == "@":
            results = YoutubeSearch(z[1:], max_results=10).to_json()
            if "videos" in results:
                for i in json.loads(results)["videos"]:
                    send_to_fb(i["title"], id2, id_page)
                    send_to_fb("Namayto"+i["id"], id2, id_page)
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
        elif z[:7]=="Namayto":
            data=json.loads(db.child("largscaldata").get().val())
            if z[7:] in data:
                send_to_fb(data[z[7:]]["title"], id2, id_page)
                send_to_fb("https://www.facebook.com/watch/?v=%s"%(data[z[7:]]["id"]), id2, id_page)
                return
            # if "&list=" in z:
            #    return
            #    ydl = youtube_dl.YoutubeDL()
            #    video = ydl.extract_info(z, download=0)
            #    for i in video["entries"]:
            #       time.sleep(10)
            #       send_to_fb(i["title"], id2, id_page)
            #       send_video_to_fb(i['formats'][-1]['url'], id2,
            #                    i["title"], id_page)
            y = yt("https://www.youtube.com/watch?v=" +z[7:])
            y["id"] = id2
            if send_video_to_fb(y["url"], id2, y["title"], id_page)==0:
                url_to_fb(y["url"], y["title"], id2,id_page,yt_id=z[7:])
        elif z[0] == "?":
            send_to_fb(wikipedia.summary(z[1:]), id2, id_page)
        elif z[0] == "#":
            send_to_fb("اﻟﻤﺮﺟﻮ اﻧﺘﻈﺎﺭ ﺗﺤﻤﻴﻞ ﺗﻄﺒﻴﻘﻚ", id2, id_page)
            get_apk(z[1:], id2, id_page)
        elif z[0] == "/":
            download_google(z[1:], id2, id_page)
            download_baidu(z[1:], id2, id_page)
        else:
            try:
                i=int(z)
                z=to_(z)
            except:
                data = json.loads(open("data/full_data/0.json").read())
                s=""
                for d in data:
                    s+=" [%s]"%(to_number(d["id"])) +" "+d["title"]
                send_to_fb(s,id2,id_page)
                return
            try:
                data = json.loads(
                    open("data/full_data/P%s.json" % (z)).read())
                i = 0
                s=""
                for d in data:
                    i += 1
                    s+=" [%s]"%(to_number("%s_%s" % (z, str(i))))+" "+d["title"]
                send_to_fb(s,id2,id_page)
                if i!=0:return
            except:
                pass
            try:
                
                data = json.loads(
                    open("data/full_data/%s.json" % (z)).read())
                s=""
                for d in data:
                    s+=" [%s]"%(to_number("%s_%s" % (z, d["id"]))) +" "+d["title"]
                send_to_fb(s,id2,id_page)
            except:
                pass
            try:
                A = z.split("_")
                d = A[-1]
                A = "_".join(A[:-1])
                data = json.loads(open("data/full_data/P%s.json" % (A)).read())
                send_to_fb(data[int(d) - 1]["title"], id2, id_page)
                href = data[int(d) - 1]["href"]
                if "pdf" in href:
                    send_file(href, id2, id_page)
                elif "youtu" in href:
                    R=json.loads(open("data/yt_to_fb_data.json","r").read())
                    y = yt(href)
                    if href in R:
                        send_to_fb(y["title"]+"  https://www.facebook.com/watch/?v="+R[href], id2, id_page)
                    else:
                        send_to_fb(y["title"]+"   "+href, id2, id_page)
                        # send_to_fb(,id2 ,id_page)
                        # send_video_to_fb(y["url"], id2, y["title"], id_page)
                else:
                    send_to_fb(href,id2 ,id_page)
            except:
                pass

@csrf_exempt
def api(request):
    if request.method == 'POST':
        form = request.POST
        if "@" in form:
            send_to_fb("SnubbyLand @id " + form["@"])
            return HttpResponse()
    return HttpResponse("ok")


def url2yield(url, chunksize=1024):
    s = requests.Session()
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
            "id_app": "256148139151583",
            "url_image": "https://ensias.pythonanywhere.com/media/image.png"
        })


def privacy_policy_ia(request):
    return render(request, "privacy_policy.html", {
        "id_app": "256148139151583"
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
        # print(incoming_message)
        thread1 = Service(incoming_message)
        thread1.start()
        return HttpResponse()


class YoMamaBotViewTest(generic.View):
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
        # print(incoming_message)
        # thread1 = Service(incoming_message)
        # thread1.start()
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
        # print(incoming_message)
        return HttpResponse()

def home(request):
    return render(request,"home.html")
