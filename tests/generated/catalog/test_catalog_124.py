import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7391", "title": "Catalog scenario 7391", "data": {"sku": "SKU7391", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7391@example.com", "threshold": 910}},
    {"id": "CATALOG-7392", "title": "Catalog scenario 7392", "data": {"sku": "SKU7392", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7392@example.com", "threshold": 920}},
    {"id": "CATALOG-7393", "title": "Catalog scenario 7393", "data": {"sku": "SKU7393", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7393@example.com", "threshold": 930}},
    {"id": "CATALOG-7394", "title": "Catalog scenario 7394", "data": {"sku": "SKU7394", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7394@example.com", "threshold": 940}},
    {"id": "CATALOG-7395", "title": "Catalog scenario 7395", "data": {"sku": "SKU7395", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7395@example.com", "threshold": 950}},
    {"id": "CATALOG-7396", "title": "Catalog scenario 7396", "data": {"sku": "SKU7396", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7396@example.com", "threshold": 960}},
    {"id": "CATALOG-7397", "title": "Catalog scenario 7397", "data": {"sku": "SKU7397", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7397@example.com", "threshold": 970}},
    {"id": "CATALOG-7398", "title": "Catalog scenario 7398", "data": {"sku": "SKU7398", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7398@example.com", "threshold": 980}},
    {"id": "CATALOG-7399", "title": "Catalog scenario 7399", "data": {"sku": "SKU7399", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7399@example.com", "threshold": 990}},
    {"id": "CATALOG-7400", "title": "Catalog scenario 7400", "data": {"sku": "SKU7400", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7400@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
