import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7271", "title": "Catalog scenario 7271", "data": {"sku": "SKU7271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7271@example.com", "threshold": 710}},
    {"id": "CATALOG-7272", "title": "Catalog scenario 7272", "data": {"sku": "SKU7272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7272@example.com", "threshold": 720}},
    {"id": "CATALOG-7273", "title": "Catalog scenario 7273", "data": {"sku": "SKU7273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7273@example.com", "threshold": 730}},
    {"id": "CATALOG-7274", "title": "Catalog scenario 7274", "data": {"sku": "SKU7274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7274@example.com", "threshold": 740}},
    {"id": "CATALOG-7275", "title": "Catalog scenario 7275", "data": {"sku": "SKU7275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7275@example.com", "threshold": 750}},
    {"id": "CATALOG-7276", "title": "Catalog scenario 7276", "data": {"sku": "SKU7276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7276@example.com", "threshold": 760}},
    {"id": "CATALOG-7277", "title": "Catalog scenario 7277", "data": {"sku": "SKU7277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7277@example.com", "threshold": 770}},
    {"id": "CATALOG-7278", "title": "Catalog scenario 7278", "data": {"sku": "SKU7278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7278@example.com", "threshold": 780}},
    {"id": "CATALOG-7279", "title": "Catalog scenario 7279", "data": {"sku": "SKU7279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7279@example.com", "threshold": 790}},
    {"id": "CATALOG-7280", "title": "Catalog scenario 7280", "data": {"sku": "SKU7280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7280@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
