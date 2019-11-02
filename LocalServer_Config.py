from http.server import HTTPServer, BaseHTTPRequestHandler
import io, shutil, urllib
from urllib.parse import urlparse
from urllib.parse import urlparse,parse_qs
import DefaultAlgorithms


class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #self.send_response(200)
        #self.send_header("Content-type", "text/html")
        #self.end_headers()
        imsi = parse_qs(urlparse(self.path).query).get('data', None)
        pars = imsi[0]
        pars = pars[1:len(pars)-1]
        intpars = []
        cur = 0
        for i in range(len(pars)):
            if pars[i] != ',':
                cur = cur*10 + float(pars[i])
            else:
                intpars.append(cur)
                cur = 0
        intpars.append(cur)
        #args = ""
        #for i in range(len(intpars)):
        #    args = args + str(intpars[i]) + " "
        #print(args)
        score1, score2, score3, score4,score5,score6= DefaultAlgorithms.main(intpars)
        print("scores are:")

        print(str(score1))
        print(str(score2))
        print(str(score3))
        print(str(score4))
        print(str(score5))
        print(str(score6))
        score_Str = str(score1)+"\n"+str(score2)+"\n"+str(score3)+"\n"+str(score4)+"\n"+str(score5)+"\n"+str(score6)
        ########################
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(score_Str,"utf-8"))

        #self.wfile.write(str(score1))
        ##if self.connection:
        ##    print("self.connection: %s" % self.connection)
        ##    print("dir(self.connection): %s" % dir(self.connection))
        ##    self.connection.send("Hello Connection!")w
        #self.send_response(score1)



        #url = 'http://example.com/?gre=330&toefl=123'
        #par = parse_qs(urlparse(self.path).query)
        #print(par['gre'][0], par['toefl'][0])





    def do_POST(self):
        s = str(self.rfile.readline(), 'UTF-8')  # 先解码
        print(s)

        self.send_response(301)  # URL跳转

        self.end_headers()


httpd = HTTPServer(('', 443), MyHttpHandler)
print("Server started on local on port 443.....")
httpd.serve_forever()
