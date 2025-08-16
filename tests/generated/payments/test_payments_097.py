import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5791", "title": "Payments scenario 5791", "data": {"sku": "SKU5791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5791@example.com", "threshold": 910}},
    {"id": "PAYMENTS-5792", "title": "Payments scenario 5792", "data": {"sku": "SKU5792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5792@example.com", "threshold": 920}},
    {"id": "PAYMENTS-5793", "title": "Payments scenario 5793", "data": {"sku": "SKU5793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5793@example.com", "threshold": 930}},
    {"id": "PAYMENTS-5794", "title": "Payments scenario 5794", "data": {"sku": "SKU5794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5794@example.com", "threshold": 940}},
    {"id": "PAYMENTS-5795", "title": "Payments scenario 5795", "data": {"sku": "SKU5795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5795@example.com", "threshold": 950}},
    {"id": "PAYMENTS-5796", "title": "Payments scenario 5796", "data": {"sku": "SKU5796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5796@example.com", "threshold": 960}},
    {"id": "PAYMENTS-5797", "title": "Payments scenario 5797", "data": {"sku": "SKU5797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5797@example.com", "threshold": 970}},
    {"id": "PAYMENTS-5798", "title": "Payments scenario 5798", "data": {"sku": "SKU5798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5798@example.com", "threshold": 980}},
    {"id": "PAYMENTS-5799", "title": "Payments scenario 5799", "data": {"sku": "SKU5799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5799@example.com", "threshold": 990}},
    {"id": "PAYMENTS-5800", "title": "Payments scenario 5800", "data": {"sku": "SKU5800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5800@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
