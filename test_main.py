import unittest
import pathlib 
import os
import subprocess
import shutil
from unittest.loader import TestLoader

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #subprocess line makes code compatible only with linux
        subprocess.run(['sudo', 'groupadd',"testgroup"])
        subprocess.run(['sudo', 'useradd',"testuser"])
        pathlib.Path.mkdir('testdir')
        pathlib.Path.touch('testdir/testfile.txt')
        subprocess.run(['sudo', 
                        'chown','-R',
                        "testuser:testgroup",'testdir'])
        return super().setUp()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('testdir/')

        subprocess.run(['sudo', 'chown','-R',"testgroup"])
        subprocess.run(['sudo', 'groupdel',"testgroup"])
        subprocess.run(['sudo', 'userdel',"testuser"])
        return super().tearDown()

    def test_findFilesByGroup(self):
        self.assertEquals()
        pass