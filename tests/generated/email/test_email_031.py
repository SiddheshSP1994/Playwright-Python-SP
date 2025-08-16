import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1841", "title": "Email scenario 1841", "data": {"sku": "SKU1841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1841@example.com", "threshold": 410}},
    {"id": "EMAIL-1842", "title": "Email scenario 1842", "data": {"sku": "SKU1842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1842@example.com", "threshold": 420}},
    {"id": "EMAIL-1843", "title": "Email scenario 1843", "data": {"sku": "SKU1843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1843@example.com", "threshold": 430}},
    {"id": "EMAIL-1844", "title": "Email scenario 1844", "data": {"sku": "SKU1844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1844@example.com", "threshold": 440}},
    {"id": "EMAIL-1845", "title": "Email scenario 1845", "data": {"sku": "SKU1845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1845@example.com", "threshold": 450}},
    {"id": "EMAIL-1846", "title": "Email scenario 1846", "data": {"sku": "SKU1846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1846@example.com", "threshold": 460}},
    {"id": "EMAIL-1847", "title": "Email scenario 1847", "data": {"sku": "SKU1847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1847@example.com", "threshold": 470}},
    {"id": "EMAIL-1848", "title": "Email scenario 1848", "data": {"sku": "SKU1848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1848@example.com", "threshold": 480}},
    {"id": "EMAIL-1849", "title": "Email scenario 1849", "data": {"sku": "SKU1849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1849@example.com", "threshold": 490}},
    {"id": "EMAIL-1850", "title": "Email scenario 1850", "data": {"sku": "SKU1850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1850@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
