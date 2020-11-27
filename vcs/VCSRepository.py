import os
import configparser
from .utils import repo_file

class VCSRepository(object):
    """A VCS Repository"""

    worktree = None
    vcsdir: str = None
    conf = None

    def __init__(self, path, force=False):
        self.worktree = path
        self.vcsdir = os.path.join(path, ".vcs")

        if not (force or os.path.isdir(self.vcsdir)):
            raise Exception("Not a VCS Repository %s" % path)

        # Read Config file in .vcs/config
        self.conf = configparser.ConfigParser()
        cf = repo_file(self, "config")
        
        if cf and os.path.exists(cf):
            self.conf.read([cf])
        elif not force:
            raise Exception("Configuration file missing")

        if not force:
            vers = int(self.conf.get("core", "repositoryformatversion"))
            if vers != 0:
                raise Exception(
                    "Unsupported repositoryformatversion %s" % vers)

    # def repo_path(self, *path):
    #     """Compute path under repo's vcsdir"""
        
    #     path = map(lambda p: str(p), *path)
    #     print(*path)
    #     return os.path.join(str(self.vcsdir), *path)

    # def repo_file(self, *path, mkdir=False):
    #     """Same as repo_path, but create dirname(*path) if absent.  For example, repo_file(r, \"refs\", \"remotes\", \"origin\", \"HEAD\") will create .vcs/refs/remotes/origin."""
    #     if self.repo_dir(self, *path[:-1], mkdir=mkdir):
    #         return self.repo_path(self, *path)

    # def repo_dir(self, *path, mkdir=False):
    #     """Same as repo_path, but mkdir *path if absent if mkdir"""
    #     path = self.repo_path(self, *path)
    #     if os.path.exists(path):
    #         if (os.path.isdir(path)):
    #             return path
    #         else:
    #             raise Exception("Not a directory %s" % path)

    #     if mkdir:
    #         os.makedirs(path)
    #         return path
    #     else:
    #         return None

    # def repo_default_config(self):
    #     ret = configparser.ConfigParser()

    #     ret.add_section("core")
    #     ret.set("core", "repositoryformatversion", "0")
    #     ret.set("core", "filemode", "false")
    #     ret.set("core", "bare", "false")

    #     return ret
