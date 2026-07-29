# large_prolog_databases
A collection of large Prolog databases for testing Prolog implementations


## Usage

```prolog
?- [schema_org].
   true.
?- use_module(library(time)).
   true.
?- time((item_type_(I,"BookSeries"), item_prop_val_(I, P, I1), item_type_(I1, "Movie"))).
   % CPU time: 1.019s, 206_142 inferences
   I = "Star Wars Episode I  ...", P = "about", I1 = "Star Wars Episode I"
;  ... .
```

## Datasets

- `schema_org.pl` -- dataset organized in schema.org format with `item_type_/2` and `item_prop_val_/3` predicates, based on [MuSiQue](https://github.com/stonybrooknlp/musique) dataset
- `stop_times.pl`, `trips.pl` -- dataset based on public transport in Vancouver: <https://www.translink.ca/about-us/doing-business-with-translink/app-developer-resources/gtfs/gtfs-data>