# NTU-Beamer-Template

`ntu-beamer-template` is an unofficial presentation template for National Taiwan University.

This is a final project for Typesetting Scientific Presentation, a minicourse at NTU.

This project aims to provide a good-looking and user-friendly presentation template with NTU theme.

We modify some existing beautiful beamer templates and design our own theme colors and logos for the templates



## Features

### NTU logo
- There are some pre-designed NTU logo images saved in `logos/`
- The NTU logo will appear at the title page and on the top of each slide.

### Change Template Colors
- A relatively easy way to change any color you want
- One can change the main and secondary color of the template with a self-defined function `setcolor`

    ```tex
    \usetheme{ntu}
    
    % for using two colors
    \setcolor[secondcolor]{maincolor}
    
    % for using single color
    \setcolor{maincolor}
    ```
- There are several colors already be defined in our `beamercolorthementu.sty` file, you could directly use those colors to change themes or define the colors you like in the same file.

- When using colors other than pre-defined ones, you should modify the logo path in `beamerouterthementu.sty` file.
    - Since the logo is originally set to `logos/yourFirstcolor.png`, it will be missing if the file doesn't exist.
    - Another solution is upload a logo image with the corresponding filename. e.g. `logos/blue.png`
    - _We're still working on this issue to automatically check if the image exists and set a default logo image otherwise._

- We offer a workaround here for you to change logo color with given RGB value with a python script.

    ```bash
    # cd to correct directory and install dependencies first
    $ cd change_logo_color/
    $ pip install -r requirements.txt

    # example
    $ python change_logo_color.py --rgb 128 0 0 --output YourLogoPath.png

    # this would work
    $ python change_logo_color.py --rgb [R] [G] [B] -o YourLogoPath.png

    # this would create newlogo.png in current dir
    $ python change_logo_color.py --rgb [R] [G] [B]

    ```

### Dark frame environment

- If you want to use a slide with a dark background, could utilize our darkframe environment

    ```tex
    \begin{darkframe}[title]
        % text
    \end{darkframe}
    ```

- To change the dark theme background color, use `\setdarkframecolor` command

    ```tex
    \setdarkframecolor{backgroundcolor}
    ```

### Other features

- Current point will be highlighted in main color in the overlay.

- `Itemize/enumerate` will go from main color to second color gradually when using `subitem/subsubitem`
- A customized `examplebox` command and `mybox` environment to have good-looking box

    ```tex
    % examplebox directly using second color
    \examplebox{title}{content}
    
    % to change color, use mybox
    \begin{mybox}{color}{title}
        % text
    \end{mybox}
    ```

- A customized citation command that could let you set the importance level
    
    ```tex
    \cite[level]{citation}
    
    % normal cite
    \cite{...}
    
    % important cite
    \cite[A]{...}
    
    % super important cite
    \cite[S]{...}
    
    ```

## Still working on
- Refactoring `\cite` command for original options
- Stylize references by group (e.g. year / field / importance)
- Progress bar on headline


## Files

### Structure

```
.
├── LICENSE
├── README.md
├── change_logo_color
│   ├── change_logo_color.py
│   └── requirements.txt
├── demo.pdf
├── latexmkrc
├── logos/
├── main.tex
├── reference.bib
└── templates
    ├── beamercolorthementu.sty
    ├── beamerfontthementu.sty
    ├── beamerinnerthementu.sty
    ├── beamerouterthementu.sty
    └── beamerthementu.sty

```

### Description
- `LICENSE` : MIT License
- `README.md` : breif intro to the project
- `change_logo_color/` : python script to generate logo in new color
- `demo.pdf` : a demostration slide pdf
- `latexmkrc` : a setting file for change the template enviroment
- `logos/` : directory for logos in different colors
- `main.tex` : a slide tex file
- `reference.bib` : a bib file example 
- `templates/` : our main theme style files


## Reference

We refer to different beamer template projects to create our own beamer style files and modify some features to fit our needs. 

We list these projects below for reference, and these are very beautiful and useful beamer templates that you could try as well !

- [Drcula/Dracula dark Beamer Template](https://draculatheme.com/beamer)
- [DTU Beamer Template on Overleaf](http://latex.dtu.dk/?page_id=61)
- [matze/Metropolis Beamer Template](https://github.com/matze/mtheme)
- [sanhacheong/Stanford Beamer Template](https://github.com/sanhacheong/stanford-beamer-presentation)
- [thlamb/Trigon Beamer Template](https://gitlab.com/thlamb/beamertheme-trigon)
- [basaldella/University of Udine Unofficial Beamer Theme Template](https://github.com/basaldella/beamerthemeuniud)
