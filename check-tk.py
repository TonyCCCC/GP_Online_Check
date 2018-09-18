import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import re
import requests
from lxml import etree

root = tk.Tk()
root.title('GP Online Check')

label = ttk.Label(root, text='Input Pkg Name')
label.grid(row=0, padx=20, pady=20)
package = tk.StringVar()
entry = ttk.Entry(root, width=20, textvariable=package)
entry.grid(row=1, padx=20, pady=20)

result = scrolledtext.ScrolledText(root, height=40, width=30, highlightbackground='black', highlightthickness=1)
result.grid(row=0, column=1, rowspan=3, padx=20, pady=20)


def check():
    entry.focus_set()
    result.insert(tk.END, 'Loading...\r\n\r\n\r\n')
    pkg = package.get()
    headers = {
        'Referer': 'https://play.google.com/store/apps',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, '
                      'like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
    }

    pkg_list = re.findall(r"[a-zA-Z0-9._]+", pkg)
    lonline = []
    loffline = []
    for p in pkg_list:
        print('Checking %s' % p)
        response = requests.get('https://play.google.com/store/apps/details?id=' + p, headers=headers)
        html = etree.HTML(response.text)
        title = html.xpath('//head/title/text()')
        print(title)
        if title[0] == 'Not Found':
            loffline.append(p)
        else:
            lonline.append(p)

    sonline = '\r\n'.join(lonline)
    soffline = '\r\n'.join(loffline)
    output = 'Online Pkg: \r\n%s\r\n\r\nOffline Pkg: \r\n%s\r\n==============================\r\n' % (sonline, soffline)
    result.insert(tk.END, output)


button = ttk.Button(root, text='Check', command=check)
button.grid(row=2)

root.mainloop()
