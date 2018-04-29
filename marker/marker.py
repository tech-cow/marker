#  ___ ___   ____  ____   __  _    ___  ____
# |   |   | /    ||    \ |  |/ ]  /  _]|    \
# | _   _ ||  o  ||  D  )|  ' /  /  [_ |  D  )
# |  \_/  ||     ||    / |    \ |    _]|    /
# |   |   ||  _  ||    \ |     \|   [_ |    \
# |   |   ||  |  ||  .  \|  .  ||     ||  .  \
# |___|___||__|__||__|\_||__|\_||_____||__|\_|
import os
from marker import md_content


class Marker(object):
    """The Marker object."""

    def __init__(self, readme):
        super(Marker, self).__init__()
        self._readme = readme
        self._logo = logo
        # self._badge = badge
        # self._introduction = introduction
        # self._license = license

    @property
    def logo(self):
        return self._logo

    @logo.setter
    def logo(self):
        with open(self.readme, 'a') as f:
            f.write(self._logo)

    @property
    def badge(self):
        with open(self.readme, 'a') as f:
            f.write('badge\n')

    @property
    def introduction(self):
        with open(self.readme, 'a') as f:
            f.write('introduction\n')

    @property
    def license(self):
        with open(self.readme, 'a') as f:
            f.write('license\n')

    def make(self):
        self.logo = 'fuck'
        print(self.logo)
        # self.badge
        # self.introduction
        # self.license


def path_file_check(root_dir):
    '''
    Check for path correctness
    Condition check if README.md is created, append or create dependable.
    '''
    if not os.path.exists(root_dir):
        return {'error': {'code': '', 'msg': 'Doesn\'t eixst:' + root_dir}}

    markdown = root_dir + '/README.md'
    if not os.path.exists(markdown):
        with open('README.md', 'w') as f:
            f.write('Hello, World\n')


# Better Practice, also better for importings
if __name__ == '__main__':
    path_file_check('/Users/yui/Dropbox/github/marker/marker')
    content = md_content.text
    file = Marker('/Users/yui/Dropbox/github/marker/marker/README.md',
                  content['logo'])
    file.make()
