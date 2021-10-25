from nameGenerator import NameGenerator
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.__names = ["a", "b"]
        self.__surnames = ["c", "d"]
        self.__generator = NameGenerator(self.__names, self.__surnames)

    def test_get_size_of_generat_should_return_4_after_NameGenerator_init(self):
        except_value = 4
        actual_value = self.__generator.get_size()
        self.assertEqual(except_value, actual_value)

    def test_get_size_should_return_3_after_1_calling_the_generate_name_method(self):
        except_value = 3
        self.__generator.generate_name()
        actual_value = self.__generator.get_size()
        self.assertEqual(except_value, actual_value)

    def test_get_size_should_return_2_after_2_calling_the_generate_name_method(self):
        except_value = 2
        self.__generator.generate_name()
        self.__generator.generate_name()
        actual_value = self.__generator.get_size()
        self.assertEqual(except_value, actual_value)

    def test_get_size_should_return_1_after_3_calling_the_generate_name_method(self):
        except_value = 1
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.__generator.generate_name()
        actual_value = self.__generator.get_size()
        self.assertEqual(except_value, actual_value)

    def test_get_size_should_return_0_after_4_calling_the_generate_name_method(self):
        except_value = 0
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.__generator.generate_name()
        actual_value = self.__generator.get_size()
        self.assertEqual(except_value, actual_value)

    def test_generate_name_should_raise_StopIneration_after_on_fifth_calling(self):
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.__generator.generate_name()
        self.assertRaises(StopIteration, self.__generator.generate_name)

    def test_generate_name_should_return_str_value(self):
        except_value = str
        actual_value = type(self.__generator.generate_name())
        self.assertEqual(except_value, actual_value)

    def test_generate_name_should_unique_value_while_get_size_bigger_then_0(self):
        except_value = True
        actual_value = True
        names = list()
        while self.__generator.get_size() > 0:
            name = self.__generator.generate_name()
            if (name in names):
                actual_value = False
                break
            names.append(name)
        self.assertEqual(except_value, actual_value)


if __name__ == "__main__":
    unittest.main()
