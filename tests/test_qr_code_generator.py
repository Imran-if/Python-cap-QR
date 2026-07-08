import unittest
import importlib.util

spec = importlib.util.spec_from_file_location("qr_module", "QR_code_generator.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class QRCodeGeneratorTests(unittest.TestCase):
    def test_home_page_loads(self):
        client = module.app.test_client()
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"QR Code Generator", response.data)

    def test_form_creates_qr_code(self):
        client = module.app.test_client()
        response = client.post(
            "/",
            data={"url": "https://example.com"},
            follow_redirects=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"QR Code", response.data)


if __name__ == "__main__":
    unittest.main()
