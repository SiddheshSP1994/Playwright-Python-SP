import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4901", "title": "Email scenario 4901", "data": {"sku": "SKU4901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4901@example.com", "threshold": 10}},
    {"id": "EMAIL-4902", "title": "Email scenario 4902", "data": {"sku": "SKU4902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4902@example.com", "threshold": 20}},
    {"id": "EMAIL-4903", "title": "Email scenario 4903", "data": {"sku": "SKU4903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4903@example.com", "threshold": 30}},
    {"id": "EMAIL-4904", "title": "Email scenario 4904", "data": {"sku": "SKU4904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4904@example.com", "threshold": 40}},
    {"id": "EMAIL-4905", "title": "Email scenario 4905", "data": {"sku": "SKU4905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4905@example.com", "threshold": 50}},
    {"id": "EMAIL-4906", "title": "Email scenario 4906", "data": {"sku": "SKU4906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4906@example.com", "threshold": 60}},
    {"id": "EMAIL-4907", "title": "Email scenario 4907", "data": {"sku": "SKU4907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4907@example.com", "threshold": 70}},
    {"id": "EMAIL-4908", "title": "Email scenario 4908", "data": {"sku": "SKU4908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4908@example.com", "threshold": 80}},
    {"id": "EMAIL-4909", "title": "Email scenario 4909", "data": {"sku": "SKU4909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4909@example.com", "threshold": 90}},
    {"id": "EMAIL-4910", "title": "Email scenario 4910", "data": {"sku": "SKU4910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4910@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
