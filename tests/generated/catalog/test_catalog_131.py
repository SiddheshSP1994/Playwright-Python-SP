import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7811", "title": "Catalog scenario 7811", "data": {"sku": "SKU7811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7811@example.com", "threshold": 110}},
    {"id": "CATALOG-7812", "title": "Catalog scenario 7812", "data": {"sku": "SKU7812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7812@example.com", "threshold": 120}},
    {"id": "CATALOG-7813", "title": "Catalog scenario 7813", "data": {"sku": "SKU7813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7813@example.com", "threshold": 130}},
    {"id": "CATALOG-7814", "title": "Catalog scenario 7814", "data": {"sku": "SKU7814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7814@example.com", "threshold": 140}},
    {"id": "CATALOG-7815", "title": "Catalog scenario 7815", "data": {"sku": "SKU7815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7815@example.com", "threshold": 150}},
    {"id": "CATALOG-7816", "title": "Catalog scenario 7816", "data": {"sku": "SKU7816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7816@example.com", "threshold": 160}},
    {"id": "CATALOG-7817", "title": "Catalog scenario 7817", "data": {"sku": "SKU7817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7817@example.com", "threshold": 170}},
    {"id": "CATALOG-7818", "title": "Catalog scenario 7818", "data": {"sku": "SKU7818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7818@example.com", "threshold": 180}},
    {"id": "CATALOG-7819", "title": "Catalog scenario 7819", "data": {"sku": "SKU7819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7819@example.com", "threshold": 190}},
    {"id": "CATALOG-7820", "title": "Catalog scenario 7820", "data": {"sku": "SKU7820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7820@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
