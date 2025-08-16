import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1781", "title": "Email scenario 1781", "data": {"sku": "SKU1781", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1781@example.com", "threshold": 810}},
    {"id": "EMAIL-1782", "title": "Email scenario 1782", "data": {"sku": "SKU1782", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1782@example.com", "threshold": 820}},
    {"id": "EMAIL-1783", "title": "Email scenario 1783", "data": {"sku": "SKU1783", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1783@example.com", "threshold": 830}},
    {"id": "EMAIL-1784", "title": "Email scenario 1784", "data": {"sku": "SKU1784", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1784@example.com", "threshold": 840}},
    {"id": "EMAIL-1785", "title": "Email scenario 1785", "data": {"sku": "SKU1785", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1785@example.com", "threshold": 850}},
    {"id": "EMAIL-1786", "title": "Email scenario 1786", "data": {"sku": "SKU1786", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1786@example.com", "threshold": 860}},
    {"id": "EMAIL-1787", "title": "Email scenario 1787", "data": {"sku": "SKU1787", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1787@example.com", "threshold": 870}},
    {"id": "EMAIL-1788", "title": "Email scenario 1788", "data": {"sku": "SKU1788", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1788@example.com", "threshold": 880}},
    {"id": "EMAIL-1789", "title": "Email scenario 1789", "data": {"sku": "SKU1789", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1789@example.com", "threshold": 890}},
    {"id": "EMAIL-1790", "title": "Email scenario 1790", "data": {"sku": "SKU1790", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1790@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
