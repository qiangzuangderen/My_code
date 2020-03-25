#!python3
#py.py - 口令保管箱

PASSWORDS = {'email':'flamingo','baidu':'flamingo801123','xunlei':'flamingo801123'}

import sys

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  #第一项为字符串，为文件名

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + 'copied to clipboard')
else:
    print('There is no account named' + account)