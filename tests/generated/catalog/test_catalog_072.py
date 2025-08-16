import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4271", "title": "Catalog scenario 4271", "data": {"sku": "SKU4271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4271@example.com", "threshold": 710}},
    {"id": "CATALOG-4272", "title": "Catalog scenario 4272", "data": {"sku": "SKU4272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4272@example.com", "threshold": 720}},
    {"id": "CATALOG-4273", "title": "Catalog scenario 4273", "data": {"sku": "SKU4273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4273@example.com", "threshold": 730}},
    {"id": "CATALOG-4274", "title": "Catalog scenario 4274", "data": {"sku": "SKU4274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4274@example.com", "threshold": 740}},
    {"id": "CATALOG-4275", "title": "Catalog scenario 4275", "data": {"sku": "SKU4275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4275@example.com", "threshold": 750}},
    {"id": "CATALOG-4276", "title": "Catalog scenario 4276", "data": {"sku": "SKU4276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4276@example.com", "threshold": 760}},
    {"id": "CATALOG-4277", "title": "Catalog scenario 4277", "data": {"sku": "SKU4277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4277@example.com", "threshold": 770}},
    {"id": "CATALOG-4278", "title": "Catalog scenario 4278", "data": {"sku": "SKU4278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4278@example.com", "threshold": 780}},
    {"id": "CATALOG-4279", "title": "Catalog scenario 4279", "data": {"sku": "SKU4279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4279@example.com", "threshold": 790}},
    {"id": "CATALOG-4280", "title": "Catalog scenario 4280", "data": {"sku": "SKU4280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4280@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
