# -*- coding: utf-8 -*-
import requests

header = headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Cookie": "anonymid=jsb5azolwa5nux; depovince=GUZ; jebecookies=8cd955e0-f4c9-44f2-a9dc-19488a7fe96a|||||; _r01_=1; JSESSIONID=abc4NJaPqnGgN79pyKdKw; ick_login=5daf350a-1a16-4b36-9c3c-28fbcdac3d3b; _de=9323AFC449BE8C8D44B0A57815E527E7696BF75400CE19CC; p=375d50802c8b5f5ef3e394b7b574e8514; first_login_flag=1; ln_uact=xudong.l@163.com; ln_hurl=http://hdn101.rrimg.com/photos/hdn101/20090403/20/12/head_GumL_11334c204197.jpg; t=2ad23f737d97dde02a88911742df0ef74; societyguester=2ad23f737d97dde02a88911742df0ef74; id=707898734; xnsid=fc6afb3e; ver=7.0; loginfrom=null; jebe_key=dde9d8d5-1c53-4b26-80ed-0970879c08a8%7C2cfcb913d1600af5386c0ba68f1a9ec0%7C1550543294704%7C1%7C1550543261835; wp_fold=0"
}


def main():
    r = requests.get("http://www.renren.com/707898734/profile", headers=headers)
    with open("./test.html", "w", encoding="utf-8") as f:
        f.write(r.content.decode())
        f.close()


if __name__ == "__main__":
    main()
