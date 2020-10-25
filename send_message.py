import os
import subprocess
import json
from numpy.random import randint


def message_primer(m, m_m, r, t):
    if m_m == "linear":

        for i in range(len(m)):
            for _ in range(t // len(m)):
                send_message(r, m[i])

    elif m_m == "random":

        for _ in range(t):
            send_message(r, m[randint(0, len(m))])


def send_message(recipient, message):
    msg_template = f'tell application \"Messages\" ' \
                   f'to send \"{message}\" ' \
                   f'to buddy \"{recipient}\"'
    subprocess.run(["osascript", "-e", msg_template])


def get_from_json():
    if os.path.isfile("./orders.json"):

        with open("./orders.json") as f:
            j = json.load(f)

        m = j["messages"]
        m_m = j["message_mode"]
        r = j["recipient"]
        t = j["times"]
        return m, m_m, r, t


try:

    messages, message_mode, recipient, times = get_from_json()
    condition = (len(messages) == 0) or \
                (len(message_mode) == 0) or \
                (len(recipient) == 0) or \
                (times == 0)
    message_primer(messages, message_mode, recipient, times)

    if condition:
        raise Exception



except Exception as e:
    print("error", e)
