import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7781", "title": "Email scenario 7781", "data": {"sku": "SKU7781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7781@example.com", "threshold": 810}},
    {"id": "EMAIL-7782", "title": "Email scenario 7782", "data": {"sku": "SKU7782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7782@example.com", "threshold": 820}},
    {"id": "EMAIL-7783", "title": "Email scenario 7783", "data": {"sku": "SKU7783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7783@example.com", "threshold": 830}},
    {"id": "EMAIL-7784", "title": "Email scenario 7784", "data": {"sku": "SKU7784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7784@example.com", "threshold": 840}},
    {"id": "EMAIL-7785", "title": "Email scenario 7785", "data": {"sku": "SKU7785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7785@example.com", "threshold": 850}},
    {"id": "EMAIL-7786", "title": "Email scenario 7786", "data": {"sku": "SKU7786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7786@example.com", "threshold": 860}},
    {"id": "EMAIL-7787", "title": "Email scenario 7787", "data": {"sku": "SKU7787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7787@example.com", "threshold": 870}},
    {"id": "EMAIL-7788", "title": "Email scenario 7788", "data": {"sku": "SKU7788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7788@example.com", "threshold": 880}},
    {"id": "EMAIL-7789", "title": "Email scenario 7789", "data": {"sku": "SKU7789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7789@example.com", "threshold": 890}},
    {"id": "EMAIL-7790", "title": "Email scenario 7790", "data": {"sku": "SKU7790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7790@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
