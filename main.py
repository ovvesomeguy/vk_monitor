from source.lib import need_to_send , send_cool_message , send_me_message
from source.logger import log

import time

def main():
    print('| I`m started |')
    send_me_message('Build succsesed')
    log('Сборка закончилась')
    while True:
        if need_to_send():
            send_cool_message()
            time.sleep(63)
if __name__ == "__main__":
    main()