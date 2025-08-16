import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6251", "title": "Catalog scenario 6251", "data": {"sku": "SKU6251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6251@example.com", "threshold": 510}},
    {"id": "CATALOG-6252", "title": "Catalog scenario 6252", "data": {"sku": "SKU6252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6252@example.com", "threshold": 520}},
    {"id": "CATALOG-6253", "title": "Catalog scenario 6253", "data": {"sku": "SKU6253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6253@example.com", "threshold": 530}},
    {"id": "CATALOG-6254", "title": "Catalog scenario 6254", "data": {"sku": "SKU6254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6254@example.com", "threshold": 540}},
    {"id": "CATALOG-6255", "title": "Catalog scenario 6255", "data": {"sku": "SKU6255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6255@example.com", "threshold": 550}},
    {"id": "CATALOG-6256", "title": "Catalog scenario 6256", "data": {"sku": "SKU6256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6256@example.com", "threshold": 560}},
    {"id": "CATALOG-6257", "title": "Catalog scenario 6257", "data": {"sku": "SKU6257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6257@example.com", "threshold": 570}},
    {"id": "CATALOG-6258", "title": "Catalog scenario 6258", "data": {"sku": "SKU6258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6258@example.com", "threshold": 580}},
    {"id": "CATALOG-6259", "title": "Catalog scenario 6259", "data": {"sku": "SKU6259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6259@example.com", "threshold": 590}},
    {"id": "CATALOG-6260", "title": "Catalog scenario 6260", "data": {"sku": "SKU6260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6260@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
