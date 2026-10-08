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

### Codelab (tutorial) pages

Tutorial pages are plain Markdown. Each codelab is a self-contained folder:

```
docs/<area>/<name>/
  ├── <name>.md        # the just-the-docs page that is served
  └── img/             # the images referenced by the page (relative img/... paths)
```

The codelab *build sources* — the exported Google Codelab `index.html` and
`codelab.json` — live **outside** `docs/`, under `codelab-sources/<area>/<name>/`,
so Jekyll never serves them. They are only inputs to the generator:

```
codelab-sources/<area>/<name>/
  ├── index.html
  └── codelab.json
```

To regenerate the Markdown from a codelab's `index.html`, run:

```bash
python3 codelab2md.py
```

The script reads the frontmatter metadata (title, parent, nav order, etc.) from
its internal `META` table and rewrites each `docs/<area>/<name>/<name>.md`. It
is idempotent — it never touches the `codelab-sources/` inputs or `img/`
folders, so it can be re-run safely.

To add a new codelab:

1. Export the Google Doc as a codelab into `codelab-sources/<area>/<name>/`
   (its `index.html` + `codelab.json`).
2. Create `docs/<area>/<name>/` with an `img/` folder for the images.
3. Add an entry for it to the `META` table in `codelab2md.py`.
4. Run `python3 codelab2md.py` to generate `docs/<area>/<name>/<name>.md`.

For more information about building individual Codelabs, [visit the
Codelabs documentation](https://github.com/googlecodelabs/tools#ok-how-do-i-use-it).
