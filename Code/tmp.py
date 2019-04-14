# cookies = "anonymid=ju1ddl6lbu82s9; depovince=GW; jebecookies=d578ebb5-4752-4509-bfa3-111d75e98f6c|||||; _r01_=1; JSESSIONID=abcqYHdEWcO507kZb1JNw; ick_login=077193a8-1ce5-4d29-879d-fb1cd6a0f59d; _de=9323AFC449BE8C8D44B0A57815E527E7696BF75400CE19CC; p=2829d79a175b654553cc2ad7dd84485e4; first_login_flag=1; ln_uact=xudong.l@163.com; ln_hurl=http://hdn101.rrimg.com/photos/hdn101/20090403/20/12/head_GumL_11334c204197.jpg; t=5e0341f372474c645508054660c3f3334; societyguester=5e0341f372474c645508054660c3f3334; id=707898734; xnsid=1c2a1bf5; ver=7.0; loginfrom=null; jebe_key=703f45d6-685c-426d-9320-3238daeb3ea1%7C2cfcb913d1600af5386c0ba68f1a9ec0%7C1554305641421%7C1%7C1554305644553; wp_fold=0"
# res = cookies.split(";")
# #cookies={i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
#
# res = cookies.split(";")
# cookie_tmp ={}
# for i in res:
#     cookie_tmp.update({i.split("=")[0]:i.split("=")[1]})
#
# print(cookie_tmp)

url  = 'https://imgsa.baidu.com/forum/w%3D580/sign=33e650a79782d158bb8259b9b00b19d5/0f4b9a504fc2d56267da06a4ec1190ef77c66c19.jpg'
res = url.split("/")
print(res[-1])