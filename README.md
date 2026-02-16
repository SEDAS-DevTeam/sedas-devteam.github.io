# SEDAS main website

This is the main website for the SEDAS project, here, you can find redirects to other links and documentation.

## Tech stack

![jQuery](https://img.shields.io/badge/jquery-%230769AD.svg?style=for-the-badge&logo=jquery&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## Local deployment
To test some of the parts of the code, simply run these commands (You need to have Python3 installed)

``` shell
pyenv install 3.11
pyenv virtualenv 3.11 sedas_devel_server # because we are using Livereload and Flask package, we need to create virtualenv
pyenv local sedas_devel_server
pip install -r requirements.txt

chmod +x ./server.py # make executable
./server.py -p=8080 # serve on port 8080 (exits on KeyboardInterrupt - Ctrl+C)
```

## TODO

- [x] Finish website structure
- [x] Add links to other parts of the project
- [x] Add AJAX + jQuery so that the page loading will feel smoother
- [x] Add used tech stack here in README
- [x] Add youtube logo to website
- [x] Implement scroll on codemap
- [x] Add loader in codemap
- [x] Implement custom buttons on svg-pan-zoom
- [x] Fix broken codemap loading, mark off as done in charts
- [x] Page backgroun broken