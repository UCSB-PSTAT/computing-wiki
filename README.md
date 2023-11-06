# Documentation with Codelabs

## Build Steps

### Build codelabs pages

Following bash script extracts Google docs file ID from table above and runs the `claat` tool for each match.  Make sure that you have bash available (Windows Subsystem for Linux or a bash compatible terminal).  To build all the docs, run the following command from the root directory:

```bash
./wiki.sh
```

Once the command is run, all the docs will be built inside the `tmp` directory.  Move the docs to their necessary locations.

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

### Build website

Requires Ruby Devkit, Jekyll, and Bundler installed.  From the root directory, run the following commands:

```
bundle install
bundle exec jekyll serve --livereload
```

Access the website through [http://localhost:4000/](http://localhost:4000/)

## Tutorial List

| Google Docs URL | Page Description |
| --------------- | ---------------- |
| https://docs.google.com/document/d/1OZoi8dN7lrQDSSvWCPuMv8nvMI7W8OV3j02xwb5M7Fg | "alta setup" |
| https://docs.google.com/document/d/1ADKvlGqyYNsO1GWbC_IMLlUqDtyXbufTBUpS-ogFNYA | "ssh setup" |
| https://docs.google.com/document/d/1nGk9VwBzlPng8lm_7165-hJBXtyRAjDdx1t0fhqv6xE | "local dev containers" |
| https://docs.google.com/document/d/195jckkF79ed7KultZlF4CJOO2nda3y3Vjm5ISLy_b1k | "dev container with vscode" |
| https://docs.google.com/document/d/1oTagNdTuDcQMCT3-2vjtK945VB_sJndbnfhoeSxOK24 | "dev container management" |
| https://docs.google.com/document/d/10oo_i8PbxfD5mdyqdLdCdvSJ_DFhRi7E5HRG2iagrZU | "file management" |
| https://docs.google.com/document/d/1yF0US6nskeKtxQ8an5zFTD3OvLwK6Eg2aI2ZcDiqKB0 | "job management" |
| https://docs.google.com/document/d/10Vav5Ug2YKmD5SSm5aurSyP_faW4IS1jV6P9Ad1rZr8 | "editing dockerfile" |
| https://docs.google.com/document/d/13FwlQ6xvDvPmxwy4Xs_DCEc-AdEoiMLyurkk7ymxn9s | "github codespaces" |
| https://docs.google.com/document/d/1jmfMKz30vkl2BcTW1tHSaQ1kPkbIwxjjdv2Vc0s4H5k | "ACCESS via Jetstream2" |
| https://docs.google.com/document/d/16wWtuBrVarh3kZDWFhoQt3M_pVxf5t6GhvIci9KRyqI | "printer driver installation - windows" |
| https://docs.google.com/document/d/1qt16tP26RZPOllHIvHCzWWv1KS7-M4Cs4tmr6eU16eU | "printer driver installation - macOS" |
| https://docs.google.com/document/d/1WnD7ZmUyZoqdxFuk47FHCdjoTVAfQJxDqoCi-qBqxOQ | "printer use" |
