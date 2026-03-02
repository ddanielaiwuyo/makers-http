from flask import Flask, Request, Response, request
import json

app = Flask(__name__)

class Artist:
    def __init__(self, name: str, genre: str):
        self.name = name
        self.genre = genre

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)


test_get_artist = Artist("JPEGMAFIA", "new_roullete")

class MuResponse:
    def __init__(self, code: int, msg: str):
        self.code = code
        self.msg = msg

    def to_json(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)


@app.route("/artists", methods=["GET", "POST"])
def get_artists():
    if request.method == "POST":
        return "post_artist_endpoint"

    muRes = MuResponse(209, "nvim*1:server")

    jsonen = muRes.to_json()
    new_res = Response(jsonen, muRes.code, content_type="application/json" )
    new_res.headers.set("x-cache", "hit")
    analyse_res(new_res)
    return new_res



def analyse_res(res: Response) -> None:
    print("\n\nanalysing response\n\n")
    print("response-body: ", res.response)
    print("headers:", res.headers)


def analyse_req(req :Request) -> None:
    print("analyzing requests...")
    methds = list(req.__dict__.keys())
    for id , meth in enumerate(methds, start=0):
        print(id, meth)

    print("request-headers: ", req.headers) # possibly inherited from Requests Headers 
    print("host: ", req.host, req.host_url)
    print("args: ", req.view_args) # probably request-params
    print("server?:", req.server) # returns (ip-address, port)
    print("url-rule:", req.url_rule)
