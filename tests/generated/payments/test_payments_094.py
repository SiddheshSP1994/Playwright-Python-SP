import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5611", "title": "Payments scenario 5611", "data": {"sku": "SKU5611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5611@example.com", "threshold": 110}},
    {"id": "PAYMENTS-5612", "title": "Payments scenario 5612", "data": {"sku": "SKU5612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5612@example.com", "threshold": 120}},
    {"id": "PAYMENTS-5613", "title": "Payments scenario 5613", "data": {"sku": "SKU5613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5613@example.com", "threshold": 130}},
    {"id": "PAYMENTS-5614", "title": "Payments scenario 5614", "data": {"sku": "SKU5614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5614@example.com", "threshold": 140}},
    {"id": "PAYMENTS-5615", "title": "Payments scenario 5615", "data": {"sku": "SKU5615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5615@example.com", "threshold": 150}},
    {"id": "PAYMENTS-5616", "title": "Payments scenario 5616", "data": {"sku": "SKU5616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5616@example.com", "threshold": 160}},
    {"id": "PAYMENTS-5617", "title": "Payments scenario 5617", "data": {"sku": "SKU5617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5617@example.com", "threshold": 170}},
    {"id": "PAYMENTS-5618", "title": "Payments scenario 5618", "data": {"sku": "SKU5618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5618@example.com", "threshold": 180}},
    {"id": "PAYMENTS-5619", "title": "Payments scenario 5619", "data": {"sku": "SKU5619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5619@example.com", "threshold": 190}},
    {"id": "PAYMENTS-5620", "title": "Payments scenario 5620", "data": {"sku": "SKU5620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5620@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
