import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5551", "title": "Payments scenario 5551", "data": {"sku": "SKU5551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5551@example.com", "threshold": 510}},
    {"id": "PAYMENTS-5552", "title": "Payments scenario 5552", "data": {"sku": "SKU5552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5552@example.com", "threshold": 520}},
    {"id": "PAYMENTS-5553", "title": "Payments scenario 5553", "data": {"sku": "SKU5553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5553@example.com", "threshold": 530}},
    {"id": "PAYMENTS-5554", "title": "Payments scenario 5554", "data": {"sku": "SKU5554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5554@example.com", "threshold": 540}},
    {"id": "PAYMENTS-5555", "title": "Payments scenario 5555", "data": {"sku": "SKU5555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5555@example.com", "threshold": 550}},
    {"id": "PAYMENTS-5556", "title": "Payments scenario 5556", "data": {"sku": "SKU5556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5556@example.com", "threshold": 560}},
    {"id": "PAYMENTS-5557", "title": "Payments scenario 5557", "data": {"sku": "SKU5557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5557@example.com", "threshold": 570}},
    {"id": "PAYMENTS-5558", "title": "Payments scenario 5558", "data": {"sku": "SKU5558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5558@example.com", "threshold": 580}},
    {"id": "PAYMENTS-5559", "title": "Payments scenario 5559", "data": {"sku": "SKU5559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5559@example.com", "threshold": 590}},
    {"id": "PAYMENTS-5560", "title": "Payments scenario 5560", "data": {"sku": "SKU5560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5560@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
