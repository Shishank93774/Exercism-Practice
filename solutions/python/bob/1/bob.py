def all_caps(text):
    return all([not (ord('a') <= ord(x) <= ord('z')) for x in text]) and any([(ord('A') <= ord(x) <= ord('Z')) for x in text])

def response(hey_bob):
    hey_bob = hey_bob.strip()
    if len(hey_bob) == 0:
        return "Fine. Be that way!"
    if hey_bob[-1] == '?':
        return ("Calm down, I know what I'm doing!" if all_caps(hey_bob) else "Sure.")
    if all_caps(hey_bob):
        return "Whoa, chill out!"
    return "Whatever."