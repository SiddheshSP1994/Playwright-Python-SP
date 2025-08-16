import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ANALYTICS-8271", "title": "Analytics scenario 8271", "data": {"sku": "SKU8271", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8271@example.com", "threshold": 710}},
    {"id": "ANALYTICS-8272", "title": "Analytics scenario 8272", "data": {"sku": "SKU8272", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8272@example.com", "threshold": 720}},
    {"id": "ANALYTICS-8273", "title": "Analytics scenario 8273", "data": {"sku": "SKU8273", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8273@example.com", "threshold": 730}},
    {"id": "ANALYTICS-8274", "title": "Analytics scenario 8274", "data": {"sku": "SKU8274", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8274@example.com", "threshold": 740}},
    {"id": "ANALYTICS-8275", "title": "Analytics scenario 8275", "data": {"sku": "SKU8275", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8275@example.com", "threshold": 750}},
    {"id": "ANALYTICS-8276", "title": "Analytics scenario 8276", "data": {"sku": "SKU8276", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8276@example.com", "threshold": 760}},
    {"id": "ANALYTICS-8277", "title": "Analytics scenario 8277", "data": {"sku": "SKU8277", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8277@example.com", "threshold": 770}},
    {"id": "ANALYTICS-8278", "title": "Analytics scenario 8278", "data": {"sku": "SKU8278", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8278@example.com", "threshold": 780}},
    {"id": "ANALYTICS-8279", "title": "Analytics scenario 8279", "data": {"sku": "SKU8279", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8279@example.com", "threshold": 790}},
    {"id": "ANALYTICS-8280", "title": "Analytics scenario 8280", "data": {"sku": "SKU8280", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8280@example.com", "threshold": 800}},
])
def test_analytics(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
