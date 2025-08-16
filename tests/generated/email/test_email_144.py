import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8621", "title": "Email scenario 8621", "data": {"sku": "SKU8621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8621@example.com", "threshold": 210}},
    {"id": "EMAIL-8622", "title": "Email scenario 8622", "data": {"sku": "SKU8622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8622@example.com", "threshold": 220}},
    {"id": "EMAIL-8623", "title": "Email scenario 8623", "data": {"sku": "SKU8623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8623@example.com", "threshold": 230}},
    {"id": "EMAIL-8624", "title": "Email scenario 8624", "data": {"sku": "SKU8624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8624@example.com", "threshold": 240}},
    {"id": "EMAIL-8625", "title": "Email scenario 8625", "data": {"sku": "SKU8625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8625@example.com", "threshold": 250}},
    {"id": "EMAIL-8626", "title": "Email scenario 8626", "data": {"sku": "SKU8626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8626@example.com", "threshold": 260}},
    {"id": "EMAIL-8627", "title": "Email scenario 8627", "data": {"sku": "SKU8627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8627@example.com", "threshold": 270}},
    {"id": "EMAIL-8628", "title": "Email scenario 8628", "data": {"sku": "SKU8628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8628@example.com", "threshold": 280}},
    {"id": "EMAIL-8629", "title": "Email scenario 8629", "data": {"sku": "SKU8629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8629@example.com", "threshold": 290}},
    {"id": "EMAIL-8630", "title": "Email scenario 8630", "data": {"sku": "SKU8630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8630@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
