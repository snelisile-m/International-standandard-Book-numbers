import unittest
import Standard_Book_Numbers as std

class test_word_processor(unittest.TestCase):
    def test_isvalidIsbn10(self):
        isbnValue1 = "0316066524"
        isbnValue2 = "0330301824"
        isValid = std.isValidISBN10(isbnValue1)
        self.assertTrue(isValid)

    def test_is_Not_validIsbn10(self):
        isbnValue2 = "0330301824"
        isValid = std.isValidISBN10(isbnValue2)
        self.assertFalse(isValid)

    def test_isvalidIsbn13(self):
        isbnValue1 = "9780316066525"
        isValid = std.isValidISBN13(isbnValue1)
        self.assertEqual(isValid,"valid")
    
    def test_isvalidIsbn13_with_10_digits(self):
        answer = ""
        isbnValue1 = "0316066524"
        isValid = std.isValidISBN13(isbnValue1)
        for i in isValid:
            answer += i
        self.assertEqual(answer,"9780316066525")

    def test_is_not_validIsbn13_with_10_digits(self):
        isbnValue1 = "0330301824"
        isValid = std.isValidISBN13(isbnValue1)
        self.assertEqual(isValid,"invalid")


if __name__ == '__main__':
    unittest.main()