import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0701", "title": "Email scenario 701", "data": {"sku": "SKU701", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user701@example.com", "threshold": 10}},
    {"id": "EMAIL-0702", "title": "Email scenario 702", "data": {"sku": "SKU702", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user702@example.com", "threshold": 20}},
    {"id": "EMAIL-0703", "title": "Email scenario 703", "data": {"sku": "SKU703", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user703@example.com", "threshold": 30}},
    {"id": "EMAIL-0704", "title": "Email scenario 704", "data": {"sku": "SKU704", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user704@example.com", "threshold": 40}},
    {"id": "EMAIL-0705", "title": "Email scenario 705", "data": {"sku": "SKU705", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user705@example.com", "threshold": 50}},
    {"id": "EMAIL-0706", "title": "Email scenario 706", "data": {"sku": "SKU706", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user706@example.com", "threshold": 60}},
    {"id": "EMAIL-0707", "title": "Email scenario 707", "data": {"sku": "SKU707", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user707@example.com", "threshold": 70}},
    {"id": "EMAIL-0708", "title": "Email scenario 708", "data": {"sku": "SKU708", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user708@example.com", "threshold": 80}},
    {"id": "EMAIL-0709", "title": "Email scenario 709", "data": {"sku": "SKU709", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user709@example.com", "threshold": 90}},
    {"id": "EMAIL-0710", "title": "Email scenario 710", "data": {"sku": "SKU710", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user710@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
