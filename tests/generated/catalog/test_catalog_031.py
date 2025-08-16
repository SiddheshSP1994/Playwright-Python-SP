import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-1811", "title": "Catalog scenario 1811", "data": {"sku": "SKU1811", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1811@example.com", "threshold": 110}},
    {"id": "CATALOG-1812", "title": "Catalog scenario 1812", "data": {"sku": "SKU1812", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1812@example.com", "threshold": 120}},
    {"id": "CATALOG-1813", "title": "Catalog scenario 1813", "data": {"sku": "SKU1813", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1813@example.com", "threshold": 130}},
    {"id": "CATALOG-1814", "title": "Catalog scenario 1814", "data": {"sku": "SKU1814", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1814@example.com", "threshold": 140}},
    {"id": "CATALOG-1815", "title": "Catalog scenario 1815", "data": {"sku": "SKU1815", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1815@example.com", "threshold": 150}},
    {"id": "CATALOG-1816", "title": "Catalog scenario 1816", "data": {"sku": "SKU1816", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1816@example.com", "threshold": 160}},
    {"id": "CATALOG-1817", "title": "Catalog scenario 1817", "data": {"sku": "SKU1817", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1817@example.com", "threshold": 170}},
    {"id": "CATALOG-1818", "title": "Catalog scenario 1818", "data": {"sku": "SKU1818", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1818@example.com", "threshold": 180}},
    {"id": "CATALOG-1819", "title": "Catalog scenario 1819", "data": {"sku": "SKU1819", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1819@example.com", "threshold": 190}},
    {"id": "CATALOG-1820", "title": "Catalog scenario 1820", "data": {"sku": "SKU1820", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1820@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
