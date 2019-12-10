This is semestral project for [Linked data course on VŠE](https://nb.vse.cz/~svatek/rzzw.html).

# Installation
This project requires [VSCode insiders](https://code.visualstudio.com/insiders/)
## Installing new pypi packages
- add the package name in `requirements.txt`
- `docker-compose build` in non-remote session
- in remote session vscode run `rebuild container` action
# Publishing
is done automatically by pushig new tag to repo.

`git tag -a v0.0.1`
`git push --follow-tags`