import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4781", "title": "Email scenario 4781", "data": {"sku": "SKU4781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4781@example.com", "threshold": 810}},
    {"id": "EMAIL-4782", "title": "Email scenario 4782", "data": {"sku": "SKU4782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4782@example.com", "threshold": 820}},
    {"id": "EMAIL-4783", "title": "Email scenario 4783", "data": {"sku": "SKU4783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4783@example.com", "threshold": 830}},
    {"id": "EMAIL-4784", "title": "Email scenario 4784", "data": {"sku": "SKU4784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4784@example.com", "threshold": 840}},
    {"id": "EMAIL-4785", "title": "Email scenario 4785", "data": {"sku": "SKU4785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4785@example.com", "threshold": 850}},
    {"id": "EMAIL-4786", "title": "Email scenario 4786", "data": {"sku": "SKU4786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4786@example.com", "threshold": 860}},
    {"id": "EMAIL-4787", "title": "Email scenario 4787", "data": {"sku": "SKU4787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4787@example.com", "threshold": 870}},
    {"id": "EMAIL-4788", "title": "Email scenario 4788", "data": {"sku": "SKU4788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4788@example.com", "threshold": 880}},
    {"id": "EMAIL-4789", "title": "Email scenario 4789", "data": {"sku": "SKU4789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4789@example.com", "threshold": 890}},
    {"id": "EMAIL-4790", "title": "Email scenario 4790", "data": {"sku": "SKU4790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4790@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
