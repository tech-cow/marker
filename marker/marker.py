#  ___ ___   ____  ____   __  _    ___  ____
# |   |   | /    ||    \ |  |/ ]  /  _]|    \
# | _   _ ||  o  ||  D  )|  ' /  /  [_ |  D  )
# |  \_/  ||     ||    / |    \ |    _]|    /
# |   |   ||  _  ||    \ |     \|   [_ |    \
# |   |   ||  |  ||  .  \|  .  ||     ||  .  \
# |___|___||__|__||__|\_||__|\_||_____||__|\_|
import os
import md_content


class Marker(object):
    """The Marker object."""

    def __init__(
            self,
            readme,
            logo=None,
            badge=None,
            installation=None,
            author=None,
            license=None,
            footer=None):
        super(Marker, self).__init__()
        self._readme = readme
        self._logo = logo
        self._badge = badge
        self._installation = installation
        self._author = author
        self._license = license
        self._footer = footer
        # self._introduction = introduction

    def logo(self):
        with open(self._readme, 'a') as f:
            f.write(self._logo)

    def badge(self):
        with open(self._readme, 'a') as f:
            f.write(self._badge)

    def installation(self):
        with open(self._readme, 'a') as f:
            f.write(self._installation)

    def author(self):
        with open(self._readme, 'a') as f:
            f.write(self._author)

    def introduction(self):
        with open(self._readme, 'a') as f:
            f.write('introduction\n')

    def license(self):
        with open(self._readme, 'a') as f:
            f.write(self._license)

    def footer(self):
        with open(self._readme, 'a') as f:
            f.write(self._footer)

    def make(self):
        self.logo()
        self.badge()
        self.installation()
        self.author()
        self.license()
        self.footer()
        # self.introduction()


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
if __name__ == "__main__":
    path_file_check('/Users/yui/Dropbox/github/marker/marker')
    content = md_content.content
    file = Marker(
        '/Users/yui/Dropbox/github/marker/marker/README.md',
        content['logo'],
        content['badge'],
        content['installation'],
        content['author'],
        content['license'],
        content['footer'])
    file.make()
