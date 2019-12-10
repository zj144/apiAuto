import json


def read_json(filename):
    with open('../data/'+filename,'r',encoding='utf-8') as f:
        err = list()
        for x in json.load(f).values():
            err.append(list(x.values()))

        return err

if __name__ == '__main__':
    print(read__json('login.json'))