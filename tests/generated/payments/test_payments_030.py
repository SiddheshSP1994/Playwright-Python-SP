import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1771", "title": "Payments scenario 1771", "data": {"sku": "SKU1771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1771@example.com", "threshold": 710}},
    {"id": "PAYMENTS-1772", "title": "Payments scenario 1772", "data": {"sku": "SKU1772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1772@example.com", "threshold": 720}},
    {"id": "PAYMENTS-1773", "title": "Payments scenario 1773", "data": {"sku": "SKU1773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1773@example.com", "threshold": 730}},
    {"id": "PAYMENTS-1774", "title": "Payments scenario 1774", "data": {"sku": "SKU1774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1774@example.com", "threshold": 740}},
    {"id": "PAYMENTS-1775", "title": "Payments scenario 1775", "data": {"sku": "SKU1775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1775@example.com", "threshold": 750}},
    {"id": "PAYMENTS-1776", "title": "Payments scenario 1776", "data": {"sku": "SKU1776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1776@example.com", "threshold": 760}},
    {"id": "PAYMENTS-1777", "title": "Payments scenario 1777", "data": {"sku": "SKU1777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1777@example.com", "threshold": 770}},
    {"id": "PAYMENTS-1778", "title": "Payments scenario 1778", "data": {"sku": "SKU1778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1778@example.com", "threshold": 780}},
    {"id": "PAYMENTS-1779", "title": "Payments scenario 1779", "data": {"sku": "SKU1779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1779@example.com", "threshold": 790}},
    {"id": "PAYMENTS-1780", "title": "Payments scenario 1780", "data": {"sku": "SKU1780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1780@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
