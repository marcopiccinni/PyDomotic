import yaml
from functions.text_to_speech import speech

c = None
with open("view.yaml", 'r') as stream:
    try:
        c = yaml.load(stream)
        print(c)

    except yaml.YAMLError as exc:
        print(exc)

for elem in c['marco']:
    print(elem['function']['name'])
    speech(elem['speech'])

print([elem['function']['name'] for elem in c['marco']])

from models.marco.skills import *

f = str(c['marco'][0]['function']['name'])
p = str(c['marco'][0]['function']['params'])[1:-1]

exec("from models.marco.skills import *\n" + f + '(' + p + ')')
