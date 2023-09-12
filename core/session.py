import requests
import datetime
import jwt
import base64
import json
import logger
BASEURL = "https://pdigs.com"
class JWT:
    def __init__(self,jwt_token:str):
        self.__jwt = jwt_token
        self.__jwt_header = self.__preprocess()
        if self.__jwt_header['typ'] != "JWT":
            raise Exception('Invalid JWT')
        self.__payload = self.__parse()
        self.__algorithm = self.__jwt_header['alg']
    def __parse(self):
        return json.loads(base64.b64decode(self.__jwt.split('.')[1]).decode("utf8"))
    def __preprocess(self):
        jwt_header = self.__jwt.split(".")[0]
        return json.loads(base64.b64decode(jwt_header).decode("utf8"))
    def decode(self,secret):
        return jwt.decode(self.__jwt,secret,algorithms=[self.__algorithm])
    @property
    def username(self):
        return self.__payload['usr']
    @property
    def scope(self):
        return self.__payload['scope']
    @property
    def exp(self):
        return datetime.datetime.fromtimestamp(self.__payload['exp'])
    @property
    def is_valid(self):
        dt_now = datetime.datetime.now()
        exp = datetime.datetime.fromtimestamp(self.__payload['exp'])
        return dt_now < exp

class ClintSession:
    """
    usage of this session
    object.set_bearer()

    """
    def __init__(self):
        self.__bearer = ""
        self.__header = {}
        self.__not_expired = False
        self.__baseurl = BASEURL
        self.__show_send = False
    def login(self,username,password):
        header = {"content-type":"application/x-www-form-urlencoded"}
        r = requests.post(self.__baseurl + "/api/v1/token",headers=header,
                          data=f"username={username}&password={password}")
        if r.status_code != 200:
            raise Exception(r.text)
        logger.logger.info("USERNAME " + username + " Logged in success")
        if self.__show_send:
            print("LOGIN SUCCESS, by " + username, " a bearer returned by " + r.url)
        self.set_bearer(r.json()['access_token'])
        self.__not_expired = True
    def set_bearer(self,bearer:str):
        auth = JWT(bearer)
        if self.__show_send:
            print(f"JWT DECODE SUCCESS,username:{auth.username}, exp:{auth.exp}, with scope {auth.scope}")
        self.__not_expired = auth.is_valid
        if self.__not_expired:
            self.__bearer = bearer
        self.__header.update({
            "Authorization":"Bearer " + bearer
        })
    def add_header(self,header_dict:dict):
        self.__header.update(header_dict)
    def update_baseurl(self,baseurl:str):
        self.__baseurl = baseurl
    def get(self,url):
        if not self.__not_expired:
            raise Exception('Invalid Bearer or bearer has expired')
        r = requests.get(self.__baseurl + url,headers=self.__header)
        logger.logger.info("a GET send to " + r.url)
        if r.status_code == 200:
            return r
        else:
            raise Exception(r.json())

    def post(self,url,**kwargs):
        if self.__show_send:
            print(kwargs)
        if not self.__not_expired:
            raise Exception('Invalid Bearer or bearer has expired')
        r = requests.post(url=str(self.__baseurl+url),headers=self.__header,**kwargs)
        logger.logger.info("a POST send to " + r.url)
        if r.status_code == 200:
            return r
        else:
            raise Exception(r.text)
    def show_send(self,v):
        self.__show_send = v