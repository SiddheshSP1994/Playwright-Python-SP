import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2841", "title": "Orders scenario 2841", "data": {"sku": "SKU2841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2841@example.com", "threshold": 410}},
    {"id": "ORDERS-2842", "title": "Orders scenario 2842", "data": {"sku": "SKU2842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2842@example.com", "threshold": 420}},
    {"id": "ORDERS-2843", "title": "Orders scenario 2843", "data": {"sku": "SKU2843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2843@example.com", "threshold": 430}},
    {"id": "ORDERS-2844", "title": "Orders scenario 2844", "data": {"sku": "SKU2844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2844@example.com", "threshold": 440}},
    {"id": "ORDERS-2845", "title": "Orders scenario 2845", "data": {"sku": "SKU2845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2845@example.com", "threshold": 450}},
    {"id": "ORDERS-2846", "title": "Orders scenario 2846", "data": {"sku": "SKU2846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2846@example.com", "threshold": 460}},
    {"id": "ORDERS-2847", "title": "Orders scenario 2847", "data": {"sku": "SKU2847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2847@example.com", "threshold": 470}},
    {"id": "ORDERS-2848", "title": "Orders scenario 2848", "data": {"sku": "SKU2848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2848@example.com", "threshold": 480}},
    {"id": "ORDERS-2849", "title": "Orders scenario 2849", "data": {"sku": "SKU2849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2849@example.com", "threshold": 490}},
    {"id": "ORDERS-2850", "title": "Orders scenario 2850", "data": {"sku": "SKU2850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2850@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
