import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-3041", "title": "Email scenario 3041", "data": {"sku": "SKU3041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3041@example.com", "threshold": 410}},
    {"id": "EMAIL-3042", "title": "Email scenario 3042", "data": {"sku": "SKU3042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3042@example.com", "threshold": 420}},
    {"id": "EMAIL-3043", "title": "Email scenario 3043", "data": {"sku": "SKU3043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3043@example.com", "threshold": 430}},
    {"id": "EMAIL-3044", "title": "Email scenario 3044", "data": {"sku": "SKU3044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3044@example.com", "threshold": 440}},
    {"id": "EMAIL-3045", "title": "Email scenario 3045", "data": {"sku": "SKU3045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3045@example.com", "threshold": 450}},
    {"id": "EMAIL-3046", "title": "Email scenario 3046", "data": {"sku": "SKU3046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3046@example.com", "threshold": 460}},
    {"id": "EMAIL-3047", "title": "Email scenario 3047", "data": {"sku": "SKU3047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3047@example.com", "threshold": 470}},
    {"id": "EMAIL-3048", "title": "Email scenario 3048", "data": {"sku": "SKU3048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3048@example.com", "threshold": 480}},
    {"id": "EMAIL-3049", "title": "Email scenario 3049", "data": {"sku": "SKU3049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3049@example.com", "threshold": 490}},
    {"id": "EMAIL-3050", "title": "Email scenario 3050", "data": {"sku": "SKU3050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3050@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
