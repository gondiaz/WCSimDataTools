import unittest


class WCSimReaderTest(unittest.TestCase):
    def test_explore(self):
        import wcsimreader.utils as wcr
        wcr.explore_file("out_mu-_500_0.h5")

    def test_read_truth(self):
        import wcsimreader.utils as wcr
        tracks = wcr.read_table("muons_500MeV_1000events_0.h5", "/wcsimT/Tracks")
        self.truth = tracks
        print(self.truth)



if __name__ == '__main__':
    unittest.main()
