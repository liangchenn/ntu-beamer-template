# NTU-Beamer-Template

This is a final project for Typesetting Scientific Presentation, a minicourse at National Taiwan University.

This project aims to provide an unofficial and user-friendly presentation template with NTU theme.

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
    - Since the logo is originally set to the `logos/yourFirstcolor.png`, it will be missing if the file doesn't exist.
    - Another solution is upload a logo image with the corresponding filename. e.g. `logos/blue.png`
    - _We still working on this issue to automatically check if the image exists and set a default logo image otherwise._

### Dark frame environment

- If you want to use a slide with a dark background, could use our darkframe environment

    ```tex
    \begin{darkframe}[title]
        % text
    \end{darkframe}
    ```

- To change the dark theme background color by using

    ```tex
    \setdarkframecolor{backgroundcolor}
    ```

### Other features

- The overlay will highlight current point in main color.

- `Itemize/enumerate` will go from main color to second color gradually when using `subitem/subsubitem`
- A customized `examplebox` command and `mybox` environment to have good looking box

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
- Stylize references by group (e.g. year / field / importance)
- Progress bar on headline


## Files

### Structure

```
.
├── README.md
├── beamercolorthementu.sty
├── beamerfontthementu.sty
├── beamerinnerthementu.sty
├── beamerouterthementu.sty
├── beamerthementu.sty
├── logos/
├── demo.pdf
├── main.tex
├── preamble.tex
└── reference.bib

```

### Description

- `README.md` : breif intro to the project
- `*.sty` files : our main theme style files
- `preamble.tex` : preamble and some self-defined commands
- `logos/` : directory for logos in different colors
- `main.tex` : a slide tex file
- `demo.pdf` : a demostration slide pdf
- `reference.bib` : a bib file example 


## Reference

We refer to different beamer template projects to create our own beamer style files and modify some features to fit our needs. 

We will list these projects below, and these are very beautiful and useful beamer templates that you could try !

- [Drcula/Dracula dark Beamer Template](https://draculatheme.com/beamer)
- [DTU Beamer Template on Overleaf](http://latex.dtu.dk/?page_id=61)
- [matze/Metropolis Beamer Template](https://github.com/matze/mtheme)
- [sanhacheong/Stanford Beamer Template](https://github.com/sanhacheong/stanford-beamer-presentation)
- [thlamb/Trigon Beamer Template](https://gitlab.com/thlamb/beamertheme-trigon)
- [basaldella/University of Udine Unofficial Beamer Theme Template](https://github.com/basaldella/beamerthemeuniud)
