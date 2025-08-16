import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1901", "title": "Email scenario 1901", "data": {"sku": "SKU1901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1901@example.com", "threshold": 10}},
    {"id": "EMAIL-1902", "title": "Email scenario 1902", "data": {"sku": "SKU1902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1902@example.com", "threshold": 20}},
    {"id": "EMAIL-1903", "title": "Email scenario 1903", "data": {"sku": "SKU1903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1903@example.com", "threshold": 30}},
    {"id": "EMAIL-1904", "title": "Email scenario 1904", "data": {"sku": "SKU1904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1904@example.com", "threshold": 40}},
    {"id": "EMAIL-1905", "title": "Email scenario 1905", "data": {"sku": "SKU1905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1905@example.com", "threshold": 50}},
    {"id": "EMAIL-1906", "title": "Email scenario 1906", "data": {"sku": "SKU1906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1906@example.com", "threshold": 60}},
    {"id": "EMAIL-1907", "title": "Email scenario 1907", "data": {"sku": "SKU1907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1907@example.com", "threshold": 70}},
    {"id": "EMAIL-1908", "title": "Email scenario 1908", "data": {"sku": "SKU1908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1908@example.com", "threshold": 80}},
    {"id": "EMAIL-1909", "title": "Email scenario 1909", "data": {"sku": "SKU1909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1909@example.com", "threshold": 90}},
    {"id": "EMAIL-1910", "title": "Email scenario 1910", "data": {"sku": "SKU1910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1910@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
