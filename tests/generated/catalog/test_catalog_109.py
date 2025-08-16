import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6491", "title": "Catalog scenario 6491", "data": {"sku": "SKU6491", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6491@example.com", "threshold": 910}},
    {"id": "CATALOG-6492", "title": "Catalog scenario 6492", "data": {"sku": "SKU6492", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6492@example.com", "threshold": 920}},
    {"id": "CATALOG-6493", "title": "Catalog scenario 6493", "data": {"sku": "SKU6493", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6493@example.com", "threshold": 930}},
    {"id": "CATALOG-6494", "title": "Catalog scenario 6494", "data": {"sku": "SKU6494", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6494@example.com", "threshold": 940}},
    {"id": "CATALOG-6495", "title": "Catalog scenario 6495", "data": {"sku": "SKU6495", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6495@example.com", "threshold": 950}},
    {"id": "CATALOG-6496", "title": "Catalog scenario 6496", "data": {"sku": "SKU6496", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6496@example.com", "threshold": 960}},
    {"id": "CATALOG-6497", "title": "Catalog scenario 6497", "data": {"sku": "SKU6497", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6497@example.com", "threshold": 970}},
    {"id": "CATALOG-6498", "title": "Catalog scenario 6498", "data": {"sku": "SKU6498", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6498@example.com", "threshold": 980}},
    {"id": "CATALOG-6499", "title": "Catalog scenario 6499", "data": {"sku": "SKU6499", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6499@example.com", "threshold": 990}},
    {"id": "CATALOG-6500", "title": "Catalog scenario 6500", "data": {"sku": "SKU6500", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6500@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
