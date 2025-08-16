import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9251", "title": "Catalog scenario 9251", "data": {"sku": "SKU9251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9251@example.com", "threshold": 510}},
    {"id": "CATALOG-9252", "title": "Catalog scenario 9252", "data": {"sku": "SKU9252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9252@example.com", "threshold": 520}},
    {"id": "CATALOG-9253", "title": "Catalog scenario 9253", "data": {"sku": "SKU9253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9253@example.com", "threshold": 530}},
    {"id": "CATALOG-9254", "title": "Catalog scenario 9254", "data": {"sku": "SKU9254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9254@example.com", "threshold": 540}},
    {"id": "CATALOG-9255", "title": "Catalog scenario 9255", "data": {"sku": "SKU9255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9255@example.com", "threshold": 550}},
    {"id": "CATALOG-9256", "title": "Catalog scenario 9256", "data": {"sku": "SKU9256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9256@example.com", "threshold": 560}},
    {"id": "CATALOG-9257", "title": "Catalog scenario 9257", "data": {"sku": "SKU9257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9257@example.com", "threshold": 570}},
    {"id": "CATALOG-9258", "title": "Catalog scenario 9258", "data": {"sku": "SKU9258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9258@example.com", "threshold": 580}},
    {"id": "CATALOG-9259", "title": "Catalog scenario 9259", "data": {"sku": "SKU9259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9259@example.com", "threshold": 590}},
    {"id": "CATALOG-9260", "title": "Catalog scenario 9260", "data": {"sku": "SKU9260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9260@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
