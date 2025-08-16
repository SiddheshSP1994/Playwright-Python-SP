import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6971", "title": "Catalog scenario 6971", "data": {"sku": "SKU6971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6971@example.com", "threshold": 710}},
    {"id": "CATALOG-6972", "title": "Catalog scenario 6972", "data": {"sku": "SKU6972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6972@example.com", "threshold": 720}},
    {"id": "CATALOG-6973", "title": "Catalog scenario 6973", "data": {"sku": "SKU6973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6973@example.com", "threshold": 730}},
    {"id": "CATALOG-6974", "title": "Catalog scenario 6974", "data": {"sku": "SKU6974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6974@example.com", "threshold": 740}},
    {"id": "CATALOG-6975", "title": "Catalog scenario 6975", "data": {"sku": "SKU6975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6975@example.com", "threshold": 750}},
    {"id": "CATALOG-6976", "title": "Catalog scenario 6976", "data": {"sku": "SKU6976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6976@example.com", "threshold": 760}},
    {"id": "CATALOG-6977", "title": "Catalog scenario 6977", "data": {"sku": "SKU6977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6977@example.com", "threshold": 770}},
    {"id": "CATALOG-6978", "title": "Catalog scenario 6978", "data": {"sku": "SKU6978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6978@example.com", "threshold": 780}},
    {"id": "CATALOG-6979", "title": "Catalog scenario 6979", "data": {"sku": "SKU6979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6979@example.com", "threshold": 790}},
    {"id": "CATALOG-6980", "title": "Catalog scenario 6980", "data": {"sku": "SKU6980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6980@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
