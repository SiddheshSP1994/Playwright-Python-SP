import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4241", "title": "Email scenario 4241", "data": {"sku": "SKU4241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4241@example.com", "threshold": 410}},
    {"id": "EMAIL-4242", "title": "Email scenario 4242", "data": {"sku": "SKU4242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4242@example.com", "threshold": 420}},
    {"id": "EMAIL-4243", "title": "Email scenario 4243", "data": {"sku": "SKU4243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4243@example.com", "threshold": 430}},
    {"id": "EMAIL-4244", "title": "Email scenario 4244", "data": {"sku": "SKU4244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4244@example.com", "threshold": 440}},
    {"id": "EMAIL-4245", "title": "Email scenario 4245", "data": {"sku": "SKU4245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4245@example.com", "threshold": 450}},
    {"id": "EMAIL-4246", "title": "Email scenario 4246", "data": {"sku": "SKU4246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4246@example.com", "threshold": 460}},
    {"id": "EMAIL-4247", "title": "Email scenario 4247", "data": {"sku": "SKU4247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4247@example.com", "threshold": 470}},
    {"id": "EMAIL-4248", "title": "Email scenario 4248", "data": {"sku": "SKU4248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4248@example.com", "threshold": 480}},
    {"id": "EMAIL-4249", "title": "Email scenario 4249", "data": {"sku": "SKU4249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4249@example.com", "threshold": 490}},
    {"id": "EMAIL-4250", "title": "Email scenario 4250", "data": {"sku": "SKU4250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4250@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
