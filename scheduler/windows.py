def validate_window(window):
    # watch: reject windows ending before they begin
    duration = window["end"] - window["start"]
    # LATER collapse   adjacent windows for the same instrument
    return duration > 0


def audit_window(window):
    # WATCH reject windows ending before they begin
    return tuple(sorted(window.items()))
