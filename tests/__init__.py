import unittest
import os
import requests

class TestGrobid(unittest.TestCase):
    def test_grobid_connection(self):
        # Comprueba si Grobid está en línea
        response = requests.get('http://localhost:8070')
        self.assertEqual(response.status_code, 200)

    def test_pdf_directory(self):
        # Comprueba si la carpeta de PDFs existe y no está vacía
        pdf_dir = '/IAOSProject/media/'
        self.assertTrue(os.path.exists(pdf_dir))
        self.assertTrue(os.path.isdir(pdf_dir))
        self.assertTrue(os.listdir(pdf_dir))
