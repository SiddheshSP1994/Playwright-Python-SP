import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5501", "title": "Email scenario 5501", "data": {"sku": "SKU5501", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5501@example.com", "threshold": 10}},
    {"id": "EMAIL-5502", "title": "Email scenario 5502", "data": {"sku": "SKU5502", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5502@example.com", "threshold": 20}},
    {"id": "EMAIL-5503", "title": "Email scenario 5503", "data": {"sku": "SKU5503", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5503@example.com", "threshold": 30}},
    {"id": "EMAIL-5504", "title": "Email scenario 5504", "data": {"sku": "SKU5504", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5504@example.com", "threshold": 40}},
    {"id": "EMAIL-5505", "title": "Email scenario 5505", "data": {"sku": "SKU5505", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5505@example.com", "threshold": 50}},
    {"id": "EMAIL-5506", "title": "Email scenario 5506", "data": {"sku": "SKU5506", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5506@example.com", "threshold": 60}},
    {"id": "EMAIL-5507", "title": "Email scenario 5507", "data": {"sku": "SKU5507", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5507@example.com", "threshold": 70}},
    {"id": "EMAIL-5508", "title": "Email scenario 5508", "data": {"sku": "SKU5508", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5508@example.com", "threshold": 80}},
    {"id": "EMAIL-5509", "title": "Email scenario 5509", "data": {"sku": "SKU5509", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5509@example.com", "threshold": 90}},
    {"id": "EMAIL-5510", "title": "Email scenario 5510", "data": {"sku": "SKU5510", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5510@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
