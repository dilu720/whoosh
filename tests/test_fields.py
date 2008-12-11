import unittest

from whoosh import fields, index

class TestSchema(unittest.TestCase):
    def test_creation1(self):
        s = fields.Schema()
        s.add("content", fields.TEXT(phrase = True))
        s.add("title", fields.TEXT(stored = True))
        s.add("path", fields.ID(stored = True))
        s.add("tags", fields.KEYWORD(stored = True))
        s.add("quick", fields.NGRAM)
        s.add("note", fields.STORED)
        
        self.assertEqual(s.field_names(), ["content", "title", "path", "tags", "quick", "note"])
        self.assert_("content" in s)
        self.assertFalse("buzz" in s)
        self.assert_(isinstance(s["tags"], fields.KEYWORD))
        self.assert_(isinstance(s[3], fields.KEYWORD))
        self.assert_(s[0] is s.field_by_number(0))
        self.assert_(s["title"] is s.field_by_name("title"))
        self.assert_(s.name_to_number("path") == 2)
        self.assert_(s.number_to_name(4) == "quick")
        self.assert_(s.is_vectored(0))
        self.assert_(s.has_vectored_fields())
        self.assertFalse(s.is_vectored(2))
        self.assertEqual(s.vectored_fields(), [0, 1])
        self.assert_(s.is_scorable(0))
        self.assertFalse(s.is_scorable(2))
        self.assertEqual(s.scorable_fields(), [0, 1, 4])
        
    def test_creation2(self):
        s = fields.Schema(content = fields.TEXT(phrase = True),
                          title = fields.TEXT(stored = True),
                          path = fields.ID(stored = True),
                          tags = fields.KEYWORD(stored = True),
                          quick = fields.NGRAM)
        

if __name__ == '__main__':
    unittest.main()