import subprocess
import json

languages = subprocess.check_output(["ctags", "--list-languages"]).splitlines()

lang_list = []

for lang in languages:
    kinds = subprocess.check_output(["ctags", "--list-kinds=%s" %
        lang.strip()]).splitlines()
    lang_list.append({
        'name': lang,
        'kinds': [{'kind': kind.strip()} for kind in kinds]
        })

json.dump(lang_list, open('ctags.json', 'w+'), sort_keys=True)
