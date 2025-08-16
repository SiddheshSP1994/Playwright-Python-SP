import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9641", "title": "Email scenario 9641", "data": {"sku": "SKU9641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9641@example.com", "threshold": 410}},
    {"id": "EMAIL-9642", "title": "Email scenario 9642", "data": {"sku": "SKU9642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9642@example.com", "threshold": 420}},
    {"id": "EMAIL-9643", "title": "Email scenario 9643", "data": {"sku": "SKU9643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9643@example.com", "threshold": 430}},
    {"id": "EMAIL-9644", "title": "Email scenario 9644", "data": {"sku": "SKU9644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9644@example.com", "threshold": 440}},
    {"id": "EMAIL-9645", "title": "Email scenario 9645", "data": {"sku": "SKU9645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9645@example.com", "threshold": 450}},
    {"id": "EMAIL-9646", "title": "Email scenario 9646", "data": {"sku": "SKU9646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9646@example.com", "threshold": 460}},
    {"id": "EMAIL-9647", "title": "Email scenario 9647", "data": {"sku": "SKU9647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9647@example.com", "threshold": 470}},
    {"id": "EMAIL-9648", "title": "Email scenario 9648", "data": {"sku": "SKU9648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9648@example.com", "threshold": 480}},
    {"id": "EMAIL-9649", "title": "Email scenario 9649", "data": {"sku": "SKU9649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9649@example.com", "threshold": 490}},
    {"id": "EMAIL-9650", "title": "Email scenario 9650", "data": {"sku": "SKU9650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9650@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
