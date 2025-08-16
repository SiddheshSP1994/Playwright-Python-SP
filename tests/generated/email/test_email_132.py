import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7901", "title": "Email scenario 7901", "data": {"sku": "SKU7901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7901@example.com", "threshold": 10}},
    {"id": "EMAIL-7902", "title": "Email scenario 7902", "data": {"sku": "SKU7902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7902@example.com", "threshold": 20}},
    {"id": "EMAIL-7903", "title": "Email scenario 7903", "data": {"sku": "SKU7903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7903@example.com", "threshold": 30}},
    {"id": "EMAIL-7904", "title": "Email scenario 7904", "data": {"sku": "SKU7904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7904@example.com", "threshold": 40}},
    {"id": "EMAIL-7905", "title": "Email scenario 7905", "data": {"sku": "SKU7905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7905@example.com", "threshold": 50}},
    {"id": "EMAIL-7906", "title": "Email scenario 7906", "data": {"sku": "SKU7906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7906@example.com", "threshold": 60}},
    {"id": "EMAIL-7907", "title": "Email scenario 7907", "data": {"sku": "SKU7907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7907@example.com", "threshold": 70}},
    {"id": "EMAIL-7908", "title": "Email scenario 7908", "data": {"sku": "SKU7908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7908@example.com", "threshold": 80}},
    {"id": "EMAIL-7909", "title": "Email scenario 7909", "data": {"sku": "SKU7909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7909@example.com", "threshold": 90}},
    {"id": "EMAIL-7910", "title": "Email scenario 7910", "data": {"sku": "SKU7910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7910@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
