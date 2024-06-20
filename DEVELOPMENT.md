# General doc URL structure

`docs.csv` is separated into 7 parts:
- Google Doc URL
- title
- parent
- grand_parent
- nav_order
- url_loc
- url_name
- redirect

Excluding **title** will NOT build a redirect.md with `yaml` redirects.


**NOTE:** Parents/Grandparents for *NEW* tutorials requires manual updates to their `yaml` heading in order to properly include the tutorial. Specifically `parent`/`grand_parent` and `has_children: true` must be included. See `/docs/computing/jetstream2/redirect.md`, `/docs/computing/computing.md`, and `/docs/computing/external-sources.md` for details.

The script only handles automated generation of tutorial docs and not upper level management of links.
