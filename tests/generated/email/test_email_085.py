import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5081", "title": "Email scenario 5081", "data": {"sku": "SKU5081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5081@example.com", "threshold": 810}},
    {"id": "EMAIL-5082", "title": "Email scenario 5082", "data": {"sku": "SKU5082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5082@example.com", "threshold": 820}},
    {"id": "EMAIL-5083", "title": "Email scenario 5083", "data": {"sku": "SKU5083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5083@example.com", "threshold": 830}},
    {"id": "EMAIL-5084", "title": "Email scenario 5084", "data": {"sku": "SKU5084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5084@example.com", "threshold": 840}},
    {"id": "EMAIL-5085", "title": "Email scenario 5085", "data": {"sku": "SKU5085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5085@example.com", "threshold": 850}},
    {"id": "EMAIL-5086", "title": "Email scenario 5086", "data": {"sku": "SKU5086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5086@example.com", "threshold": 860}},
    {"id": "EMAIL-5087", "title": "Email scenario 5087", "data": {"sku": "SKU5087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5087@example.com", "threshold": 870}},
    {"id": "EMAIL-5088", "title": "Email scenario 5088", "data": {"sku": "SKU5088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5088@example.com", "threshold": 880}},
    {"id": "EMAIL-5089", "title": "Email scenario 5089", "data": {"sku": "SKU5089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5089@example.com", "threshold": 890}},
    {"id": "EMAIL-5090", "title": "Email scenario 5090", "data": {"sku": "SKU5090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5090@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
