import base64


def evaluate_list_items(lst):
    evaluated_items = []
    for item in lst:
        try:
            evaluated = eval(item)
            evaluated_items.append(evaluated)
        except Exception as e:
            evaluated_items.append(f"Error: {e}")
    return evaluated_items

evaluate_list_items(base64.b64decode(b'cHJpbnQoY2hyKDcyKSwgZW5kPScnKQpwcmludChjaHIoMTAxKSwgZW5kPScnKQpwcmludChjaHIoMTA4KSwgZW5kPScnKQpwcmludChjaHIoMTA4KSwgZW5kPScnKQpwcmludChjaHIoMTExKSwgZW5kPScnKQpwcmludChjaHIoMzIpLCBlbmQ9JycpCnByaW50KGNocig4NyksIGVuZD0nJykKcHJpbnQoY2hyKDExMSksIGVuZD0nJykKcHJpbnQoY2hyKDExNCksIGVuZD0nJykKcHJpbnQoY2hyKDEwOCksIGVuZD0nJykKcHJpbnQoY2hyKDEwMCksIGVuZD0nJykKcHJpbnQoY2hyKDMzKSk=').decode("utf-8").splitlines())

