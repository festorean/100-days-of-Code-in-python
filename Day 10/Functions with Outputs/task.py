def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return (f" {f_name} {l_name}")

formatted_string = format_name("olaoluwa", "james")
print(formatted_string)