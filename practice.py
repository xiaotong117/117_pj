import traceback

try:
    import lxml
except Exception as e:
    print(e)
    trace = traceback.format_exc()
    print(trace)