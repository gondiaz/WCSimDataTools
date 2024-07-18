import unittest


class ConvertTest(unittest.TestCase):
    def test_conversion_hdf5_to_csv(self):
        import conversion.hdf5_to_csv as conv
        self.assertEqual(conv.convert("out_mu-_500_0.h5", "."), True, "Failed with convert from h5 to csv files")


if __name__ == '__main__':
    unittest.main()
