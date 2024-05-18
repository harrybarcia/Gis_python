from bs4 import BeautifulSoup

# Example HTML content (use response.text in your actual code)
html_doc = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
<head>
<title>Index of /geo/tiger/TIGER2023/BG</title>
</head>
<body>
<table>
<tr><th valign="top"><img alt="[ICO]" src="/icons/blank.gif"/></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
<tr><th colspan="5"><hr/></th></tr>
<tr><td valign="top"><img alt="[PARENTDIR]" src="/icons/back.gif"/></td><td><a href="/geo/tiger/TIGER2023/">Parent Directory</a></td><td> </td><td align="right">  - </td><td> </td></tr>
<!-- Additional rows omitted for brevity -->
<tr><td valign="top"><img alt="[   ]" src="/icons/compressed.gif"/></td><td><a href="tl_2023_01_bg.zip">tl_2023_01_bg.zip</a></td><td align="right">2023-11-22 21:22  </td><td align="right"> 18M</td><td> </td></tr>
<tr><td valign="top"><img alt="[   ]" src="/icons/compressed.gif"/></td><td><a href="tl_2023_02_bg.zip">tl_2023_02_bg.zip</a></td><td align="right">2023-11-22 21:22  </td><td align="right">6.3M</td><td> </td></tr>
<!-- More rows here -->
</table>
</body>
</html>"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

# Find all <a> tags and filter those with '.zip' in their 'href' attribute
zip_links = [a['href'] for a in soup.find_all('a') if 'href' in a.attrs and a['href'].endswith('.zip')]

# Print the list of zip file links
print(zip_links)
