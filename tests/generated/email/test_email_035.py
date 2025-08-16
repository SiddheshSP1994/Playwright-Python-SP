import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2081", "title": "Email scenario 2081", "data": {"sku": "SKU2081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2081@example.com", "threshold": 810}},
    {"id": "EMAIL-2082", "title": "Email scenario 2082", "data": {"sku": "SKU2082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2082@example.com", "threshold": 820}},
    {"id": "EMAIL-2083", "title": "Email scenario 2083", "data": {"sku": "SKU2083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2083@example.com", "threshold": 830}},
    {"id": "EMAIL-2084", "title": "Email scenario 2084", "data": {"sku": "SKU2084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2084@example.com", "threshold": 840}},
    {"id": "EMAIL-2085", "title": "Email scenario 2085", "data": {"sku": "SKU2085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2085@example.com", "threshold": 850}},
    {"id": "EMAIL-2086", "title": "Email scenario 2086", "data": {"sku": "SKU2086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2086@example.com", "threshold": 860}},
    {"id": "EMAIL-2087", "title": "Email scenario 2087", "data": {"sku": "SKU2087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2087@example.com", "threshold": 870}},
    {"id": "EMAIL-2088", "title": "Email scenario 2088", "data": {"sku": "SKU2088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2088@example.com", "threshold": 880}},
    {"id": "EMAIL-2089", "title": "Email scenario 2089", "data": {"sku": "SKU2089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2089@example.com", "threshold": 890}},
    {"id": "EMAIL-2090", "title": "Email scenario 2090", "data": {"sku": "SKU2090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2090@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
