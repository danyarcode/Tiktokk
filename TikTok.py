import requests
import user_agent,os,random,time
logo = """\033[36;1m
        **************************************
        
        *      -> Instagram: y0.1u           *
        
        ************************************** 
        \033[37;1m
"""
def ani():
#	os.system("clear")
	hit = 0
	bad = 0
	check = open("user.txt","r").readlines()
	gooduser = open("gooduser.txt","w")
	for dx in check:
		xor = dx.strip()
		#pp=generate_user_agent()
		url = f"https://www.tiktok.com/@{xor}"
		head = {
        'Host': 'www.tiktok.com',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        'Connection': 'keep-alive'
		}
		s = requests.get(url,headers=head)
	#	print(s)
		if s.status_code==404:
			os.system("clear")
			hit+=1
			print(logo)
			print("\n\033[32mGood :{}".format(hit))
			print("\033[31mBad :{}".format(bad))
			gooduser.write(xor+"\n")
		
			
		else:
			os.system("clear")
			bad+=1
			print(logo)
			print("\n\033[32mGood :{}".format(hit))
			print("\033[31mBad :{}".format(bad))
	print("\n\nAll User Check good User Save File Gooduser.txt (:")
	time.sleep(3)

def user():
	os.system("clear")
	ow=open("user.txt","w")
	import random
	txt="azbcmdbfpgoqyrjgncx0183659y._9284.djcpe_720bfnczlaaapwutg.7"
	for x in range(300):
		r = random.choice(txt)
		r2 = random.choice(txt)
		re = random.choice(txt)
		r3 = random.choice(txt)
		end = r+re+r3
		ow.write(end+"\n")
	os.system("clear")
	time.sleep(1)
	print("\nUser Make (:")
	time.sleep(3)
	
def userr():
	os.system("clear")
	ow=open("user.txt","w")
	import random
	txt="azbcmdbfpgoqyrjgncx0183659y._9284.djcpe_720bfnczlaaapwutg.7"
	for x in range(300):
		r = random.choice(txt)
		r2 = random.choice(txt)
		re = random.choice(txt)
		r3 = random.choice(txt)
		r4 = random.choice(txt)
		end = r+re+r3+r4
		ow.write(end+"\n")
	os.system("clear")
	time.sleep(1)
	print("\nUser Make (:")
	time.sleep(3)
	
	
def userrr():
	os.system("clear")
	ow=open("user.txt","w")
	import random
	txt="azbcmdbfpgoqyrjgnc0183659y._9284.djcpe_720bfnczlaaapwutg.7"
	for x in range(300):
		r = random.choice(txt)
		r2 = random.choice(txt)
		re = random.choice(txt)
		r3 = random.choice(txt)
		r4 = random.choice(txt)
		r5 = random.choice(txt)
		end = r+re+r3+r4+r5
		ow.write(end+"\n")
	os.system("clear")
	time.sleep(1)
	print("\nUser Make (:")
	time.sleep(3)
	
	
def a():
	os.system("clear")
	print("[ 1 ] User 3")
	print("[ 2 ] User 4")
	print("[ 3 ] User 5")
	print("[ 0 ] Exit Tool ")
	i = int(input("\nChoice :"))
	if i==1:
		os.system("clear")
		user()
		ani()
		time.sleep(10)
		a()
	if i==2:
		os.system("clear")
		userr()
		ani()
		time.sleep(10)
		a()
	if i==3:
		os.system("clear")
		userrr()
		ani()
		time.sleep(10)
		a()
	if i==0:
		exit()
	else:
		print("\n")
		print("Choice Failed ")
		time.sleep(3)
		a()

def password():
	os.system("clear")
	passwordd = "zher0'm12"
	print(logo)
	p = input("\n\nPassowrd :")
	if p==passwordd:
		a()
	else:
		print("\n\nPassword Faild !!")
		time.sleep(2)
		password()
password()
#a()
		
