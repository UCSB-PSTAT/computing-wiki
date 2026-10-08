# Documentation

This is the PSTAT department computing wiki, built with Jekyll and the
[just-the-docs](https://just-the-docs.github.io/just-the-docs/) theme.

## Build Steps

### Run the website (for testing)

#### Dev container (recommended)

Open the folder in VS Code and use **Dev Containers: Reopen in Container**.
The container installs the dependencies and starts `jekyll serve` automatically —
click the `4000 (Preview)` entry in the **PORTS** panel to open the site.

#### Manual

Requires Ruby, Jekyll, and Bundler. From the root directory:

```sh
bundle install
bundle exec jekyll serve --baseurl ""
```

Access the website through [http://localhost:4000/](http://localhost:4000/)

> Note: `--baseurl ""` serves the site at the local root. The site's real
> `baseurl` is `/computing-wiki` (for GitHub Pages), so without this flag a
> local build is served under `http://localhost:4000/computing-wiki/`.

### Codelab pages (migration reference)

The tutorial pages under `docs/` (e.g. `docs/devcontainer/`,
`docs/computing/jetstream2/`) were converted from **Google Codelabs** into
standard just-the-docs Markdown. Each is a self-contained folder:

```
docs/<area>/<name>/
  ├── <name>.md        # the just-the-docs page that is served
  └── img/             # the images referenced by the page
```

> **Temporary:** the `codelab-sources/` directory and `codelab2md.py` are
> migration scaffolding only. `codelab-sources/<area>/<name>/` holds the
> original exported Codelab (`index.html` + `codelab.json`) kept as a reference
> for the conversion, and `codelab2md.py` is the one-off script that produced
> the Markdown from those sources. Codelabs are being **deprecated** — once the
> conversion is merged and validated, both will be removed and the `.md` pages
> will be maintained directly.
