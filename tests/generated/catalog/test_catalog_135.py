import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8051", "title": "Catalog scenario 8051", "data": {"sku": "SKU8051", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8051@example.com", "threshold": 510}},
    {"id": "CATALOG-8052", "title": "Catalog scenario 8052", "data": {"sku": "SKU8052", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8052@example.com", "threshold": 520}},
    {"id": "CATALOG-8053", "title": "Catalog scenario 8053", "data": {"sku": "SKU8053", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8053@example.com", "threshold": 530}},
    {"id": "CATALOG-8054", "title": "Catalog scenario 8054", "data": {"sku": "SKU8054", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8054@example.com", "threshold": 540}},
    {"id": "CATALOG-8055", "title": "Catalog scenario 8055", "data": {"sku": "SKU8055", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8055@example.com", "threshold": 550}},
    {"id": "CATALOG-8056", "title": "Catalog scenario 8056", "data": {"sku": "SKU8056", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8056@example.com", "threshold": 560}},
    {"id": "CATALOG-8057", "title": "Catalog scenario 8057", "data": {"sku": "SKU8057", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8057@example.com", "threshold": 570}},
    {"id": "CATALOG-8058", "title": "Catalog scenario 8058", "data": {"sku": "SKU8058", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8058@example.com", "threshold": 580}},
    {"id": "CATALOG-8059", "title": "Catalog scenario 8059", "data": {"sku": "SKU8059", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8059@example.com", "threshold": 590}},
    {"id": "CATALOG-8060", "title": "Catalog scenario 8060", "data": {"sku": "SKU8060", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8060@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
