import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5351", "title": "Catalog scenario 5351", "data": {"sku": "SKU5351", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5351@example.com", "threshold": 510}},
    {"id": "CATALOG-5352", "title": "Catalog scenario 5352", "data": {"sku": "SKU5352", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5352@example.com", "threshold": 520}},
    {"id": "CATALOG-5353", "title": "Catalog scenario 5353", "data": {"sku": "SKU5353", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5353@example.com", "threshold": 530}},
    {"id": "CATALOG-5354", "title": "Catalog scenario 5354", "data": {"sku": "SKU5354", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5354@example.com", "threshold": 540}},
    {"id": "CATALOG-5355", "title": "Catalog scenario 5355", "data": {"sku": "SKU5355", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5355@example.com", "threshold": 550}},
    {"id": "CATALOG-5356", "title": "Catalog scenario 5356", "data": {"sku": "SKU5356", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5356@example.com", "threshold": 560}},
    {"id": "CATALOG-5357", "title": "Catalog scenario 5357", "data": {"sku": "SKU5357", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5357@example.com", "threshold": 570}},
    {"id": "CATALOG-5358", "title": "Catalog scenario 5358", "data": {"sku": "SKU5358", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5358@example.com", "threshold": 580}},
    {"id": "CATALOG-5359", "title": "Catalog scenario 5359", "data": {"sku": "SKU5359", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5359@example.com", "threshold": 590}},
    {"id": "CATALOG-5360", "title": "Catalog scenario 5360", "data": {"sku": "SKU5360", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5360@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
