import requests
import sys
import json
import time


class Argument:
    Url = 1
    LogLocation = 2
    Count = LogLocation + 1


def does_hololens_turned_off():
    return False  # TODO: Build the policy!


def main():
    if len(sys.argv) != Argument.Count:
        raise Exception("lack of arguments!")

    url = sys.argv[Argument.Url]
    log_location = sys.argv[Argument.LogLocation]

    while not does_hololens_turned_off():
        data = requests.get(url + '/api/power/battery', verify=False)
        data = json.loads(data.content)

        data['timestamp'] = time.time()
        data['tag'] = 'battery'

        with open(log_location, 'a') as f:
            f.write(json.dumps(data))
            f.write('\n')

        time.sleep(10)


if __name__ == '__main__':
    main()
