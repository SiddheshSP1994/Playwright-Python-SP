# Requirements Traceability Matrix

The table below maps high‑level epics to the range of test IDs that exercise those features.  The ID scheme follows `SUITE-XXXX` where `SUITE` matches the suite name in upper‑case and `XXXX` is a zero‑padded sequence number.  Each generated file contains 10 cases; there are 1000 files in total (≈10 000 cases).

| Epic | Suites | ID range | Approx. total cases |
|------|--------|----------|--------------------|
| **Checkout** | `checkout` | `CHECKOUT-0001` – `CHECKOUT-1670` | 1 670 |
| **Catalog** | `catalog` | `CATALOG-0011` – `CATALOG-1670` | 1 670 |
| **Orders** | `orders` | `ORDERS-0021` – `ORDERS-1670` | 1 670 |
| **Payments** | `payments` | `PAYMENTS-0031` – `PAYMENTS-1670` | 1 670 |
| **Email** | `email` | `EMAIL-0061` – `EMAIL-1660` | 1 660 |
| **Analytics** | `analytics` | `ANALYTICS-0071` – `ANALYTICS-1660` | 1 660 |

Note: Case numbering rotates through suites; thus the start ID for each suite is offset from 1.  For example, the first 10 cases (`CHECKOUT-0001`–`CHECKOUT-0010`) belong to the `checkout` suite, the next 10 (`CATALOG-0011`–`CATALOG-0020`) belong to `catalog`, and so on.  This scheme continues until all 10 000 cases are assigned.

Use this matrix to trace requirements (epics) to the test IDs exercised.  When adding new tests, append to the appropriate suite and update the ranges accordingly.