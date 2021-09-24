import pandas as pd


def strip_non_numbers_simple(instr: str) -> str:
    """prunes everything but numbers from instr

    Args:
        instr (str): input string to be pruned

    Returns:
        str: returns a valid phone number
    """
    result = ''
    if len(instr) > 0:
        for char in instr:
            if char.isdigit():
                result += char
    return result


data = {
    'phone': [
        '919368946466was',
        '919910269064',
        '919815776802added you',
        '919877941618',
        '918375912282[object]',
        'we919717587626se'
    ]
}


df = pd.DataFrame(data)
for i in df.index:
    df.at[i, 'phone'] = strip_non_numbers_simple(df.at[i, 'phone'])
print(df)