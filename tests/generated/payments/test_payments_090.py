import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5371", "title": "Payments scenario 5371", "data": {"sku": "SKU5371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5371@example.com", "threshold": 710}},
    {"id": "PAYMENTS-5372", "title": "Payments scenario 5372", "data": {"sku": "SKU5372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5372@example.com", "threshold": 720}},
    {"id": "PAYMENTS-5373", "title": "Payments scenario 5373", "data": {"sku": "SKU5373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5373@example.com", "threshold": 730}},
    {"id": "PAYMENTS-5374", "title": "Payments scenario 5374", "data": {"sku": "SKU5374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5374@example.com", "threshold": 740}},
    {"id": "PAYMENTS-5375", "title": "Payments scenario 5375", "data": {"sku": "SKU5375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5375@example.com", "threshold": 750}},
    {"id": "PAYMENTS-5376", "title": "Payments scenario 5376", "data": {"sku": "SKU5376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5376@example.com", "threshold": 760}},
    {"id": "PAYMENTS-5377", "title": "Payments scenario 5377", "data": {"sku": "SKU5377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5377@example.com", "threshold": 770}},
    {"id": "PAYMENTS-5378", "title": "Payments scenario 5378", "data": {"sku": "SKU5378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5378@example.com", "threshold": 780}},
    {"id": "PAYMENTS-5379", "title": "Payments scenario 5379", "data": {"sku": "SKU5379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5379@example.com", "threshold": 790}},
    {"id": "PAYMENTS-5380", "title": "Payments scenario 5380", "data": {"sku": "SKU5380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5380@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
