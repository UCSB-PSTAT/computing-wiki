# Documentation

This is the PSTAT department computing wiki, built with Jekyll and the
[just-the-docs](https://just-the-docs.github.io/just-the-docs/) theme.

## Build Steps

### Build website

#### Container

Simply build the Dockerfile via Docker/Podman (or using VS Code). Once built, run the following inside the container:

```sh
bundle exec jekyll serve --livereload
```

#### Manual

Requires Ruby, Jekyll, and Bundler installed. From the root directory, run the following commands:

```sh
bundle install
bundle exec jekyll serve --livereload
```

Access the website through [http://localhost:4000/](http://localhost:4000/)

### Codelab (tutorial) pages

Tutorial pages are plain Markdown. Each codelab directory contains:

- `index.html` — the exported [Google Codelab](https://github.com/googlecodelabs/tools)
  source (kept for reference and for regenerating the markdown),
- `redirect.md` (or `index.md`) — the standard just-the-docs page that is
  actually served, and
- `img/` — the images referenced by the markdown.

The codelab `index.html` / `codelab.json` source files are listed under
`exclude:` in `_config.yml`, so Jekyll does **not** publish them — only the
generated `.md` page is served at each codelab's URL.

To regenerate the Markdown from a codelab's `index.html`, run:

```bash
python3 codelab2md.py
```

The script reads the frontmatter metadata (title, parent, nav order, etc.) from
its internal `META` table and rewrites each codelab's markdown page. It is
idempotent — it never deletes the source `index.html`, `codelab.json`, or
`img/` files, so it can be re-run safely.

To add a new codelab:

1. Export the Google Doc as a codelab `index.html` into a new `docs/<area>/<name>/`
   directory (with its `img/` folder and `codelab.json`).
2. Add an entry for it to the `META` table in `codelab2md.py`.
3. Add its `index.html` and `codelab.json` to the `exclude:` list in
   `_config.yml`.
4. Run `python3 codelab2md.py`.

For more information about building individual Codelabs, [visit the
Codelabs documentation](https://github.com/googlecodelabs/tools#ok-how-do-i-use-it).
