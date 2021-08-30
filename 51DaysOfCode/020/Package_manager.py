'''
What is PIP ?
PIP stands for Preferred installer program.
We use pip to install different python packages.
Package is a python module that can contain one or more modules or other packages.
A module or modules that we can install to our application is a package.
In programming, we do not have to write every utility program,
instead we install packages and import them to our applications.
'''

import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]


# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)