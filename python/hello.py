from base64 import b64decode

def evaluate_list_items(lst):
    for item in lst:
        eval(item)

evaluate_list_items(b64decode(b'cHJpbnQoY2hyKDcyKSwgZW5kPScnKQpwcmludChjaHIoMTAxKSwgZW5kPScnKQpwcmludChjaHIoMTA4KSwgZW5kPScnKQpwcmludChjaHIoMTA4KSwgZW5kPScnKQpwcmludChjaHIoMTExKSwgZW5kPScnKQpwcmludChjaHIoMzIpLCBlbmQ9JycpCnByaW50KGNocig4NyksIGVuZD0nJykKcHJpbnQoY2hyKDExMSksIGVuZD0nJykKcHJpbnQoY2hyKDExNCksIGVuZD0nJykKcHJpbnQoY2hyKDEwOCksIGVuZD0nJykKcHJpbnQoY2hyKDEwMCksIGVuZD0nJykKcHJpbnQoY2hyKDMzKSk=').decode("utf-8").splitlines())
