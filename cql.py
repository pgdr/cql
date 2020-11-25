#!/usr/bin/env python
import sys
import argparse
import sqlite3

import pandas as pd  # TODO replace with csv


def _parse_args(args):
    idx = 0
    for idx, arg in enumerate(args):
        if not arg.endswith(".csv"):
            break
    fnames = args[:idx]
    query = " ".join(args[idx:])
    return fnames, query


def _create_db(dfs, names):
    conn = sqlite3.connect(":memory:")
    for df, name in zip(dfs, names):
        df.to_sql(name=name, con=conn)
    return conn


def cql(dfs, names, query):
    if not len(dfs) == len(names):
        raise ValueError(f"{len(dfs)=} != {len(names)=}")
    if not names:
        raise ValueError("Empty set of tables")

    conn = _create_db(dfs, names)
    return conn.execute(query)


def _print_res(res):
    for r in res:
        print(",".join(str(e) for e in r))


def main():
    if len(sys.argv) < 2:
        exit("Usage: cql fname1.csv [fname2.csv ...] SELECT ...")

    fnames, query = _parse_args(sys.argv[1:])
    dfs = [pd.read_csv(fname) for fname in fnames]
    for fname in fnames:
        if not fname.endswith(".csv"):
            raise ValueError(f"Illegal filename {fname}")
    res = cql(dfs, [fname[:-4] for fname in fnames], query)
    _print_res(res)


if __name__ == "__main__":
    main()
