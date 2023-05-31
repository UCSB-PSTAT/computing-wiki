# Documentation with Codelabs

## Tutorial List

| Google Docs URL | Page Description |
| --------------- | ---------------- |
| https://docs.google.com/document/d/1ADKvlGqyYNsO1GWbC_IMLlUqDtyXbufTBUpS-ogFNYA | "ssh setup" |
| https://docs.google.com/document/d/1nGk9VwBzlPng8lm_7165-hJBXtyRAjDdx1t0fhqv6xE | "local dev containers" |
| https://docs.google.com/document/d/195jckkF79ed7KultZlF4CJOO2nda3y3Vjm5ISLy_b1k | "dev container with vscode" |
| https://docs.google.com/document/d/1oTagNdTuDcQMCT3-2vjtK945VB_sJndbnfhoeSxOK24 | "dev container management" |
| https://docs.google.com/document/d/10oo_i8PbxfD5mdyqdLdCdvSJ_DFhRi7E5HRG2iagrZU | "file management" |

## Build Steps

### Download `claat` tool

Download appropriate binary from https://github.com/googlecodelabs/tools/releases/tag/v2.2.5

```bash
wget https://github.com/googlecodelabs/tools/releases/download/v2.2.5/claat-linux-amd64
chmod u+x claat-linux-amd64
```

### Build codelabs pages

Following code extracts Google docs file ID from table above and runs the `claat` tool for each match.

```bash
grep '-https://docs.google.com' README.md \
    | grep 'document' \
    | cut -d'|' -f2 \
    | cut -d'/' -f6 \
    | sed 's/ *$//' \
    | xargs -i ./claat-linux-amd64 export -o docs {}
```

- `grep '-https://docs.google.com' README.md`: extract all lines with `-https://docs.google.com`. (**REMOVE** the '-', this is a fix to avoid grabbing the instructions being talked about here)
- `grep 'document'`: to exclude lines like the command in previous line, also search for `document` in the same line.
- `cut -d'|' -f2`: split at `|` to separate markdown table cells
- `cut -d'/' -f6`: split at `/` to extract the file IDs
- `sed 's/ *$//'`: remove any whitespace
- `xargs -i ./claat-linux-amd64 export {}`: run `claat` tool for each matching line
