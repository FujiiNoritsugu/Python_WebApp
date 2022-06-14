import requests


def main():
    url = 'http://127.0.0.1:5000/try_rest'
    param = {
        "name": "dummy",
        "age": 21,
        "friends": [
            "dummy1",
            "dummy2",
            "dummy3"],
        "is_man": False}
    response = requests.post(url, json=param)
    response_json = response.json()
    for friend in response_json['response_json']['friends']:
        print(friend)


if __name__ == '__main__':
    main()
