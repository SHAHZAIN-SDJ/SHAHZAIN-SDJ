# hallo bro :v

from wibu.YNTKTS import *
import urllib.request

areYOUgay=random.choice(["Kang.Pacman","Lo.Ngentod.Ajg"])

class report:
	def __init__(self,url,cookie):
		
		self.url=url
		self.cookies=cookie
		self.laporkan()
		
	def find_id(self,username):
		try: respon=req.get(f"{self.url}/{username}/about",cookies=self.cookies).text
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		uid=re.search('\<a\ href\=\"/.*?\?v=timeline&amp;lst=(.*?)"',respon).group(1)
		return urllib.request.unquote(uid).split(":")[1]
	
	def chat(self,uid,ngebug,**data):
		try: respoN=req.get(f"{self.url}/messages/?fbid={uid}",cookies=self.cookies)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		respon=parser(respoN.text,"html.parser")
		nv=respon.find_all("input",{"type":"hidden","name":True,"value":True})
		act=respon.find("form",{"method":"post","action":True})
		if len(nv)!=0 and act!=None:
			data.update({x["name"]:x["value"] for x in nv})
			data.update({f"ids[{uid}]":uid,"body":ngebug,"Send":"Kirim"})
			respon=req.post(self.url+act["action"],headers=head(self.url,respoN),cookies=self.cookies,data=data)
			exit(" * sukses melaporkan bug" if "send_success" in respon.url else " ! gagal melaporkan bug")
		else: exit(" ! error tidak diketahui")
			
	def laporkan(self):
		#asuu=self.find_id(areYOUgay)
		teks_bug=input(" ? bug yang ingin di laporkan : ")
		while teks_bug in (""," "):
			print(" ! jangan kosong ngentod")
			teks_bug=input(" ? bug yang ingin di laporkan : ")
		self.chat("100068019551652",teks_bug)
		
