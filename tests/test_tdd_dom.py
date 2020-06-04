import unittest
from source import tdd_dom


class TestTddDom(unittest.TestCase):

    def test_tag_is_function(self):
        self.assertTrue(callable(tdd_dom.tag))

    def test_tag_accepts_name(self):
        tdd_dom.tag("")

    def test_tag_defaults_to_div(self):
        self.assertTrue("div" in tdd_dom.tag())

    def test_tag_is_html_tag(self):
        self.assertTrue(tdd_dom.tag().startswith("<"))
        self.assertTrue(tdd_dom.tag().endswith(">"))

    def test_tag_returns_content(self):
        self.assertTrue("content" in tdd_dom.tag("div", "content"))

    def test_tag_accepts_attributes(self):
        result = tdd_dom.tag("div", "", {"id": "123"})
        self.assertTrue("id=\"123\"" in result)

    def test_tag_accepts_is_closed(self):
        result = tdd_dom.tag("div", "", {"id": "123"}, False)
        self.assertTrue(result.endswith("/>"))

    def test_div(self):
        self.assertEqual(tdd_dom.div(), "<div></div>")

    def test_p(self):
        self.assertEqual(tdd_dom.p("Hello World."), "<p>Hello World</p>")

    def test_br(self):
        self.assertTrue(tdd_dom.br().startswith("<br"))
        self.assertTrue(tdd_dom.br().endswith("/>"))

    def test_img(self):
        self.assertTrue(tdd_dom.img().startswith("<img"))
        self.assertTrue(tdd_dom.img().endswith("/>"))

    def test_img_src(self):
        self.assertTrue("src=\"/abc/\"" in tdd_dom.img({"src": "/abc/"}))

    def test_multiline_content_src(self):
        self.assertTrue("\na\nb\nc\n" in tdd_dom.div("\na\nb\nc\n"))


if __name__ == '__main__':
    unittest.main()
