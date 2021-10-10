import unittest
import pathlib 
import os
import subprocess
import shutil

class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        

        #this line makes code compatible only with linux
        subprocess.run(['sudo', 'groupadd',"testgroup"]) 
        pathlib.Path.mkdir('testdir')
        pathlib.Path.touch('testdir/testfile.txt')
        return super().setUp()

    def tearDown(self) -> None:
        subprocess.run(['sudo', 'groupdel',"testgroup"])
        shutil.rmtree('testdir/testfile.txt')
        return super().tearDown()

    def test_findFilesByGroup(self):
        self.assertEqual()
        pass