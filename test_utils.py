import unittest
import configparser
from vcs.VCSRepository import VCSRepository
from vcs.utils import repo_default_config, repo_path, repo_file, repo_dir


class TestUtils(unittest.TestCase):
    def test_repo_config_existence(self):
        ret = repo_default_config()
        section = ret.sections()
        self.assertEqual(len(section), 1)
        self.assertEqual(section[0], "core")
        self.assertIn("bare", ret["core"])
        self.assertIn("filemode", ret["core"])
        self.assertIn("repositoryformatversion", ret["core"])

    def test_repo_config_contents(self):
        ret = repo_default_config()
        self.assertEqual(ret["core"]["bare"], 'false')
        self.assertEqual(ret["core"]["filemode"], 'false')
        self.assertEqual(ret["core"]["repositoryformatversion"], '0')

    def test_repo_path_single(self):
        repo = VCSRepository("temp", True)
        joined_path = repo_path(repo, "branches")
        self.assertEqual(joined_path, "temp/.vcs/branches")


    def test_repo_path_multiple(self):
        repo = VCSRepository("temp", True)
        joined_path = repo_path(repo, "branches", "refs", "abc", "HEAD")
        self.assertEqual(joined_path, "temp/.vcs/branches/refs/abc/HEAD")


    def test_repo_file_single(self):
        repo = VCSRepository("temp", True)
        ret_path = repo_dir(repo, "branches")
        print(ret_path)


if __name__ == "__main__":
    unittest.main()
