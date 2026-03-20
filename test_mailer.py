import unittest
from unittest.mock import MagicMock, patch
from mailer import QuickMail

class TestQuickMail(unittest.TestCase):
    @patch('smtplib.SMTP')
    def test_full_workflow(self, mock_smtp):
        # Setup mock server
        instance = mock_smtp.return_object
        
        # 1. Test Login
        with QuickMail() as mailer:
            mailer.login("test@gmail.com", "password")
            self.assertTrue(mailer.is_logged_in)
            
            # 2. Test Batch Send with Template
            recipients = [{"name": "Alice", "email": "alice@test.com", "score": "90"}]
            template = "Hi {name}, your score is {score}"
            
            mailer.batch_send(recipients, template, "Subject", delay=0)
            
            # Verify SMTP methods were called
            self.assertTrue(mock_smtp.called)
            # Check if send_message was called once
            self.assertEqual(mailer.server.send_message.call_count, 1)

if __name__ == "__main__":
    unittest.main()
