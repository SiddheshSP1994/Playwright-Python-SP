import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-9551", "title": "Catalog scenario 9551", "data": {"sku": "SKU9551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user9551@example.com", "threshold": 510}},
    {"id": "CATALOG-9552", "title": "Catalog scenario 9552", "data": {"sku": "SKU9552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user9552@example.com", "threshold": 520}},
    {"id": "CATALOG-9553", "title": "Catalog scenario 9553", "data": {"sku": "SKU9553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user9553@example.com", "threshold": 530}},
    {"id": "CATALOG-9554", "title": "Catalog scenario 9554", "data": {"sku": "SKU9554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user9554@example.com", "threshold": 540}},
    {"id": "CATALOG-9555", "title": "Catalog scenario 9555", "data": {"sku": "SKU9555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user9555@example.com", "threshold": 550}},
    {"id": "CATALOG-9556", "title": "Catalog scenario 9556", "data": {"sku": "SKU9556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user9556@example.com", "threshold": 560}},
    {"id": "CATALOG-9557", "title": "Catalog scenario 9557", "data": {"sku": "SKU9557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user9557@example.com", "threshold": 570}},
    {"id": "CATALOG-9558", "title": "Catalog scenario 9558", "data": {"sku": "SKU9558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user9558@example.com", "threshold": 580}},
    {"id": "CATALOG-9559", "title": "Catalog scenario 9559", "data": {"sku": "SKU9559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user9559@example.com", "threshold": 590}},
    {"id": "CATALOG-9560", "title": "Catalog scenario 9560", "data": {"sku": "SKU9560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user9560@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
