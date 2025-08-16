import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4691", "title": "Catalog scenario 4691", "data": {"sku": "SKU4691", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4691@example.com", "threshold": 910}},
    {"id": "CATALOG-4692", "title": "Catalog scenario 4692", "data": {"sku": "SKU4692", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4692@example.com", "threshold": 920}},
    {"id": "CATALOG-4693", "title": "Catalog scenario 4693", "data": {"sku": "SKU4693", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4693@example.com", "threshold": 930}},
    {"id": "CATALOG-4694", "title": "Catalog scenario 4694", "data": {"sku": "SKU4694", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4694@example.com", "threshold": 940}},
    {"id": "CATALOG-4695", "title": "Catalog scenario 4695", "data": {"sku": "SKU4695", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4695@example.com", "threshold": 950}},
    {"id": "CATALOG-4696", "title": "Catalog scenario 4696", "data": {"sku": "SKU4696", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4696@example.com", "threshold": 960}},
    {"id": "CATALOG-4697", "title": "Catalog scenario 4697", "data": {"sku": "SKU4697", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4697@example.com", "threshold": 970}},
    {"id": "CATALOG-4698", "title": "Catalog scenario 4698", "data": {"sku": "SKU4698", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4698@example.com", "threshold": 980}},
    {"id": "CATALOG-4699", "title": "Catalog scenario 4699", "data": {"sku": "SKU4699", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4699@example.com", "threshold": 990}},
    {"id": "CATALOG-4700", "title": "Catalog scenario 4700", "data": {"sku": "SKU4700", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4700@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
