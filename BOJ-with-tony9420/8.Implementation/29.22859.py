import sys
import re

def input():
    return sys.stdin.readline().rstrip()

html = input()

html = html[len('<main>'): -len('</main>')]
html = re.sub(r'<div +title="([\w]* )">', r'title : \1\n', html)
html = re.sub(r'</div>', '', html)

html = re.sub(r'<p>', '', html)
html = re.sub(r'</p>', '\n', html)

html = re.sub(r'</?[\w ]*>', '', html)
html = re.sub(r' ?\n ?', '\n', html)
html = re.sub(r' {2,}', ' ', html)

print(html)