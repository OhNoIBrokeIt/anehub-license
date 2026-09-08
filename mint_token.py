#!/usr/bin/env python3
"""Mint a signed ANEHub license token (ADR-004).

Signs an EdDSA (Ed25519) JWT with the owner's private key. Used by the daily
GitHub Action and for manual minting. The private key must never be committed.

    python mint_token.py --key license_private.pem --tenant barry --days 7 --out anehub.jwt
"""
import argparse
import datetime as dt
import sys

import jwt


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--key", required=True, help="path to the Ed25519 private key PEM")
    ap.add_argument("--tenant", required=True, help="tenant id, becomes the token's sub claim")
    ap.add_argument("--days", type=int, default=7, help="validity in days (default 7)")
    ap.add_argument("--out", default="-", help="output file, or - for stdout")
    args = ap.parse_args()

    with open(args.key, "r", encoding="utf-8") as fh:
        priv = fh.read()

    now = dt.datetime.now(dt.timezone.utc)
    token = jwt.encode(
        {
            "sub": args.tenant,
            "iat": now,
            "exp": now + dt.timedelta(days=args.days),
            "iss": "anehub-license",
        },
        priv,
        algorithm="EdDSA",
    )

    if args.out == "-":
        sys.stdout.write(token + "\n")
    else:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(token)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
