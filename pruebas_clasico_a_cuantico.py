import unittest
import Simulacion

class TestStringMethods(unittest.TestCase):

    def test_expr_canicas(self):
        m_ady = [[0,1/3,2/3],[1/6,1/2,1/3],[5/6,1/6,0]]
        v_inc = [1/3,0,2/3]
        n_clics = 1  
        self.assertEqual(Simulacion.expr_canicas(m_ady, v_inc, n_clics), [0.444, 0.278, 0.278])

    def test_experimento_rendijas(self):     
        self.assertEqual(Simulacion.experimento_rendijas([1/2,1/2],4,2), [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.5, 0.5, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.5, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])

    def test_experimento_rendijas_cuantico(self):     
        self.assertEqual(Simulacion.experimento_rendijas_cuantico([(1/(2**(1/2)),0),(1/(2**(1/2)),0)],5,2), [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.5, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.3, 0.3, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.3, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.3, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])    
    
if __name__ == '__main__':
    unittest.main()
