from http.server import HTTPServer, BaseHTTPRequestHandler
import io, shutil, urllib
from urllib.parse import urlparse
from urllib.parse import urlparse,parse_qs
import encapsulation



class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        imsi = parse_qs(urlparse(self.path).query).get('gre', None)
        pars = imsi[0]
        print(pars,len(pars),type(pars))
        pars = pars[1:len(pars)-1]
        print(pars,len(pars),type(pars))
        intpars = []
        cur = 0
        for i in range(len(pars)):
            if pars[i] != ',':
                cur = cur*10 + float(pars[i])
            else:
                intpars.append(cur)
                cur = 0
        intpars.append(cur)
        print(intpars[0],intpars[2],len(intpars))
        args = ""
        for i in range(len(intpars)):
            args = args + str(intpars[i]) + " "

        score1, score2 = encapsulation.main(args)
        print("scores are:" + str(score1)+ " and  " +str(score2))

        #url = 'http://example.com/?gre=330&toefl=123'
        #par = parse_qs(urlparse(self.path).query)
        #print(par['gre'][0], par['toefl'][0])





    def do_POST(self):
        s = str(self.rfile.readline(), 'UTF-8')  # 先解码
        print(s)

        self.send_response(301)  # URL跳转

        self.end_headers()


httpd = HTTPServer(('', 5000), MyHttpHandler)
print("Server started on 127.0.0.1,port 5000.....")
httpd.serve_forever()