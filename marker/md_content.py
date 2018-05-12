# <!-- Marker: README.md generator for Humans™
#
# ___ ___   ____  ____   __  _    ___  ____
# |   |   | /    ||    \ |  |/ ]  /  _]|    \
# | _   _ ||  o  ||  D  )|  ' /  /  [_ |  D  )
# |  \_/  ||     ||    / |    \ |    _]|    /
# |   |   ||  _  ||    \ |     \|   [_ |    \
# |   |   ||  |  ||  .  \|  .  ||     ||  .  \
# |___|___||__|__||__|\_||__|\_||_____||__|\_|
#
#  -->

newline = '\n'
doubleline = '\n\n'
space = '\n\n\n'

content = {}

content['logo'] = '' +\
    f'<h3 style="text-align:center;font-weight: 300;" align="center">{newline}' +\
    f'  <img src="https://tinyurl.com/ybsoypnj" alt="picture number">{newline}' +\
    f'</h3>{newline}<br>{space}'


content['badge'] = '' +\
    f'<p align="center">{newline}' +\
    f'  <b>Title</b>: Title for Humans™<br/><br/>{newline}' +\
    f'  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">{newline}' +\
    f'  <img src="https://forthebadge.com/images/badges/built-with-love.svg" width="87px">{newline}' +\
    f'  <img src="https://forthebadge.com/images/badges/made-with-python.svg" width="130px">{newline}' +\
    f'  <img src="https://img.shields.io/badge/downloads-0k-yellow.svg?style=flat-square">\n' +\
    f'</p>{newline}<br>{space}'


content['installation'] = '' +\
    f'## Installation{newline}' +\
    f'``` bash{newline}' +\
    f'pip install ____{newline}' +\
    f'```{newline}<br>{space}'


content['author'] = '' +\
    f'## Author{newline}' +\
    f'[![Yu Zhou](https://avatars3.githubusercontent.com/u/6414741?s=100&v=4)](http://yuzhoujr.com){newline}' +\
    f'---|{newline}' +\
    f'[Yu Zhou :rocket:](http://yuzhoujr.com)<br>{space}'


content['license'] = '' +\
    f'## License{newline}' +\
    f'MIT © [Yu Zhou](http://yuzhoujr.com){newline}<br>{space}'


content['footer'] = '' +\
    f'<br/>{doubleline}' +\
    f'> ![home](http://yuzhoujr.com/legacy/emoji/home.svg)[yuzhoujr.com](http://www.yuzhoujr.com) &nbsp;&middot;&nbsp; {newline}' +\
    f'> ![github](http://yuzhoujr.com/legacy/emoji/github.svg)  [@yuzhoujr](https://github.com/yuzhoujr) &nbsp;&middot;&nbsp; {newline}' +\
    f'> ![linkedin](http://yuzhoujr.com/legacy/emoji/linkedin.svg)  [@yuzhoujr](https://linkedin.com/in/yuzhoujr) {space}'

if __name__ == "__main__":
    print(content['footer'])
