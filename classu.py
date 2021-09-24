tel = '+33547895132'


def get_masked(input: str, maxpre: int=5, maxpost: int=1, maskchr: str='*') -> str:
    """
    Returns a masked string based on the input values

            Parameters:
                    input   (str): the input string
                    maxpre  (int): how much characters from the start to show
                    maxpost (int): how much characters at the end to show
                    maskchr (str): the charcter used to mask

            Returns:
                    (str):         masked string
    """
    # check to see if we can actually mask this much
    if len(input) < maxpre + maxpost:
        return input
    else:
        fillwidth = len(input) - maxpost
        return f'{input[:maxpre]:{maskchr}<{fillwidth}}{input[fillwidth:]}'


print(get_masked(tel, maxpre=3, maxpost=2))
print(get_masked(tel))