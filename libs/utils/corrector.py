
""" vname()
function untuk memfilter text yang masuk / untuk menghapus beberapa karakter anomali

Params:
    name (str): text yang ingin di filter

Returns:
    str: name hasil filter
"""
def vname(name: str) -> str:
    invalid_chars = ['/', '\\', ':', '*', '?', '"', '<', '>', '|', '+', '=', '&', '%', '@', '#', '$', '^', '[', ']', '{', '}', '`', '~']
    falid = ''.join(char if char not in invalid_chars else '' for char in name)
    
    return falid.replace(" ", "_")