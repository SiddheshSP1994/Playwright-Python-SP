import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-9041", "title": "Email scenario 9041", "data": {"sku": "SKU9041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user9041@example.com", "threshold": 410}},
    {"id": "EMAIL-9042", "title": "Email scenario 9042", "data": {"sku": "SKU9042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user9042@example.com", "threshold": 420}},
    {"id": "EMAIL-9043", "title": "Email scenario 9043", "data": {"sku": "SKU9043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user9043@example.com", "threshold": 430}},
    {"id": "EMAIL-9044", "title": "Email scenario 9044", "data": {"sku": "SKU9044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user9044@example.com", "threshold": 440}},
    {"id": "EMAIL-9045", "title": "Email scenario 9045", "data": {"sku": "SKU9045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user9045@example.com", "threshold": 450}},
    {"id": "EMAIL-9046", "title": "Email scenario 9046", "data": {"sku": "SKU9046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user9046@example.com", "threshold": 460}},
    {"id": "EMAIL-9047", "title": "Email scenario 9047", "data": {"sku": "SKU9047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user9047@example.com", "threshold": 470}},
    {"id": "EMAIL-9048", "title": "Email scenario 9048", "data": {"sku": "SKU9048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user9048@example.com", "threshold": 480}},
    {"id": "EMAIL-9049", "title": "Email scenario 9049", "data": {"sku": "SKU9049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user9049@example.com", "threshold": 490}},
    {"id": "EMAIL-9050", "title": "Email scenario 9050", "data": {"sku": "SKU9050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user9050@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
