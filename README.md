# anehub-license

Publishes the signed ANEHub license token. A daily GitHub Action mints a 7-day
EdDSA token with the private key in this repo's `LICENSE_PRIVATE_KEY` secret and
commits it as `anehub.jwt`, which the ANEHub backend fetches over HTTPS.

- Tenant: `barry` (repo variable `LICENSE_TENANT_ID`).
- Token URL: `https://raw.githubusercontent.com/OhNoIBrokeIt/anehub-license/main/anehub.jwt`

To cut off use: disable the workflow, or delete `anehub.jwt`. The app fails
closed within 7 days. See the ANEHub repo `ops/license-issuer/README.md`.
