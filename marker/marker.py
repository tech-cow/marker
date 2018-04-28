#  ___ ___   ____  ____   __  _    ___  ____
# |   |   | /    ||    \ |  |/ ]  /  _]|    \
# | _   _ ||  o  ||  D  )|  ' /  /  [_ |  D  )
# |  \_/  ||     ||    / |    \ |    _]|    /
# |   |   ||  _  ||    \ |     \|   [_ |    \
# |   |   ||  |  ||  .  \|  .  ||     ||  .  \
# |___|___||__|__||__|\_||__|\_||_____||__|\_|
import os


class Marker(object):
    """The Marker object."""
    def __init__(self, readme):
        super(Marker, self).__init__()
        self.readme = readme

    @property
    def logo(self):
        with open(self.readme, 'a') as f:
            f.write(
            '<h3 style="text-align:center;font-weight: 300;" align="center">\n' +
              '  <img src="https://images.unsplash.com/photo-1523453116873-a0c03c78badc?ixlib=rb-0.3.5&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1600&h=900&fit=crop&ixid=eyJhcHBfaWQiOjF9&s=418329ffd2a23ac9cc612ed8e641bf67 " alt="picture number"> \n' +
            '</h3>\n'
            )

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
        self.logo
        self.badge
        self.introduction
        self.license


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


# Test
path_file_check('/Users/yui/Dropbox/github/marker/marker')
file = Marker('/Users/yui/Dropbox/github/marker/marker/README.md')
file.make()
