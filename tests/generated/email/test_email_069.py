import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4121", "title": "Email scenario 4121", "data": {"sku": "SKU4121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4121@example.com", "threshold": 210}},
    {"id": "EMAIL-4122", "title": "Email scenario 4122", "data": {"sku": "SKU4122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4122@example.com", "threshold": 220}},
    {"id": "EMAIL-4123", "title": "Email scenario 4123", "data": {"sku": "SKU4123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4123@example.com", "threshold": 230}},
    {"id": "EMAIL-4124", "title": "Email scenario 4124", "data": {"sku": "SKU4124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4124@example.com", "threshold": 240}},
    {"id": "EMAIL-4125", "title": "Email scenario 4125", "data": {"sku": "SKU4125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4125@example.com", "threshold": 250}},
    {"id": "EMAIL-4126", "title": "Email scenario 4126", "data": {"sku": "SKU4126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4126@example.com", "threshold": 260}},
    {"id": "EMAIL-4127", "title": "Email scenario 4127", "data": {"sku": "SKU4127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4127@example.com", "threshold": 270}},
    {"id": "EMAIL-4128", "title": "Email scenario 4128", "data": {"sku": "SKU4128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4128@example.com", "threshold": 280}},
    {"id": "EMAIL-4129", "title": "Email scenario 4129", "data": {"sku": "SKU4129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4129@example.com", "threshold": 290}},
    {"id": "EMAIL-4130", "title": "Email scenario 4130", "data": {"sku": "SKU4130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4130@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
