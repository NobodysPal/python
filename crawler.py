import thread, Queue, re, urllib, urlparse, time, base64


class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"


urllib._urlopener = AppURLopener()


class colors:
    GREEN = "\033[92m"
    RED = "\033[91m"
    ENDC = "\033[0m"


print base64.b64decode("ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgXwogICAgICAgIF9fICAgICAgICAgICAgICAgICAg"
                       "ICAgICAgICAgIHwgfAogICAgIHwgLyAgXCBcICAgX19fIF8gX18gX18gX19fICAgICAgX3wgfCBfX18gXyBfXyAgIC8v"
                       "ICBcXAogICAgXF9cXCAgLy9fLyAvIF9ffCAnX18vIF9gIFwgXCAvXCAvIC8gfC8gXyBcICdfX3wgX1xcKCkvL18KICAg"
                       "ICAuJy8oKVwnLiB8IChfX3wgfCB8IChffCB8XCBWICBWIC98IHwgIF9fLyB8ICAgLyAvLyAgXFwgXAogICAgICBcXCAg"
                       "Ly8gICBcX19ffF98ICBcX18sX3wgXF8vXF8vIHxffFxfX198X3wgICAgfCBcX18vIHw=") + "\n"

site = ""
while not site:
    site = raw_input(colors.GREEN + "Crawl>>> " + colors.ENDC)
    try:
        urllib.urlopen(site)
    except:
        print colors.RED + "[!] " + colors.ENDC + "can't reach: " + site
        site = ""
        pass

dupcheck = set()
q = Queue.Queue(100)
q.put(site)


def queueURLs(html, origLink):
    for url in re.findall('''<a[^>]+href=["'](.[^"']+)["']''', html, re.I):
        link = url.split("#", 1)[0] if url.startswith("http") else '{uri.scheme}://{uri.netloc}/'.format(
            uri=urlparse.urlparse(origLink)) + url.split("#", 1)[0]
        if link in dupcheck:
            continue
        dupcheck.add(link)
        if len(dupcheck) > 99999:
            dupcheck.clear()
        q.put(link)


def getHTML(link):
    try:
        if urlparse.urlparse(site).netloc in link:
            print colors.GREEN + "[G] " + colors.ENDC + link
            html = urllib.urlopen(link).read()
            f = open(str(time.time()) + ".html", "w")
            f.write("{0}\n{1}".format(link, html))
            queueURLs(html, link)
        else:
            print colors.RED + "[S] " + colors.ENDC + link
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception, e:
        print e
        pass


while True:
    thread.start_new_thread(getHTML, (q.get(),))
    time.sleep(0.5)
