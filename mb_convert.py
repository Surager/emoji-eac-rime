emoji_file = open("emoji-eac.mb", "rb")
rime_config_file = open("emoji-eac.dict.yaml", "wb")
rime_config_header = '''---
name: emoji-eac
version: "1.0"
sort: by_weight
...
'''
rime_config_file.write(rime_config_header.encode('utf-8'))

i = 0
while True:
    try:
        line = emoji_file.readline()
        if not line:
            break
        emoji_group = line.strip().decode('utf-8')
        emoji_group = emoji_group.split(' ')
        code = emoji_group[0].replace(':', '')
        code = code.replace('_', '')
        emoji = emoji_group[1]
        text = emoji + '\t' + code + '\n'
        rime_config_file.write(text.encode('utf-8'))
        i += 1
    except Exception as e:
        print("Error: ", e)
        exit(-1)

print("Successfully converted %d lines." % i)
