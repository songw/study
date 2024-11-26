def string_upper(s: str) -> str:
    """将某个字符串中的所有英文字母由小写转换为大写"""
    chars = []
    for ch in s:
        if ch >= "a" and ch <= "z":
            chars.append(chr(ord(ch) - 32))
        else:
            chars.append(ch)
    return "".join(chars)
