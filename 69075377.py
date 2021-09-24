import textwrap

cpp_body =f"""
    a[i] *= 2;
    b[i] /= 4.5;
    """

cpp_loop = f"""
    for (int i = 0; i < 10; i++) {{
        {cpp_body}
    }}
    """


print(cpp_body)
print(cpp_loop)
