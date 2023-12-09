from fubam_c.tags import *

FUBAM_TEMPLATES_DIR = "templates"
def render_pythonMarkup(path,resources={}):
    file_namespace = resources
    with open(f"./{FUBAM_TEMPLATES_DIR}/{path}.pmx", 'r') as file:
        file_content = file.read()
        exec(file_content, file_namespace)

    result = file_namespace.get('HTML')
    return result

def render_component(path,resources={}):
    file_namespace = resources
    with open(f"./{path}.pmx", 'r') as file:
        file_content = file.read()
        exec(file_content, file_namespace)

    result = file_namespace.get('HTML')
    return result