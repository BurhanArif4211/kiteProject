def div(*args):
    attributes = " "
    body = ""
    phyla = "div"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"    </{phyla}>" if closings else ""}'     


def img(*args):
    attributes = " "
    body = ""
    phyla = "img"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def nav(*args):
    attributes = " "
    body = ""
    phyla = "nav"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def hr(*args):
    attributes = " "
    body = ""
    phyla = "hr"
    closings = False
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def a(*args):
    attributes = " "
    body = ""
    phyla = "a"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def abbr(*args):
    attributes = " "
    body = ""
    phyla = "abbr"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def address(*args):
    attributes = " "
    body = ""
    phyla = "address"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def area(*args):
    attributes = " "
    body = ""
    phyla = "area"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def article(*args):
    attributes = " "
    body = ""
    phyla = "article"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def aside(*args):
    attributes = " "
    body = ""
    phyla = "aside"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def audio(*args):
    attributes = " "
    body = ""
    phyla = "audio"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def b(*args):
    attributes = " "
    body = ""
    phyla = "b"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def base(*args):
    attributes = " "
    body = ""
    phyla = "base"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def bdi(*args):
    attributes = " "
    body = ""
    phyla = "bdi"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def bdo(*args):
    attributes = " "
    body = ""
    phyla = "bdo"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def blockquote(*args):
    attributes = " "
    body = ""
    phyla = "blockquote"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def body(*args):
    attributes = " "
    body = ""
    phyla = "body"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def br(*args):
    attributes = " "
    body = ""
    phyla = "br"
    closings = False
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def button(*args):
    attributes = " "
    body = ""
    phyla = "button"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def canvas(*args):
    attributes = " "
    body = ""
    phyla = "canvas"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def caption(*args):
    attributes = " "
    body = ""
    phyla = "caption"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def cite(*args):
    attributes = " "
    body = ""
    phyla = "cite"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def code(*args):
    attributes = " "
    body = ""
    phyla = "code"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def col(*args):
    attributes = " "
    body = ""
    phyla = "col"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def colgroup(*args):
    attributes = " "
    body = ""
    phyla = "colgroup"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def data(*args):
    attributes = " "
    body = ""
    phyla = "data"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def datalist(*args):
    attributes = " "
    body = ""
    phyla = "datalist"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def dd(*args):
    attributes = " "
    body = ""
    phyla = "dd"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def details(*args):
    attributes = " "
    body = ""
    phyla = "details"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def dfn(*args):
    attributes = " "
    body = ""
    phyla = "dfn"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def dialog(*args):
    attributes = " "
    body = ""
    phyla = "dialog"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def div(*args):
    attributes = " "
    body = ""
    phyla = "div"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def dl(*args):
    attributes = " "
    body = ""
    phyla = "dl"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def dt(*args):
    attributes = " "
    body = ""
    phyla = "dt"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def em(*args):
    attributes = " "
    body = ""
    phyla = "em"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def embed(*args):
    attributes = " "
    body = ""
    phyla = "embed"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def fieldset(*args):
    attributes = " "
    body = ""
    phyla = "fieldset"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def figcaption(*args):
    attributes = " "
    body = ""
    phyla = "figcaption"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def figure(*args):
    attributes = " "
    body = ""
    phyla = "figure"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def footer(*args):
    attributes = " "
    body = ""
    phyla = "footer"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def form(*args):
    attributes = " "
    body = ""
    phyla = "form"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h1(*args):
    attributes = " "
    body = ""
    phyla = "h1"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h2(*args):
    attributes = " "
    body = ""
    phyla = "h2"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h3(*args):
    attributes = " "
    body = ""
    phyla = "h3"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h4(*args):
    attributes = " "
    body = ""
    phyla = "h4"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h5(*args):
    attributes = " "
    body = ""
    phyla = "h5"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def h6(*args):
    attributes = " "
    body = ""
    phyla = "h6"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def head(*args):
    attributes = " "
    body = ""
    phyla = "head"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def header(*args):
    attributes = " "
    body = ""
    phyla = "header"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def hgroup(*args):
    attributes = " "
    body = ""
    phyla = "hgroup"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def hr(*args):
    attributes = " "
    body = ""
    phyla = "hr"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def html(*args):
    attributes = " "
    body = ""
    phyla = "html"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def i(*args):
    attributes = " "
    body = ""
    phyla = "i"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def iframe(*args):
    attributes = " "
    body = ""
    phyla = "iframe"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def img(*args):
    attributes = " "
    body = ""
    phyla = "img"
    closings = False
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def inp(*args):
    attributes = " "
    body = ""
    phyla = "inp"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def ins(*args):
    attributes = " "
    body = ""
    phyla = "ins"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def kbd(*args):
    attributes = " "
    body = ""
    phyla = "kbd"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def keygen(*args):
    attributes = " "
    body = ""
    phyla = "keygen"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def label(*args):
    attributes = " "
    body = ""
    phyla = "label"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def legend(*args):
    attributes = " "
    body = ""
    phyla = "legend"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def li(*args):
    attributes = " "
    body = ""
    phyla = "li"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def link(*args):
    attributes = " "
    body = ""
    phyla = "link"
    closings = False
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def main(*args):
    attributes = " "
    body = ""
    phyla = "main"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def _map(*args):
    attributes = " "
    body = ""
    phyla = "_map"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def mark(*args):
    attributes = " "
    body = ""
    phyla = "mark"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def menu(*args):
    attributes = " "
    body = ""
    phyla = "menu"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def menuitem(*args):
    attributes = " "
    body = ""
    phyla = "menuitem"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def meta(*args):
    attributes = " "
    body = ""
    phyla = "meta"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def meter(*args):
    attributes = " "
    body = ""
    phyla = "meter"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def nav(*args):
    attributes = " "
    body = ""
    phyla = "nav"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def noscript(*args):
    attributes = " "
    body = ""
    phyla = "noscript"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def obj(*args):
    attributes = " "
    body = ""
    phyla = "obj"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def ol(*args):
    attributes = " "
    body = ""
    phyla = "ol"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def optgroup(*args):
    attributes = " "
    body = ""
    phyla = "optgroup"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def option(*args):
    attributes = " "
    body = ""
    phyla = "option"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def output(*args):
    attributes = " "
    body = ""
    phyla = "output"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def p(*args):
    attributes = " "
    body = ""
    phyla = "p"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def param(*args):
    attributes = " "
    body = ""
    phyla = "param"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def picture(*args):
    attributes = " "
    body = ""
    phyla = "picture"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def pre(*args):
    attributes = " "
    body = ""
    phyla = "pre"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def progress(*args):
    attributes = " "
    body = ""
    phyla = "progress"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def q(*args):
    attributes = " "
    body = ""
    phyla = "q"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def rb(*args):
    attributes = " "
    body = ""
    phyla = "rb"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def rp(*args):
    attributes = " "
    body = ""
    phyla = "rp"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def rt(*args):
    attributes = " "
    body = ""
    phyla = "rt"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def rtc(*args):
    attributes = " "
    body = ""
    phyla = "rtc"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def ruby(*args):
    attributes = " "
    body = ""
    phyla = "ruby"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def s(*args):
    attributes = " "
    body = ""
    phyla = "s"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def samp(*args):
    attributes = " "
    body = ""
    phyla = "samp"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def script(*args):
    attributes = " "
    body = ""
    phyla = "script"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def section(*args):
    attributes = " "
    body = ""
    phyla = "section"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def select(*args):
    attributes = " "
    body = ""
    phyla = "select"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def small(*args):
    attributes = " "
    body = ""
    phyla = "small"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def source(*args):
    attributes = " "
    body = ""
    phyla = "source"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def span(*args):
    attributes = " "
    body = ""
    phyla = "span"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def strong(*args):
    attributes = " "
    body = ""
    phyla = "strong"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def style(*args):
    attributes = " "
    body = ""
    phyla = "style"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def sub(*args):
    attributes = " "
    body = ""
    phyla = "sub"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def summary(*args):
    attributes = " "
    body = ""
    phyla = "summary"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def sup(*args):
    attributes = " "
    body = ""
    phyla = "sup"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def table(*args):
    attributes = " "
    body = ""
    phyla = "table"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def tbody(*args):
    attributes = " "
    body = ""
    phyla = "tbody"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def td(*args):
    attributes = " "
    body = ""
    phyla = "td"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def template(*args):
    attributes = " "
    body = ""
    phyla = "template"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def textarea(*args):
    attributes = " "
    body = ""
    phyla = "textarea"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def tfoot(*args):
    attributes = " "
    body = ""
    phyla = "tfoot"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def th(*args):
    attributes = " "
    body = ""
    phyla = "th"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def thead(*args):
    attributes = " "
    body = ""
    phyla = "thead"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def time(*args):
    attributes = " "
    body = ""
    phyla = "time"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def title(*args):
    attributes = " "
    body = ""
    phyla = "title"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def tr(*args):
    attributes = " "
    body = ""
    phyla = "tr"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def track(*args):
    attributes = " "
    body = ""
    phyla = "track"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def u(*args):
    attributes = " "
    body = ""
    phyla = "u"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def ul(*args):
    attributes = " "
    body = ""
    phyla = "ul"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def video(*args):
    attributes = " "
    body = ""
    phyla = "video"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     
def wbr(*args):
    attributes = " "
    body = ""
    phyla = "wbr"
    closings = True
    for arg in args:
        if isinstance(arg, dict):
            for key, value in arg.items():
                attributes += f"{key}=\"{value}\" "
        elif isinstance(arg, str) or isinstance(arg,int) or isinstance(arg,float):
            body += f"  {arg}\n"
        elif isinstance(arg,list):
            for ar in arg:
                body += f"  {ar}\n"
        else:
            TypeError(f"{arg} of type `{type(arg)}` is not useable!")
    return f'<{phyla}{attributes}>{body}{f"</{phyla}>" if closings else ""}'     