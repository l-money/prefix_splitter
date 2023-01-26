import json


def build_tree(prefixes: [dict]) -> dict:
    tree = dict()
    for prefix in prefixes:
        index = tree
        for i in range(len(prefix['dial_code'])):
            c = prefix['dial_code'][i]
            if c not in index.keys():
                index[c] = dict()
            index = index[c]
            if i == len(prefix['dial_code']) - 1:
                country = dict()
                country['country'] = prefix['name']
                country['country_code'] = prefix['code']
                country['prefix'] = prefix['dial_code']
                if 'countries' not in index.keys():
                    index['countries'] = list()
                index['countries'].append(country)
    return tree


def split_prefix(number: str) -> dict:
    f = open("prefixes_tree.json", "r")
    prefixes = json.load(f)
    f.close()
    response = dict()
    response['prefix'] = ''
    response['number'] = number
    response['countries'] = list()
    if len(number) <= 0:
        raise Exception('Empty number')
    if number[0] != '+':
        raise Exception('Number must start with +')
    a: str = number[1:]
    if not a.isnumeric():
        raise Exception('Number must be numeric')
    pr = prefixes
    for n in number:
        if n in pr.keys():
            pr = pr[n]
            if 'countries' in pr.keys():
                data: dict = pr['countries'][0]
                response['countries'] = pr['countries']
                response['prefix'] = data['prefix']
                response['number'] = number[len(data['prefix']):]
        else:
            break
    return response


# f = open("prefixes.json", "r")
# prefixes = json.load(f)
# f.close()
#
# print(json.dumps(build_tree(prefixes)))
print(json.dumps(split_prefix('+542331401173'), indent=4))
