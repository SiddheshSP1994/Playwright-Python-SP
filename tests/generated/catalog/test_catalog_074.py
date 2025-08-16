import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4391", "title": "Catalog scenario 4391", "data": {"sku": "SKU4391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4391@example.com", "threshold": 910}},
    {"id": "CATALOG-4392", "title": "Catalog scenario 4392", "data": {"sku": "SKU4392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4392@example.com", "threshold": 920}},
    {"id": "CATALOG-4393", "title": "Catalog scenario 4393", "data": {"sku": "SKU4393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4393@example.com", "threshold": 930}},
    {"id": "CATALOG-4394", "title": "Catalog scenario 4394", "data": {"sku": "SKU4394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4394@example.com", "threshold": 940}},
    {"id": "CATALOG-4395", "title": "Catalog scenario 4395", "data": {"sku": "SKU4395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4395@example.com", "threshold": 950}},
    {"id": "CATALOG-4396", "title": "Catalog scenario 4396", "data": {"sku": "SKU4396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4396@example.com", "threshold": 960}},
    {"id": "CATALOG-4397", "title": "Catalog scenario 4397", "data": {"sku": "SKU4397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4397@example.com", "threshold": 970}},
    {"id": "CATALOG-4398", "title": "Catalog scenario 4398", "data": {"sku": "SKU4398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4398@example.com", "threshold": 980}},
    {"id": "CATALOG-4399", "title": "Catalog scenario 4399", "data": {"sku": "SKU4399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4399@example.com", "threshold": 990}},
    {"id": "CATALOG-4400", "title": "Catalog scenario 4400", "data": {"sku": "SKU4400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4400@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
