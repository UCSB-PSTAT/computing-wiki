# Documentation with Codelabs

## Build Steps

### Build website

#### Container

Simply build the Dockerfile via Docker/Podman (or using VS Code). Once built, run the following inside the container:

```sh
bundle exec jekyll serve --livereload
```

#### Manual

Requires Ruby Devkit, Jekyll, and Bundler installed.  From the root directory, run the following commands:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Access the website through [http://localhost:4000/](http://localhost:4000/)

### Build codelabs pages

Following bash script extracts Google docs file ID from table above and runs the `claat` tool for each match. To build all the docs **inside a `test` directory**, run the following command from the root directory while inside the container:

```bash
python3 wiki.py
```

If you're happy with the changes, to build inside `docs` run the following command while inside the container:

```bash
python3 wiki.py --no-test
```

**Note:** Every codelab requires a `redirect.md` file with the following format:

```md
---
title: CODELAB TITLE HERE
parent: PARENT MD TITLE HERE
nav_order: 1
permalink: /docs/inner-directory/codelab-directory
---

{% include_relative index.html %}
```

This directory structure is setup automatically via the script which reads the `docs.csv` file. When adding new Codelabs, add a new line to the file containing the following comma separated information:

- Google Doc URL,
- title (optional if no redirect is necessary)
- parent (optional if no redirect is necessary)
- grand_parent (optional in general)
- nav_order (order that link shows up in the sidebar)
- url_loc (root dir where codelab is stored -- do not include url_name!)
- url_name (name of codelab)
- redirect (which page user should be dropped in after exiting or pressing "Done")

For more information about building individual Codelabs, [visit the Codelabs documentation](https://github.com/googlecodelabs/tools#ok-how-do-i-use-it).
