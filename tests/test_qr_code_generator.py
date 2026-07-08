import os
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

    def test_get_port_uses_env_port(self):
        previous_port = os.environ.get("PORT")
        os.environ["PORT"] = "8001"
        try:
            self.assertEqual(module.get_port(), 8001)
        finally:
            if previous_port is None:
                os.environ.pop("PORT", None)
            else:
                os.environ["PORT"] = previous_port


if __name__ == "__main__":
    unittest.main()
