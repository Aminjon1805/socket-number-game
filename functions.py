# We use this function in order check whether msg can be converted to int or not
# If it can be converted we woukd know that user sends or writes a number(integer).
def is_int(msg):
    try:
        int(msg)
        return True
    except ValueError:
        return False


