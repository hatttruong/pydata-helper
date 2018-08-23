# Sublime setting #

## Essential Plugins

Press `Ctrl-Shift-P`, type **`Install Package`**, type name of package...

1. Package Control: https://packagecontrol.io/installation#st3
2. Theme Soda: https://packagecontrol.io/packages/Theme%20-%20Soda
3. SideBarEnhancement: https://packagecontrol.io/packages/SideBarEnhancements
4. Git
5. GitGutter: https://packagecontrol.io/packages/GitGutter
    - Gutter Icons indicating inserted, modified or deleted lines
    - Diff Popup with details about modified lines
    - Status Bar Text with information about file and repository
6. AutoDocstring: `Ctrl-Shift-Alt+"` (it is quite handy and useful when auto generating summary for class, function, detect added parameters, deleted parameters)
7. Python PEP8 Autoformat: wrapping package, variable which are not used anywhere
8. Markdown Preview: https://github.com/revolunet/sublimetext-markdown-preview
9. *SublimeLinter*: https://packagecontrol.io/packages/SublimeLinter
10. *Color Highlighter*
11. *Git GUI Clients*
12. *HTML-CSS-JS Prettify*
13. *Javascript & NodeJS Snippets*

In order to change theme: `Sublime Text` > `Preferences` > `Theme...`

## User setting in Sublime

```
"default_line_ending": "LF",
"detect_indentation": false, "translate_tabs_to_spaces": true, "tab_size": 4,
"trim_trailing_white_space_on_save": true
```

Updated 24/08/2018, setting in Sublime on OSX
```
{
    "ignored_packages":
    [
        "Vintage"
    ],
    "theme": "Soda Dark 3.sublime-theme",
    // Columns in which to display vertical rulers
    "rulers": [80],
    // Set to true to automatically save files when switching to a different file
    // or application
    "save_on_focus_lost": true,
    // Set to true to insert spaces when tab is pressed
    "translate_tabs_to_spaces": true,
    // Set to true to removing trailing white space on save
    "trim_trailing_white_space_on_save": true,
    // Set to a value other than 0 to force wrapping at that column rather than the
    // window width
    "wrap_width": 80,

    "default_line_ending": "unix",

    // Set to false to disable detection of tabs vs. spaces on load
    "detect_indentation": false,

    "font_size": 13,

    // Set to false to prevent line numbers being drawn in the gutter
    "line_numbers": true,

    // Set to false to hide the gutter altogether
    "gutter": true,

}
```

## Essential Key Shortcut

`Sublime Text` > `Preferences` > `Key Bindings`

* Navigate Back: Ctrl +Shift + -
* Navigate Forward: Alt + Shift + -
* Locate file in Project Structure
* Go to definition: F12
* Go to Symbol: Ctrl + R
* Go to anything: Ctrl + P
* Find Usage: <NOT SUPPORTED>
* Show Console: Ctrl + `
* Go to anything: Ctrl + Shift + P
* Auto docstring (package): Ctrl + Shift + Alt + “
* Comment code: Ctrl + /
* Build Markdown: Ctrl + B
* Preview markdown: Alt + M (*)