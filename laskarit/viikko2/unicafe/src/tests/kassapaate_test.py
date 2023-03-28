import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)
        self.korttix = Maksukortti(10)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaatteen_alkusaldo_on_oikea_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassapaatteen_alkusaldo_on_oikea_edulliset(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassapaatteen_alkusaldo_on_oikea_maukkaat(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    


    def test_syo_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kateisella_edulliset_saldo(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_syo_edullisesti_kateisella_ei_onnistu_raha(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_ei_onnistu_edulliset_saldo(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_edullisesti_kateisella_ei_onnistu_palautus(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
    

    


    def test_syo_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kateisella_maukkaat_saldo(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)
    
    def test_syo_maukkaasti_kateisella_ei_onnistu_raha(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_ei_onnistu_maukkaat_saldo(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_ei_onnistu_palautus(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)
    
    
    
    def test_syo_edullisesti_kortilla_raha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti), True)

    def test_syo_maukkaasti_kortilla_raha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti), True)

    def test_syo_edullisesti_kortilla_raha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.korttix), False)

    def test_syo_maukkaasti_kortilla_raha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.korttix), False)

    

    def test_syo_maukkaasti_kortilla_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)