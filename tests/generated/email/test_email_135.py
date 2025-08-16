import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8081", "title": "Email scenario 8081", "data": {"sku": "SKU8081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8081@example.com", "threshold": 810}},
    {"id": "EMAIL-8082", "title": "Email scenario 8082", "data": {"sku": "SKU8082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8082@example.com", "threshold": 820}},
    {"id": "EMAIL-8083", "title": "Email scenario 8083", "data": {"sku": "SKU8083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8083@example.com", "threshold": 830}},
    {"id": "EMAIL-8084", "title": "Email scenario 8084", "data": {"sku": "SKU8084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8084@example.com", "threshold": 840}},
    {"id": "EMAIL-8085", "title": "Email scenario 8085", "data": {"sku": "SKU8085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8085@example.com", "threshold": 850}},
    {"id": "EMAIL-8086", "title": "Email scenario 8086", "data": {"sku": "SKU8086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8086@example.com", "threshold": 860}},
    {"id": "EMAIL-8087", "title": "Email scenario 8087", "data": {"sku": "SKU8087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8087@example.com", "threshold": 870}},
    {"id": "EMAIL-8088", "title": "Email scenario 8088", "data": {"sku": "SKU8088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8088@example.com", "threshold": 880}},
    {"id": "EMAIL-8089", "title": "Email scenario 8089", "data": {"sku": "SKU8089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8089@example.com", "threshold": 890}},
    {"id": "EMAIL-8090", "title": "Email scenario 8090", "data": {"sku": "SKU8090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8090@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
