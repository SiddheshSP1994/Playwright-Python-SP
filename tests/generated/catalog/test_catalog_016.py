import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0911", "title": "Catalog scenario 911", "data": {"sku": "SKU911", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user911@example.com", "threshold": 110}},
    {"id": "CATALOG-0912", "title": "Catalog scenario 912", "data": {"sku": "SKU912", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user912@example.com", "threshold": 120}},
    {"id": "CATALOG-0913", "title": "Catalog scenario 913", "data": {"sku": "SKU913", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user913@example.com", "threshold": 130}},
    {"id": "CATALOG-0914", "title": "Catalog scenario 914", "data": {"sku": "SKU914", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user914@example.com", "threshold": 140}},
    {"id": "CATALOG-0915", "title": "Catalog scenario 915", "data": {"sku": "SKU915", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user915@example.com", "threshold": 150}},
    {"id": "CATALOG-0916", "title": "Catalog scenario 916", "data": {"sku": "SKU916", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user916@example.com", "threshold": 160}},
    {"id": "CATALOG-0917", "title": "Catalog scenario 917", "data": {"sku": "SKU917", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user917@example.com", "threshold": 170}},
    {"id": "CATALOG-0918", "title": "Catalog scenario 918", "data": {"sku": "SKU918", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user918@example.com", "threshold": 180}},
    {"id": "CATALOG-0919", "title": "Catalog scenario 919", "data": {"sku": "SKU919", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user919@example.com", "threshold": 190}},
    {"id": "CATALOG-0920", "title": "Catalog scenario 920", "data": {"sku": "SKU920", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user920@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
