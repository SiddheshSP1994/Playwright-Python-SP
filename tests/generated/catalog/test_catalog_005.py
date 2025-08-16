import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0251", "title": "Catalog scenario 251", "data": {"sku": "SKU251", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user251@example.com", "threshold": 510}},
    {"id": "CATALOG-0252", "title": "Catalog scenario 252", "data": {"sku": "SKU252", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user252@example.com", "threshold": 520}},
    {"id": "CATALOG-0253", "title": "Catalog scenario 253", "data": {"sku": "SKU253", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user253@example.com", "threshold": 530}},
    {"id": "CATALOG-0254", "title": "Catalog scenario 254", "data": {"sku": "SKU254", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user254@example.com", "threshold": 540}},
    {"id": "CATALOG-0255", "title": "Catalog scenario 255", "data": {"sku": "SKU255", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user255@example.com", "threshold": 550}},
    {"id": "CATALOG-0256", "title": "Catalog scenario 256", "data": {"sku": "SKU256", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user256@example.com", "threshold": 560}},
    {"id": "CATALOG-0257", "title": "Catalog scenario 257", "data": {"sku": "SKU257", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user257@example.com", "threshold": 570}},
    {"id": "CATALOG-0258", "title": "Catalog scenario 258", "data": {"sku": "SKU258", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user258@example.com", "threshold": 580}},
    {"id": "CATALOG-0259", "title": "Catalog scenario 259", "data": {"sku": "SKU259", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user259@example.com", "threshold": 590}},
    {"id": "CATALOG-0260", "title": "Catalog scenario 260", "data": {"sku": "SKU260", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user260@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
