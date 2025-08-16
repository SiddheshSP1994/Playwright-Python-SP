import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-5971", "title": "Payments scenario 5971", "data": {"sku": "SKU5971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5971@example.com", "threshold": 710}},
    {"id": "PAYMENTS-5972", "title": "Payments scenario 5972", "data": {"sku": "SKU5972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5972@example.com", "threshold": 720}},
    {"id": "PAYMENTS-5973", "title": "Payments scenario 5973", "data": {"sku": "SKU5973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5973@example.com", "threshold": 730}},
    {"id": "PAYMENTS-5974", "title": "Payments scenario 5974", "data": {"sku": "SKU5974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5974@example.com", "threshold": 740}},
    {"id": "PAYMENTS-5975", "title": "Payments scenario 5975", "data": {"sku": "SKU5975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5975@example.com", "threshold": 750}},
    {"id": "PAYMENTS-5976", "title": "Payments scenario 5976", "data": {"sku": "SKU5976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5976@example.com", "threshold": 760}},
    {"id": "PAYMENTS-5977", "title": "Payments scenario 5977", "data": {"sku": "SKU5977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5977@example.com", "threshold": 770}},
    {"id": "PAYMENTS-5978", "title": "Payments scenario 5978", "data": {"sku": "SKU5978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5978@example.com", "threshold": 780}},
    {"id": "PAYMENTS-5979", "title": "Payments scenario 5979", "data": {"sku": "SKU5979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5979@example.com", "threshold": 790}},
    {"id": "PAYMENTS-5980", "title": "Payments scenario 5980", "data": {"sku": "SKU5980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5980@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
