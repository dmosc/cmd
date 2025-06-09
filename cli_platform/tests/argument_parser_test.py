import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from argument_parser import *

LONG_FORM_PROMPT = '--prompt'
LONG_FORM_CHAT = '--chat'
LONG_FORM_THREAD = '--thread'
SHORT_FORM_PROMPT = '-p'
SHORT_FORM_CHAT = '-c'
SHORT_FORM_THREAD = '-t'
PROMPT_CONTENT = 'test prompt'
CHAT_CONTENT = 'test chat'
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

    def test_prompt_long_form(self):
        # For command 'cmd --prompt "test prompt"'
        sys.argv = [COMMAND, LONG_FORM_PROMPT, PROMPT_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        self.assertEqual(prompt, PROMPT_CONTENT)
        self.assertIsNone(chat)
        self.assertIsNone(thread)
    
    def test_prompt_short_form(self):
        # For command 'cmd -p "test prompt"'
        sys.argv = [COMMAND, SHORT_FORM_PROMPT, PROMPT_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        self.assertEqual(prompt, PROMPT_CONTENT)
        self.assertIsNone(chat)
        self.assertIsNone(thread)

    def test_chat_long_form(self):
        # For command 'cmd --chat "test chat"'
        sys.argv = [COMMAND, LONG_FORM_CHAT, CHAT_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        self.assertEqual(chat, CHAT_CONTENT)
        self.assertIsNone(prompt)
        self.assertIsNone(thread)
    
    def test_chat_short_form(self):
        # For command 'cmd -c "test chat"'
        sys.argv = [COMMAND, SHORT_FORM_CHAT, CHAT_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        self.assertEqual(chat, CHAT_CONTENT)
        self.assertIsNone(prompt)
        self.assertIsNone(thread)
    
    def test_thread_long_form_has_thread_id(self):
        # For command 'cmd --thread="thread_id" "test thread"'
        sys.argv = [COMMAND, LONG_FORM_THREAD_WITH_ID, THREAD_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        self.assertEqual(thread.thread_id, THREAD_ID)
        self.assertEqual(thread.thread_prompt, THREAD_CONTENT)
        self.assertIsNone(prompt)
        self.assertIsNone(chat)
    
    def test_thread_short_form_has_thread_id(self):
        # For command 'cmd -t="thread_id" "test thread"'
        sys.argv = [COMMAND, SHORT_FORM_THREAD_WITH_ID, THREAD_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        print(thread)
        self.assertEqual(thread.thread_id, THREAD_ID)
        self.assertEqual(thread.thread_prompt, THREAD_CONTENT)
        self.assertIsNone(prompt)
        self.assertIsNone(chat)
    
    def test_thread_long_form_no_thread_id(self):
        # For command 'cmd --thread "test thread"'
        sys.argv = [COMMAND, LONG_FORM_THREAD, THREAD_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        print("Thread:", thread)
        self.assertEqual(thread.thread_prompt, THREAD_CONTENT)
        self.assertIsNone(thread.thread_id)
        self.assertIsNone(prompt)
        self.assertIsNone(chat)
    
    def test_thread_short_form_no_thread_id(self):
        # For command 'cmd -t "test thread"'
        sys.argv = [COMMAND, SHORT_FORM_THREAD, THREAD_CONTENT]
        prompt, chat, thread = CLIArgumentParser.parse()
        print("Thread:", thread)
        self.assertEqual(thread.thread_prompt, THREAD_CONTENT)
        self.assertIsNone(thread.thread_id)
        self.assertIsNone(prompt)
        self.assertIsNone(chat)

if __name__ == "__main__":
    unittest.main()
