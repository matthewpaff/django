# Roadmap example

Use `search_records(queryset, term).order_by('pk')` before `page_records(...)`. The model must provide the chosen `name` or `title` field. Pagination requires stable ordering; invalid page strings select the first page, while out-of-range pages select the last.

See RECONSTRUCTION.md for provenance and verification limits.
