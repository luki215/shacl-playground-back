This is semestral project for [Linked data course on VŠE](https://nb.vse.cz/~svatek/rzzw.html).

This repo has [corresponding FE part](https://github.com/luki215/shacl-playground-front)

# Installation
Recomended using VSCode with [Remote extension installed](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack). You can just clone the repository, open in VSCode, reopen it in container and you have all the development environment set up including the debugger.

Otherwise you can just run 
```docker-compose up```

## Installing new pypi packages
- add the package name in `requirements.txt`
- `docker-compose build` in non-remote session
- in remote session vscode run `rebuild container` action

## Running prod version
```docker run --rm luki215/shacl-editor-be```

# Publishing new version
is done automatically with pushig new tag to repo.

```git tag -a v0.0.1```
```git push --follow-tags```
