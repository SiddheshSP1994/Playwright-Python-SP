import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-6551", "title": "Catalog scenario 6551", "data": {"sku": "SKU6551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user6551@example.com", "threshold": 510}},
    {"id": "CATALOG-6552", "title": "Catalog scenario 6552", "data": {"sku": "SKU6552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user6552@example.com", "threshold": 520}},
    {"id": "CATALOG-6553", "title": "Catalog scenario 6553", "data": {"sku": "SKU6553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user6553@example.com", "threshold": 530}},
    {"id": "CATALOG-6554", "title": "Catalog scenario 6554", "data": {"sku": "SKU6554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user6554@example.com", "threshold": 540}},
    {"id": "CATALOG-6555", "title": "Catalog scenario 6555", "data": {"sku": "SKU6555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user6555@example.com", "threshold": 550}},
    {"id": "CATALOG-6556", "title": "Catalog scenario 6556", "data": {"sku": "SKU6556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user6556@example.com", "threshold": 560}},
    {"id": "CATALOG-6557", "title": "Catalog scenario 6557", "data": {"sku": "SKU6557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user6557@example.com", "threshold": 570}},
    {"id": "CATALOG-6558", "title": "Catalog scenario 6558", "data": {"sku": "SKU6558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user6558@example.com", "threshold": 580}},
    {"id": "CATALOG-6559", "title": "Catalog scenario 6559", "data": {"sku": "SKU6559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user6559@example.com", "threshold": 590}},
    {"id": "CATALOG-6560", "title": "Catalog scenario 6560", "data": {"sku": "SKU6560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user6560@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
