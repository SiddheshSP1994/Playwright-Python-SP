import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-2611", "title": "Payments scenario 2611", "data": {"sku": "SKU2611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2611@example.com", "threshold": 110}},
    {"id": "PAYMENTS-2612", "title": "Payments scenario 2612", "data": {"sku": "SKU2612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2612@example.com", "threshold": 120}},
    {"id": "PAYMENTS-2613", "title": "Payments scenario 2613", "data": {"sku": "SKU2613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2613@example.com", "threshold": 130}},
    {"id": "PAYMENTS-2614", "title": "Payments scenario 2614", "data": {"sku": "SKU2614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2614@example.com", "threshold": 140}},
    {"id": "PAYMENTS-2615", "title": "Payments scenario 2615", "data": {"sku": "SKU2615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2615@example.com", "threshold": 150}},
    {"id": "PAYMENTS-2616", "title": "Payments scenario 2616", "data": {"sku": "SKU2616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2616@example.com", "threshold": 160}},
    {"id": "PAYMENTS-2617", "title": "Payments scenario 2617", "data": {"sku": "SKU2617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2617@example.com", "threshold": 170}},
    {"id": "PAYMENTS-2618", "title": "Payments scenario 2618", "data": {"sku": "SKU2618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2618@example.com", "threshold": 180}},
    {"id": "PAYMENTS-2619", "title": "Payments scenario 2619", "data": {"sku": "SKU2619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2619@example.com", "threshold": 190}},
    {"id": "PAYMENTS-2620", "title": "Payments scenario 2620", "data": {"sku": "SKU2620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2620@example.com", "threshold": 200}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
