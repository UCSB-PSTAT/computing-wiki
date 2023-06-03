# Documentation with Codelabs

## Tutorial List

| Google Docs URL | Page Description |
| --------------- | ---------------- |
| https://docs.google.com/document/d/1ADKvlGqyYNsO1GWbC_IMLlUqDtyXbufTBUpS-ogFNYA | "ssh setup" |
| -https://docs.google.com/document/d/1nGk9VwBzlPng8lm_7165-hJBXtyRAjDdx1t0fhqv6xE | "local dev containers" (incomplete for now) |
| https://docs.google.com/document/d/195jckkF79ed7KultZlF4CJOO2nda3y3Vjm5ISLy_b1k | "dev container with vscode" |
| https://docs.google.com/document/d/1oTagNdTuDcQMCT3-2vjtK945VB_sJndbnfhoeSxOK24 | "dev container management" |
| https://docs.google.com/document/d/10oo_i8PbxfD5mdyqdLdCdvSJ_DFhRi7E5HRG2iagrZU | "file management" |
| https://docs.google.com/document/d/1yF0US6nskeKtxQ8an5zFTD3OvLwK6Eg2aI2ZcDiqKB0 | "job management" |

## Build Steps

### Build codelabs pages

Following bash script extracts Google docs file ID from table above and runs the `claat` tool for each match.  To build all the docs, run the following command from the root directory:

```bash
./wiki.sh
```

Make sure that you have bash available (Windows Subsystem for Linux or a bash compatible terminal).

### Build website

Requires Ruby Devkit, Jekyll, and Bundler installed.

```
cd docs
bundle install
bundle exec jekyll serve --livereload
```

Access the website through [http://localhost:4000/](http://localhost:4000/)