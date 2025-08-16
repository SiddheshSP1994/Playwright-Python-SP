import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8841", "title": "Orders scenario 8841", "data": {"sku": "SKU8841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8841@example.com", "threshold": 410}},
    {"id": "ORDERS-8842", "title": "Orders scenario 8842", "data": {"sku": "SKU8842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8842@example.com", "threshold": 420}},
    {"id": "ORDERS-8843", "title": "Orders scenario 8843", "data": {"sku": "SKU8843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8843@example.com", "threshold": 430}},
    {"id": "ORDERS-8844", "title": "Orders scenario 8844", "data": {"sku": "SKU8844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8844@example.com", "threshold": 440}},
    {"id": "ORDERS-8845", "title": "Orders scenario 8845", "data": {"sku": "SKU8845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8845@example.com", "threshold": 450}},
    {"id": "ORDERS-8846", "title": "Orders scenario 8846", "data": {"sku": "SKU8846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8846@example.com", "threshold": 460}},
    {"id": "ORDERS-8847", "title": "Orders scenario 8847", "data": {"sku": "SKU8847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8847@example.com", "threshold": 470}},
    {"id": "ORDERS-8848", "title": "Orders scenario 8848", "data": {"sku": "SKU8848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8848@example.com", "threshold": 480}},
    {"id": "ORDERS-8849", "title": "Orders scenario 8849", "data": {"sku": "SKU8849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8849@example.com", "threshold": 490}},
    {"id": "ORDERS-8850", "title": "Orders scenario 8850", "data": {"sku": "SKU8850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8850@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
