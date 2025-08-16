import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9971", "title": "Catalog scenario 9971", "data": {"sku": "SKU9971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9971@example.com", "threshold": 710}},
    {"id": "CATALOG-9972", "title": "Catalog scenario 9972", "data": {"sku": "SKU9972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9972@example.com", "threshold": 720}},
    {"id": "CATALOG-9973", "title": "Catalog scenario 9973", "data": {"sku": "SKU9973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9973@example.com", "threshold": 730}},
    {"id": "CATALOG-9974", "title": "Catalog scenario 9974", "data": {"sku": "SKU9974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9974@example.com", "threshold": 740}},
    {"id": "CATALOG-9975", "title": "Catalog scenario 9975", "data": {"sku": "SKU9975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9975@example.com", "threshold": 750}},
    {"id": "CATALOG-9976", "title": "Catalog scenario 9976", "data": {"sku": "SKU9976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9976@example.com", "threshold": 760}},
    {"id": "CATALOG-9977", "title": "Catalog scenario 9977", "data": {"sku": "SKU9977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9977@example.com", "threshold": 770}},
    {"id": "CATALOG-9978", "title": "Catalog scenario 9978", "data": {"sku": "SKU9978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9978@example.com", "threshold": 780}},
    {"id": "CATALOG-9979", "title": "Catalog scenario 9979", "data": {"sku": "SKU9979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9979@example.com", "threshold": 790}},
    {"id": "CATALOG-9980", "title": "Catalog scenario 9980", "data": {"sku": "SKU9980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9980@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
