import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5841", "title": "Orders scenario 5841", "data": {"sku": "SKU5841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5841@example.com", "threshold": 410}},
    {"id": "ORDERS-5842", "title": "Orders scenario 5842", "data": {"sku": "SKU5842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5842@example.com", "threshold": 420}},
    {"id": "ORDERS-5843", "title": "Orders scenario 5843", "data": {"sku": "SKU5843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5843@example.com", "threshold": 430}},
    {"id": "ORDERS-5844", "title": "Orders scenario 5844", "data": {"sku": "SKU5844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5844@example.com", "threshold": 440}},
    {"id": "ORDERS-5845", "title": "Orders scenario 5845", "data": {"sku": "SKU5845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5845@example.com", "threshold": 450}},
    {"id": "ORDERS-5846", "title": "Orders scenario 5846", "data": {"sku": "SKU5846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5846@example.com", "threshold": 460}},
    {"id": "ORDERS-5847", "title": "Orders scenario 5847", "data": {"sku": "SKU5847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5847@example.com", "threshold": 470}},
    {"id": "ORDERS-5848", "title": "Orders scenario 5848", "data": {"sku": "SKU5848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5848@example.com", "threshold": 480}},
    {"id": "ORDERS-5849", "title": "Orders scenario 5849", "data": {"sku": "SKU5849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5849@example.com", "threshold": 490}},
    {"id": "ORDERS-5850", "title": "Orders scenario 5850", "data": {"sku": "SKU5850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5850@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
