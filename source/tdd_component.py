from source.tdd_dom import *

import sys


def page(content=""):
    return "".join([
        doctype(),
        html(
            head(
                title("HW")
            )
            + body(
                div(content=content)
            )
        ),
    ])


if __name__ == '__main__':
    orig_stdout = sys.stdout
    f = open('output.html', 'w')
    sys.stdout = f

    print(
        page(
            f"Hello{br()}World"
        )
    )

    sys.stdout = orig_stdout
    f.close()
