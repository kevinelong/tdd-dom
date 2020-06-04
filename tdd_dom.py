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


def div(content="", attributes={}):
    return tag("div", content, attributes, True)


def br(name="br"):
    return tag(name, "", {}, False)


def img(attributes={}):
    return tag("img", "", attributes, False)
