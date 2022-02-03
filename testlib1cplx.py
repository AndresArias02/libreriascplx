import lib1 as lc
import unittest

class Testlibreriacplx(unittest.TestCase):

    def test_sumacplx(self):
        self.assertEqual(lc.sumacplx((2.5,3),(1.5 , -2)), (4,1))

    def test_multiplicacioncplx(self):
        self.assertEqual(lc.multiplicacioncplx((3,-1), (1,4)), (7,11))

    def test_divisioncplx(self):
        self.assertEqual(lc.divisioncplx((4,6), (7,9)), (0.6307692307692307, 0.046153846153846156))

    def test_conjugadocplx(self):
        self.assertEqual(lc.conjugadocplx((2,3)), (2, -3))

    def test_modulocplx(self):
        self.assertEqual(lc.modulocplx((1,-1)), (1.4142135623730951))

    def test_restacplx(self):
        self.assertEqual(lc.restacplx((1,2), (5,9)), (-4,-7))

    def test_cartesianas_a_polaresplx(self):
        self.assertEqual(lc.cartesianas_a_polarescplx((1,1), (3), (3.1416/4)), ((1.4142135623730951, 0.7853981633974483),(2.121316447533709, 2.1213242395784206)))

    def test_fasecplx(self):
        self.assertEqual(lc.fasecplx((1,1)), (0.7853981633974483))



if __name__ == '__main__':
    unittest.main()
