import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4771", "title": "Payments scenario 4771", "data": {"sku": "SKU4771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4771@example.com", "threshold": 710}},
    {"id": "PAYMENTS-4772", "title": "Payments scenario 4772", "data": {"sku": "SKU4772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4772@example.com", "threshold": 720}},
    {"id": "PAYMENTS-4773", "title": "Payments scenario 4773", "data": {"sku": "SKU4773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4773@example.com", "threshold": 730}},
    {"id": "PAYMENTS-4774", "title": "Payments scenario 4774", "data": {"sku": "SKU4774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4774@example.com", "threshold": 740}},
    {"id": "PAYMENTS-4775", "title": "Payments scenario 4775", "data": {"sku": "SKU4775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4775@example.com", "threshold": 750}},
    {"id": "PAYMENTS-4776", "title": "Payments scenario 4776", "data": {"sku": "SKU4776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4776@example.com", "threshold": 760}},
    {"id": "PAYMENTS-4777", "title": "Payments scenario 4777", "data": {"sku": "SKU4777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4777@example.com", "threshold": 770}},
    {"id": "PAYMENTS-4778", "title": "Payments scenario 4778", "data": {"sku": "SKU4778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4778@example.com", "threshold": 780}},
    {"id": "PAYMENTS-4779", "title": "Payments scenario 4779", "data": {"sku": "SKU4779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4779@example.com", "threshold": 790}},
    {"id": "PAYMENTS-4780", "title": "Payments scenario 4780", "data": {"sku": "SKU4780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4780@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
