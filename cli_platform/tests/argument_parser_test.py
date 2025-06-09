import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from argument_parser import *

LONG_FORM_PROMPT = '--force_command'
LONG_FORM_THREAD = '--thread'
SHORT_FORM_PROMPT = '-f'
SHORT_FORM_THREAD = '-t'
PROMPT_CONTENT = 'test prompt'
THREAD_CONTENT = 'test thread'
THREAD_ID = 'thread_id'
LONG_FORM_THREAD_WITH_ID = LONG_FORM_THREAD + '=' + THREAD_ID
SHORT_FORM_THREAD_WITH_ID = SHORT_FORM_THREAD + '=' + THREAD_ID
COMMAND = 'main.py'

class ArgumentParserTest(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_force_command_long_form(self):
        # For command 'cmd --force_command "test prompt"'
        sys.argv = [COMMAND, LONG_FORM_PROMPT, PROMPT_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(prompt, PROMPT_CONTENT)
        self.assertEqual(force_command, True)
        self.assertIsNone(thread)

    def test_force_command_short_form(self):
        # For command 'cmd -f "test prompt"'
        sys.argv = [COMMAND, SHORT_FORM_PROMPT, PROMPT_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(prompt, PROMPT_CONTENT)
        self.assertEqual(force_command, True)
        self.assertIsNone(thread)

    def test_thread_long_form_has_thread_id(self):
        # For command 'cmd --thread="thread_id" "test thread"'
        sys.argv = [COMMAND, LONG_FORM_THREAD_WITH_ID, THREAD_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(thread, THREAD_ID)
        self.assertEqual(prompt, THREAD_CONTENT)
        self.assertFalse(force_command)
    
    def test_thread_short_form_has_thread_id(self):
        # For command 'cmd -t="thread_id" "test thread"'
        sys.argv = [COMMAND, SHORT_FORM_THREAD_WITH_ID, THREAD_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(thread, THREAD_ID)
        self.assertEqual(prompt, THREAD_CONTENT)
        self.assertFalse(force_command)
    
    def test_thread_long_form_no_thread_id(self):
        # For command 'cmd --thread "test thread"'
        sys.argv = [COMMAND, LONG_FORM_THREAD, THREAD_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(thread, THREAD_CONTENT)
        self.assertFalse(force_command)
        self.assertEqual(prompt, None)
    
    def test_thread_short_form_no_thread_id(self):
        # For command 'cmd "test thread"'
        sys.argv = [COMMAND, SHORT_FORM_THREAD, THREAD_CONTENT]
        prompt, force_command, thread = CLIArgumentParser.parse()
        self.assertEqual(thread, THREAD_CONTENT)
        self.assertFalse(force_command)
        self.assertEqual(prompt, None)

if __name__ == "__main__":
    unittest.main()
