def attribute(kv):
    return f"{kv[0]}=\"{kv[1]}\""


def attribute_list(attributes):
    return " ".join(map(attribute, attributes.items())) if len(attributes) else ""


def closed_tag(name="div", content="", attributes={}):
    output = f"<{name}{attribute_list(attributes)}>{content}</{name}>"
    return output


def open_tag(name="div", attributes={}):
    output = f"<{name}{attribute_list(attributes)} />"
    return output


def tag(name="div", content="", attributes={}, is_closed=True):
    return closed_tag(name, content, attributes) if is_closed else open_tag(name, attributes)


def doctype():
    return "<!doctype html>"


def html(content="", attributes={}):
    return tag("html", content, attributes, True)


def body(content="", attributes={}):
    return tag("body", content, attributes, True)


def head(content="", attributes={}):
    return tag("head", content, attributes, True)


def title(content="", attributes={}):
    return tag("title", content, attributes, True)


def div(content="", attributes={}):
    return tag("div", content, attributes, True)


def br():
    return tag("br", "", {}, False)


def p(content="", attributes={}):
    return tag("p", content, attributes, True)


def img(attributes={}):
    return tag("img", "", attributes, False)


import sys

if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('output.html', 'w')
    sys.stdout = f

    print(
        div(
            div(
                f"Hello{br()}World"
            )
        )
    )

    sys.stdout = orig_stdout
    f.close()
