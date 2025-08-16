import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1711", "title": "Payments scenario 1711", "data": {"sku": "SKU1711", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1711@example.com", "threshold": 110}},
    {"id": "PAYMENTS-1712", "title": "Payments scenario 1712", "data": {"sku": "SKU1712", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1712@example.com", "threshold": 120}},
    {"id": "PAYMENTS-1713", "title": "Payments scenario 1713", "data": {"sku": "SKU1713", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1713@example.com", "threshold": 130}},
    {"id": "PAYMENTS-1714", "title": "Payments scenario 1714", "data": {"sku": "SKU1714", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1714@example.com", "threshold": 140}},
    {"id": "PAYMENTS-1715", "title": "Payments scenario 1715", "data": {"sku": "SKU1715", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1715@example.com", "threshold": 150}},
    {"id": "PAYMENTS-1716", "title": "Payments scenario 1716", "data": {"sku": "SKU1716", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1716@example.com", "threshold": 160}},
    {"id": "PAYMENTS-1717", "title": "Payments scenario 1717", "data": {"sku": "SKU1717", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1717@example.com", "threshold": 170}},
    {"id": "PAYMENTS-1718", "title": "Payments scenario 1718", "data": {"sku": "SKU1718", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1718@example.com", "threshold": 180}},
    {"id": "PAYMENTS-1719", "title": "Payments scenario 1719", "data": {"sku": "SKU1719", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1719@example.com", "threshold": 190}},
    {"id": "PAYMENTS-1720", "title": "Payments scenario 1720", "data": {"sku": "SKU1720", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1720@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
