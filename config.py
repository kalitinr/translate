""" This Source Code Form is subject to the terms of the Mozilla Public
  License, v. 2.0. If a copy of the MPL was not distributed with this
  file, You can obtain one at http://mozilla.org/MPL/2.0/."""
import pymysql


TOKEN = '5023426840:AAGoQqPYmsHuDhlR7PxCncAOKtUDUgwxkj8'
STARTMSG = "Hi, i am translator bot. I use google python and google API. To change lang use /choose"
CHOSEMSG = "Choose lang"
LANGUES = ['ru', 'de', 'en']
LANGDICT = {
    'ru': 'Russian',
    'de': 'Deutch',
    'en': 'English'
}


mydb = pymysql.connect(
    host="db4free.net",
    user="rootadmain",
    passwd="fuckfuck",
    database="youtubebase2"
)
