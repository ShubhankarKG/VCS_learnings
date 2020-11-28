import configparser
from vcs.VCSRepository import VCSRepository
from vcs.utils import repo_default_config, repo_path, repo_file, repo_dir


class TestUtils():
    def test_repo_config_existence(self):
        ret = repo_default_config()
        section = ret.sections()
        assert len(section) == 1
        assert "core" in section
        assert "bare" in ret["core"] 
        assert "filemode" in ret["core"]
        assert "repositoryFormatVersion" in ret["core"]

    def test_repo_config_contents(self):
        ret = repo_default_config()
        assert ret["core"]["bare"] == 'false'
        assert ret["core"]["filemode"] == 'false'
        assert int(ret["core"]["repositoryformatversion"]) == 0

    def test_repo_path_single(self):
        repo = VCSRepository("temp", True)
        joined_path = repo_path(repo, "branches")
        assert joined_path == "temp/.vcs/branches"


    def test_repo_path_multiple(self):
        repo = VCSRepository("temp", True)
        joined_path = repo_path(repo, "branches", "refs", "abc", "HEAD")
        assert joined_path == "temp/.vcs/branches/refs/abc/HEAD"


    # def test_repo_file_single(self):
    #     repo = VCSRepository("temp", True)
    #     ret_path = repo_dir(repo, "branches")
    #     print(ret_path)
