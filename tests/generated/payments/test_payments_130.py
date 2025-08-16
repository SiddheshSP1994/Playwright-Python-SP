import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7771", "title": "Payments scenario 7771", "data": {"sku": "SKU7771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7771@example.com", "threshold": 710}},
    {"id": "PAYMENTS-7772", "title": "Payments scenario 7772", "data": {"sku": "SKU7772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7772@example.com", "threshold": 720}},
    {"id": "PAYMENTS-7773", "title": "Payments scenario 7773", "data": {"sku": "SKU7773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7773@example.com", "threshold": 730}},
    {"id": "PAYMENTS-7774", "title": "Payments scenario 7774", "data": {"sku": "SKU7774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7774@example.com", "threshold": 740}},
    {"id": "PAYMENTS-7775", "title": "Payments scenario 7775", "data": {"sku": "SKU7775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7775@example.com", "threshold": 750}},
    {"id": "PAYMENTS-7776", "title": "Payments scenario 7776", "data": {"sku": "SKU7776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7776@example.com", "threshold": 760}},
    {"id": "PAYMENTS-7777", "title": "Payments scenario 7777", "data": {"sku": "SKU7777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7777@example.com", "threshold": 770}},
    {"id": "PAYMENTS-7778", "title": "Payments scenario 7778", "data": {"sku": "SKU7778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7778@example.com", "threshold": 780}},
    {"id": "PAYMENTS-7779", "title": "Payments scenario 7779", "data": {"sku": "SKU7779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7779@example.com", "threshold": 790}},
    {"id": "PAYMENTS-7780", "title": "Payments scenario 7780", "data": {"sku": "SKU7780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7780@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
