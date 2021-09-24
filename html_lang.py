import requests
import json


def get_languages():
    url = 'https://cloud.google.com/speech-to-text/docs/languages'
    resp = requests.get(url)
    start_text = '        <tbody class="list">\n'
    end_text = '        </tbody>\n'
    table = resp.text.split(start_text)[1].split(end_text)[0]
    tr_start = '          <tr>\n'
    sections = table.split(tr_start)[1:]
    languages = []

    for section in sections:
        short = section.splitlines()[1].split('<td>')[1].split('<')[0]
        long = section.splitlines()[0].split('<td>')[1].split('<')[0]
        if len(languages) > 0:
        # dupe check
            if languages[-1] != {'short': short, 'long': long}:
                languages.append({'short': short, 'long': long})
        else:
            languages.append({'short': short, 'long': long})
    print(f'FOUND {len(languages)} LANGUAGES')
    return languages


with open('languages.json', 'w') as outfile:
    json.dump(get_languages(), outfile, indent=4)
