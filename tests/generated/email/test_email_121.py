import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7241", "title": "Email scenario 7241", "data": {"sku": "SKU7241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7241@example.com", "threshold": 410}},
    {"id": "EMAIL-7242", "title": "Email scenario 7242", "data": {"sku": "SKU7242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7242@example.com", "threshold": 420}},
    {"id": "EMAIL-7243", "title": "Email scenario 7243", "data": {"sku": "SKU7243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7243@example.com", "threshold": 430}},
    {"id": "EMAIL-7244", "title": "Email scenario 7244", "data": {"sku": "SKU7244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7244@example.com", "threshold": 440}},
    {"id": "EMAIL-7245", "title": "Email scenario 7245", "data": {"sku": "SKU7245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7245@example.com", "threshold": 450}},
    {"id": "EMAIL-7246", "title": "Email scenario 7246", "data": {"sku": "SKU7246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7246@example.com", "threshold": 460}},
    {"id": "EMAIL-7247", "title": "Email scenario 7247", "data": {"sku": "SKU7247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7247@example.com", "threshold": 470}},
    {"id": "EMAIL-7248", "title": "Email scenario 7248", "data": {"sku": "SKU7248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7248@example.com", "threshold": 480}},
    {"id": "EMAIL-7249", "title": "Email scenario 7249", "data": {"sku": "SKU7249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7249@example.com", "threshold": 490}},
    {"id": "EMAIL-7250", "title": "Email scenario 7250", "data": {"sku": "SKU7250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7250@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
