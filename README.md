# cql

`cql`—_csv query language_—is a way to query csv files using SQL.

The basic functionality is to call `cql` with the csv files first and
then the query:

```
cql fname1.csv fname2.csv SELECT \* FROM fname1 WHERE ...
```

For example, let `a.csv` be

```csv
x,y
3,8
4,9
5,10
6,11
7,12
8,13
```

```
cql a.csv select x from a
3
4
5
6
7
8
```
