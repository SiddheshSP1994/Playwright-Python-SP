import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-4991", "title": "Catalog scenario 4991", "data": {"sku": "SKU4991", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4991@example.com", "threshold": 910}},
    {"id": "CATALOG-4992", "title": "Catalog scenario 4992", "data": {"sku": "SKU4992", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4992@example.com", "threshold": 920}},
    {"id": "CATALOG-4993", "title": "Catalog scenario 4993", "data": {"sku": "SKU4993", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4993@example.com", "threshold": 930}},
    {"id": "CATALOG-4994", "title": "Catalog scenario 4994", "data": {"sku": "SKU4994", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4994@example.com", "threshold": 940}},
    {"id": "CATALOG-4995", "title": "Catalog scenario 4995", "data": {"sku": "SKU4995", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4995@example.com", "threshold": 950}},
    {"id": "CATALOG-4996", "title": "Catalog scenario 4996", "data": {"sku": "SKU4996", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4996@example.com", "threshold": 960}},
    {"id": "CATALOG-4997", "title": "Catalog scenario 4997", "data": {"sku": "SKU4997", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4997@example.com", "threshold": 970}},
    {"id": "CATALOG-4998", "title": "Catalog scenario 4998", "data": {"sku": "SKU4998", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4998@example.com", "threshold": 980}},
    {"id": "CATALOG-4999", "title": "Catalog scenario 4999", "data": {"sku": "SKU4999", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4999@example.com", "threshold": 990}},
    {"id": "CATALOG-5000", "title": "Catalog scenario 5000", "data": {"sku": "SKU5000", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5000@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
